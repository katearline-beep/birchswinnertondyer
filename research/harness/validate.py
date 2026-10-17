#!/usr/bin/env python3
"""Fail-closed structural checks for research experiment metadata.

This DOES NOT prove a mathematical claim, and does not execute user-supplied
commands. Read research/harness/README.md before interpreting results.
"""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "research/harness/experiments.json"
STATUSES = {"planned", "computationally_reproduced",
            "conditionally_supported", "externally_reviewed"}
KINDS = {"exact_math", "validation_method", "analogy"}

def require(test, msg):
    if not test:
        raise ValueError(msg)

def validate(manifest, root=ROOT, ledger=None):
    require(type(manifest) is dict and manifest.get("schema_version") == 1,
            "Invalid manifest schema version")
    items = manifest.get("experiments")
    require(type(items) is list and bool(items), "Missing experiments")
    if ledger is None:
        ledger = (root / "CLAIMS.md").read_text(encoding="utf8")
    claim_ids = set(re.findall(r"\| (C-\d{4}) \|", ledger))
    require(bool(claim_ids), "Claim ledger empty")
    seen = set()
    for x in items:
        require(type(x) is dict, "Experiment must be an object")
        identifier = x.get("id")
        require(type(identifier) is str and bool(re.fullmatch(r"EX-\d{3}", identifier)),
                "Experiment ID must be EX-000 style")
        require(identifier not in seen, "Duplicate experiment "+identifier)
        seen.add(identifier)
        refs = x.get("claim_ids")
        require(type(refs) is list and bool(refs) and
                all(type(z) is str and z in claim_ids for z in refs),
                identifier+": claim must appear in CLAIMS.md")
        require(x.get("status") in STATUSES, identifier+": unknown status")
        require(type(x.get("human_reviewed")) is bool,
                identifier+": human review status must be explicit")
        if x["human_reviewed"]:
            require(x["status"] == "externally_reviewed",
                    identifier+": human reviewed conflicts with status")
            for k in ("reviewer", "review_evidence"):
                require(type(x.get(k)) is str and len(x[k].strip())>12,
                        identifier+": independent review provenance required")
        else:
            require(x["status"] != "externally_reviewed",
                    identifier+": cannot claim external review without reviewer evidence")
        for k in ("question", "decisive_observation", "negative_control",
                  "stop_condition"):
            require(type(x.get(k)) is str and len(x[k].strip()) >= 28,
                    identifier+": inadequate "+k)
        for k in ("dependencies", "commands", "artifacts",
                  "nonclaims", "cross_disciplines"):
            require(type(x.get(k)) is list and bool(x[k]),
                    identifier+": missing "+k)
        require(all(type(z) is str and len(z.strip()) >= 10 for z in x["dependencies"]),
                identifier+": unusable dependency")
        require(all(type(z) is str and len(z.strip())>=10 for z in x["nonclaims"]),
                identifier+": missing explicit nonclaims")
        for command in x["commands"]:
            require(type(command) is str and
                    re.match(r"^(python3? -I -B |gp -q -f )", command) is not None,
                    identifier+": document reproducible commands; do not execute metadata")
        for file in x["artifacts"]:
            require(type(file) is str and not file.startswith("/") and
                    ".." not in Path(file).parts and
                    (root / file).is_file(),
                    identifier+": missing or unsafe artifact: "+str(file))
        for transfer in x["cross_disciplines"]:
            require(type(transfer) is dict and
                    transfer.get("kind") in KINDS, identifier+": transfer lacks kind")
            for key in ("discipline", "mechanism", "proof_boundary", "validating_test",
                        "reference"):
                require(type(transfer.get(key)) is str and
                        len(transfer[key].strip()) >= 15,
                        identifier+": incomplete transfer "+key)
            testpath = transfer["validating_test"]
            require(not testpath.startswith("/") and
                    ".." not in Path(testpath).parts and
                    (root / testpath).is_file(),
                    identifier+": transfer test missing")
            require(transfer["reference"].startswith("https://"),
                    identifier+": transfer needs documented source")
    return len(items)

def main():
    n=validate(json.loads(MANIFEST.read_text(encoding="utf8")))
    print(f"PASS: {n} research experiments structurally documented")
    print("NONCLAIM: syntax and metadata policy checks are NOT mathematics review")

if __name__=="__main__":
    main()
