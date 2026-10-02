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

**Not yet deployed from this generated package.**

Fill the following only from observed evidence:

- deployed commit: `PENDING`
- predeployment source SHA-256: `8a0a5f5b5802540ee6c51fc049705b0e039e0c5bc8a72d544e134d06fc8924ad`
- predeployment source bytes: `28949`
- contract address: `PENDING`
- deployment transaction: `PENDING`
- deployment finality: `PENDING`
- consensus result: `PENDING`
- runtime chain ID: `PENDING`
- explorer address URL: `PENDING`
- exact-head CI run: `PENDING`
