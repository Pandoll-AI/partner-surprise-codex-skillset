#!/usr/bin/env python3
"""Generate a lightweight surprise plan from local JSON inputs.

This script is intentionally dependency-free. It does not browse the web or book anything.
Codex should use it as a structured helper, then verify live facts separately when tools are available.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path


def run_json(cmd: list[str]) -> dict:
    proc = subprocess.run(cmd, check=True, capture_output=True, text=True)
    try:
        return json.loads(proc.stdout)
    except json.JSONDecodeError as exc:
        raise SystemExit(f"Could not parse JSON from {' '.join(cmd)}: {exc}\n{proc.stdout}")


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", default="data/partner_profile.example.json")
    parser.add_argument("--anniversaries", default="data/anniversaries.example.json")
    parser.add_argument("--constraints", default="data/constraints.example.json")
    parser.add_argument("--candidates", default="data/candidates.example.json")
    parser.add_argument("--date", default=None)
    parser.add_argument("--days", type=int, default=45)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[4]
    trigger_script = root / ".agents/skills/life-event-trigger-radar/scripts/trigger_scan.py"
    score_script = root / ".agents/skills/gift-idea-selector/scripts/score_gifts.py"

    trigger_cmd = [sys.executable, str(trigger_script), "--profile", args.profile, "--anniversaries", args.anniversaries, "--constraints", args.constraints, "--days", str(args.days), "--format", "json"]
    if args.date:
        trigger_cmd.extend(["--date", args.date])

    score_cmd = [sys.executable, str(score_script), "--profile", args.profile, "--constraints", args.constraints, "--candidates", args.candidates, "--format", "json"]

    triggers = run_json(trigger_cmd)
    scored = run_json(score_cmd)

    top_trigger = triggers.get("triggers", [{}])[0]
    top_options = scored.get("ranked_candidates", [])[:3]

    brief = {
        "top_trigger": top_trigger,
        "recommended_options": top_options,
        "next_steps": [
            "Verify live trend evidence, prices, reservation availability, and delivery times.",
            "Choose the lowest-pressure option if partner is tired or busy.",
            "Prepare one sincere sentence and one practical Plan B.",
        ],
    }
    print(json.dumps(brief, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
