// -*- mode: typescript; indent-tabs-mode: nil; js-basic-offset: 4 -*-
//
// This file is part of Genie
//
// Copyright 2019-2021 The Board of Trustees of the Leland Stanford Junior University
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

import * as argparse from 'argparse';
import * as fs from 'fs';
import * as Tp from 'thingpedia';

import * as StreamUtils from '../lib/utils/stream-utils';

import { getConfig, DEFAULT_THINGPEDIA_URL } from './lib/argutils';

export function initArgparse(subparsers : argparse.SubParser) {
    const parser = subparsers.add_parser('download-templates', {
        add_help: true,
        description: "Download primitive templates from Thingpedia."
    });
    parser.add_argument('-l', '--locale', {
        required: false,
        default: 'en-US',
        help: `BGP 47 locale tag of the natural language to download the snapshot for (defaults to 'en-US', American English)`
    });
    parser.add_argument('--thingpedia-url', {
        required: false,
        help: `base URL of Thingpedia server to contact; defaults to '${DEFAULT_THINGPEDIA_URL}'`
    });
    parser.add_argument('--developer-key', {
        required: false,
        default: '',
        help: `developer key to use when contacting Thingpedia`
    });
    parser.add_argument('-o', '--output', {
        required: true,
        type: fs.createWriteStream
    });
}

export async function execute(args : any) {
    if (!args.thingpedia_url)
        args.thingpedia_url = await getConfig('thingpedia.url', process.env.THINGPEDIA_URL || DEFAULT_THINGPEDIA_URL);
    if (!args.developer_key)
        args.developer_key = await getConfig('thingpedia.developer-key', process.env.THINGPEDIA_DEVELOPER_KEY || null);

    let url = args.thingpedia_url + '/api/v3/examples/all?locale=' + args.locale;
    if (args.developer_key)
        url += '&developer_key=' + args.developer_key;

    args.output.end(await Tp.Helpers.Http.get(url, { accept: 'application/x-thingtalk' }));
    await StreamUtils.waitFinish(args.output);
}
