#!/usr/bin/env python3
"""Scan upcoming surprise triggers from simple JSON files.

The output is a ranked JSON or Markdown list. Lunar holidays are not computed;
add them manually in anniversaries.json when needed.
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Any

FIXED_KOREA_EVENTS = [
    {"name": "Valentine's Day", "month": 2, "day": 14, "category": "seasonal_romance", "default_scale": "small", "importance": 3},
    {"name": "White Day", "month": 3, "day": 14, "category": "seasonal_romance", "default_scale": "small", "importance": 4},
    {"name": "Parents' Day Korea", "month": 5, "day": 8, "category": "family_care", "default_scale": "small", "importance": 3},
    {"name": "Rose Day", "month": 5, "day": 14, "category": "optional_romance", "default_scale": "tiny", "importance": 2},
    {"name": "Pepero Day", "month": 11, "day": 11, "category": "playful_romance", "default_scale": "tiny", "importance": 3},
    {"name": "Christmas Eve", "month": 12, "day": 24, "category": "seasonal_romance", "default_scale": "medium", "importance": 4},
    {"name": "Christmas Day", "month": 12, "day": 25, "category": "family_or_romance", "default_scale": "medium", "importance": 4},
    {"name": "New Year's Eve", "month": 12, "day": 31, "category": "reflection", "default_scale": "small", "importance": 3},
]

@dataclass
class Trigger:
    date: str
    days_until: int
    name: str
    category: str
    reason: str
    suggested_scale: str
    urgency_score: float
    emotional_note: str
    risk_note: str


def load_json(path: str | Path, default: Any) -> Any:
    p = Path(path)
    if not p.exists():
        return default
    with p.open("r", encoding="utf-8") as f:
        return json.load(f)


def parse_today(value: str | None) -> date:
    if value:
        return datetime.strptime(value, "%Y-%m-%d").date()
    return date.today()


def next_fixed_date(today: date, month: int, day: int) -> date:
    candidate = date(today.year, month, day)
    if candidate < today:
        candidate = date(today.year + 1, month, day)
    return candidate


def parse_custom_event_date(today: date, raw: str) -> date | None:
    raw = raw.strip()
    for fmt in ("%Y-%m-%d", "%m-%d"):
        try:
            dt = datetime.strptime(raw, fmt).date()
            if fmt == "%m-%d":
                dt = date(today.year, dt.month, dt.day)
                if dt < today:
                    dt = date(today.year + 1, dt.month, dt.day)
            return dt
        except ValueError:
            continue
    return None


def scale_for(days_until: int, importance: int, default: str) -> str:
    if importance >= 5 and days_until <= 30:
        return "premium"
    if importance >= 4 and days_until <= 21:
        return "medium"
    if days_until <= 3:
        return "tiny"
    return default


def urgency(days_until: int, importance: int) -> float:
    time_score = max(0.0, 60 - days_until) / 60
    return round((importance * 0.65) + (time_score * 5 * 0.35), 2)


def build_triggers(today: date, days: int, profile: dict[str, Any], anniversaries: dict[str, Any], constraints: dict[str, Any]) -> list[Trigger]:
    triggers: list[Trigger] = []
    horizon = today + timedelta(days=days)
    enjoys_commercial_days = profile.get("preferences", {}).get("enjoys_commercial_romance_days", True)

    for ev in FIXED_KOREA_EVENTS:
        if ev["category"] == "optional_romance" and not enjoys_commercial_days:
            continue
        dt = next_fixed_date(today, ev["month"], ev["day"])
        if dt <= horizon:
            du = (dt - today).days
            triggers.append(Trigger(
                date=dt.isoformat(),
                days_until=du,
                name=ev["name"],
                category=ev["category"],
                reason=f"Korea-context seasonal hook: {ev['name']}",
                suggested_scale=scale_for(du, ev["importance"], ev["default_scale"]),
                urgency_score=urgency(du, ev["importance"]),
                emotional_note="Use as a gentle, culturally familiar reason; keep it personal rather than commercial.",
                risk_note="Can feel performative if the gesture is generic. Add one personal detail.",
            ))

    for ev in anniversaries.get("events", []):
        dt = parse_custom_event_date(today, str(ev.get("date", "")))
        if not dt or dt > horizon:
            continue
        importance = int(ev.get("importance", 4))
        du = (dt - today).days
        triggers.append(Trigger(
            date=dt.isoformat(),
            days_until=du,
            name=ev.get("name", "Personal event"),
            category=ev.get("category", "personal"),
            reason=ev.get("reason", "Personal milestone"),
            suggested_scale=scale_for(du, importance, ev.get("default_scale", "small")),
            urgency_score=urgency(du, importance),
            emotional_note=ev.get("emotional_note", "Connect the gesture to shared memory and gratitude."),
            risk_note=ev.get("risk_note", "Avoid making the event about your effort; centre the partner's experience."),
        ))

    mood = profile.get("recent_context", {}).get("mood_signal")
    if mood:
        triggers.append(Trigger(
            date=today.isoformat(),
            days_until=0,
            name="Mood-care recovery gesture",
            category="mood_care",
            reason=f"Recent context suggests: {mood}",
            suggested_scale="tiny",
            urgency_score=4.4,
            emotional_note="Best as low-pressure care: remove burden, bring comfort, or write a sincere note.",
            risk_note="Do not frame it as fixing their mood. Make it easy to accept or decline.",
        ))

    if not triggers:
        triggers.append(Trigger(
            date=today.isoformat(),
            days_until=0,
            name="Just-because appreciation",
            category="everyday_romance",
            reason="No strong calendar trigger; a small unexpected gesture may feel more sincere.",
            suggested_scale="tiny",
            urgency_score=2.5,
            emotional_note="Keep it simple and specific: one favourite snack, one task handled, one short note.",
            risk_note="Avoid over-engineering. The point is attentiveness.",
        ))

    triggers.sort(key=lambda t: (-t.urgency_score, t.days_until))
    return triggers


def to_markdown(triggers: list[Trigger]) -> str:
    lines = ["# Upcoming Surprise Triggers", "", "| Rank | Date | D- | Trigger | Scale | Reason |", "|---:|---|---:|---|---|---|"]
    for i, t in enumerate(triggers, start=1):
        lines.append(f"| {i} | {t.date} | {t.days_until} | {t.name} | {t.suggested_scale} | {t.reason} |")
    lines.append("")
    if triggers:
        top = triggers[0]
        lines += [
            "## Top trigger note",
            f"- Emotional note: {top.emotional_note}",
            f"- Risk note: {top.risk_note}",
        ]
    return "\n".join(lines)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", default="data/partner_profile.example.json")
    parser.add_argument("--anniversaries", default="data/anniversaries.example.json")
    parser.add_argument("--constraints", default="data/constraints.example.json")
    parser.add_argument("--date", default=None)
    parser.add_argument("--days", type=int, default=60)
    parser.add_argument("--format", choices=["json", "md"], default="md")
    args = parser.parse_args()

    today = parse_today(args.date)
    profile = load_json(args.profile, {})
    anniversaries = load_json(args.anniversaries, {"events": []})
    constraints = load_json(args.constraints, {})
    triggers = build_triggers(today, args.days, profile, anniversaries, constraints)

    if args.format == "json":
        print(json.dumps({"today": today.isoformat(), "horizon_days": args.days, "triggers": [asdict(t) for t in triggers]}, ensure_ascii=False, indent=2))
    else:
        print(to_markdown(triggers))


if __name__ == "__main__":
    main()
