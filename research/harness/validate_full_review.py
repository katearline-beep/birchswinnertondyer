#!/usr/bin/env python3
"""Fail-closed structural review gate; cannot judge mathematical truth.

Checks presence of a weekly BSD big-picture checkpoint and all six tracks,
nonclaim accounting, typed evidence, provenance, review chronology, and
consistent proof-status flags. Does not search the literature or prove BSD.
"""
from datetime import date
from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parents[2]
CURRENT = ROOT / "research/reviews/current.json"
TRACKS = {f"H{i}" for i in range(1,7)}
EVIDENCE_CATEGORIES = {
    "finite_computation", "conditional_published_theorem",
    "existing_algebraic_theory", "provisional_computational_certificate",
    "hypothesis_and_method_audit", "numerical_evidence",
    "published_theorem", "external_mathematical_review"
}
DECISIONS = {"active_limited","active_prioritized","parked","diagnostic","killed"}
FLAGS = {
    "general_BSD_proved", "exact_complex_Lpp_zero_proved",
    "analytic_rank_four_proved", "Sha_finiteness_for_E_proved",
    "full_BSD_leading_coefficient_proved", "new_bridge_to_complex_Lpp_proved",
    "independently_human_reviewed"
}

def need(ok, msg):
    if not ok:
        raise ValueError(msg)

def substantial(doc, key, minimum=60):
    v=doc.get(key)
    need(type(v) is str and len(v.strip())>=minimum, "Missing or short "+key)

def validate(obj, root=ROOT):
    need(type(obj) is dict and obj.get("schema_version")==1, "Unknown review schema")
    need(re.fullmatch(r"WPR-\d{4}-\d{2}-\d{2}-\d{2}",obj.get("review_id","")) is not None,
         "Invalid review ID")
    reviewed=date.fromisoformat(obj["reviewed_on"])
    due=date.fromisoformat(obj["next_due_on"])
    need(due>reviewed and (due-reviewed).days<=7,
         "Next whole-problem review must be scheduled within seven days")
    need(obj.get("reviewer_type")=="ai_assisted_unreviewed",
         "Review cannot assert independent human approval through a metadata edit")
    need(obj.get("target_curve")=="234446.a1", "Incorrect focal curve")
    for k in ["goal_general","goal_specific","deepest_open_implication",
              "mathematical_breakthrough_since_previous",
              "selected_next_experiment","selected_experiment_kill_criterion",
              "conservative_next_lemma","credible_leapfrog",
              "speculative_wild_option","deprioritized_work",
              "negative_control_reviewed"]:
        substantial(obj,k)
    flags=obj.get("status_flags")
    need(type(flags) is dict and set(flags)==FLAGS,
         "All seven truth-status fields required")
    need(all(type(value) is bool for value in flags.values()),"Proof flags must be booleans")
    need(not any(flags.values()),
         "Do not self-promote to proven BSD or expert review via a review snapshot")
    need(obj.get("new_proven_bridge_evidence")==[],
         "No proved L'' bridge exists in this review; would require independent claim-ledger review")
    need(type(obj.get("previous_review_id")) in (str,type(None)),
         "Previous review reference must be typed")
    claims=obj.get("claim_ids_audited")
    ledger=(root / "CLAIMS.md").read_text(encoding="utf8")
    expected_claims=set(re.findall(r"^\| (C-\d{4}) \|",ledger,re.M))
    need(bool(expected_claims),"No claim IDs in canonical ledger")
    need(type(claims) is list and len(claims)==len(expected_claims) and set(claims)==expected_claims,
         "Review must inspect ALL C-series claims actually present in CLAIMS.md")
    need(type(obj.get("reviewed_prs")) is list and
         all(re.fullmatch(r"#\d+",p) for p in obj["reviewed_prs"]) and
         len(obj["reviewed_prs"])>0,"Provide prior merged PR identifiers")
    tracks=obj.get("tracks")
    need(type(tracks) is list and len(tracks)==6, "Audit all six leapfrog tracks")
    need({x.get("track") for x in tracks}==TRACKS,
         "No leapfrog track may disappear from full-problem review")
    for t in tracks:
        need(t.get("decision") in DECISIONS,
             "Invalid track decision "+str(t.get("track")))
        for key in ("last_evidence","missing_bridge","falsifier","next_test"):
            substantial(t,key,45)
    classes=obj.get("evidence_classes")
    need(type(classes) is list and len(classes)>=5,
         "Need an explicit class-by-class evidence assessment")
    for row in classes:
        need(row.get("category") in EVIDENCE_CATEGORIES,"Unknown evidence class")
        substantial(row,"statement",35)
    nonclaims=obj.get("not_established")
    need(type(nonclaims) is list and len(nonclaims)>=5 and
         all(type(z) is str and len(z)>=22 for z in nonclaims),
         "List the central unresolved proof obligations")
    references=obj.get("sources")
    need(type(references) is list and len(references)>=5,
         "Review must cite actual sources")
    for value in references:
        need(type(value) is str and
             (value.startswith("https://") or
              (not value.startswith("/") and ".." not in Path(value).parts and
               (root/value).is_file())),"Broken/unsafe review source: "+str(value))
    doc=obj.get("journal_path")
    need(type(doc) is str and doc.startswith("research/reviews/") and
         re.fullmatch(r"research/reviews/\d{4}-\d{2}-\d{2}-whole-problem(?:-\d{2})?\.md",doc) and
         (root/doc).is_file(),"Immutable dated review journal is required")
    return 6

def main():
    d=json.loads(CURRENT.read_text(encoding="utf8"))
    n=validate(d)
    print("PASS: full BSD goal, seven no-proof flags, every live claim and "+str(n)+" research tracks reviewed")
    print("PASS: next review date within seven days and historical checkpoint exists")
    print("NONCLAIM: structured review metadata and passing CI never prove BSD")

if __name__=="__main__":
    main()
