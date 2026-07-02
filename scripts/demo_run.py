#!/usr/bin/env python3
"""Run a demo of the skillset using example data."""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path


def main() -> None:
    root = Path(__file__).resolve().parents[1]
    cmd = [
        sys.executable,
        str(root / "scripts/generate_surprise_brief.py"),
        "--profile", str(root / "data/partner_profile.example.json"),
        "--anniversaries", str(root / "data/anniversaries.example.json"),
        "--constraints", str(root / "data/constraints.example.json"),
        "--candidates", str(root / "data/candidates.example.json"),
        "--date", "2026-07-02",
    ]
    subprocess.run(cmd, check=True)


if __name__ == "__main__":
    main()
