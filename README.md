# EVIDENCESPEND

**Semantic double-spend protection for evidentiary artefacts.**

EVIDENCESPEND is a standalone reusable GenLayer Intelligent Contract primitive with **no frontend**.

Blockchains prevent the same token from being spent twice. Evidence-heavy protocols have an analogous problem: one underlying report, observation, audit, interview, measurement, or analysis can be rehosted, reformatted, paraphrased, summarised, or repackaged and then presented as if it were independent proof for multiple obligations.

EVIDENCESPEND makes evidence reuse explicit and enforceable.

```text
Requirement A: independent security audit      <- Report X accepted
Requirement B: independent operational review  <- Report X summary submitted

Exact hashes differ.
URLs differ.
Wording differs.

GenLayer consensus:
DERIVED_EVIDENCE

Deterministic protocol:
BLOCKED
```

## What the model decides

Only the semantic relationship between one candidate evidence record and the bounded set of prior evidence records relevant to the current reuse rule:

- `SAME_EVIDENCE`
- `DERIVED_EVIDENCE`
- `OVERLAPPING_EVIDENCE`
- `INDEPENDENT_EVIDENCE`
- `AMBIGUOUS`

Validators independently re-run that classification through a custom `run_nondet_unsafe` validator.

## What deterministic code decides

The model never sees or chooses the reuse policy. Deterministic contract logic owns:

- whether a requirement is `SHAREABLE`, `EXCLUSIVE`, or `INDEPENDENT_REQUIRED`;
- which previous accepted evidence is relevant to compare;
- exact-digest identity;
- authorization;
- how many evidence items a requirement needs;
- whether an accepted item fills the requirement;
- whether a prior exclusive spend reserves an evidence cluster;
- whether an independence group is satisfied;
- all final `ACCEPTED | BLOCKED | AMBIGUOUS` state transitions.

## Reuse modes

### SHAREABLE

The same evidence may satisfy different requirements unless a previous or current requirement reserves it exclusively. Within one multi-item requirement, separate counted items must still be independent so one report cannot count twice toward `required_count`.

### EXCLUSIVE

Evidence accepted under an exclusive requirement semantically reserves that underlying evidentiary work. A later requirement cannot consume the same, derived, or materially overlapping evidence, even if the new record has a different hash or URL.

### INDEPENDENT_REQUIRED

Requirements can share a non-zero `independence_group`. Evidence accepted into one member of the group must be semantically independent from prior accepted evidence in that group.

## Exact hashes first, semantic consensus second

Every evidence record carries a caller-supplied 64-character SHA-256-style content commitment. When two relevant records have the same digest, EVIDENCESPEND deterministically treats them as the same artefact and never calls the model.

Different digests do **not** imply independence. Different files may still be the same underlying work in a new wrapper, which is exactly where GenLayer consensus is used.

## Important trust boundary

EVIDENCESPEND does **not** claim that submitted evidence is true, authentic, authoritative, or currently available at its `source_ref`.

The contract deliberately judges only immutable submitted evidence descriptors. Authentication can be supplied by an upstream primitive or application. This keeps the primitive narrow: **evidence identity/reuse is separated from evidence truth**.

The `content_digest` is a registrant-provided commitment and is not fetched from the internet by this contract. Authorized consumers decide which evidence records to attempt to spend.

## Why this is reusable

Possible consumers include:

- grant and milestone systems requiring multiple independent reviews;
- security programmes requiring independent audits;
- governance systems requiring distinct attestations;
- research reproducibility workflows;
- insurance claims requiring separate evidence sources;
- procurement and compliance systems where one report must not satisfy multiple independent controls;
- agent assurance systems that require genuinely separate evaluations.

## Contract flow

```text
create_ledger
    |
    +-- add_requirement(... SHAREABLE ...)
    +-- add_requirement(... EXCLUSIVE ...)
    +-- add_requirement(... INDEPENDENT_REQUIRED, group=7 ...)
    +-- authorize bounded consumers
    |
seal_ledger
    |
register_evidence  (any registrant; immutable evidence record)
    |
spend_evidence     (authorized consumer only)
    |
    +-- exact relevant digest duplicate? ----------> BLOCKED
    |
    +-- no relevant prior evidence? --------------> ACCEPTED
    |
    +-- consensus relation to prior evidence
           |
           +-- all INDEPENDENT_EVIDENCE ----------> ACCEPTED
           +-- SAME / DERIVED / OVERLAPPING ------> BLOCKED
           +-- any AMBIGUOUS ---------------------> AMBIGUOUS
```

## Bounded state

The reference implementation intentionally bounds consensus work:

- up to 12 requirements per ledger;
- up to 16 accepted spends per ledger;
- up to 16 semantic comparators per spend;
- up to 4 counted evidence items per requirement;
- up to 8 authorized consumers including the creator.

This keeps semantic comparison cost explicit rather than hiding unbounded loops behind a reusable interface.

## Network and toolchain

This repository is for **stable Studionet only**:

- network: `studionet`
- chain ID: **61999**
- RPC: `https://studio.genlayer.com/api`
- repository-local GenLayer CLI: **0.39.1**
- Direct Mode GenVM SDK pin in tests: **v0.2.12**
- `gltest`: **v0.29.2**
- no Studio-dev
- no chain 61997
- no frontend
- no application backend

## Local verification

```bash
npm install
npm run toolchain:check
python scripts/repo-preflight.py
pytest tests/invariants -q
pip install -r requirements-test.txt
pytest tests/direct -v -s
python scripts/source-digest.py
```

Direct Mode dependencies require network access during initial installation. CI runs the same checks on Ubuntu.

## Documentation

- `docs/ARCHITECTURE.md`
- `docs/SECURITY.md`
- `docs/INVARIANTS.md`
- `docs/THREAT_MODEL.md`
- `LIVE_DEMO.md`
- `DEPLOYMENT.md`
- `REVIEW_EVIDENCE.md`
- `SUBMISSION.md`

Deployment evidence files intentionally contain no fabricated transaction data. They must only be filled from actual finalized Studionet 61999 observations.
