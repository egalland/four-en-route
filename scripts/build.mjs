import { readFileSync, writeFileSync } from 'node:fs';
import { stripTypeScriptTypes } from 'node:module';
writeFileSync('docs/app.js', stripTypeScriptTypes(readFileSync('src/app.ts','utf8')));
