#!/usr/bin/env python3
"""Emit profile job-board summary as terminal window title (OSC \\033]0;...\\007).

Reads data/jobs.yaml via render_jobs.py (same deadline filter as README job board).
Used by Grok SessionStart/Stop hooks (~/.grok/hooks/profile-job-board.json).

Usage:
  python3 scripts/profile_job_title.py           # set terminal title (OSC to stdout)
  python3 scripts/profile_job_title.py --text    # print title line only (no OSC)
  python3 scripts/profile_job_title.py --clear   # reset title to default
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

from render_jobs import format_terminal_title  # noqa: E402

OSC_SET_TITLE = "\033]0;%s\007"
OSC_CLEAR = "\033]0;\007"


def emit_title(title: str, stream=None) -> None:
    out = stream or sys.stdout
    out.write(OSC_SET_TITLE % title)
    out.flush()


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description="Profile job board terminal title")
    parser.add_argument("--text", action="store_true", help="print title line only")
    parser.add_argument("--clear", action="store_true", help="reset terminal title")
    parser.add_argument("--max-len", type=int, default=80, help="truncate title")
    args = parser.parse_args(argv)

    if args.clear:
        if not args.text:
            sys.stdout.write(OSC_CLEAR)
            sys.stdout.flush()
        return 0

    title = format_terminal_title(max_len=args.max_len)
    if args.text:
        print(title)
    else:
        emit_title(title)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())