---
name: surprise-orchestrator
description: Surprise planning for a romantic partner. Use when the user wants a thoughtful event, gift, restaurant, travel, recovery gesture, anniversary plan, Korean seasonal event plan, or trend-backed romantic action.
---

# Surprise Orchestrator

Purpose: turn the user's context into one practical, emotionally intelligent surprise plan with a natural, honest reason.

## When to trigger

Use this skill when the user asks for:

- a surprise for a romantic partner
- anniversary, birthday, White Day, Valentine's Day, Pepero Day, Christmas, Parents' Day, school/family milestone, or seasonal plan
- a recovery gesture after stress, argument, disappointment, or a bad day
- gift, restaurant, hotel, short trip, date course, flower, letter, message, or small care action
- “trend analysis” to justify why a recommendation is timely

Do not use for generic travel, generic shopping, or restaurant search unless the relationship-surprise purpose is explicit.

## Required inputs

Look for these files first, but continue with sensible defaults if some are missing:

- `data/partner_profile.json`
- `data/partner_profile.example.json`
- `data/anniversaries.json` or `data/anniversaries.example.json`
- `data/constraints.json` or `data/constraints.example.json`
- `data/candidates.json` or `data/candidates.example.json`

If `data/partner_profile.json` is missing or clearly still empty, pause surprise planning and run the partner preference interview first. Read `../partner-profile-maintainer/references/profile_interview_ko.md`, ask the 12 questions in manageable batches, then create or update `data/partner_profile.json` before recommending gifts, restaurants, travel, or messages. Use the example profile only for demos, not as a substitute for real preferences.

If live web, calendar, email, or booking tools are available, use only with the user's authorisation and only as needed.

## Core workflow

1. **Frame the objective**
   - Identify the occasion, emotional tone, budget, lead time, and whether it should be small, medium, or premium.
   - Default to Seoul/Korea context unless user says otherwise.
   - Never assume private sensitive facts not provided.

2. **Trigger scan**
   - Invoke or follow `life-event-trigger-radar`.
   - Find upcoming dates, seasonal hooks, stress/recovery signals, and “just because” opportunities.
   - Assign an urgency level: today, 1–3 days, 1 week, 2–4 weeks, or later.

3. **Trend evidence**
   - Invoke or follow `trend-research-scout`.
   - For every trend-backed claim, collect date, source, and what it actually supports.
   - Do not use “famous”, “viral”, “newly opened”, “highly rated”, “celebrity-used”, or “popular” unless verified.
   - If browsing is unavailable, output search queries and mark trend claims as “needs verification”.

4. **Generate candidates**
   Create at least 6 options across different effort/budget levels:
   - small care action
   - gift
   - restaurant/date course
   - experience/class/show
   - overnight or day trip
   - message/letter/ritual

5. **Score candidates**
   Use this rubric from 1 to 5:
   - fit to partner profile
   - timeliness / natural reason
   - surprise value without burden
   - logistics feasibility
   - emotional warmth
   - risk level, reverse-scored

6. **Select top 3**
   Provide one safest choice, one memorable choice, and one premium choice.
   Include a clear “why this now?” explanation.

7. **Create execution plan**
   For the recommended option, include:
   - exact action
   - timing
   - reservation/order checklist
   - budget range
   - message/card text
   - what to say naturally
   - contingency plan
   - risk check

8. **Review before final**
   Ask internally:
   - Is the reason honest?
   - Could this create pressure or extra work for the partner?
   - Is it aligned with the partner's actual tastes rather than the user's fantasy?
   - Did I avoid fake evidence?
   - Is there a simple version if time/budget collapses?

## Output format

Use the template in `references/output_templates.md` unless the user requests another format.

## Tone

Warm, calm, practical. The plan should feel like someone becoming more attentive, not like a marketing campaign.
