---
name: gift-idea-selector
description: Gift selection for partner surprises. Use to propose and score gifts by partner preference, budget, novelty, emotional meaning, trend evidence, logistics, and risk.
---

# Gift Idea Selector

Purpose: recommend gifts that feel personal, timely, and low-pressure.

## Use this skill when

- The user wants a small or premium gift for a romantic partner.
- A Korean seasonal occasion such as White Day, Pepero Day, Christmas, birthday, or anniversary is near.
- A mood-care gesture needs a tangible element.
- The user has gift candidates and wants prioritisation.

## Gift principles

- Personal fit beats price.
- Pair physical gifts with a specific sentence explaining why it fits the partner.
- Avoid gifts that imply criticism, such as diet, anti-ageing, self-improvement, or domestic labour tools, unless explicitly requested by partner.
- Avoid burdensome gifts requiring the partner to schedule, learn, store, or maintain something.
- Check allergies, sizes, colours, brand preferences, and return policy.

## Workflow

1. Read partner profile and constraints.
2. Generate or load candidate gifts.
3. Run `scripts/score_gifts.py` when candidates exist.
4. For top options, add:
   - personal reason
   - timely reason
   - presentation idea
   - message/card wording
   - risk and fallback
5. If live shopping/search tools are available, verify current price, stock, delivery, and return policy.

## Output

Use this structure:

```markdown
## Gift shortlist

| Rank | Gift | Why it fits | Why now | Budget | Risk | Verdict |
|---:|---|---|---|---:|---|---|

## Best choice
- Gift:
- Add-on detail:
- How to give it:
- Natural sentence:
- Card wording:
- Backup:
```
