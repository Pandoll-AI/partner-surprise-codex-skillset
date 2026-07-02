#!/usr/bin/env python3
"""Print a travel/staycation research template."""
from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--location", default="Seoul or nearby Korea")
    parser.add_argument("--nights", type=int, default=1)
    parser.add_argument("--tone", default="restorative")
    args = parser.parse_args()

    print(f"""# Travel/staycation research brief

- Location scope: {args.location}
- Nights: {args.nights}
- Tone: {args.tone}

## Need to verify
- Availability:
- Price:
- Cancellation policy:
- Travel time:
- Weather/seasonal fit:
- Childcare/family logistics:
- Restaurant/spa/package details:

## Candidate table
| Option | Why now | Evidence | Burden | Budget | Risk |
|---|---|---|---:|---:|---|
|  |  |  |  |  |  |

## Reveal sentence
“요즘 당신이 좀 쉬는 시간이 필요해 보여서, 부담 없이 갈 수 있는 곳으로 내가 알아봤어. 무리하지 말고 마음에 들면 같이 가자.”
""")


if __name__ == "__main__":
    main()
