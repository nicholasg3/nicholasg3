# Job board data

Edit `jobs.yaml` to add or update listings on the [opportunities page](../jobs.md).

## Add a posting

```yaml
  - id: unique-slug-2026
    organization: Organization Name
    title: Role Title
    location: City, Country
    deadline: "2026-12-31"   # YYYY-MM-DD — auto-removed after this date (UTC)
    posted: "2026-06-29"
    apply_url: "https://..."
    summary: >
      One paragraph on the role.
    requirements:
      - Bullet one
    tags:
      - tag-one
```

Push to `main`. GitHub Actions re-renders `jobs.md` immediately and daily.

## Remove early

Delete the entry from `jobs.yaml`, or set `deadline` to a past date.

## Fields

| Field | Required | Notes |
|-------|----------|-------|
| `id` | yes | Stable slug |
| `organization` | yes | |
| `title` | yes | |
| `deadline` | yes | ISO date |
| `apply_url` | yes | JD or application link |
| `location` | no | |
| `posted` | no | |
| `summary` | no | |
| `responsibilities` | no | list |
| `requirements` | no | list |
| `travel` | no | string |
| `tags` | no | list |