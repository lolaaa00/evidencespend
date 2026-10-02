# EVIDENCESPEND reviewer evidence

## Status

**NOT YET DEPLOYED from this generated package.**

This file must remain factual. Fill only after actual execution on stable Studionet 61999.

## Repository proof

- repository: `https://github.com/lolaaa00/evidencespend`
- final submission commit: `PENDING`
- exact-head CI run: `PENDING`
- source file: `contracts/evidence_spend.py`
- predeployment source SHA-256: `8a0a5f5b5802540ee6c51fc049705b0e039e0c5bc8a72d544e134d06fc8924ad`
- predeployment source byte count: `28949`

## Deployment proof

- network: Studionet
- chain ID: `61999`
- RPC: `https://studio.genlayer.com/api`
- CLI: repository-local `0.39.1`
- contract address: `PENDING`
- deployment transaction: `PENDING`
- finality: `PENDING`
- consensus result: `PENDING`
- explorer URL: `PENDING`
- `runtime_chain_id()`: `PENDING`

## Direct Mode proof

- GenVM SDK pin: `v0.2.12`
- gltest pin: `v0.29.2`
- local direct tests: `35 passed, 0 failed` (Python 3.12.13)
- local invariant tests: `18 passed, 0 failed`
- CI status: `PENDING`

## Predeployment hostile audit

- malicious-leader defense: custom validator independently recomputes and requires the exact normalized relation vector;
- exact duplicate defense: relevant equal digests are blocked deterministically before semantic consensus;
- derivative/overlap/ambiguity handling: bounded vocabulary and fail-closed settlement are enforced by deterministic code;
- prompt injection boundary: all submitted descriptors are labeled untrusted data and validators re-run classification;
- state mutation: only accepted decisions enter accepted-spend history or increment accepted count;
- policy separation: comparator selection and `SHAREABLE`, `EXCLUSIVE`, and `INDEPENDENT_REQUIRED` settlement remain deterministic;
- authorization and bounds: configuration freezes on seal, spending is limited to authorized consumers, and all state/consensus loops are capped;
- finding: no contract defect found in the predeployment audit or the 35-test Direct Mode suite.

## Live lifecycle

### Ledger creation

- tx: `PENDING`
- finality: `PENDING`

### Requirement creation and seal

- add requirement tx: `PENDING`
- seal tx: `PENDING`

### Evidence A accepted

- evidence registration tx: `PENDING`
- spend tx: `PENDING`
- decision ID: `PENDING`
- state after: `PENDING`

### Evidence B semantic reuse blocked

- evidence registration tx: `PENDING`
- spend tx: `PENDING`
- observed relation: `PENDING`
- blocker evidence ID: `PENDING`
- requirement state unchanged: `PENDING`

### Evidence C independent and accepted

- evidence registration tx: `PENDING`
- spend tx: `PENDING`
- observed relation: `PENDING`
- requirement satisfied: `PENDING`

## Claims reviewers can verify after completion

Do not mark these VERIFIED until the evidence above exists:

- [ ] deployed source matches repository source
- [ ] deployment is FINALIZED on chain 61999
- [ ] exact digest duplicate is blocked deterministically
- [ ] semantic derivative/reuse is blocked under consensus
- [ ] independent evidence is accepted
- [ ] blocked/ambiguous attempts do not increase accepted count
- [ ] requirement reaches satisfied state only after enough independent evidence
