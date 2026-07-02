---
name: trend-research-scout
description: Trend research for partner surprise ideas. Use when recommendations need current evidence about restaurants, hotels, gifts, pop culture, reviews, openings, seasonal menus, exhibitions, travel spots, or Korean lifestyle trends.
---

# Trend Research Scout

Purpose: make the surprise feel timely and well-chosen without inventing evidence.

## Use this skill for

- “요즘 뜨는” restaurants, cafes, hotels, exhibitions, neighbourhoods, gifts, brands, experiences
- newly opened or recently renovated venues
- seasonal menus, limited editions, pop-ups, performances, flower seasons, hotel packages
- celebrity or influencer trend claims
- verifying whether an idea has real public evidence

## Hard rule

Never write a trend claim as fact unless it has been verified during the current run or supplied by the user. If browsing/search tools are unavailable, generate search queries and clearly mark the claim as `needs verification`.

## Source quality ladder

Prefer sources in this order:

1. Official venue/brand/hotel/event pages for factual details
2. Booking/reservation platforms for availability and price ranges
3. Reputable media and lifestyle publications for trend context
4. Review platforms for sentiment, checked against recency and volume
5. Blogs/social posts only as weak signals, not as proof

## Research workflow

1. Clarify the category:
   - restaurant/cafe
   - gift/brand
   - hotel/travel
   - exhibition/performance
   - experience/class

2. Generate targeted queries with `scripts/trend_query_builder.py`.

3. Search with date awareness.
   - Current year and current season matter.
   - For Seoul/Korea, include Korean search terms.
   - For London/UK context, include local terms only if relevant.

4. Extract facts:
   - What is new or timely?
   - Who recommends it?
   - What exactly is popular: menu, room, location, product, service?
   - Price, opening hours, location, reservation constraints, delivery lead time.

5. Assign evidence confidence:
   - High: official + current reputable source or current reservation data
   - Medium: several recent independent sources but limited official detail
   - Low: social/blog-only trend signal
   - Unknown: no live verification

6. Convert evidence into a natural reason.
   Examples:
   - “최근 새로 오픈해서 평이 좋다고 해서 같이 가보고 싶었어.”
   - “이번 시즌 한정 메뉴가 있어서 당신 생각이 났어.”
   - “요즘 이 동네가 데이트 코스로 다시 많이 언급돼서, 가볍게 산책까지 묶어봤어.”

## Output schema

```markdown
## Trend evidence brief

- Idea:
- Trend claim:
- Evidence confidence: High / Medium / Low / Unknown
- Sources checked:
  - Source, date checked, what it supports
- Caveats:
- Natural reason sentence:
- Search queries used:
```
