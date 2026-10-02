# EVIDENCESPEND reviewer evidence

## Status

Deployed and exercised on stable Studionet 61999 on 2 October 2026.

## Repository proof

- repository: `https://github.com/lolaaa00/evidencespend`
- deployed source commit: `a32dd78a8537a35ff9926f92e607dd39e8c72d9f`
- predeployment exact-head CI: `https://github.com/lolaaa00/evidencespend/actions/runs/37005025968` (`success`)
- source file: `contracts/evidence_spend.py`
- source SHA-256: `8a0a5f5b5802540ee6c51fc049705b0e039e0c5bc8a72d544e134d06fc8924ad`
- source byte count: `28949`

## Deployment proof

- network: Studionet
- chain ID: `61999`
- RPC: `https://studio.genlayer.com/api`
- CLI: repository-local `0.39.1`
- signer: `probe` / `0xaa18ecd158aec67c75a51768b747cb3247a21689`
- contract address: `0xed7c9bC18b9881984F248Fa0FF1eeec30d701571`
- deployment transaction: `0xd3a1e2981ef0c0c18b01ccf1408ace2f10ebb05b0a76f9062eb4273a584d7c18`
- finality: `FINALIZED`
- consensus result: `MAJORITY_AGREE`
- execution result: `SUCCESS`
- runtime chain ID: `61999`
- explorer: `https://genlayer-explorer.vercel.app`

## Test proof

- GenVM SDK pin: `v0.2.12`
- gltest pin: `v0.29.2`
- local Direct Mode: `35 passed, 0 failed`
- local invariants: `18 passed, 0 failed`
- predeployment CI: `success`

## Live lifecycle

All transaction hashes below were observed as `FINALIZED` with `MAJORITY_AGREE`.

### Ledger and requirements

- ledger ID: `1`
- create ledger tx: `0x0bfb2e76807716e8834828f85c96613ade43b2b3d5b5b09d0080c50ca2da1df3`
- requirement `1`: `INDEPENDENT_REQUIRED`, group `7`, count `2`; tx `0xa3b60cc9b75f06d050a9b1a70e1a6b9a0edb446dfc026731577a394db462181b`
- requirement `2`: `SHAREABLE`; tx `0xb04314740b50001df138b59421557197fcdc32f70373bd9ee038071e08eac93c`
- requirement `3`: `SHAREABLE`; tx `0x051a05601d3d251b4d48ab1445f27ab23889a15cd0f03aa6d998fcbfc4cd3198`
- requirement `4`: `EXCLUSIVE`; tx `0x97c8f9a2f19f5314439d165ddc06b22e55e5fd4a811f4d0d4a6c00870fdc284c`
- requirement `5`: post-exclusive reuse probe; tx `0xcd1c8136d21f78827dec2e3ee7ae74c325ae72be73a26272cc325e0358dd943c`
- seal tx: `0x7cb12785a84e3b76911184555c02ec9ead12e9e940f141be5732db11a36d4836`

### Evidence records

- evidence `1`: RFC 9110 text, digest `21c1cdce6ab0e5509b04d84a28000836c7a087cf786efe6f04877ebfff47232a`; registration tx `0x8c4de0c96f68203b7462c15cbc55dd5799427c31bc8ff149dbd7f546628cc49b`
- evidence `2`: RFC 9110 mirror, same digest; registration tx `0xee56f6fe9fceab3170c78e64f9de36c05744046dca4210ccd7704b4424289416`
- evidence `3`: NIST SP 800-115 PDF, digest `58e5ed41e5c8ca34ce14fd80b70f118f2c6d613d1647bc307edca30bcc45f063`; registration tx `0x4aae12407c9e5fdac35986b6427a48fcb46e704b12d4cc1f9e7811077ac7015d`
- evidence `4`: NIST SP 800-115 landing page, digest `8f72c41be52d4d3923fad5d434374e95493bd7b9cf34ec060257205478d379b7`; registration tx `0xbcc93a46a4a662ea8a5157f8f6e7e9e33ecd89bfed6c55cbc195cc3c166f785c`
- evidence `5`: OWASP Testing Guide v4, digest `f85a2a25c5a9c288776165dc9e82c0d740dfd476fa2f7f26cb2bcb9210294577`; registration tx `0xb7ba67597b3c1473f68678ca2e1c0f2b04a79b09b449b64108f9f783068aec55`

### Policy proofs

- EXCLUSIVE acceptance: decision `1`, evidence `1`, status `ACCEPTED`; tx `0x374e1049f828fe35c11e805b62ab8c82acbffac9319b3c41bd44a19a083389c3`
- exact duplicate after exclusive spend: decision `2`, evidence `2`, status `BLOCKED`, relation `SAME_EVIDENCE`, blocker `1`; tx `0x6b1f75ac26296962a6afcc40c55cf59b2dea5f67d35818ef7e4263fc6ec2239c`
- independent requirement first item: decision `3`, evidence `3`, status `ACCEPTED`; tx `0x2754d750069fe5ac72ca4239ea029a001acf4f168731f8e0a9bd8ba9254b4451`
- different-digest semantic reuse: decision `4`, evidence `4`, status `BLOCKED`, relation `SAME_EVIDENCE`, blocker `3`; tx `0x8d337c3795af4ca74a3a490299098311bcd209259a3db819ca2299d7bd2bb49b`
- genuinely independent item: decision `5`, evidence `5`, status `ACCEPTED`; tx `0x1ab21ba0a32db35047938426c5c000134f60e9dfdda4a522c54e108d6f0e3383`
- requirement `1` final state: accepted evidence `[3, 5]`, accepted count `2`, satisfied `true`
- SHAREABLE proof one: decision `6`, evidence `3`, requirement `2`, status `ACCEPTED`; tx `0x6c657de45fe509fe9a943951a623d51ae882f1e4f9c824a3df4fab337b27ff8f`
- SHAREABLE proof two: decision `7`, the same evidence `3`, requirement `3`, status `ACCEPTED`; tx `0x1f60f7da1a37f3c096b2b70ca7fbdce76003389e13ad811e19d1c0fb6e491027`
- final ledger accepted-spend IDs: `[1, 3, 5, 6, 7]`; blocked decisions `2` and `4` did not enter accepted history

## Digest/view boundary

`get_evidence(3)` returned the exact registered digest `58e5ed41e5c8ca34ce14fd80b70f118f2c6d613d1647bc307edca30bcc45f063`.
The frozen contract does not expose a consumer method that accepts an expected digest and returns true/false, so an altered-expected-hash false result is not claimed. Exact digest equality is instead enforced during relevant spend comparison, as decision `2` demonstrates.

## Hostile audit

- validators independently recompute and require the exact normalized relation vector;
- equal relevant digests are blocked before semantic consensus;
- distinct-digest sameness, derivation, overlap, independence, and ambiguity use a bounded vocabulary;
- submitted descriptors are explicitly treated as hostile data;
- only accepted decisions mutate accepted counts and accepted-spend history;
- comparator selection, authorization, reuse policy, and settlement are deterministic and bounded;
- no contract defect was found in hostile review, Direct Mode, or the finalized live lifecycle.

## Scope limitation

The contract accounts for semantic evidence reuse. It does not prove truth, authorship, URL authenticity, legal independence, or the correctness of caller-supplied digests.
