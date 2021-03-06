// -*- mode: typescript; indent-tabs-mode: nil; js-basic-offset: 4 -*-
//
// This file is part of Genie
//
// Copyright 2021 The Board of Trustees of the Leland Stanford Junior University
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

import { Ast, } from 'thingtalk';
import {
    ContextInfo,
} from '../state_manip';

export function checkIsReminder(ctx : ContextInfo, fname : string) : ContextInfo|null {
    if (ctx.currentFunction!.qualifiedName !== ('org.thingpedia.builtin.thingengine.builtin.' + fname))
        return null;

    if (!(ctx.current!.stmt.stream instanceof Ast.FunctionCallExpression && (ctx.current!.stmt.stream.name === 'ontimer'
        || ctx.current!.stmt.stream.name === 'attimer' || ctx.current!.stmt.stream.name === 'timer')))
        return null;

    return ctx;
}
