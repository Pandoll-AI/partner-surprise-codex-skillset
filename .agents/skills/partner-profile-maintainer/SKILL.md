---
name: partner-profile-maintainer
description: Maintain or bootstrap a partner preference profile for surprise planning. Use when partner_profile.json is missing, when the user needs a 10-15 question preference interview, or when updating structured JSON about likes, dislikes, sizes, allergies, restaurants, gifts, schedules, anniversaries, and relationship context without storing unnecessary private data.
---

# Partner Profile Maintainer

Purpose: keep surprise planning grounded in real preferences rather than generic ideas.

## Use this skill when

- `data/partner_profile.json` is missing, empty, or only copied from the example.
- The user says partner liked/disliked a gift, restaurant, trip, or message.
- The user wants to record anniversaries, sizes, allergies, favourite colours, cuisines, brands, or constraints.
- The user wants the future recommendations to improve.

## Data minimisation

Store only what helps surprise planning:

- stable preferences
- constraints and allergies
- meaningful dates
- previous surprises and reactions
- budget/lead-time defaults

Do not store:

- private messages
- sensitive health details beyond practical constraints volunteered by user
- location history
- secrets or credentials
- anything partner would reasonably consider invasive

## Workflow

1. Check whether `data/partner_profile.json` exists.
2. If it is missing or empty, read `references/profile_interview_ko.md` and run the 12-question interview before making surprise recommendations.
3. Identify new facts from the user's message or interview answers.
4. Decide which file should change:
   - `data/partner_profile.json`
   - `data/anniversaries.json`
   - `data/constraints.json`
   - `data/candidates.json`
5. Update conservatively.
6. Preserve examples and existing fields.
7. Run `scripts/validate_profile.py`.
8. Summarise what changed and why.

## Interview handling

Ask the interview in 2-3 short batches rather than one long wall of text. Keep every question optional. If the user skips an answer, store nothing for that field and continue with defaults.

Do not ask for full legal names, private messages, exact location history, secrets, or sensitive details. For health, ask only practical constraints that affect safety, such as allergies or dietary restrictions.

## Preference confidence

Mark preference confidence when possible:

- high: directly stated by partner or repeated positive reaction
- medium: inferred from repeated behaviour
- low: one-off weak signal

## Output

```markdown
## Profile update summary
- Added:
- Updated:
- Unchanged:
- Uncertain / needs confirmation:
```
