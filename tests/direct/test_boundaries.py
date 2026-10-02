"""Boundary and immutable-policy tests for EVIDENCESPEND."""
CONTRACT = "contracts/evidence_spend.py"
SDK = "v0.2.12"
SHAREABLE = 1
INDEPENDENT = 3


def test_seal_requires_requirement(direct_vm, direct_deploy, direct_alice):
    direct_vm.sender = direct_alice
    c = direct_deploy(CONTRACT, sdk_version=SDK)
    ledger = c.create_ledger("x", "scope")
    with direct_vm.expect_revert("at least one requirement"):
        c.seal_ledger(ledger)


def test_no_requirement_after_seal(direct_vm, direct_deploy, direct_alice):
    direct_vm.sender = direct_alice
    c = direct_deploy(CONTRACT, sdk_version=SDK)
    ledger = c.create_ledger("x", "scope")
    c.add_requirement(ledger, "r", "definition", SHAREABLE, 0, 1)
    c.seal_ledger(ledger)
    with direct_vm.expect_revert("sealed"):
        c.add_requirement(ledger, "r2", "definition", SHAREABLE, 0, 1)


def test_no_consumer_after_seal(direct_vm, direct_deploy, direct_alice, direct_bob):
    direct_vm.sender = direct_alice
    c = direct_deploy(CONTRACT, sdk_version=SDK)
    ledger = c.create_ledger("x", "scope")
    c.add_requirement(ledger, "r", "definition", SHAREABLE, 0, 1)
    c.seal_ledger(ledger)
    with direct_vm.expect_revert("sealed"):
        c.add_authorized_consumer(ledger, direct_bob)


def test_independent_mode_requires_nonzero_group(direct_vm, direct_deploy, direct_alice):
    direct_vm.sender = direct_alice
    c = direct_deploy(CONTRACT, sdk_version=SDK)
    ledger = c.create_ledger("x", "scope")
    with direct_vm.expect_revert("nonzero group"):
        c.add_requirement(ledger, "r", "definition", INDEPENDENT, 0, 1)


def test_invalid_reuse_mode_rejected(direct_vm, direct_deploy, direct_alice):
    direct_vm.sender = direct_alice
    c = direct_deploy(CONTRACT, sdk_version=SDK)
    ledger = c.create_ledger("x", "scope")
    with direct_vm.expect_revert("invalid reuse mode"):
        c.add_requirement(ledger, "r", "definition", 9, 0, 1)


def test_required_count_is_bounded(direct_vm, direct_deploy, direct_alice):
    direct_vm.sender = direct_alice
    c = direct_deploy(CONTRACT, sdk_version=SDK)
    ledger = c.create_ledger("x", "scope")
    with direct_vm.expect_revert("required_count"):
        c.add_requirement(ledger, "r", "definition", SHAREABLE, 0, 0)
    with direct_vm.expect_revert("required_count"):
        c.add_requirement(ledger, "r", "definition", SHAREABLE, 0, 5)


def test_digest_must_be_64_hex(direct_vm, direct_deploy, direct_alice):
    direct_vm.sender = direct_alice
    c = direct_deploy(CONTRACT, sdk_version=SDK)
    with direct_vm.expect_revert("64 lowercase hex"):
        c.register_evidence("x", "abc", "https://example.com/x", "p", "text")
    with direct_vm.expect_revert("64 lowercase hex"):
        c.register_evidence("x", "g" * 64, "https://example.com/x", "p", "text")


def test_requirement_cannot_overfill(direct_vm, direct_deploy, direct_alice):
    direct_vm.sender = direct_alice
    c = direct_deploy(CONTRACT, sdk_version=SDK)
    ledger = c.create_ledger("x", "scope")
    req = c.add_requirement(ledger, "r", "definition", SHAREABLE, 0, 1)
    c.seal_ledger(ledger)
    e1 = c.register_evidence("x", "a" * 64, "https://example.com/1", "p", "text")
    e2 = c.register_evidence("y", "b" * 64, "https://example.com/2", "p", "other")
    c.spend_evidence(req, e1)
    with direct_vm.expect_revert("already satisfied"):
        c.spend_evidence(req, e2)


def test_constants(direct_vm, direct_deploy):
    c = direct_deploy(CONTRACT, sdk_version=SDK)
    x = c.protocol_constants()
    assert x["reuse_shareable"] == 1
    assert x["reuse_exclusive"] == 2
    assert x["reuse_independent"] == 3
    assert x["decision_accepted"] == 1
    assert x["decision_blocked"] == 2
    assert x["decision_ambiguous"] == 3
    assert x["max_required_count"] == 4


def test_runtime_chain(direct_vm, direct_deploy):
    c = direct_deploy(CONTRACT, sdk_version=SDK)
    assert int(c.runtime_chain_id()) >= 0
