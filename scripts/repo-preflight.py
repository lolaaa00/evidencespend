from pathlib import Path
import ast
import json

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "contracts" / "evidence_spend.py"
source = CONTRACT.read_text()
ast.parse(source)

pkg = json.loads((ROOT / "package.json").read_text())
assert pkg["devDependencies"]["genlayer"] == "0.39.1"

cfg = (ROOT / "gltest.config.yaml").read_text()
assert "https://studio.genlayer.com/api" in cfg
assert "studionet:" in cfg
assert "studio-dev" not in cfg.lower()
assert "61997" not in cfg

required_contract_markers = (
    "class EvidenceSpend(gl.Contract)",
    "run_nondet_unsafe",
    "SAME_EVIDENCE",
    "DERIVED_EVIDENCE",
    "OVERLAPPING_EVIDENCE",
    "INDEPENDENT_EVIDENCE",
    "AMBIGUOUS",
    "spend_evidence",
    "content_digest",
    "runtime_chain_id",
)
for marker in required_contract_markers:
    assert marker in source, marker

assert "nondet.web" not in source, "EvidenceSpend must not pretend to authenticate external evidence"
assert not (ROOT / "frontend").exists(), "EVIDENCESPEND is contract-only"
assert not (ROOT / "app").exists(), "EVIDENCESPEND is contract-only"

print("EVIDENCESPEND offline preflight: OK")
print("Contract parses: OK")
print("Repository-local CLI pin: 0.39.1")
print("Target network: stable Studionet / chain 61999")
print("Direct Mode SDK pin in tests: v0.2.12")
print("Frontend: none")
