#!/usr/bin/env python3
"""Generate a practical surprise brief from local JSON inputs.

This top-level wrapper calls the skill helper scripts and prints a Korean-friendly Markdown brief.
It does not browse the web; live facts must be verified separately by Codex/web/MCP tools.
"""
from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path
from typing import Any


def run_json(cmd: list[str]) -> dict[str, Any]:
    proc = subprocess.run(cmd, check=True, capture_output=True, text=True)
    return json.loads(proc.stdout)


def money(n: Any) -> str:
    try:
        return f"{int(n):,}원"
    except Exception:
        return str(n)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", default="data/partner_profile.example.json")
    parser.add_argument("--anniversaries", default="data/anniversaries.example.json")
    parser.add_argument("--constraints", default="data/constraints.example.json")
    parser.add_argument("--candidates", default="data/candidates.example.json")
    parser.add_argument("--date", default=None)
    parser.add_argument("--days", type=int, default=45)
    args = parser.parse_args()

    root = Path(__file__).resolve().parents[1]
    trigger_script = root / ".agents/skills/life-event-trigger-radar/scripts/trigger_scan.py"
    score_script = root / ".agents/skills/gift-idea-selector/scripts/score_gifts.py"

    trigger_cmd = [sys.executable, str(trigger_script), "--profile", args.profile, "--anniversaries", args.anniversaries, "--constraints", args.constraints, "--days", str(args.days), "--format", "json"]
    if args.date:
        trigger_cmd.extend(["--date", args.date])
    score_cmd = [sys.executable, str(score_script), "--profile", args.profile, "--constraints", args.constraints, "--candidates", args.candidates, "--format", "json"]

    triggers = run_json(trigger_cmd).get("triggers", [])
    candidates = run_json(score_cmd).get("ranked_candidates", [])

    top_trigger = triggers[0] if triggers else {}
    top = candidates[0] if candidates else {}
    alternatives = candidates[1:3]

    print("# 이번 서프라이즈 브리프")
    print()
    print("## 1. 트리거 / 자연스러운 이유")
    print(f"- 트리거: {top_trigger.get('name', 'Just-because appreciation')}")
    print(f"- 날짜: {top_trigger.get('date', 'today')} (D-{top_trigger.get('days_until', 0)})")
    print(f"- 이유: {top_trigger.get('reason', '특별한 날이 아니어도 먼저 챙기는 행동')}")
    print(f"- 추천 규모: {top_trigger.get('suggested_scale', 'tiny')}")
    print(f"- 감정 포인트: {top_trigger.get('emotional_note', '작지만 구체적인 배려')}")
    print()
    print("## 2. 가장 추천하는 액션")
    print(f"- 액션: {top.get('name', 'Handwritten note + small care gesture')}")
    print(f"- 카테고리: {top.get('category', 'care_gesture')}")
    print(f"- 예산: {money(top.get('budget_krw', 0))}")
    print(f"- 점수: {top.get('score', 'n/a')}/100")
    print(f"- 왜 지금인지: {top.get('why_now', '대화 직후 작은 행동으로 보여주기 좋음')}")
    print(f"- 자연스러운 말: {top.get('natural_reason', '특별한 날은 아니지만 당신을 더 자주 챙기고 싶어서 준비했어.')}")
    print()
    print("## 3. 실행 체크리스트")
    print("- 오늘: 필요한 물건을 사고, 메시지는 짧게 손으로 적기")
    print("- 실행 전: 파트너에게 추가 일정 부담이 생기지 않는지 확인")
    print("- 실행 순간: 설명을 길게 하지 말고 한 문장으로 전달")
    print("- 이후: 반응을 관찰하되 평가받으려 하지 않기")
    print()
    print("## 4. 메시지")
    print(top.get("message", "요즘 내가 너무 루틴하게만 지낸 것 같아. 오늘은 작지만 당신이 편했으면 해서 준비했어."))
    print()
    print("## 5. 대안")
    for i, alt in enumerate(alternatives, 1):
        print(f"{i}. {alt.get('name')} — {money(alt.get('budget_krw', 0))}, score {alt.get('score')}/100")
    print()
    print("## 6. 리스크 체크")
    print(f"- 주요 리스크: {top.get('risk_note', top_trigger.get('risk_note', '과하게 설명하거나 생색내면 효과가 줄어듦'))}")
    print(f"- 플랜 B: {top.get('plan_b', '작은 선물 대신 집안일 하나를 먼저 끝내고 짧은 메모를 남기기')}")
    print()
    print("## 7. 검증 필요")
    print("- 식당, 호텔, 여행, 제품, 트렌드가 들어간 경우 가격/예약/영업시간/배송/후기는 실행 당일 기준으로 재확인하세요.")


if __name__ == "__main__":
    main()
