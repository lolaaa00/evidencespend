# EVIDENCESPEND deployment

## Non-negotiable network

Use **stable Studionet only**:

- chain ID: `61999`
- RPC: `https://studio.genlayer.com/api`
- repository-local GenLayer CLI: `0.39.1`

Do **not** use:

- chain `61997`;
- Studio-dev;
- global CLI `0.40.0rc2`;
- any RC network/toolchain substituted for the pinned repository configuration.

## Windows-friendly preparation

From the unzipped repository folder:

```powershell
npm install
npx genlayer --version
npm run toolchain:check
python scripts/repo-preflight.py
pytest tests/invariants -q
```

Create/activate a Python virtual environment if desired, then install Direct Mode tooling:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements-test.txt
pytest tests/direct -v -s
```

## Network proof

```powershell
npx genlayer network set studionet
npx genlayer network info
```

Do not proceed unless network info proves chain `61999` and the stable Studio endpoint.

## Deploy

```powershell
npm run deploy:studionet
```

After deployment, call `runtime_chain_id()` and require exactly `61999`.

## Finality

Deployment and lifecycle writes are not review evidence until their transactions are FINALIZED. Capture final status and consensus outcome from Studio/explorer.

## Deployment record

- deployed source commit: `a32dd78a8537a35ff9926f92e607dd39e8c72d9f`
- source SHA-256: `8a0a5f5b5802540ee6c51fc049705b0e039e0c5bc8a72d544e134d06fc8924ad`
- source bytes: `28949`
- contract address: `0xed7c9bC18b9881984F248Fa0FF1eeec30d701571`
- deployment transaction: `0xd3a1e2981ef0c0c18b01ccf1408ace2f10ebb05b0a76f9062eb4273a584d7c18`
- deployment finality: `FINALIZED`
- consensus result: `MAJORITY_AGREE`
- execution result: `SUCCESS`
- runtime chain ID: `61999`
- explorer: `https://genlayer-explorer.vercel.app`
- predeployment exact-head CI: `https://github.com/lolaaa00/evidencespend/actions/runs/37005025968` (`success`)

See `REVIEW_EVIDENCE.md` for finalized lifecycle transactions and policy proofs.
