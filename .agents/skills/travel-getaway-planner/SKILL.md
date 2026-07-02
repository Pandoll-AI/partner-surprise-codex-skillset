---
name: travel-getaway-planner
description: Couple travel or staycation planning for partner surprises. Use to propose Seoul staycations, Korea weekend getaways, hotels, seasonal trips, rest-focused retreats, or family-compatible breaks with logistics and trend evidence.
---

# Travel Getaway Planner

Purpose: plan a short trip or staycation that feels restorative rather than burdensome.

## Use this skill when

- The user wants to propose a hotel, weekend getaway, day trip, or staycation.
- A seasonal travel hook exists: flowers, autumn foliage, snow, beach, school holiday, hotel package, exhibition.
- The user needs a plan with childcare, travel time, budget, cancellation, and a low-energy fallback.

## Workflow

1. Clarify trip scale:
   - 2–4 hour micro-break
   - Seoul staycation
   - day trip
   - one-night getaway
   - family trip with romantic moment embedded
2. Read profile and constraints.
3. Invoke `trend-research-scout` for current hotel/travel evidence.
4. Build options by burden level:
   - lowest burden
   - best memory value
   - premium/restorative
5. Verify or flag:
   - travel time
   - room availability
   - cancellation policy
   - school/family schedule
   - weather/season
   - fatigue risk
6. Recommend only if logistics truly help her rest.

## Avoid

- Surprise trips that require sudden packing, childcare, or schedule rearrangement by partner.
- Non-refundable booking unless user has high confidence.
- Overcrowded trend destinations when partner needs calm.

## Output

```markdown
# Getaway plan

## Best option
- Destination/hotel:
- Natural reason:
- Trend/seasonal evidence status:
- Why it fits the partner:
- Burden level:

## Logistics
- Dates:
- Transport:
- Budget:
- Booking/cancellation:
- Childcare/family plan:
- Packing burden:

## How to reveal
- Message:
- Physical reveal idea:

## Backup
- If weather changes:
- If the partner is tired:
- If booking fails:
```
