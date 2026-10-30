#!/usr/bin/env bash
set -euo pipefail

ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SOURCE="$ROOT/.agents/skills/project-continuity"
MARKER=".installed-by-project-continuity"
MODE=install
if [ "$#" -gt 0 ]; then MODE="$1"; fi

CODEX_HOME_DIR="$(printenv CODEX_HOME || true)"
if [ -z "$CODEX_HOME_DIR" ]; then CODEX_HOME_DIR="$HOME/.codex"; fi

if [ ! -f "$SOURCE/SKILL.md" ]; then
  echo "Skill source not found: $SOURCE" >&2
  exit 1
fi

install_one() {
  local parent="$1"
  local dest="$parent/project-continuity"
  local tmp
  local old=""
  mkdir -p "$parent"

  if [ -e "$dest" ]; then
    if [ ! -f "$dest/$MARKER" ]; then
      echo "Refusing to overwrite unmanaged skill directory: $dest" >&2
      return 1
    fi
    if diff -qr -x "$MARKER" "$SOURCE" "$dest" >/dev/null; then
      echo "Already in sync: $dest"
      return 0
    fi
  fi

  tmp="$(mktemp -d "$parent/.project-continuity.tmp.XXXXXX")"
  if ! cp -R "$SOURCE/." "$tmp/"; then
    rm -rf "$tmp"
    return 1
  fi
  touch "$tmp/$MARKER"

  if [ -e "$dest" ]; then
    old="$(mktemp -d "$parent/.project-continuity.old.XXXXXX")"
    rmdir "$old"
    if ! mv "$dest" "$old"; then
      rm -rf "$tmp"
      return 1
    fi
  fi

  if ! mv "$tmp" "$dest"; then
    if [ -n "$old" ] && [ -d "$old" ]; then mv "$old" "$dest"; fi
    rm -rf "$tmp"
    return 1
  fi

  if [ -n "$old" ] && [ -d "$old" ]; then rm -rf "$old"; fi
  echo "Installed: $dest"
}

check_one() {
  local parent="$1"
  local dest="$parent/project-continuity"
  if [ ! -f "$dest/SKILL.md" ]; then
    echo "Missing: $dest" >&2
    return 1
  fi
  if diff -qr -x "$MARKER" "$SOURCE" "$dest" >/dev/null; then
    echo "In sync: $dest"
  else
    echo "Out of sync: $dest" >&2
    return 1
  fi
}

case "$MODE" in
  install)
    install_one "$CODEX_HOME_DIR/skills"
    install_one "$HOME/.gemini/antigravity-cli/skills"
    ;;
  check)
    check_one "$CODEX_HOME_DIR/skills"
    check_one "$HOME/.gemini/antigravity-cli/skills"
    ;;
  *)
    echo "Usage: $0 [install|check]" >&2
    exit 2
    ;;
esac
