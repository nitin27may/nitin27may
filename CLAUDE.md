# CLAUDE.md

This repo is `README.md`, the images it uses in `assets/`, and the script that
generates the graphics in `tools/`. `README.md` is the
GitHub **profile** README: it renders at github.com/nitin27may, above every repo
in the account. There is no build, no test, and no deploy: pushing to `master`
publishes it.

That makes the risk here editorial rather than technical. What follows is the
context needed to change it without breaking something invisible.

**Fetch before editing.** This file is also edited on github.com and through
pull requests, so a local clone goes stale. Run `git pull` first; a review
written against an old local copy is a review of the wrong page.

## Audience

Recruiters, hiring managers, and engineers who land on the profile. The first
screen must answer: who, what level, where, what proof, how to reach.

## README structure

GitHub's sidebar already shows the name, bio line, location, and links, and the
pinned repos sit directly under the README as cards with live star counts. The
README does what those cannot: positioning, proof, and how the work is done. Do
not repeat the name as an `#` heading or put a contact row at the top.

Sections, in this order:

1. Banner image (`assets/banner.svg`), then one positioning paragraph, then the
   stats strip
2. `## How I work`: principles, with keyless and zero trust first. It sits above
   the projects because it is the differentiator; the projects are the proof
3. `## Selected work`: `e-commerce-agents` featured first as an `###` heading
   with a description, stack tags, the product screenshot, and the architecture
   graphic; then `### More projects` as a bullet list, each with a bold linked
   repo name, a docs link where a site exists, one or two sentences, and stack
   tags on a second line. Stack tags are inline code. Do not use a three-column
   table here: repo names wrap badly at profile width
4. `## Stack`: one table, five rows
5. `## Writing`: named blog posts with links
6. `## Work with me`: one paragraph linking to `nitinksingh.com/work/`, then the
   contact row with icons

## Graphics

`tools/generate_assets.py assets` writes the banner, the stats strip, and the
architecture graphic. Edit the script and regenerate; do not hand-edit those
SVGs.

- The banner is one dark panel used in both themes. The stats strip and the
  architecture graphic have `-light` and `-dark` versions, switched with a
  `<picture>` element and `prefers-color-scheme`
- Colours follow the blog: teal `#0d9488` as the accent, gold `#D4AF37` for one
  highlight, blue for services, slate for infrastructure, green for approval
- The stats are written as floors (15+, 280+, 90+) and are static. Recheck them
  when editing: total stars across non-fork repos, and the item count in the
  blog feed
- The architecture graphic replaced a Mermaid block. GitHub drew that block
  large and sparse, and can fail to render it at all, which dumps the diagram
  source into the page. Do not go back to Mermaid here
- `assets/e-commerce-agents.png` is `docs/images/flow-product-search.png` from
  the `e-commerce-agents` repo, scaled to 1700px wide. It has a faint vertical
  line from the original capture; replace it when a cleaner screenshot exists
- Every image needs `alt` text that carries the same information as the image

## Doc links are a claim about an estate

Six repositories carry a `nitinksingh.com/<repo>/` documentation link. Those six
are the ones that actually have a published doc site. Two generators, and the
split matters when a link goes dead:

| Repo | Generator | Deploys |
|---|---|---|
| `ai-resources` | MkDocs Material | `.github/workflows/deploy.yml` |
| `ms-graph-mcp` | MkDocs Material | **by hand**, no workflow |
| `mcp-generator` | MkDocs Material | **by hand**, no workflow |
| `mean-docker` | Jekyll | `jekyll-gh-pages.yml` |
| `clean-architecture-docker-dotnet-angular` | Jekyll | `jekyll-gh-pages.yml` |
| `e-commerce-agents` | Jekyll | `jekyll-gh-pages.yml` |

The two hand-deployed sites are the ones most likely to be stale relative to
their repo. A green CI badge on those repos says nothing about their docs.

**Do not add a doc link for a repo that has no site.** Before adding one,
confirm the site actually serves: the URL pattern is predictable, which makes it
easy to write a link to a 404. `aspire-Microservices` is listed without a docs
link for this reason.

## Editing guidelines

- Proof over claims: every capability mentioned should link to a repo or a post
- Positioning is cloud-neutral: Nitin's production work is mostly on Azure, but he
  is open to any cloud and any AI stack. Keep "Azure" out of the banner headline,
  keep the sentence saying so in the opening paragraph, and do not claim AWS or
  GCP project experience that the repos do not show
- Keyless architecture and zero trust are the lead themes; keep them in the
  opener, in "How I work", and in the featured posts
- No third-party widgets: no stats cards, view counters, typing animations,
  streak or snake graphs, GIFs, or badge rows. Every image is a file in this repo
- The contact row uses four icons (website, LinkedIn, X, email).
  They are SVGs in `assets/`, 16px, one mid-grey (`#768390`) that reads on light
  and dark themes. Do not swap them for shields.io badges: shields can no longer
  render the LinkedIn logo
- The contact row must stay on one source line. Its labels are the handles, each
  icon's `alt` names the platform, and the icon and the label are separate links
  so the underline does not run under the gap between them
- Star and fork counts are written as rounded floors ("100+ stars") so they do
  not go stale; raise them when a repo crosses the next round number. Earlier
  versions used live `img.shields.io/github/stars` badges; they were removed
  because a typo or rename degrades silently to an "invalid" badge
- Framework versions in the stack tags must match each repo's current description
- Blog post titles and URLs come from the feed at
  `https://nitinksingh.com/index.xml`; do not write them from memory
- Check layout by rendering, not by reading the Markdown: post the file to
  GitHub's `/markdown` API and view the HTML at about 850px wide, in light and
  dark

## Overlap with the blog

`nitinksingh.com/projects/` covers the same estate in longer form, and
`nitinksingh.com/work/` is the contact/consulting page this README links to. A
repo added here usually belongs there too; the two drifting apart is the normal
failure mode. That site lives in the `nitin27may.github.io` repo.

## Voice

Direct, first person, specific about what was built and why. No emojis, no
"passionate about", no buzzword lists beyond the Stack table, which is
deliberately a scannable index rather than prose.

The default branch is `master`, not `main`.

## Pending

Items that need input from Nitin before they can go into the README:

- [ ] Change the email shown in the GitHub profile sidebar to the Hotmail address
  used in the README (profile settings on github.com)
- [ ] Two or three quantified outcomes from client or employer work that can be
  stated publicly, anonymized if needed (scale, cost, latency, team size). Add
  as an "Impact" section between the opener and "Selected work"
- [ ] Confirm the featured posts under "Writing" (currently chosen for the
  keyless, zero trust, and agent themes)
- [ ] Pinned repos, set by hand on github.com. Pinned as of 2026-11-21:
  e-commerce-agents, mean-docker, clean-architecture-docker-dotnet-angular,
  dictum, learnplay-ai, ms-graph-mcp. Suggested: replace dictum and learnplay-ai
  with mcp-generator and aspire-Microservices so the pins match "Selected work"
- [ ] Add descriptions to `powershell-examples` and `npm-custom-module`, or
  archive them
- [ ] `nitinksingh.com/projects/` should list the same repos as "Selected work"
