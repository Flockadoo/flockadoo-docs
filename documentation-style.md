# Documentation style guide

This repo is the source for the [Flockadoo documentation](README.md), built with Zensical and published at docs.flockadoo.ai. Pages are **user guides** — written for people using the dashboard, API, or provider client.

## Examples

Use generic, fictional names so examples do not look like someone's private account:

- Flocks: **flockadoo-flock1**, **flockadoo-flock2**
- Models: real public model IDs are fine (e.g. `Qwen/Qwen2.5-7B-Instruct`)
- Prefix with **“For example,”** when illustrating a scenario

Do not use real flock names, emails, or API keys in published docs.

## Voice

- Address the reader as **you**
- Bold dashboard labels: **Flocks**, **Settings**, **Save**
- Prefer short steps and tables over long prose

## Scope by folder

| Folder | Purpose |
|--------|---------|
| `getting-started/` | Provider onboarding (requirements, signup, install) |
| `consumer/` | Calling the API, spending caps, consumer dashboard |
| `provider/` | Provider dashboard (flocks, pricing, settings) |
| `provider-client/` | Installing and running the provider client |

Keep implementation details (database tables, microservice names) out of these guides. Technical architecture belongs in **flockadoo-server** `documentation/technical.md`.

## New pages

1. Add the file under the right folder in `docs/`.
2. Add an entry to `nav` in `zensical.toml`.

Callouts use admonition syntax (`!!! info`, `!!! warning`) with the body indented four spaces.
3. Link related pages at the bottom of the article.

## Cursor agents

Editor rules for this repo live in `.cursor/rules/1000-documentation-style.mdc`.
