#!/usr/bin/env python3
"""Validate Project Continuity v1.2 Execution Records (standard library only)."""
from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

STATUSES = {"planned", "active", "blocked", "review", "completed", "failed", "cancelled"}
REQUIRED_META = {"id", "work_item_id", "backend", "backend_version", "run_id", "objective", "status", "created", "updated", "schema_version", "revision"}
REQUIRED_SECTIONS = {"Objective", "Run", "Task map", "Evidence and outputs", "Blockers and decisions", "Reconciliation", "Next action", "History"}


def parse_frontmatter(text: str) -> tuple[dict[str, str], str]:
    if not text.startswith("---\n"):
        raise ValueError("missing YAML frontmatter opener")
    end = text.find("\n---\n", 4)
    if end < 0:
        raise ValueError("missing YAML frontmatter closer")
    data: dict[str, str] = {}
    for number, line in enumerate(text[4:end].splitlines(), 1):
        if not line.strip() or line.lstrip().startswith("#"):
            continue
        if line.startswith((" ", "\t")) or ":" not in line:
            raise ValueError(f"unsupported frontmatter syntax at line {number}")
        key, value = line.split(":", 1)
        key = key.strip()
        if not key or key in data:
            raise ValueError(f"empty or duplicate frontmatter key: {key!r}")
        data[key] = value.strip().strip('"').strip("'")
    return data, text[end + 5:]


def validate(path: Path) -> list[str]:
    try:
        text = path.read_text(encoding="utf-8")
        meta, body = parse_frontmatter(text)
    except (OSError, UnicodeError, ValueError) as exc:
        return [str(exc)]
    errors: list[str] = []
    missing = REQUIRED_META - meta.keys()
    if missing:
        errors.append("missing metadata: " + ", ".join(sorted(missing)))
    if meta.get("schema_version") != "1.2":
        errors.append("schema_version must be 1.2")
    if meta.get("status") not in STATUSES:
        errors.append(f"invalid status: {meta.get('status')!r}")
    for field, pattern, message in (
        ("id", r"E-\d{8}-[a-z0-9]+(?:-[a-z0-9]+)*", "id must match E-YYYYMMDD-lowercase-slug"),
        ("work_item_id", r"W-\d{8}-[a-z0-9]+(?:-[a-z0-9]+)*", "work_item_id must match W-YYYYMMDD-lowercase-slug"),
    ):
        if not re.fullmatch(pattern, meta.get(field, "")):
            errors.append(message)
    if not meta.get("objective", "").strip():
        errors.append("objective must not be empty")
    try:
        if int(meta.get("revision", "")) < 1:
            raise ValueError
    except ValueError:
        errors.append("revision must be a positive integer")
    if meta.get("status") != "planned" and not meta.get("run_id", "").strip():
        errors.append("run_id is required once status is not planned")
    sections = set(re.findall(r"^## (.+?)\s*$", body, re.M))
    absent = REQUIRED_SECTIONS - sections
    if absent:
        errors.append("missing sections: " + ", ".join(sorted(absent)))
    action = re.search(r"^## Next action\s*$([\s\S]*?)(?=^## |\Z)", body, re.M)
    if action and meta.get("status") not in {"completed", "cancelled"} and not action.group(1).strip():
        errors.append("Next action section is empty for an unsettled execution")
    if re.search(r"^## Next actions\s*$", body, re.M):
        errors.append("use one 'Next action' section, not plural 'Next actions'")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("execution_record", type=Path)
    args = parser.parse_args()
    errors = validate(args.execution_record)
    if errors:
        for error in errors:
            print(f"ERROR: {error}", file=sys.stderr)
        return 1
    print(f"Valid Execution Record: {args.execution_record}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
