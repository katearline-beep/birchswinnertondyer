#!/usr/bin/env python3
"""Structural integrity gate for leapfrog hypotheses; NEVER a theorem prover.

Validates known baselines, conjectural bridge, downside, falsifier, stopping
rule, literature pointer, source experiment, and honest review status.
No executable command is evaluated from the manifest.
"""
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[2]
REGISTRY=ROOT/"research/harness/leapfrogs.json"
EXPERIMENTS=ROOT/"research/harness/experiments.json"
FIELDS=(
 "title","known_baseline","missing_arrow","hypothetical_bridge",
 "if_then_statement","would_unlock","unverified_dependencies",
 "negative_control","next_decisive_test","kill_criterion",
 "not_unlocked"
)

def require(condition, reason):
    if not condition:
        raise ValueError(reason)

def validate(doc, experiments, root=ROOT):
    require(type(doc) is dict and doc.get("schema_version")==1,
            "Unsupported leapfrog schema")
    leapfrogs=doc.get("leapfrogs")
    require(type(leapfrogs) is list and len(leapfrogs)>0, "No leapfrog candidates")
    require(type(experiments) is dict and type(experiments.get("experiments")) is list,
            "Missing ordinary experiment registry")
    experiment_ids={exp["id"] for exp in experiments["experiments"]}
    high_risk={exp["id"] for exp in experiments["experiments"] if exp["id"]>="EX-004"}
    ids,linked=set(),set()
    for item in leapfrogs:
        require(type(item) is dict,"Leapfrog must be a record")
        ident=item.get("id","")
        require(type(ident) is str and re.fullmatch(r"LF-\d{3}",ident) is not None,
                "Invalid leapfrog ID")
        require(ident not in ids,"Duplicate leapfrog ID: "+ident)
        ids.add(ident)
        exp=item.get("experiment_id")
        require(type(exp) is str and exp in experiment_ids,
                ident+": missing or unknown experiment")
        require(exp not in linked,ident+": experiment linked twice")
        linked.add(exp)
        for name in FIELDS:
            value=item.get(name)
            require(type(value) is str and len(value.strip())>=40,
                    ident+": missing substantial "+name)
        require(item["if_then_statement"].startswith("IF "),
                ident+": conditional statement must begin 'IF '")
        require("THEN " in item["if_then_statement"],
                ident+": conditional statement must contain THEN")
        require(item["gate"] in ("G0","G1","G2","G3","G4"),
                ident+": invalid gate")
        require(item["decision"] in ("active","parked","killed","diagnostic"),
                ident+": invalid decision")
        require(item.get("reviewed") is False,
                ident+": cannot claim expert review without separately archived evidence and human protocol")
        require(item.get("proof_status")=="speculative",
                ident+": no conjecture can self-award proof status")
        require(item.get("novelty_status")=="unverified",
                ident+": no candidate can claim novelty without documented independent literature audit")
        require(item["source"].startswith("https://"),
                ident+": no credible literature link")
        path=item.get("test_path","")
        require(type(path) is str and not path.startswith("/") and
                ".." not in Path(path).parts and (root/path).is_file(),
                ident+": missing or unsafe falsification program")
        logs=item.get("decision_log")
        require(type(logs) is list and bool(logs), ident+": missing decision log")
        require(all(type(z) is dict and
                    re.fullmatch(r"\d{4}-\d{2}-\d{2}",z.get("date","")) is not None and
                    z.get("outcome") in ("active","parked","killed","diagnostic") and
                    isinstance(z.get("evidence"),str) and len(z["evidence"])>=25
                    for z in logs),ident+": inadequate decision evidence")
        require(logs[-1]["outcome"]==item["decision"],ident+": stale decision log")
    require(linked==high_risk,
            "All high-risk EX-004+ must be represented, missing="+str(sorted(high_risk-linked)))
    return len(leapfrogs)

def main():
    x=json.loads(REGISTRY.read_text(encoding="utf8"))
    y=json.loads(EXPERIMENTS.read_text(encoding="utf8"))
    count=validate(x,y)
    print(f"PASS: {count} leapfrog candidates have nonimplication, test, kill and review boundaries")
    print("NONCLAIM: metadata validation is not proof of any leapfrog or BSD theorem")

if __name__=="__main__":
    main()
