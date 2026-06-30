---
name: profile-job-board
description: >
  Add or update job postings on Nick's public GitHub profile README job board.
  Use when asked about profile job board, opportunities, jobs.yaml, nicholasg3
  profile posting, or circulating roles on the profile README. NOT the Codex
  job scanner (Google Sheet) — see project_job_scanner.md.
metadata:
  short-description: "Profile README opportunities board"
---

# Profile job board

Nick's **GitHub profile README** includes an **Opportunities** section that auto-expires listings after their application deadline.

## Locations

| What | Path |
|------|------|
| Local repo | `/Users/nicholasgarcia/code/nicholasg3-profile` |
| GitHub | https://github.com/nicholasg3/nicholasg3 |
| Job data | `data/jobs.yaml` |
| Renderer | `scripts/render_jobs.py` |
| README markers | `<!-- job-board:start -->` … `<!-- job-board:end -->` |
| CI workflow | `.github/workflows/job-board.yml` |
| In-repo docs | `data/README.md` |

## Do NOT confuse with job scanner

The **Codex job scanner** (daily pulls → Google Sheet) is a separate system. Do not rebuild it or treat Notion "scan openings" tasks as unstarted work. See `project_job_scanner.md` in Claude memory.

## Add or update a listing

1. Edit `data/jobs.yaml` — copy the template in the file header or `data/README.md`.
2. Set `deadline` as `YYYY-MM-DD` (UTC). Jobs with `deadline < today` are **inactive**.
3. Push to `main`.
4. GitHub Actions re-renders `README.md` on push to `jobs.yaml` and **daily at 00:15 UTC**.

Required fields: `id`, `organization`, `title`, `deadline`, `apply_url`.

## Remove early

Delete the entry from `jobs.yaml`, or set `deadline` to a past date, then push.

## Preview locally

```bash
cd /Users/nicholasgarcia/code/nicholasg3-profile
.venv/bin/python scripts/render_jobs.py              # patches README.md
.venv/bin/python scripts/profile_job_title.py --text # terminal title preview
```

## Terminal title (Grok)

Active opportunities can appear in the **terminal window title** via OSC:

```bash
/Users/nicholasgarcia/code/nicholasg3-profile/.venv/bin/python \
  /Users/nicholasgarcia/code/nicholasg3-profile/scripts/profile_job_title.py
```

Wired on Grok `SessionStart` / `Stop` in `~/.grok/hooks/profile-job-board.json`.

Example: `Opportunities: 1 active · Simon AI policy · due Jul 15` or `Opportunities: none`.

## Triggers

Use this skill when the user mentions: profile job board, opportunities section, `jobs.yaml`, nicholasg3 profile posting, Simon Institute listing, or circulating a role on the profile README.