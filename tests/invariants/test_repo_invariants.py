from pathlib import Path
import ast
import json

ROOT = Path(__file__).resolve().parents[2]
CONTRACT = ROOT / "contracts" / "evidence_spend.py"


def source():
    return CONTRACT.read_text()


def test_contract_parses_as_python():
    ast.parse(source())


def test_contract_is_single_primary_intelligent_contract():
    s = source()
    assert "class EvidenceSpend(gl.Contract)" in s
    assert "class EvidenceSpend" in s


def test_consensus_boundary_is_custom_validator_not_format_only():
    s = source()
    assert "run_nondet_unsafe" in s
    assert "validator_fn" in s
    assert "own = classify_relations" in s
    assert "leader_relations == own_relations" in s


def test_relation_vocabulary_is_bounded():
    s = source()
    for relation in (
        "SAME_EVIDENCE",
        "DERIVED_EVIDENCE",
        "OVERLAPPING_EVIDENCE",
        "INDEPENDENT_EVIDENCE",
        "AMBIGUOUS",
    ):
        assert relation in s


def test_exact_digest_identity_is_deterministic():
    s = source()
    assert "content_digest" in s
    assert "str(prior.content_digest) == str(evidence.content_digest)" in s


def test_llm_does_not_decide_reuse_policy_or_counts():
    s = source()
    body = s[s.index("def relation_prompt"):s.index("def classify_relations")]
    assert '"reuse_mode"' not in body
    assert '"required_count"' not in body
    assert '"accepted_count"' not in body
    assert "Do not consider any reuse policy" in body


def test_no_web_fetch_or_external_source_claim_is_hidden_in_consensus():
    s = source()
    assert "nondet.web" not in s
    assert "Judge only the frozen submitted descriptors" in s


def test_ambiguous_fails_closed_without_acceptance():
    s = source()
    assert "DECISION_AMBIGUOUS" in s
    assert "relation == REL_AMBIGUOUS_NAME" in s


def test_authorized_consumers_are_frozen_on_seal():
    s = source()
    assert "add_authorized_consumer" in s
    assert "ledger is sealed" in s
    assert "caller is not authorized for ledger" in s


def test_contract_is_bounded():
    s = source()
    for name in ("MAX_REQUIREMENTS", "MAX_ACCEPTED_SPENDS", "MAX_COMPARATORS", "MAX_REQUIRED_COUNT"):
        assert name in s


def test_runtime_chain_id_is_exposed():
    assert "def runtime_chain_id" in source()


def test_local_genlayer_cli_is_exactly_pinned():
    pkg = json.loads((ROOT / "package.json").read_text())
    assert pkg["devDependencies"]["genlayer"] == "0.39.1"


def test_studionet_rpc_is_stable_and_no_studio_dev():
    cfg = (ROOT / "gltest.config.yaml").read_text().lower()
    assert "https://studio.genlayer.com/api" in cfg
    assert "studionet:" in cfg
    assert "61997" not in cfg
    assert "studio-dev" not in cfg


def test_toolchain_guard_requires_chain_61999():
    guard = (ROOT / "scripts" / "check-toolchain.mjs").read_text()
    assert "61999" in guard
    assert "0.39.1" in guard
    assert "61997" in guard  # guard explicitly refuses it


def test_repo_has_no_frontend_directory():
    assert not (ROOT / "frontend").exists()
    assert not (ROOT / "app").exists()


def test_no_backend_framework_dependencies():
    for p in ROOT.rglob("*"):
        if p == Path(__file__):
            continue
        if any(part in {"node_modules", ".venv", ".git", "artifacts"} for part in p.parts):
            continue
        if p.is_file() and p.suffix in {".py", ".js", ".mjs", ".json", ".md"}:
            text = p.read_text(errors="ignore").lower()
            assert "supabase" not in text
            assert "firebase" not in text
            assert "express()" not in text


def test_direct_mode_pin_is_v0212():
    tests = "\n".join(p.read_text() for p in (ROOT / "tests" / "direct").glob("*.py"))
    assert 'SDK = "v0.2.12"' in tests


def test_submission_does_not_claim_unobserved_deployment():
    text = (ROOT / "SUBMISSION.md").read_text().lower()
    assert "not yet deployed" in text
    assert "fill only after" in text
