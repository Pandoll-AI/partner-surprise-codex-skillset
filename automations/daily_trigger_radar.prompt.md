# Daily trigger radar automation

Use `$life-event-trigger-radar` and `$surprise-orchestrator`.

Task:

Scan the next 14 days using `data/partner_profile.json`, `data/anniversaries.json`, and `data/constraints.json` if available. Identify whether I should do a tiny, small, medium, or premium surprise for my partner.

Rules:

- Do not invent live facts.
- If trend or venue research is needed, generate exact search queries and mark them as needs verification.
- Prefer low-burden gestures on normal weekdays.
- Output only if there is a meaningful trigger or a very easy “just because” opportunity.

Output:

1. Trigger
2. Recommended scale
3. One action I can do today
4. Exact Korean message
5. Risk check
