#!/usr/bin/env python3
"""Render active job board section from data/jobs.yaml into jobs.md markers."""
from __future__ import annotations

import json
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
JOBS_PAGE = ROOT / "jobs.md"
JOBS_JSON = ROOT / "jobs.json"
START = "<!-- job-board:start -->"
END = "<!-- job-board:end -->"

# Fields carried into the public jobs.json (in addition to id/kind).
_JSON_FIELDS = [
    "organization",
    "title",
    "location",
    "deadline",
    "posted",
    "apply_url",
    "tags",
    "summary",
    "responsibilities",
    "requirements",
    "notes",
]


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


def _job_to_json(job: dict) -> dict:
    out: dict = {
        "id": job.get("id", ""),
        "kind": str(job.get("kind", "job")).lower(),
    }
    for field in _JSON_FIELDS:
        value = job.get(field)
        if field == "apply_url":
            value = job.get("apply_url") or job.get("url") or ""
        if isinstance(value, str):
            value = value.strip()
        elif value is None:
            value = [] if field in ("tags", "responsibilities", "requirements") else ""
        out[field] = value
    return out


def render_json(today: date | None = None) -> str:
    today = today or date.today()
    jobs = _active(_load_jobs(), today)
    data = {
        "updated": today.isoformat(),
        "jobs": [_job_to_json(job) for job in jobs],
    }
    return json.dumps(data, indent=2, ensure_ascii=False) + "\n"


def write_jobs_json(today: date | None = None) -> bool:
    new_text = render_json(today)
    old_text = JOBS_JSON.read_text(encoding="utf-8") if JOBS_JSON.exists() else None
    if old_text == new_text:
        return False
    JOBS_JSON.write_text(new_text, encoding="utf-8")
    return True


def _render_job(job: dict, today: date) -> str:
    org = job.get("organization", "Organization")
    title = job.get("title", "Role")
    loc = job.get("location", "")
    dl = str(job.get("deadline", ""))
    url = job.get("apply_url") or job.get("url") or ""
    # kind: "job" (default) or "program" (courses, fellowships, classes).
    # Programs get neutral labels: Details / Express interest by.
    kind = str(job.get("kind", "job")).lower()
    detail_label = "Details" if kind == "program" else "Job description"
    by_label = "Express interest by" if kind == "program" else "Apply by"
    lines = [f"### {title} — {org}", ""]
    if loc:
        lines.append(f"**Location:** {loc}  ")
    lines.append(f"**{by_label}:** {_fmt_deadline(dl, today)}  ")
    if url:
        lines.append(f"**{detail_label}:** [View posting]({url})  ")
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


def _short_job_label(job: dict) -> str:
    """Compact label for terminal title (~20 chars)."""
    title = (job.get("title") or "Role").strip()
    org = (job.get("organization") or "").strip()
    org_short = org.split()[0] if org else ""
    lower = title.lower()
    if "ai policy" in lower:
        role = "AI policy"
    elif len(title) <= 24:
        role = title
    else:
        role = title[:24].rstrip() + "…"
    if org_short:
        return f"{org_short} {role}"
    return role


def format_terminal_title(today: date | None = None, max_len: int = 80) -> str:
    """One-line summary for terminal window title (OSC)."""
    today = today or date.today()
    jobs = _active(_load_jobs(), today)
    if not jobs:
        return "Opportunities: none"
    n = len(jobs)
    short = _short_job_label(jobs[0])
    dl = _parse_deadline(str(jobs[0]["deadline"]))
    due = dl.strftime("%b %-d") if sys.platform != "win32" else dl.strftime("%b %d")
    if n == 1:
        line = f"Opportunities: 1 active · {short} · due {due}"
    else:
        line = f"Opportunities: {n} active · {short} · due {due}"
    return line[:max_len]


def render_section(today: date | None = None) -> str:
    today = today or date.today()
    jobs = _active(_load_jobs(), today)
    parts = [
        "## Opportunities",
        "",
        "Roles I am helping circulate. Listings **auto-remove after the application deadline**.",
        "",
        f"_Updated {today.isoformat()}. "
        "[Add or edit listings](https://github.com/nicholasg3/nicholasg3/blob/main/data/jobs.yaml)._",
        "",
    ]
    if not jobs:
        parts.append("_No active postings right now._")
    else:
        for i, job in enumerate(jobs):
            if i:
                # Blank line BEFORE the --- is load-bearing: without it,
                # Markdown parses the previous line + --- as a setext H2
                # (this made the tags line render huge, 2026-09-05).
                parts.append("")
                parts.append("---")
                parts.append("")
            parts.append(_render_job(job, today))
    return "\n".join(parts).rstrip() + "\n"


def patch_jobs_page(section: str) -> bool:
    text = JOBS_PAGE.read_text(encoding="utf-8")
    if START not in text or END not in text:
        raise SystemExit(f"jobs.md must contain {START} and {END}")
    pattern = re.compile(
        re.escape(START) + r".*?" + re.escape(END),
        re.DOTALL,
    )
    new_block = f"{START}\n{section.rstrip()}\n{END}"
    new_text = pattern.sub(new_block, text, count=1)
    if new_text == text:
        return False
    JOBS_PAGE.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    section = render_section()
    changed = patch_jobs_page(section)
    json_changed = write_jobs_json()
    n = len(_active(_load_jobs(), date.today()))
    print(
        f"Active jobs: {n}; jobs.md {'updated' if changed else 'unchanged'}; "
        f"jobs.json {'updated' if json_changed else 'unchanged'}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())