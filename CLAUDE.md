# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Purpose

This is a GitHub profile repository. It contains only a `README.md` that serves as the public-facing profile page for the `nitin27may` GitHub account. There is no application code, build system, or dependencies.

## Audience

Recruiters, hiring managers, and engineers who land on the profile. The first screen must answer: who, what level, where, what proof, how to reach.

## README Structure

Sections, in this order:

1. `# Nitin Singh` with a short positioning paragraph and a single contact line (location, blog, LinkedIn, X, email)
2. `## Selected work`: table of repos (Project, What it is, Stack), followed by one Mermaid diagram of the `e-commerce-agents` topology
3. `## How I work`: principles, with keyless and zero trust first
4. `## Stack`: one table, five rows
5. `## Writing`: named blog posts with links

## Editing Guidelines

- Proof over claims: every capability mentioned should link to a repo or a post
- Keyless architecture and zero trust are the lead themes; keep them in the opener, in "How I work", and in the featured posts
- No widgets: no stats cards, view counters, typing animations, streak or snake graphs, GIFs, or badge rows
- The only icons are the four on the contact line (website, LinkedIn, X, email). They are SVGs in `assets/`, 16px, one mid-grey (`#768390`) that reads on light and dark themes. Do not swap them for shields.io badges: shields can no longer render the LinkedIn logo
- No emojis, no horizontal rules between sections
- Star and fork counts are written as rounded floors ("100+ stars") so they do not go stale; raise them when a repo crosses the next round number
- Framework versions in the Stack column must match each repo's current description
- At most one Mermaid diagram, using the house dual-theme classDefs (mid-tone fills, white text, no filled subgraphs)
- Blog post titles and URLs come from the feed at `https://nitinksingh.com/index.xml`; do not write them from memory

## Pending

Items that need input from Nitin before they can go into the README:

- [ ] Availability line near the top: open to roles, consulting, or neither
- [ ] Two or three quantified outcomes from client or employer work that can be stated publicly, anonymized if needed (scale, cost, latency, team size). Add as an "Impact" section between the opener and "Selected work"
- [ ] Confirm the featured posts under "Writing" (currently chosen for the keyless, zero trust, and agent themes)
- [ ] Pinned repos, set by hand on github.com. Currently pinned: e-commerce-agents, mean-docker, clean-architecture-docker-dotnet-angular, dictum, learnplay-ai, ms-graph-mcp. Suggested: replace dictum and learnplay-ai with mcp-generator and aspire-Microservices so the pins match "Selected work"
- [ ] Add descriptions to `powershell-examples` and `npm-custom-module`, or archive them
- [ ] Commit and push `README.md` and this file
