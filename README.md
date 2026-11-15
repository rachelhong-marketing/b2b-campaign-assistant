# B2B Campaign Assistant

> **B2B Campaign Lifecycle Toolkit**, step 1 of 5
>
> **1. Plan** → [2. Set up](https://github.com/rachelhong-marketing/b2b-paid-media-planner) → [3. Test](https://github.com/rachelhong-marketing/b2b-campaign-test-planner) → [4. Report](https://github.com/rachelhong-marketing/b2b-campaign-reporting-agent) → [5. Prove](https://github.com/rachelhong-marketing/b2b-pipeline-attribution-tool)

An AI agent that takes a B2B marketing team from an approved master brief to launch-ready channel briefs and copy. It summarizes the brief and finds the gaps, drafts paid search, paid social and email briefs, reviews copy and creative, and checks keyword lists. It works from the team's own templates, brand rules, audience criteria and past results, not from generic best practice.

It runs as a Claude Code skill, with Python checks for anything that has to be exact (budget math, character limits, approved claims, keyword rules). There's also a Microsoft Copilot version for teams that work in Microsoft 365.

All data here is made up. Fernhill Software is a fictional company.

## Why this exists

Turning one master brief into four or five channel briefs is slow, and the same mistakes slip through every time: budgets that don't add up, a persona sales doesn't sell to, a 34-character Google headline, a "3x faster" claim nobody can source, a keyword blocked by the team's own negative list. A general AI assistant writes fluent briefs but invents numbers and ignores your rules. This agent is built the other way around: your files are the source of truth, the checks are code, and anything it can't trace gets marked `[MISSING]` or `[CONFIRM]`.

## What it does

| Task | You ask | You get |
|---|---|---|
| **1. Summarize a master brief** | "Summarize the Q3 master brief" | A one-page summary plus open questions: gaps, budget conflicts, date conflicts, personas not in the audience file, unapproved claims, and who answers each one |
| **2. Draft a channel brief** | "Draft the paid search brief" | A brief in your template's structure, with targeting from your audience file, copy within limits, and the past learning it applied |
| **3. Review copy or a creative** | "Review this LinkedIn copy" | Score (1-5), what works, what to fix with a rewrite that passes the limits, and risks |
| **4. Review keywords** | "Check this keyword list" | Duplicates, keywords blocked by negatives, length and match type errors, competitor terms, and ad groups competing |

See real outputs on the sample campaign in [`examples/`](examples/): a [brief summary](examples/01-master-brief-summary.md), a [paid search brief](examples/02-paid-search-brief.md) and a [copy review](examples/03-copy-review.md).

## Use it with Claude Code

Download the repo, open the folder in Claude Code, and ask:

- "Summarize the Q3 Data Readiness master brief and list open questions."
- "Draft a paid social brief for LinkedIn."
- "Review sample-data/ad-copy-sample.csv."
- "Check sample-data/keywords-sample.csv against our negative keywords."

The skill is in [`.claude/skills/campaign-assistant/SKILL.md`](.claude/skills/campaign-assistant/SKILL.md). To use it for your own team, replace the files in [`knowledge/`](knowledge/) and [`rules/`](rules/) with yours.

## Use it in Microsoft Copilot

[`copilot/`](copilot/) has the same agent as Copilot instructions (paste-ready, about 3,100 characters) and a setup guide: SharePoint knowledge folders, conversation starters and guardrail tests. Copilot can't run the Python checks, so the guide says what a person should double-check.

## The checks (command line)

Python 3 only, nothing to install.

```bash
python3 -m assistant brief knowledge/01-campaign-plans/2026-q3-data-readiness-master-brief.md
python3 -m assistant copy sample-data/ad-copy-sample.csv
python3 -m assistant keywords sample-data/keywords-sample.csv --negatives sample-data/negative-keywords.csv
python3 -m unittest discover -s tests
```

| Check | What it catches on the sample data |
|---|---|
| `brief` | Tactic budgets add up to $130,000 vs. a $120,000 total; a tactic that starts before launch; no pipeline target; no owner for the nurture; [TBD] and [CONFIRM] placeholders |
| `copy` | Google headlines over 30 characters; too few headlines and descriptions; "3x" and "500+" claims that aren't approved proof points; avoid-list words ("best-in-class", "revolutionary"); wrong terminology ("quiz"); ALL CAPS and "!!" in an email subject |
| `keywords` | Duplicates; keywords blocked by the negatives "free" and "jobs"; a 16-word keyword; a misspelled match type; competitor brand terms; one keyword in two ad groups |

Character limits live in [`rules/copy-limits.csv`](rules/copy-limits.csv) and brand words in [`rules/brand-words.csv`](rules/brand-words.csv). Platform limits change, so check them against current platform documentation.

## What's in the repo

| Folder | What it holds |
|---|---|
| `knowledge/01-campaign-plans/` | A master brief with planted gaps |
| `knowledge/02-brief-templates/` | Paid search, paid social and email templates, plus an approved example |
| `knowledge/03-brand-and-channel/` | Voice, terminology, approved proof points, channel best practices |
| `knowledge/04-audience/` | Target account criteria, personas, competitors |
| `knowledge/05-performance/` | Creative performance log |
| `rules/` | Character limits and brand words used by the checks |
| `assistant/` | The Python checks |
| `sample-data/` | Ad copy, keywords and negatives with planted problems |
| `examples/` | Example outputs |
| `copilot/` | Copilot version |
| `tests/` | Tests |

## The B2B Campaign Lifecycle Toolkit

Five tools, one per step of a B2B campaign, from the brief to proving pipeline. Each works on its own; together they cover the whole cycle. All sample data is made up.

| Step | Tool | What it does |
|---|---|---|
| 1. Plan | **B2B Campaign Assistant** (this repo) | Turn a master brief into channel briefs; review copy and creative before launch. |
| 2. Set up | [B2B Paid Media Planner](https://github.com/rachelhong-marketing/b2b-paid-media-planner) | Plan channels and retargeting, then build and check tracking links before launch. |
| 3. Test | [B2B Campaign Test Planner](https://github.com/rachelhong-marketing/b2b-campaign-test-planner) | Size tests on leads and MQLs, not clicks, and read the results. |
| 4. Report | [B2B Campaign Reporting Agent](https://github.com/rachelhong-marketing/b2b-campaign-reporting-agent) | Consolidate ad platform and CRM data into one file, check every channel and funnel stage for gaps, and draft insights. |
| 5. Prove | [B2B Pipeline Attribution Tool](https://github.com/rachelhong-marketing/b2b-pipeline-attribution-tool) | Check the CRM data can be trusted, then show sourced and influenced pipeline. |

## About the author

**Rachel Hong** has worked in B2B demand generation and marketing analytics for more than ten years, at marketing and advertising technology companies. She builds campaigns, reporting and the AI workflows that help marketing teams plan and measure them.

[LinkedIn](https://www.linkedin.com/in/rachelhongatbaruch/)
