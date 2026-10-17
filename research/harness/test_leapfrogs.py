#!/usr/bin/env python3
"""Adversarial corruption tests for leapfrog protocol gate (not proof checking)."""
from copy import deepcopy
import json
from pathlib import Path
from runpy import run_path

code=run_path(str(Path(__file__).resolve().with_name("validate_leapfrogs.py")))
validator=code["validate"]
data=json.loads(code["REGISTRY"].read_text(encoding="utf8"))
experiments=json.loads(code["EXPERIMENTS"].read_text(encoding="utf8"))
assert validator(data,experiments)==6

def must_reject(label,mutation):
    corrupted=deepcopy(data)
    mutation(corrupted)
    try:
        validator(corrupted,experiments)
    except ValueError:
        print("PASS rejection:",label)
        return
    raise AssertionError("FALSE ACCEPTANCE: "+label)

must_reject("invented theorem status",
  lambda x:x["leapfrogs"][0].update(proof_status="established"))
must_reject("fabricated review",
  lambda x:x["leapfrogs"][0].update(reviewed=True))
must_reject("unjustified novelty",
  lambda x:x["leapfrogs"][0].update(novelty_status="world_first"))
must_reject("missing conjectural bridge",
  lambda x:x["leapfrogs"][0].update(missing_arrow=""))
must_reject("no IF THEN structure",
  lambda x:x["leapfrogs"][0].update(if_then_statement="BSD is certainly true"))
must_reject("no falsifier",
  lambda x:x["leapfrogs"][0].update(negative_control=""))
must_reject("wrong experimental reference",
  lambda x:x["leapfrogs"][0].update(experiment_id="EX-999"))
must_reject("test path traversal",
  lambda x:x["leapfrogs"][0].update(test_path="../../../etc/passwd"))
must_reject("undocumented decision change",
  lambda x:x["leapfrogs"][0].update(decision="killed"))
must_reject("missing whole moonshot track",
  lambda x:x["leapfrogs"].pop())
print("PASS: ten falsification controls for leapfrog research protocol")
