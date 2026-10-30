#!/usr/bin/env python3
"""Validate Project Continuity Work Items without third-party dependencies."""

from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

STATUSES = {
    "proposed", "ready", "in_progress", "blocked",
    "review", "done", "cancelled",
}
REQUIRED_METADATA = {
    "id", "title", "status", "priority", "created", "updated",
    "created_by", "assigned_to", "next_agent", "schema_version", "revision",
}
REQUIRED_SECTIONS = {
    "Objective",
    "Context",
    "Findings and decisions",
    "Evidence and references",
    "Completed",
    "Current state and workspace snapshot",
    "Next action",
    "Acceptance criteria",
    "Constraints, risks, and assumptions",
    "Handoff log",
    "Validation log",
}


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter opener")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("missing YAML frontmatter closer")
    raw = text[4:end]
    data: dict[str, str] = {}
    for line_no, line in enumerate(raw.splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")) or ":" not in line:
            raise ValueError(f"unsupported frontmatter syntax at line {line_no}")
        key, value = line.split(":", 1)
        key = key.strip()
        if not key or key in data:
            raise ValueError(f"empty or duplicate frontmatter key: {key!r}")
        data[key] = value.strip().strip('"').strip("'")
    return data, text[end + 5:]


def validate(path: Path) -> list[str]:
    errors: list[str] = []
    try:
        text = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
    except (OSError, UnicodeError, ValueError) as exc:
        return [str(exc)]

    missing = REQUIRED_METADATA - meta.keys()
    if missing:
        errors.append("missing metadata: " + ", ".join(sorted(missing)))
    if meta.get("status") not in STATUSES:
        errors.append(f"invalid status: {meta.get('status')!r}")
    if meta.get("schema_version") != "1.1":
        errors.append("schema_version must be 1.1")
    try:
        revision = int(meta.get("revision", ""))
        if revision < 1:
            raise ValueError
    except ValueError:
        errors.append("revision must be a positive integer")

    if not re.fullmatch(r"W-\d{8}-[a-z0-9]+(?:-[a-z0-9]+)*", meta.get("id", "")):
        errors.append("id must match W-YYYYMMDD-lowercase-slug")
    if not meta.get("title"):
        errors.append("title must not be empty")

    sections = set(re.findall(r"^## (.+?)\s*$", body, re.M))
    missing_sections = REQUIRED_SECTIONS - sections
    if missing_sections:
        errors.append("missing sections: " + ", ".join(sorted(missing_sections)))

    next_action = re.search(
        r"^## Next action\s*$([\s\S]*?)(?=^## |\Z)", body, re.M
    )
    if next_action and not next_action.group(1).strip():
        errors.append("Next action section is empty")

    if re.search(r"^## Next actions\s*$", body, re.M):
        errors.append("use one 'Next action' section, not plural 'Next actions'")

    if meta.get("status") == "done" and not re.search(
        r"^- \[x\] .+", body, re.M
    ):
        errors.append("done item must contain at least one checked completion item")

    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("work_item", type=Path)
    args = parser.parse_args()
    errors = validate(args.work_item)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Valid Work Item: {args.work_item}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
