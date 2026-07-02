#!/usr/bin/env python3
"""Validate basic JSON structure for surprise-planning data files."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

REQUIRED_PROFILE_KEYS = {"preferences"}
REQUIRED_ANNIV_KEYS = {"events"}


def load(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def check_file(path: Path, required: set[str]) -> list[str]:
    errors: list[str] = []
    if not path.exists():
        return [f"Missing: {path}"]
    try:
        data = load(path)
    except json.JSONDecodeError as exc:
        return [f"Invalid JSON in {path}: {exc}"]
    missing = required - set(data.keys())
    if missing:
        errors.append(f"{path}: missing keys {sorted(missing)}")
    return errors


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--profile", default="data/partner_profile.example.json")
    parser.add_argument("--anniversaries", default="data/anniversaries.example.json")
    parser.add_argument("--constraints", default="data/constraints.example.json")
    args = parser.parse_args()

    errors: list[str] = []
    errors.extend(check_file(Path(args.profile), REQUIRED_PROFILE_KEYS))
    errors.extend(check_file(Path(args.anniversaries), REQUIRED_ANNIV_KEYS))
    # Constraints are flexible but should parse.
    cpath = Path(args.constraints)
    if cpath.exists():
        try:
            load(cpath)
        except json.JSONDecodeError as exc:
            errors.append(f"Invalid JSON in {cpath}: {exc}")

    if errors:
        print("Validation failed:")
        for e in errors:
            print(f"- {e}")
        raise SystemExit(1)
    print("Profile files look valid.")


if __name__ == "__main__":
    main()
