#!/usr/bin/env bash
set -euo pipefail
MODE="${1:-global}"
ROOT_DIR="$(cd "$(dirname "$0")" && pwd)"

if [[ "$MODE" == "global" ]]; then
  mkdir -p "$HOME/.agents/skills" "$HOME/.codex/agents"
  rsync -a "$ROOT_DIR/.agents/skills/" "$HOME/.agents/skills/"
  rsync -a "$ROOT_DIR/.codex/agents/" "$HOME/.codex/agents/"
  echo "Installed skills to $HOME/.agents/skills and agents to $HOME/.codex/agents"
elif [[ "$MODE" == "project" ]]; then
  mkdir -p .agents/skills .codex/agents
  rsync -a "$ROOT_DIR/.agents/skills/" .agents/skills/
  rsync -a "$ROOT_DIR/.codex/agents/" .codex/agents/
  echo "Installed skills to current project .agents/skills and .codex/agents"
else
  echo "Usage: ./install.sh [global|project]" >&2
  exit 2
fi
