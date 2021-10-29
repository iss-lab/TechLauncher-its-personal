// -*- mode: typescript; indent-tabs-mode: nil; js-basic-offset: 4 -*-
//
// This file is part of Almond
//
// Copyright 2016-2021 The Board of Trustees of the Leland Stanford Junior University
//
// Licensed under the Apache License, Version 2.0 (the "License");
// you may not use this file except in compliance with the License.
// You may obtain a copy of the License at
//
//    http://www.apache.org/licenses/LICENSE-2.0
//
// Unless required by applicable law or agreed to in writing, software
// distributed under the License is distributed on an "AS IS" BASIS,
// WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
// See the License for the specific language governing permissions and
// limitations under the License.
//
// Author: Giovanni Campagna <gcampagn@cs.stanford.edu>

import assert from 'assert';
import * as semver from 'semver';
import * as rpc from 'transparent-rpc';

import * as Tp from 'thingpedia';
import * as ThingTalk from 'thingtalk';

import * as Config from '../config';

import * as db from './db';
import * as device from '../model/device';
import * as organization from '../model/organization';
import * as schemaModel from '../model/schema';
import * as exampleModel from '../model/example';
import * as entityModel from '../model/entity';
import * as stringModel from '../model/strings';
import * as discovery from './discovery';

import * as DatasetUtils from './dataset';
import * as SchemaUtils from './manifest_to_schema';
import * as I18n from './i18n';
import * as codeStorage from './code_storage';
import { NotFoundError, ForbiddenError, BadRequestError } from './errors';
import resolveLocation from './location-linking';
import { parseOldOrNewSyntax } from './compat';

const CATEGORIES = new Set(['media', 'social-network', 'home', 'communication', 'health', 'service', 'data-management']);

// FIXME this info needs to be in Thingpedia
interface ExtendedEntityRecord extends Tp.BaseClient.EntityTypeRecord {
    subtype_of ?: string[]|null;
}

export default class ThingpediaClientCloud extends Tp.BaseClient implements rpc.Stubbable<keyof Tp.BaseClient> {
    $rpcMethods = [
        'getModuleLocation',
        'getDeviceCode',
        'getSchemas',
        'getMixins',
        'getDeviceSetup',
        'getDeviceFactories',
        'getDeviceList',
        'searchDevice',
        'getKindByDiscovery',
        'getExamplesByKinds',
        'getExamplesByKey',
        'clickExample',
        'lookupEntity',
        'lookupLocation',
        'getAllEntityTypes',
    ] as const;

    private _developerKey : string|null;
    private _locale : string;
    protected language : string;
    protected _dbClient : db.Client|null;
    private _thingtalkVersion : string;
    private _needsCompatibility : boolean;

    constructor(developerKey : string|null|undefined, locale ?: string, thingtalk_version ?: string, dbClient : db.Client|null = null) {
        super();

        this._developerKey = developerKey ?? null;
        this._locale = locale || 'en-US';
        this.language = I18n.localeToLanguage(this._locale);

        this._dbClient = dbClient;
        this._thingtalkVersion = thingtalk_version || ThingTalk.version;
        this._needsCompatibility = semver.satisfies(this._thingtalkVersion, '<2.0.0');
    }

    get developerKey() {
        return this._developerKey;
    }

    get locale() {
        return this._locale;
    }

    protected _withClient<T>(func : (client : db.Client) => Promise<T>) : Promise<T> {
        if (this._dbClient)
            return func(this._dbClient);
        else
            return db.withClient(func);
    }

    protected async _getOrg(dbClient : db.Client) : Promise<{ id : number, is_admin : boolean }|null> {
        if (!this.developerKey)
            return null;
        const [org] = await organization.getByDeveloperKey(dbClient, this.developerKey);
        return org || null;
    }
    protected async _getOrgId(dbClient : db.Client) {
        const org = await this._getOrg(dbClient);
        if (org === null)
            return null;
        else if (org.is_admin)
            return -1;
        else
            return org.id;
    }

    async getModuleLocation(kind : string, version ?: number) {
        const [approvedVersion, maxVersion] = await this._withClient(async (dbClient) => {
            const org = await this._getOrg(dbClient);
            const dev = await device.getDownloadVersion(dbClient, kind, org);
            if (!dev.downloadable)
                throw new BadRequestError('No Code Available');
            return [dev.approved_version, dev.version];
        });
        if (maxVersion === null || (version !== undefined && version > maxVersion))
            throw new ForbiddenError('Not Authorized');
        if (version === undefined)
            version = maxVersion;

        const developer = approvedVersion === null || version > approvedVersion;

        return codeStorage.getDownloadLocation(kind, version, developer);
    }

    getDeviceCode(kind : string) {
        return this._withClient(async (dbClient) => {
            const orgId = await this._getOrgId(dbClient);
            const classes = await this._internalGetDeviceCode([kind], orgId, dbClient);
            if (classes.length < 1)
                throw new NotFoundError();
            return classes[0];
        });
    }

    private async _internalGetDeviceCode(kinds : string[], orgId : number|null, dbClient : db.Client) {
        const devs = await device.getFullCodeByPrimaryKinds(dbClient, kinds, orgId);
        let schemas : schemaModel.SchemaMetadata[]|undefined;
        if (this.language !== 'en')
            schemas = await schemaModel.getMetasByKinds(dbClient, kinds, orgId, this.language);
        return Promise.all(devs.map(async (dev) => {
            const code = dev.code;

            // fast path without parsing the code
            if (this.language === 'en' && !this._needsCompatibility &&
                !/(makeArgMap|\$context)/.test(code) /* quick check for old-syntax constructs */)
                return code;

            const parsed = parseOldOrNewSyntax(code, {
                locale: 'en-US',
                timezone: 'UTC'
            });
            assert(parsed instanceof ThingTalk.Ast.Library);
            const classDef = parsed.classes[0];

            if (this.language !== 'en') {
                assert(schemas);
                const schema = schemas.find((schema) => schema.kind === dev.primary_kind);
                if (schema)
                    SchemaUtils.mergeClassDefAndSchema(classDef, schema);
            }

            return ThingTalk.Syntax.serialize(parsed, ThingTalk.Syntax.SyntaxType.Normal, undefined, {
                compatibility: this._thingtalkVersion
            });
        }));
    }

    getSchemas(schemas : string[], withMetadata ?: boolean) {
        if (schemas.length === 0)
            return Promise.resolve('');

        return this._withClient(async (dbClient) => {
            if (withMetadata) {
                const orgId = await this._getOrgId(dbClient);
                return (await this._internalGetDeviceCode(schemas, orgId, dbClient)).join('\n');
            } else {
                const rows = await schemaModel.getTypesAndNamesByKinds(dbClient, schemas, await this._getOrgId(dbClient));
                const classDefs = SchemaUtils.schemaListToClassDefs(rows, false);
                return ThingTalk.Syntax.serialize(classDefs, ThingTalk.Syntax.SyntaxType.Normal, undefined, {
                    compatibility: this._thingtalkVersion
                });
            }
        });
    }

    searchDevice(q : string) {
        return this._withClient(async (dbClient) => {
            const org = await this._getOrg(dbClient);
            return device.getByFuzzySearch(dbClient, q, org);
        });
    }

    getDeviceList(klass : string|undefined, page : number, page_size : number) {
        return this._withClient(async (dbClient) => {
            const org = await this._getOrg(dbClient);
            if (klass) {
                if (['online','physical','data','system'].indexOf(klass) >= 0)
                    return device.getByCategory(dbClient, klass, org, page*page_size, page_size+1);
                else if (CATEGORIES.has(klass))
                    return device.getBySubcategory(dbClient, klass, org, page*page_size, page_size+1);
                else
                    throw new BadRequestError("Invalid class parameter");
            } else {
                return device.getAllApproved(dbClient, org, page*page_size, page_size+1);
            }
        });
    }

    private _ensureDeviceFactory(device : device.FactoryRow) : Tp.BaseClient.DeviceFactory|null {
        if (device.factory !== null)
            return typeof device.factory === 'string' ? JSON.parse(device.factory) : device.factory;
        return null;
    }

    getDeviceFactories(klass ?: string) {
        return this._withClient(async (dbClient) => {
            const org = await this._getOrg(dbClient);

            let devices;
            if (klass) {
                if (['online','physical','data','system'].indexOf(klass) >= 0)
                    devices = await device.getByCategoryWithCode(dbClient, klass, org);
                else if (CATEGORIES.has(klass))
                    devices = await device.getBySubcategoryWithCode(dbClient, klass, org);
                else
                    throw new BadRequestError("Invalid class parameter");
            } else {
                devices = await device.getAllApprovedWithCode(dbClient, org);
            }

            const factories = [];
            for (const d of devices) {
                const factory = this._ensureDeviceFactory(d);
                if (factory)
                    factories.push(factory);
            }
            return factories;
        });
    }

    getDeviceSetup(kinds : string[]) {
        if (kinds.length === 0)
            return Promise.resolve({});

        return this._withClient(async (dbClient) => {
            const org = await this._getOrg(dbClient);

            for (let i = 0; i < kinds.length; i++) {
                 if (kinds[i] === 'messaging')
                     kinds[i] = Config.MESSAGING_DEVICE;
            }

            const devices = await device.getDevicesForSetup(dbClient, kinds, org);
            const names : Record<string, string> = {};
            devices.forEach((d) => {
                names[d.primary_kind] = d.name;
            });

            const result : Record<string, Tp.BaseClient.DeviceFactory | Tp.BaseClient.MultipleDeviceFactory> = {};
            devices.forEach((d : any) => {
                try {
                    d.factory = this._ensureDeviceFactory(d);
                    if (d.factory) {
                        if (d.for_kind in result) {
                            if (result[d.for_kind].type !== 'multiple') {
                                const first_choice = result[d.for_kind];
                                assert(first_choice.type !== 'multiple');
                                result[d.for_kind] = { type: 'multiple', text: names[d.for_kind] || d.for_kind, choices: [first_choice] };
                            }
                            const existing = result[d.for_kind];
                            assert(existing.type === 'multiple');
                            existing.choices.push(d.factory);
                        } else {
                            result[d.for_kind] = d.factory;
                        }
                        if (d.for_kind === Config.MESSAGING_DEVICE)
                            result['messaging'] = d.factory;
                    }
                } catch(e) { /**/ }
            });

            for (const kind of kinds) {
                if (!(kind in result))
                    result[kind] = { type: 'multiple', text: names[kind] || kind, choices: [] };
            }

            return result;
        });
    }

    getKindByDiscovery(body : any) : Promise<string> {
        return this._withClient(async (dbClient) => {
            const decoded = await discovery.decode(dbClient, body);
            if (decoded === null)
                throw new NotFoundError();
            return decoded.primary_kind;
        });
    }

    private _makeDataset(name : string, rows : Array<Omit<exampleModel.PrimitiveTemplateRow, "language"|"type">>, dbClient : db.Client, options = {}) {
        return DatasetUtils.examplesToDataset(`org.thingpedia.dynamic.${name}`, this.language, rows, {
            dbClient: dbClient,
            needs_compatibility: this._needsCompatibility,
            thingtalk_version: this._thingtalkVersion,
            ...options
        });
    }

    getExamplesByKey(key : string, accept = 'application/x-thingtalk') {
        return this._withClient(async (dbClient) => {
            const rows = await exampleModel.getByKey(dbClient, key, await this._getOrgId(dbClient), this.language);
            switch (accept) {
            case 'application/x-thingtalk;editMode=1':
                return this._makeDataset(`by_key.${key.replace(/[^a-zA-Z0-9]+/g, '_')}`,
                    rows, dbClient, { editMode: true });
            default:
                return this._makeDataset(`by_key.${key.replace(/[^a-zA-Z0-9]+/g, '_')}`,
                    rows, dbClient);
            }
        });
    }

    getExamplesByKinds(kinds : string[], accept = 'application/x-thingtalk') {
        if (!Array.isArray(kinds))
            kinds = [kinds];
        if (kinds.length === 0)
            return Promise.resolve('');
        return this._withClient(async (dbClient) => {
            const rows = await exampleModel.getByKinds(dbClient, kinds, await this._getOrgId(dbClient), this.language);
            switch (accept) {
            case 'application/x-thingtalk;editMode=1':
                if (kinds.length === 1)
                    return this._makeDataset(kinds[0], rows, dbClient, { editMode: true });

                return this._makeDataset(`by_kinds.${kinds.map((k) => k.replace(/[^a-zA-Z0-9]+/g, '_')).join('__')}`,
                    rows, dbClient, { editMode: true });
            default:
                return this._makeDataset(`by_kinds.${kinds.map((k) => k.replace(/[^a-zA-Z0-9]+/g, '_')).join('__')}`,
                    rows, dbClient);
            }
        });
    }

    getAllExamples(accept = 'application/x-thingtalk') {
        return this._withClient(async (dbClient) => {
            const rows = await exampleModel.getBaseByLanguage(dbClient, await this._getOrgId(dbClient), this.language);
            switch (accept) {
            case 'application/x-thingtalk;editMode=1':
                return this._makeDataset(`everything`, rows, dbClient, { editMode: true });
            default:
                return this._makeDataset(`everything`, rows, dbClient);
            }
        });
    }

    clickExample(exampleId : number) {
        return this._withClient((dbClient) => {
            return exampleModel.click(dbClient, exampleId);
        });
    }

    lookupEntity(entityType : string, searchTerm : string) {
        return this._withClient((dbClient) => {
            return Promise.all([entityModel.lookupWithType(dbClient, this.language, entityType, searchTerm),
                                entityModel.get(dbClient, entityType, this.language)]);
        }).then(([rows, metarows]) => {
            const data = rows.map((r) => ({ type: r.entity_id, value: r.entity_value, canonical: r.entity_canonical, name: r.entity_name }));
            const meta = { name: metarows.name, has_ner_support: metarows.has_ner_support, is_well_known: metarows.is_well_known };
            return { data, meta };
        });
    }

    lookupLocation(searchTerm : string, around ?: {
        latitude : number;
        longitude : number;
    }) {
        return resolveLocation(this.locale, searchTerm, around);
    }

    getAllDeviceNames() {
        return this._withClient(async (dbClient) => {
            return schemaModel.getAllApproved(dbClient, await this._getOrgId(dbClient));
        });
    }

    async getThingpediaSnapshot(getMeta ?: boolean, snapshotId = -1) {
        return this._withClient(async (dbClient) => {
            if (snapshotId >= 0) {
                if (getMeta)
                    return schemaModel.getSnapshotMeta(dbClient, snapshotId, this.language, await this._getOrgId(dbClient));
                else
                    return schemaModel.getSnapshotTypes(dbClient, snapshotId, await this._getOrgId(dbClient));
            } else {
                if (getMeta)
                    return schemaModel.getCurrentSnapshotMeta(dbClient, this.language, await this._getOrgId(dbClient));
                else
                    return schemaModel.getCurrentSnapshotTypes(dbClient, await this._getOrgId(dbClient));
            }
        });
    }

    getAllEntityTypes(snapshotId = -1) : Promise<ExtendedEntityRecord[]> {
        return this._withClient((dbClient) => {
            if (snapshotId >= 0)
                return entityModel.getSnapshot(dbClient, snapshotId);
            else
                return entityModel.getAll(dbClient);
        }).then((rows) => {
            return rows.map((r) => ({
                type: r.id,
                name: r.name,
                is_well_known: r.is_well_known,
                has_ner_support: r.has_ner_support,
                subtype_of: r.subtype_of ? (r.subtype_of.startsWith('[') ? JSON.parse(r.subtype_of) : [r.subtype_of]) : []
            }));
        });
    }

    getAllStrings() {
        return this._withClient((dbClient) => {
            return stringModel.getAll(dbClient, this.language);
        }).then((rows) => {
            return rows.map((r) => ({
                type: r.type_name,
                name: r.name,
                license: r.license,
                attribution: r.attribution
            }));
        });
    }

    invokeQuery() : never {
        throw new Error(`not implemented yet`);
    }
}
