# CLAUDE.md

This repo is one file. `README.md` is the GitHub **profile** README — it renders
at github.com/nitin27may, above every repo in the account. There is no build, no
test, and no deploy: pushing to `master` publishes it.

That makes the risk here editorial rather than technical. What follows is the
context needed to change it without breaking something invisible.

## The project tables are a claim about an estate, not a list of favourites

Six repositories are listed, each with a `nitinksingh.com/<repo>/` documentation
link. Those six are the ones that actually have a published doc site. Two
generators, and the split matters when a link goes dead:

| Repo | Generator | Deploys |
|---|---|---|
| `ai-resources` | MkDocs Material | `.github/workflows/deploy.yml` |
| `ms-graph-mcp` | MkDocs Material | **by hand** — no workflow |
| `mcp-generator` | MkDocs Material | **by hand** — no workflow |
| `mean-docker` | Jekyll | `jekyll-gh-pages.yml` |
| `clean-architecture-docker-dotnet-angular` | Jekyll | `jekyll-gh-pages.yml` |
| `e-commerce-agents` | Jekyll | `jekyll-gh-pages.yml` |

The two hand-deployed sites are the ones most likely to be stale relative to
their repo. A green CI badge on those repos says nothing about their docs.

**Do not add a doc link for a repo that has no site.** Before adding a row,
confirm the site actually serves — the URL pattern is predictable, which makes it
easy to write a link to a 404.

## The star badges are live images, not text

Each row carries a `img.shields.io/github/stars/...` badge. The count is
rendered server-side by shields.io into an SVG, so it does not appear in the raw
Markdown and `curl` on this file cannot verify it. **Checking whether the counts
render correctly needs a headless browser against the rendered profile page**,
not a fetch of README.md.

Consequence: a typo in a repo name inside a badge URL degrades to a badge reading
"invalid" or "repo not found" rather than an error anyone notices. If you rename
a repo, both the badge URL and the link need updating.

## Overlap with the blog

`nitinksingh.com/projects/` covers the same estate in longer form, and
`nitinksingh.com/work/` is the contact/consulting page this README links to
twice. A repo added here usually belongs there too — the two drifting apart is
the normal failure mode. That site lives in the `nitin27may.github.io` repo.

## Voice

Match the existing register: direct, first person, specific about what was built
and why. No emojis, no "passionate about", no buzzword lists beyond the
Technical Focus section, which is deliberately a scannable index rather than
prose. The Technical Focus blocks use two trailing spaces for line breaks — keep
them or the categories collapse into one paragraph.

The default branch is `master`, not `main`.
