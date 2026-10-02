# EVIDENCESPEND threat model

## Protected property

A ledger should not count one underlying evidentiary work product as multiple independent or exclusively consumable proofs merely because it has been repackaged into different records.

## Adversaries considered

### Rehosting

The same artefact is uploaded under another URL and a new evidence ID.

Mitigation: identical digest blocks deterministically; different digest can still be `SAME_EVIDENCE` under consensus.

### Paraphrasing or summarising

A report is rewritten or condensed to appear new.

Mitigation: bounded semantic relations include `DERIVED_EVIDENCE`.

### Partial repackaging

A candidate reuses material portions of an earlier audit while adding small independent material.

Mitigation: `OVERLAPPING_EVIDENCE` fails independence-sensitive reuse.

### Prompt injection

Evidence text instructs the model to label itself independent.

Mitigation: untrusted-data prompt boundary plus independent validator rerun.

### Malicious leader

Leader proposes an independence result that validators do not reproduce.

Mitigation: custom validator requires exact normalized relation-vector agreement.

### Unauthorized front-running

An outsider tries to consume a ledger requirement before the intended consumer.

Mitigation: only frozen authorized consumers may spend.

## Out of scope

EVIDENCESPEND does not prove:

- that evidence is factually true;
- that its issuer is who the record claims;
- that a source URL is official;
- that the caller supplied the correct content digest;
- legal independence under any jurisdiction;
- that an upstream authentication primitive is secure.

These are deliberate boundaries, not hidden assumptions.
