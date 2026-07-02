---
name: restaurant-date-planner
description: Restaurant and date-course planning for partner surprises. Use to choose a timely Seoul/Korea restaurant, cafe, dessert, bar, exhibition, walk, or date route with verified trend/review rationale and logistics.
---

# Restaurant Date Planner

Purpose: create date plans that feel effortless for the partner and well-prepared by the user.

## Use this skill when

- The user wants a dinner/lunch/cafe/date course surprise.
- The user needs a “natural reason” such as a new opening, seasonal menu, good reviews, neighbourhood trend, or shared memory.
- The plan needs childcare, timing, reservation, transport, and Plan B logistics.

## Workflow

1. Read partner profile and constraints.
2. Decide tone:
   - comforting casual
   - elegant but not stiff
   - celebratory premium
   - playful trend/date course
3. Invoke `trend-research-scout` for current venue evidence.
4. Shortlist 3–5 venue/course options.
5. Verify or flag:
   - opening hours
   - reservation availability
   - location/parking/transit
   - dietary restrictions/allergies
   - price range
   - noise/crowding
   - cancellation policy
6. Build one main plan and one low-energy fallback.

## Date course shape

Prefer a compact route:

- pretext / invitation sentence
- first stop: restaurant/cafe
- second stop: short walk or dessert
- optional small gift or note
- end early enough not to burden the partner

## Output

```markdown
# Date plan

## Recommendation
- Venue/course:
- Natural reason:
- Trend evidence status:
- Why it fits the partner:

## Logistics
- Time:
- Reservation:
- Transport:
- Budget:
- Childcare/family coverage:

## Exact words
- Invitation:
- At the table:
- Card/message:

## Plan B
- If reservation fails:
- If the partner is tired:
- If weather is bad:
```
