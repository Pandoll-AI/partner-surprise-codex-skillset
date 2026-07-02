# Profile Schema Notes

## partner_profile.json

- `name_label`: optional; avoid storing full legal names unless useful.
- `preferences.likes`: tags for food, style, activities, brands.
- `preferences.dislikes`: tags to avoid.
- `preferences.style_tags`: design/tone preferences.
- `preferences.allergies_or_hard_constraints`: practical safety constraints.
- `recent_context`: optional, short-lived context; remove when stale.
- `history`: previous surprises and reactions.

## anniversaries.json

- Use `YYYY-MM-DD` for one-off exact dates.
- Use `MM-DD` for annual recurring dates.
- `importance`: 1 to 5.
- `default_scale`: tiny, small, medium, premium.

## constraints.json

- budget
- travel time
- childcare/family constraints
- dietary constraints
- public attention preference
- default location
