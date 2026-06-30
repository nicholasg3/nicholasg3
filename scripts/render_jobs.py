#!/usr/bin/env python3
"""Render active job board section from data/jobs.yaml into README.md markers."""
from __future__ import annotations

import re
import sys
from datetime import date, datetime
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None  # type: ignore

ROOT = Path(__file__).resolve().parent.parent
JOBS_FILE = ROOT / "data" / "jobs.yaml"
README = ROOT / "README.md"
START = "<!-- job-board:start -->"
END = "<!-- job-board:end -->"


def _parse_deadline(value: str) -> date:
    return datetime.strptime(value.strip(), "%Y-%m-%d").date()


def _load_jobs() -> list[dict]:
    if yaml is None:
        raise SystemExit("PyYAML required: pip install pyyaml")
    raw = yaml.safe_load(JOBS_FILE.read_text(encoding="utf-8")) or {}
    jobs = raw.get("jobs") or []
    if not isinstance(jobs, list):
        raise SystemExit("jobs.yaml: 'jobs' must be a list")
    return jobs


def _active(jobs: list[dict], today: date) -> list[dict]:
    out: list[dict] = []
    for job in jobs:
        if not isinstance(job, dict):
            continue
        dl = job.get("deadline")
        if not dl:
            continue
        try:
            if _parse_deadline(str(dl)) >= today:
                out.append(job)
        except ValueError as e:
            print(f"WARN: skip job {job.get('id')}: bad deadline {dl!r} ({e})", file=sys.stderr)
    out.sort(key=lambda j: _parse_deadline(str(j["deadline"])))
    return out


def _fmt_deadline(dl: str, today: date) -> str:
    d = _parse_deadline(dl)
    days = (d - today).days
    base = d.strftime("%B %-d, %Y") if sys.platform != "win32" else d.strftime("%B %d, %Y")
    if days == 0:
        return f"**{base}** (today)"
    if days == 1:
        return f"**{base}** (1 day left)"
    if days <= 14:
        return f"**{base}** ({days} days left)"
    return f"**{base}**"


def _render_job(job: dict, today: date) -> str:
    org = job.get("organization", "Organization")
    title = job.get("title", "Role")
    loc = job.get("location", "")
    dl = str(job.get("deadline", ""))
    url = job.get("apply_url") or job.get("url") or ""
    lines = [f"### {title} — {org}", ""]
    if loc:
        lines.append(f"**Location:** {loc}  ")
    lines.append(f"**Apply by:** {_fmt_deadline(dl, today)}  ")
    if url:
        lines.append(f"**Job description:** [View posting]({url})  ")
    lines.append("")
    if job.get("summary"):
        lines.append(str(job["summary"]).strip())
        lines.append("")
    if job.get("responsibilities"):
        lines.append("**Responsibilities:**")
        for item in job["responsibilities"]:
            lines.append(f"- {item}")
        lines.append("")
    if job.get("requirements"):
        lines.append("**Looking for:**")
        for item in job["requirements"]:
            lines.append(f"- {item}")
        lines.append("")
    if job.get("travel"):
        lines.append(f"**Travel:** {str(job['travel']).strip()}")
        lines.append("")
    tags = job.get("tags") or []
    if tags:
        lines.append(" ".join(f"`{t}`" for t in tags))
        lines.append("")
    return "\n".join(lines).rstrip()


def render_section(today: date | None = None) -> str:
    today = today or date.today()
    jobs = _active(_load_jobs(), today)
    parts = [
        "## Opportunities",
        "",
        "Roles I am helping circulate. Listings **auto-remove after the application deadline**.",
        "",
        f"_Updated {today.isoformat()}. [Add or edit listings](data/jobs.yaml)._",
        "",
    ]
    if not jobs:
        parts.append("_No active postings right now._")
    else:
        for i, job in enumerate(jobs):
            if i:
                parts.append("---")
                parts.append("")
            parts.append(_render_job(job, today))
    return "\n".join(parts).rstrip() + "\n"


def patch_readme(section: str) -> bool:
    text = README.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit(f"README.md must contain {START} and {END}")
    pattern = re.compile(
        re.escape(START) + r".*?" + re.escape(END),
        re.DOTALL,
    )
    new_block = f"{START}\n{section.rstrip()}\n{END}"
    new_text = pattern.sub(new_block, text, count=1)
    if new_text == text:
        return False
    README.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    section = render_section()
    changed = patch_readme(section)
    n = len(_active(_load_jobs(), date.today()))
    print(f"Active jobs: {n}; README {'updated' if changed else 'unchanged'}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())