#!/usr/bin/env python3
"""Negative-control tests for the research manifest validator."""
from copy import deepcopy
import json
from pathlib import Path
from runpy import run_path
module = run_path(str(Path(__file__).resolve().with_name("validate.py")))
MANIFEST, validate = module["MANIFEST"], module["validate"]

base=json.loads(MANIFEST.read_text(encoding="utf8"))
assert validate(base)==len(base["experiments"])

def rejects(mutator, label):
    candidate=deepcopy(base)
    mutator(candidate)
    try:
        validate(candidate)
    except ValueError:
        print("PASS negative control:",label)
        return
    raise AssertionError("Validator wrongly accepted: "+label)

rejects(lambda x: x["experiments"][0].update({"human_reviewed":True}),
        "unattributed expert-review claim")
rejects(lambda x: x["experiments"][0].update({"status":"externally_reviewed"}),
        "external status without reviewer")
rejects(lambda x: x["experiments"][0]["cross_disciplines"][1].pop("proof_boundary"),
        "analogy missing mathematical limitation")
rejects(lambda x: x["experiments"][0].update({"claim_ids":["C-9999"]}),
        "invented claim ID")
rejects(lambda x: x["experiments"][0].update({"negative_control":""}),
        "no falsifier")
rejects(lambda x: x["experiments"][0]["artifacts"].append("../../etc/passwd"),
        "path traversal")
rejects(lambda x: x["experiments"][1]["commands"].append("rm -rf /"),
        "untrusted shell command metadata")
rejects(lambda x: x["experiments"].append(deepcopy(x["experiments"][0])),
        "duplicate experiment")
print("PASS: research metadata validator is fail-closed on eight corruptions")
