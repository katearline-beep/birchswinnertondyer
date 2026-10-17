#!/usr/bin/env python3
"""WPR-1 full-problem review snapshot *structure* validator.

No code can validate whether a claim is mathematically true. Reviewer status
and proof-evidence requirements are guardrails against unearned promotion.
"""
import json
import re
from pathlib import Path
from datetime import date

ROOT=Path(__file__).resolve().parents[2]
PATH=ROOT/"research/harness/reviews.json"
LEAPFROGS=ROOT/"research/harness/leapfrogs.json"
LEVELS={"rank_equality_single_curve","strong_bsd_single_curve","general_bsd"}
CLASS={"prior_art_plus_numerical","numerical_consistency","open_problem",
       "conditional_theorem","expert_reviewed_theorem"}

def check(c,msg):
    if not c: raise ValueError(msg)

def valid(data,leapfrogs):
    check(type(data) is dict and data.get("schema_version")==1 and data.get("protocol")=="WPR-1",
          "wrong WPR schema/protocol")
    reviews=data.get("reviews")
    check(type(reviews) is list and len(reviews)>0,"must have full-problem reviews")
    check(type(leapfrogs) is dict and type(leapfrogs.get("leapfrogs")) is list,
          "must link existing leapfrog registry")
    all_routes={i["id"] for i in leapfrogs["leapfrogs"]}
    seen=set()
    previous_date=None
    for rev in reviews:
        check(type(rev) is dict,"review must be object")
        rid=rev.get("id")
        check(type(rid) is str and re.fullmatch(r"WPR-\d{3}",rid) is not None,"bad review ID")
        check(rid not in seen,"duplicate review")
        seen.add(rid)
        value=rev.get("date")
        try:
            d=date.fromisoformat(value)
        except (TypeError,ValueError):
            raise ValueError("invalid review date")
        check(previous_date is None or d>=previous_date,"reviews out of date order")
        previous_date=d
        check(type(rev.get("base_main_commit")) is str and re.fullmatch(r"[0-9a-f]{40}",rev["base_main_commit"]) is not None,
              "need audited commit")
        check(rev.get("reviewer_role")=="internal_research_agent","reviewer identity must be explicit")
        check(rev.get("external_math_review") is False,"structural checker cannot self-award peer review")
        for key in ("trigger","confirmed_project_outputs","decisive_missing_arrow",
                    "failed_routes","prior_art_vs_new","next_decisive_question",
                    "next_action","decision","nonclaims"):
            check(type(rev.get(key)) is str and len(rev[key].strip())>=45,
                  "missing full-problem field "+key)
        levels=rev.get("levels")
        check(type(levels) is list and len(levels)==3 and
              {x.get("key") for x in levels}==LEVELS,"must audit all three BSD levels")
        for entry in levels:
            check(entry.get("status")=="open",
                  "unproved BSD milestone cannot be self-promoted")
            check(entry.get("evidence_category") in CLASS,"invalid evidence classification")
            for key in ("target","proved","missing"):
                check(type(entry.get(key)) is str and len(entry[key].strip())>60,
                      "missing level "+entry["key"]+" "+key)
            check(type(entry.get("source")) is str and entry["source"].startswith("https://"),
                  "needs authoritative link per level")
        check(rev.get("math_theorems_new_to_literature")==[],
              "machine-checker cannot validate novelty of new theorem")
        for k in ("exact_rank4_complex_bridge_established","sha_finiteness_established","general_bsd_proven"):
            check(rev.get(k) is False,"unsupported mathematical milestone claim "+k)
        paths=rev.get("routes")
        check(type(paths) is list and len(paths)==len(all_routes),"review must cover all routes")
        check({x.get("id") for x in paths}==all_routes,"review missing/unknown route")
        for route in paths:
            for k in ("assessment","next_test"):
                check(type(route.get(k)) is str and len(route[k].strip())>35,
                      "route review needs assessment and falsifiable next test")
            check(route.get("decision") in {
                "downrank_until_non_circular_bridge","park_high_cost_work",
                "priority_literature_gate","park","low_cost_diagnostic","active","kill",
                "reassess"}, "unknown route decision")
        refs=rev.get("sources")
        check(type(refs) is list and len(refs)>=3 and
              all(type(u) is str and u.startswith("https://") for u in refs),
              "review needs independent authoritative sources")
    return len(reviews)

def main():
    d=json.loads(PATH.read_text(encoding="utf8"))
    l=json.loads(LEAPFROGS.read_text(encoding="utf8"))
    n=valid(d,l)
    print(f"PASS: {n} whole-BSD review snapshot(s), all three goal levels and every research track")
    print("NONCLAIM: structural validation and latest review do not prove the mathematics")

if __name__=="__main__":
    main()
