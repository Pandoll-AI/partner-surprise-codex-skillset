# Partner profile interview prompt

Use `$partner-profile-maintainer`.

Task:

If `data/partner_profile.json` does not exist or still looks like the example file, run the partner preference interview before creating surprise plans.

Rules:

- Ask the 12 questions from `references/profile_interview_ko.md` in 2-3 short batches.
- Let the user skip any question.
- Store only information useful for surprise planning.
- Do not ask for full legal names, private messages, exact location history, secrets, or sensitive details.
- For safety, ask only practical constraints such as allergies, dietary restrictions, budget, travel burden, and public-attention preference.

Output:

1. Interview questions
2. Draft `data/partner_profile.json` fields
3. Optional updates for `anniversaries.json` and `constraints.json`
4. Privacy check summary
