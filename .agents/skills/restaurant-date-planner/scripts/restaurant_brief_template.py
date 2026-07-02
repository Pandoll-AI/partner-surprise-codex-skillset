#!/usr/bin/env python3
"""Print a restaurant/date plan research template."""
from __future__ import annotations

import argparse


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--location", default="Seoul")
    parser.add_argument("--tone", default="warm elegant")
    parser.add_argument("--occasion", default="just-because appreciation")
    args = parser.parse_args()

    print(f"""# Restaurant/date research brief

- Location: {args.location}
- Tone: {args.tone}
- Occasion: {args.occasion}

## Need to verify
- Official opening hours:
- Reservation availability:
- Price/course/menu:
- Recent reviews:
- Noise/crowding:
- Dietary fit:
- Nearby second stop:

## Candidate table
| Venue | Why now | Evidence | Budget | Logistics | Risk |
|---|---|---|---:|---|---|
|  |  |  |  |  |  |

## Natural invitation sentence
“요즘 여기가 [verified reason]로 괜찮아 보여서, 당신이랑 조용히 가보고 싶었어.”
""")


if __name__ == "__main__":
    main()
