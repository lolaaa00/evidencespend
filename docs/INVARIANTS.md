# EVIDENCESPEND invariants

1. **Policy immutability after seal**  
   Requirements and authorized consumers cannot be added after the ledger is sealed.

2. **Only authorized consumers spend**  
   Registering evidence does not grant the registrant permission to consume a ledger requirement.

3. **Exact digest wins deterministically**  
   Relevant records with identical content digests are always treated as the same artefact. An LLM cannot override this.

4. **One item cannot count twice toward one requirement**  
   Every additional counted item in the same requirement must be semantically independent from its prior counted items.

5. **Exclusive reservation is bidirectional in time**  
   A current exclusive requirement cannot reuse a prior shareable artefact, and a prior exclusive spend prevents later semantic reuse by a shareable requirement.

6. **Independence groups fail closed**  
   An `INDEPENDENT_REQUIRED` requirement compares against prior accepted evidence in its group and only accepts `INDEPENDENT_EVIDENCE`.

7. **Ambiguity never consumes evidence**  
   `AMBIGUOUS` produces a receipt but does not increase accepted count or append an accepted spend.

8. **Blocked attempts never mutate accepted state**  
   A blocked receipt exists for auditability, but the requirement and ledger accepted-spend histories remain unchanged.

9. **The model cannot choose policy**  
   The relation prompt does not contain reuse mode, independence policy, counts, authorization, or final settlement rules.

10. **Bounded consensus work**  
    The ledger and comparator sets are explicitly capped. A transaction does not silently grow into an unbounded semantic loop.

11. **No hidden evidence-authentication claim**  
    The contract does not fetch `source_ref` and never claims that a source is authentic, truthful, current, or authoritative.

12. **Stable Studionet only for this repository**  
    Deployment guard requires repository-local CLI 0.39.1 and chain 61999. 61997/Studio-dev is explicitly rejected.
