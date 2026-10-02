# EVIDENCESPEND architecture

## Primitive boundary

EVIDENCESPEND solves one question:

> May this evidence record count toward this requirement without violating the ledger's frozen evidence-reuse rules?

It intentionally does not decide whether the underlying evidence is true or authoritative.

## Objects

### Ledger

A ledger defines a bounded evidence-consumption domain. The creator configures requirements and optional authorized consumers while the ledger is `OPEN`. Sealing freezes policy.

### Requirement

A requirement contains:

- human-readable definition;
- `reuse_mode`;
- optional `independence_group`;
- deterministic `required_count`;
- accepted evidence IDs.

### Evidence

An immutable evidence record contains:

- registrant;
- label;
- caller-supplied content digest;
- source reference;
- provenance description;
- bounded evidence fingerprint text.

No later mutation method exists.

### SpendDecision

Every semantic attempt produces an auditable receipt:

- `ACCEPTED`;
- `BLOCKED` with first blocker and relation;
- `AMBIGUOUS` with fail-closed relation.

Only accepted decisions enter the ledger's accepted-spend history.

## Comparator selection

The model never selects what should be compared. Deterministic code includes prior accepted evidence when at least one condition holds:

1. it was accepted into the same requirement;
2. the current requirement is `EXCLUSIVE`;
3. the prior requirement was `EXCLUSIVE`;
4. the current requirement is `INDEPENDENT_REQUIRED` and the prior requirement shares its non-zero independence group.

This is the key policy/consensus separation.

## Exact identity shortcut

Relevant records with an identical content digest are deterministically `SAME_EVIDENCE` and blocked. No LLM is called.

## Consensus boundary

For distinct digests, the candidate and all relevant comparators are encoded as untrusted JSON data. The leader classifies one bounded relation per comparator. Validators independently execute the same classifier and require exact agreement on the relation vector.

The prompt is policy-blind. It cannot see requirement reuse mode, required count, accepted count, or desired result.

## Settlement

After consensus:

- any `AMBIGUOUS` relation returns an `AMBIGUOUS` receipt and changes no accepted state;
- any `SAME`, `DERIVED`, or `OVERLAPPING` relation returns a `BLOCKED` receipt and changes no accepted state;
- all relevant relations must be `INDEPENDENT_EVIDENCE` before the evidence can be accepted;
- no relevant prior evidence means the evidence can be accepted without an LLM call.

## Why the contract stores blocked receipts

A rejected attempt is useful protocol history. It demonstrates that the evidence was considered and why it did not consume a requirement, while avoiding mutation of the accepted-spend set.
