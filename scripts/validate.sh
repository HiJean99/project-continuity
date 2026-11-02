#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILL="$ROOT/.agents/skills/project-continuity"

grep -q '^name: project-continuity$' "$SKILL/SKILL.md"
grep -q '^description: ' "$SKILL/SKILL.md"

for file in \
  "$SKILL/references/memory-model.md" \
  "$SKILL/references/work-item-format.md" \
  "$SKILL/references/operations.md" \
  "$SKILL/references/AGENTS-section.md" \
  "$SKILL/references/orca-integration.md" \
  "$SKILL/references/execution-record-format.md" \
  "$SKILL/templates/PROJECT.md" \
  "$SKILL/templates/STATE.md" \
  "$SKILL/templates/DECISIONS.md" \
  "$SKILL/templates/OPEN_QUESTIONS.md" \
  "$SKILL/templates/WORK_ITEM.md" \
  "$SKILL/templates/EXECUTION_RECORD.md" \
  "$SKILL/templates/work-README.md"
do
  test -s "$file"
done

bash -n "$ROOT/scripts/install-global.sh"
bash -n "$ROOT/scripts/validate.sh"
python3 -m unittest discover -s "$ROOT/tests" -v
python3 -m py_compile "$ROOT/.agents/skills/project-continuity/scripts/validate_work_item.py" "$ROOT/.agents/skills/project-continuity/scripts/validate_execution.py"

echo "Project Continuity Skill structure: OK"
echo "Shell scripts syntax: OK"
