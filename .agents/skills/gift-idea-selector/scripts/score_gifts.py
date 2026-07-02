#!/usr/bin/env python3
"""Score surprise candidates against partner profile and constraints."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

CATEGORY_WEIGHTS = {
    "fit": 0.30,
    "timeliness": 0.18,
    "surprise": 0.16,
    "logistics": 0.14,
    "warmth": 0.22,
}


def load_json(path: str | Path, default: Any) -> Any:
    p = Path(path)
    if not p.exists():
        return default
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def clamp(value: float, lo: float = 1.0, hi: float = 5.0) -> float:
    return max(lo, min(hi, value))


def tag_fit(candidate_tags: list[str], liked_tags: list[str], avoid_tags: list[str]) -> tuple[float, list[str]]:
    candidate_set = {t.lower() for t in candidate_tags}
    liked_set = {t.lower() for t in liked_tags}
    avoid_set = {t.lower() for t in avoid_tags}
    hits = sorted(candidate_set & liked_set)
    risks = sorted(candidate_set & avoid_set)
    score = 2.5 + min(2.0, len(hits) * 0.7) - min(2.0, len(risks) * 1.0)
    return clamp(score), hits + [f"avoid:{r}" for r in risks]


def score_candidate(c: dict[str, Any], profile: dict[str, Any], constraints: dict[str, Any]) -> dict[str, Any]:
    prefs = profile.get("preferences", {})
    liked_tags = prefs.get("likes", []) + prefs.get("style_tags", [])
    avoid_tags = prefs.get("dislikes", []) + prefs.get("avoid", [])
    fit, tag_notes = tag_fit(c.get("tags", []), liked_tags, avoid_tags)

    budget = c.get("budget_krw", 0)
    max_budget = constraints.get("budget", {}).get("max_krw")
    budget_note = "within budget"
    budget_penalty = 0.0
    if max_budget and budget > max_budget:
        budget_penalty = min(2.0, (budget - max_budget) / max_budget * 2)
        budget_note = "over budget"

    raw = {
        "fit": c.get("fit", fit),
        "timeliness": c.get("timeliness", 3),
        "surprise": c.get("surprise", 3),
        "logistics": c.get("logistics", 3),
        "warmth": c.get("warmth", 3),
        "risk": c.get("risk", 2) + budget_penalty,
    }
    positive = sum(clamp(raw[k]) * w for k, w in CATEGORY_WEIGHTS.items())
    risk_penalty = ((clamp(raw["risk"]) - 1.0) / 4.0) * 20.0
    normalized = round(((positive - 1.0) / 4.0) * 100.0 - risk_penalty, 1)
    return {
        **c,
        "score": max(0.0, min(100.0, normalized)),
        "score_breakdown": {k: round(clamp(v), 1) for k, v in raw.items()},
        "tag_notes": tag_notes,
        "budget_note": budget_note,
    }


def render_md(ranked: list[dict[str, Any]]) -> str:
    lines = ["# Gift / Surprise Candidate Ranking", "", "| Rank | Candidate | Category | Score | Budget | Why now | Risk |", "|---:|---|---|---:|---:|---|---|"]
    for i, c in enumerate(ranked, 1):
        lines.append(
            f"| {i} | {c.get('name','')} | {c.get('category','')} | {c.get('score',0)} | {c.get('budget_krw',0):,} KRW | {c.get('why_now','')} | {c.get('risk_note','')} |"
        )
    if ranked:
        best = ranked[0]
        lines += [
            "",
            "## Best candidate",
            f"- Name: {best.get('name','')}",
            f"- Natural reason: {best.get('natural_reason','')}",
            f"- Message: {best.get('message','')}",
            f"- Plan B: {best.get('plan_b','')}",
        ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", default="data/partner_profile.example.json")
    parser.add_argument("--constraints", default="data/constraints.example.json")
    parser.add_argument("--candidates", default="data/candidates.example.json")
    parser.add_argument("--format", choices=["json", "md"], default="md")
    args = parser.parse_args()

    profile = load_json(args.profile, {})
    constraints = load_json(args.constraints, {})
    candidates_doc = load_json(args.candidates, {"candidates": []})
    ranked = [score_candidate(c, profile, constraints) for c in candidates_doc.get("candidates", [])]
    ranked.sort(key=lambda x: x["score"], reverse=True)

    if args.format == "json":
        print(json.dumps({"ranked_candidates": ranked}, ensure_ascii=False, indent=2))
    else:
        print(render_md(ranked))


if __name__ == "__main__":
    main()
