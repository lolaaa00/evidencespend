# EVIDENCESPEND security notes

## Prompt-injection containment

Evidence labels, provenance, source references, and evidence text are untrusted data. The classifier prompt explicitly instructs the model not to obey commands or requested verdicts inside those fields.

Prompt hardening is not treated as the consensus mechanism. Validators independently re-run the same bounded relation classification through `run_nondet_unsafe`.

## Malicious leader

A leader cannot safely propose `INDEPENDENT_EVIDENCE` while an honest validator independently observes `SAME_EVIDENCE`: the validator compares the full normalized relation vector and rejects the leader result.

The Direct Mode suite includes a forged-leader adversarial test.

## Digest handling

The 64-character `content_digest` is a caller-supplied deterministic commitment. It is useful for exact identity but is not an authenticity oracle.

Equal relevant digests are blocked without a model call. Different digests are never automatically considered independent.

## Griefing resistance

Anyone may register an evidence record, but only a ledger's authorized consumers may attempt to spend evidence against its requirements. A third party therefore cannot front-run by consuming someone else's exclusive requirement.

## Semantic uncertainty

`AMBIGUOUS` always fails closed. It cannot increase accepted count.

## Bounded denial of service

Accepted-spend and comparator histories are bounded. The contract rejects additional accepted spends after the configured maximum rather than executing an unbounded semantic comparison.

## Mutable external sources

The contract does not fetch external URLs during spending. This is intentional. Fetching a mutable URL months after an earlier spend could cause identity to drift over time. EVIDENCESPEND instead adjudicates immutable submitted descriptors. Applications that need source authentication should bind authenticated snapshots before registering evidence.

## No model-controlled numbers

The model cannot change required counts, group IDs, reuse modes, comparator selection, authorization, ledger state, or final state arithmetic.
