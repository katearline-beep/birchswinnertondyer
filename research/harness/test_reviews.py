#!/usr/bin/env python3
"""Adversarial corruption controls for the whole-BSD review gate."""
from copy import deepcopy
import json
from pathlib import Path
from runpy import run_path

fn=run_path(str(Path(__file__).resolve().with_name("validate_reviews.py")))
source=json.loads(fn["PATH"].read_text(encoding="utf8"))
tracks=json.loads(fn["LEAPFROGS"].read_text(encoding="utf8"))
check=fn["valid"]
assert check(source,tracks)==1

def reject(label,mutation):
    x=deepcopy(source)
    mutation(x)
    try:
        check(x,tracks)
    except ValueError:
        print("PASS negative control:",label)
        return
    raise AssertionError("review checker falsely accepted: "+label)

reject("erasing general BSD goal",lambda x:x["reviews"][0]["levels"].pop(2))
reject("fake rank-four proof",lambda x:x["reviews"][0].update(exact_rank4_complex_bridge_established=True))
reject("fake Sha finiteness",lambda x:x["reviews"][0].update(sha_finiteness_established=True))
reject("fake general BSD solution",lambda x:x["reviews"][0].update(general_bsd_proven=True))
reject("fake novel theorem",lambda x:x["reviews"][0].update(math_theorems_new_to_literature=["A made-up theorem"]))
reject("removing failed routes",lambda x:x["reviews"][0].update(failed_routes=""))
reject("forgetting one leapfrog",lambda x:x["reviews"][0]["routes"].pop(0))
reject("deleting the missing complex derivative arrow",lambda x:x["reviews"][0].update(decisive_missing_arrow=""))
reject("inventing external peer review",lambda x:x["reviews"][0].update(external_math_review=True))
reject("changing prior-art status to proved",lambda x:x["reviews"][0]["levels"][0].update(status="proved"))
print("PASS: 10 whole-problem review false-positive controls")
