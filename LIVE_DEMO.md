# EVIDENCESPEND live lifecycle

Run this only after deployment to **stable Studionet 61999** and only record transactions after they are FINALIZED.

The demo should prove the primitive, not merely deployment.

## Scenario

A release requires two genuinely independent security reviews.

### 1. Create the ledger

Title:

`Release assurance`

Scope:

`Security evidence for release candidate RC-1`

### 2. Add one requirement

- name: `Two independent security reviews`
- definition: `Two materially independent security reviews of RC-1. A rehost, summary, derivative, or materially overlapping review cannot count as the second review.`
- reuse mode: `INDEPENDENT_REQUIRED` (`3`)
- independence group: `7`
- required count: `2`

Seal the ledger.

### 3. Register Evidence A

Use a real bounded evidence descriptor and calculate the SHA-256 of the original artefact off-chain.

Spend Evidence A. Because the requirement has no prior accepted evidence, the expected result is:

`ACCEPTED`

Expected requirement state:

- accepted count: `1`
- remaining: `1`

### 4. Register Evidence B as a repackaged derivative

Use a different content digest and source reference, but make the frozen descriptor truthfully state that B is a summary/repackaging of A.

Spend Evidence B.

Expected GenLayer relation:

`DERIVED_EVIDENCE` or `SAME_EVIDENCE`

Expected final state:

`BLOCKED`

Expected requirement state remains:

- accepted count: `1`
- remaining: `1`

### 5. Register Evidence C as truly independent

Use a genuinely separate reviewer/method/source descriptor.

Spend Evidence C.

Expected relation to Evidence A:

`INDEPENDENT_EVIDENCE`

Expected final state:

`ACCEPTED`

Requirement becomes satisfied:

- accepted count: `2`
- remaining: `0`

## Reviewer evidence to capture

For every write transaction record:

- transaction hash;
- final status;
- consensus result;
- contract address;
- explorer URL;
- method and exact arguments;
- relevant before/after view state.

Also capture:

- `runtime_chain_id()` = `61999`;
- source SHA-256 and byte count from `python scripts/source-digest.py`;
- exact Git commit deployed;
- exact CI run for that commit.

Never describe `ACCEPTED` transaction status as blockchain finality. Require FINALIZED evidence.
