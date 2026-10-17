#!/usr/bin/env python3
"""Adversarial tests of full-problem research review coverage (NOT theorem tests)."""
from copy import deepcopy
from pathlib import Path
from runpy import run_path
import json

module=run_path(str(Path(__file__).resolve().with_name("validate_full_review.py")))
check=module["validate"]
current=json.loads(module["CURRENT"].read_text(encoding="utf8"))
assert check(current)==6

def must_reject(description, mutator):
    corrupted=deepcopy(current)
    mutator(corrupted)
    try:
        check(corrupted)
    except (ValueError,TypeError,KeyError):
        print("PASS rejection:",description)
        return
    raise AssertionError("FALSE ACCEPTANCE: "+description)

must_reject("pretend BSD is proved",lambda d:d["status_flags"].update(general_BSD_proved=True))
must_reject("pretend L'' zero proved",lambda d:d["status_flags"].update(exact_complex_Lpp_zero_proved=True))
must_reject("fabricated independent review",lambda d:d.update(reviewer_type="independent_peer_review"))
must_reject("new theorem untracked",lambda d:d["new_proven_bridge_evidence"].append("source-free proof"))
must_reject("omit parked H4",lambda d:d["tracks"].pop(3))
must_reject("duplicate H1",lambda d:d["tracks"][1].update(track="H1"))
must_reject("missing open obstruction",lambda d:d.update(deepest_open_implication="solved"))
must_reject("no negative control",lambda d:d.update(negative_control_reviewed=""))
must_reject("review scheduled more than a week ahead",lambda d:d.update(next_due_on="2026-11-10"))
must_reject("empty evidence classification",lambda d:d.update(evidence_classes=[]))
must_reject("missing immutable journal",lambda d:d.update(journal_path="research/reviews/missing.md"))
must_reject("missing claim ledger coverage",lambda d:d["claim_ids_audited"].remove("C-0008"))
must_reject("unsafe external file path",lambda d:d["sources"].append("../../etc/passwd"))
print("PASS: 13 full-problem integrity negative controls")
