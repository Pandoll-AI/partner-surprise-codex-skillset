#!/usr/bin/env python3
"""Build bilingual trend research queries for surprise planning."""
from __future__ import annotations

import argparse
import json
from datetime import date

CATEGORY_TERMS = {
    "restaurant": ["restaurant", "fine dining", "new opening", "tasting menu", "date course", "예약", "신상 맛집", "파인다이닝", "데이트 코스"],
    "cafe": ["cafe", "dessert", "new cafe", "date cafe", "카페", "디저트", "신상 카페", "데이트 카페"],
    "gift": ["gift", "brand", "limited edition", "partner gift", "선물", "브랜드", "한정판", "파트너 선물"],
    "hotel": ["hotel package", "staycation", "romantic hotel", "호텔 패키지", "호캉스", "스테이케이션"],
    "travel": ["weekend getaway", "travel trend", "couple trip", "주말 여행", "커플 여행", "여행지 추천"],
    "exhibition": ["exhibition", "performance", "date idea", "전시", "공연", "데이트"],
}


def build_queries(category: str, location: str, season: str, partner_tags: list[str], year: int) -> list[str]:
    terms = CATEGORY_TERMS.get(category, CATEGORY_TERMS["gift"])
    tags = " ".join(partner_tags[:4])
    queries = [
        f"{location} {year} {season} {terms[0]} {terms[2]} {tags}".strip(),
        f"{location} {year} {season} {terms[-3]} {terms[-2]} {tags}".strip(),
        f"{location} {year} best {category} for partner anniversary review recent",
        f"{location} {year} {category} newly opened popular reservation price",
        f"{location} {year} {season} 데이트 {terms[-1]} 후기 예약 가격",
    ]
    # De-duplicate while preserving order
    seen = set()
    out = []
    for q in queries:
        normalized = " ".join(q.split())
        if normalized not in seen:
            seen.add(normalized)
            out.append(normalized)
    return out


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--category", default="restaurant", choices=sorted(CATEGORY_TERMS.keys()))
    parser.add_argument("--location", default="Seoul")
    parser.add_argument("--season", default="current season")
    parser.add_argument("--partner-tags", default="")
    parser.add_argument("--year", type=int, default=date.today().year)
    parser.add_argument("--format", choices=["json", "lines"], default="lines")
    args = parser.parse_args()

    tags = [x.strip() for x in args.partner_tags.split(",") if x.strip()]
    queries = build_queries(args.category, args.location, args.season, tags, args.year)
    if args.format == "json":
        print(json.dumps({"queries": queries}, ensure_ascii=False, indent=2))
    else:
        for q in queries:
            print(q)


if __name__ == "__main__":
    main()
