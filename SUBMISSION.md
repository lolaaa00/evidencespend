# EVIDENCESPEND submission notes

## One-line description

EVIDENCESPEND prevents the same underlying evidentiary work from being counted twice when hashes, URLs, formatting or wording change.

## Overview

Blockchains prevent double-spending of tokens. Evidence-heavy protocols need an analogous primitive for proof. The same audit, observation, report or analysis can be rehosted, summarised or repackaged and then presented as if it were independent evidence for several obligations.

EVIDENCESPEND separates semantic identity from deterministic policy. Evidence records are immutable. Exact matching content commitments are identified deterministically. For distinct commitments, GenLayer validators independently classify the candidate against the bounded relevant history as `SAME_EVIDENCE`, `DERIVED_EVIDENCE`, `OVERLAPPING_EVIDENCE`, `INDEPENDENT_EVIDENCE` or `AMBIGUOUS`. Deterministic contract code alone selects comparator scope and enforces `SHAREABLE`, `EXCLUSIVE` and `INDEPENDENT_REQUIRED` reuse rules.

The model never sees requirement reuse mode, authorization, required counts or accepted counts and cannot choose final settlement. Ambiguity fails closed without consuming a requirement.

The primitive deliberately does not authenticate or judge the truth of evidence; upstream systems may bind authenticated evidence snapshots before registering them. Its reusable job is narrower: stop semantic evidence reuse from masquerading as independent proof.

## Network

Stable Studionet, chain `61999`, RPC `https://studio.genlayer.com/api`.

Repository-local CLI `0.39.1`. Direct Mode SDK pin `v0.2.12`. No frontend.

## Evidence status

**Not yet deployed from this generated package. Fill only after actual finalised 61999 deployment and lifecycle execution.**

See `REVIEW_EVIDENCE.md`.
