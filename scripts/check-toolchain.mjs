import { execFileSync } from 'node:child_process';
import { readFileSync, existsSync } from 'node:fs';
import path from 'node:path';

const EXPECTED_VERSION = '0.39.1';
const EXPECTED_RPC = 'https://studio.genlayer.com/api';
const EXPECTED_CHAIN = '61999';
const bin = process.platform === 'win32'
  ? path.join('node_modules', '.bin', 'genlayer.cmd')
  : path.join('node_modules', '.bin', 'genlayer');

function fail(message) {
  console.error('EVIDENCESPEND toolchain guard: ' + message);
  process.exit(1);
}

if (!existsSync(bin)) fail('local GenLayer CLI missing; run npm install');
const version = execFileSync(bin, ['--version'], {
  encoding: 'utf8',
  shell: process.platform === 'win32',
}).trim();
if (!version.includes(EXPECTED_VERSION) || /0\.40|rc2/i.test(version)) {
  fail('expected repository-local CLI ' + EXPECTED_VERSION + '; got ' + version);
}
const pkg = JSON.parse(readFileSync('package.json', 'utf8'));
if (pkg?.devDependencies?.genlayer !== EXPECTED_VERSION) {
  fail('package.json must pin genlayer exactly to ' + EXPECTED_VERSION);
}
const cfg = readFileSync('gltest.config.yaml', 'utf8');
if (!cfg.includes(EXPECTED_RPC) || !cfg.includes('studionet:')) {
  fail('stable Studionet RPC/config missing');
}
if (/studio-dev|61997/i.test(cfg)) {
  fail('refusing Studio-dev / 61997 configuration');
}
console.log('OK: repository-local GenLayer CLI ' + EXPECTED_VERSION);
console.log('OK: stable Studionet RPC ' + EXPECTED_RPC);
console.log('Required deployment chain ID: ' + EXPECTED_CHAIN);
