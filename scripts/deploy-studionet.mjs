import { execFileSync } from 'node:child_process';
import { existsSync } from 'node:fs';
import path from 'node:path';

const VERSION = '0.39.1';
const RPC = 'https://studio.genlayer.com/api';
const CHAIN = '61999';
const bin = process.platform === 'win32'
  ? path.join('node_modules', '.bin', 'genlayer.cmd')
  : path.join('node_modules', '.bin', 'genlayer');
const opts = { shell: process.platform === 'win32' };

function fail(message) {
  console.error('EVIDENCESPEND deploy guard: ' + message);
  process.exit(1);
}

if (!existsSync(bin)) fail('run npm install first');
const version = execFileSync(bin, ['--version'], { encoding: 'utf8', ...opts }).trim();
if (!version.includes(VERSION) || /0\.40|rc2/i.test(version)) {
  fail('refusing deployment with ' + version);
}
execFileSync(bin, ['network', 'set', 'studionet'], { stdio: 'inherit', ...opts });
const info = execFileSync(bin, ['network', 'info'], { encoding: 'utf8', ...opts });
console.log(info);
if (!info.includes(CHAIN) || !info.includes('studio.genlayer.com')) {
  fail('network info did not prove stable Studionet ' + CHAIN);
}
execFileSync(
  bin,
  ['deploy', '--contract', 'contracts/evidence_spend.py', '--rpc', RPC],
  { stdio: 'inherit', ...opts },
);
