---
name: life-event-trigger-radar
description: Trigger radar for partner surprises. Use to scan anniversaries, birthdays, Korean couple days, seasonal events, family milestones, mood-recovery moments, and upcoming windows for thoughtful action.
---

# Life Event Trigger Radar

Purpose: find when a thoughtful surprise should happen and why it would feel natural.

## Trigger categories

1. **Hard dates**
   - birthday
   - wedding anniversary
   - first meeting / proposal / relocation / school milestones
   - partner's work milestones

2. **Korean seasonal romance/care dates**
   - Valentine's Day: 14 February
   - White Day: 14 March
   - Rose Day: 14 May, optional only if partner enjoys these unofficial days
   - Pepero Day: 11 November
   - Christmas Eve / Christmas
   - year-end, New Year, school term transitions
   - Parents' Day: 8 May, when family/parent role matters

3. **Mood and care triggers**
   - after a difficult conversation
   - visible fatigue, stress, disappointment, or loneliness
   - before/after partner's big presentation, deadline, trip, important appointment, or family obligation

4. **Opportunity windows**
   - free evening
   - childcare coverage
   - school holiday
   - good weather
   - newly opened venue or limited seasonal menu, only if verified

## Workflow

- Read the available `data/*.json` files.
- Run `scripts/trigger_scan.py` when local date scanning is helpful.
- Prioritise near-term actions but do not overdo every minor occasion.
- Each trigger should include:
  - date
  - reason
  - suggested scale: tiny, small, medium, premium
  - lead time
  - why it may matter emotionally
  - risk of feeling forced or performative

## Output

Return a ranked list of triggers for the next 7, 14, 30, and 60 days. Include one “just because” opportunity if no strong trigger exists.
