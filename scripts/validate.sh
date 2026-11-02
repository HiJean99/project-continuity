#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SKILL="$ROOT/.agents/skills/project-continuity"

grep -q '^name: project-continuity$' "$SKILL/SKILL.md"
grep -q '^description: ' "$SKILL/SKILL.md"
test "$(cat "$SKILL/VERSION")" = "1.3.0"
grep -q "Do not use for routine coding tasks" "$SKILL/SKILL.md"

for file in \
  "$SKILL/references/memory-model.md" \
  "$SKILL/references/work-item-format.md" \
  "$SKILL/references/operations.md" \
  "$SKILL/references/AGENTS-section.md" \
  "$SKILL/references/when-to-use.md" \
  "$SKILL/references/legacy-v1.2-orca-integration.md" \
  "$SKILL/references/legacy-v1.2-execution-record-format.md" \
  "$SKILL/templates/PROJECT.md" \
  "$SKILL/templates/STATE.md" \
  "$SKILL/templates/DECISIONS.md" \
  "$SKILL/templates/OPEN_QUESTIONS.md" \
  "$SKILL/templates/WORK_ITEM.md" \
  "$SKILL/templates/LEGACY_V1.2_EXECUTION_RECORD.md" \
  "$SKILL/templates/work-README.md" \
  "$SKILL/VERSION"
do
  test -s "$file"
done

bash -n "$ROOT/scripts/install-global.sh"
bash -n "$ROOT/scripts/validate.sh"
python3 -m unittest discover -s "$ROOT/tests" -v
python3 -m py_compile "$ROOT/.agents/skills/project-continuity/scripts/validate_work_item.py" "$ROOT/.agents/skills/project-continuity/scripts/validate_execution.py"

echo "Project Continuity v$(cat "$SKILL/VERSION") Skill structure: OK"
echo "Shell scripts syntax: OK"
