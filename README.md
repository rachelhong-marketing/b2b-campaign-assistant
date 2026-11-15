# B2B Campaign Assistant

> **B2B Campaign Lifecycle Toolkit**, step 1 of 5
>
> **1. Plan** → [2. Set up](https://github.com/rachelhong-marketing/b2b-paid-media-planner) → [3. Test](https://github.com/rachelhong-marketing/b2b-campaign-test-planner) → [4. Report](https://github.com/rachelhong-marketing/b2b-campaign-reporting-agent) → [5. Prove](https://github.com/rachelhong-marketing/b2b-pipeline-attribution-tool)

An AI agent that takes a B2B marketing team from a go-to-market plan to launch-ready campaign briefs and copy. It drafts the master campaign brief, turns it into paid search, paid social and email briefs, brainstorms search keywords, and writes the landing page, search ads, social ads and emails from your asset abstract or landing page. Then it checks every draft, and reviews copy and keywords your team already wrote.

It works from the team's own plan, templates, brand rules, audience criteria and past results, not from generic best practice. It runs as a Claude Code skill, with Python checks for anything that has to be exact (budget math, character limits, approved claims, keyword rules). There's also a Microsoft Copilot version for teams that work in Microsoft 365.

All data here is made up. Fernhill Software is a fictional company.

## Why this exists

Getting from a go-to-market plan to live ads takes a stack of documents: a master brief, four or five channel briefs, a keyword list, a landing page, and copy for every channel. It's slow, and the same mistakes slip through every time: budgets that don't add up, a persona sales doesn't sell to, an ad promoting a guide that isn't published yet, a 34-character Google headline, a "3x faster" claim nobody can source, a keyword blocked by the team's own negative list.

A general AI assistant writes fluent drafts but invents numbers and ignores your rules. This agent is built the other way around: your files are the source of truth, the checks are code and run on every draft, and anything it can't trace gets marked `[MISSING]` or `[CONFIRM]`.

## What it does

| Step | You ask | You get |
|---|---|---|
| **1. Draft the master brief** | "Draft the Q3 master brief from the H2 go-to-market plan" | A master brief in your template: objective, KPIs, audience, message, funnel stages, tactics with budgets, owners and dates, plus open questions. Budgets add up and no tactic promotes an asset before it's ready. |
| **2. Check a master brief** | "Summarize the Q3 master brief" | A one-page summary plus open questions: gaps, budget and date conflicts, personas not in the audience file, unapproved claims, and who answers each one |
| **3. Draft channel briefs** | "Draft the paid search brief" | A brief in your template's structure, with targeting from your audience file and the past learning it applied |
| **4. Brainstorm keywords** | "Brainstorm keywords for the search campaign" | Ad groups mapped to the brief's themes, keywords with match types, and negatives, as a CSV ready to upload |
| **5. Draft the landing page** | "Draft the landing page from the assessment abstract" | Page title, headline, subheadline, what you get, how it works, proof, form and button, written to your landing page template |
| **6. Draft ad and email copy** | "Write the search, LinkedIn, Meta and email copy" | Search ads, social ads and emails within every limit, using approved proof points and past learnings, with a tracking value per ad |
| **7. Review copy** | "Review this LinkedIn copy" | Score (1-5), what works, what to fix with a rewrite that passes the limits, and risks |
| **8. Review keywords** | "Check this keyword list" | Duplicates, keywords blocked by negatives, length and match type errors, competitor terms, and ad groups competing |

See the outputs on the sample campaign in [`examples/`](examples/):

1. [Master brief draft](examples/01-master-brief-draft.md), from the [go-to-market plan](knowledge/00-strategy/2026-h2-data-quality-gtm-plan.md)
2. [Master brief check](examples/02-master-brief-check.md), on a hand-written brief with planted problems
3. [Paid search brief](examples/03-paid-search-brief.md)
4. [Keyword draft](examples/04-keyword-draft.md)
5. [Landing page draft](examples/05-landing-page-draft.md), from the [asset abstract](knowledge/06-assets/data-readiness-assessment-abstract.md)
6. [Ad and email copy drafts](examples/06-copy-drafts.md)
7. [Copy review](examples/07-copy-review.md)

Every draft in steps 1, 4, 5 and 6 passed the checks below; the check output is at the end of each example.

## Use it with Claude Code

Download the repo, open the folder in Claude Code, and ask:

- "Draft the Q3 Data Readiness master brief from the H2 go-to-market plan."
- "Draft a paid social brief for LinkedIn."
- "Brainstorm keywords and negatives for the search campaign."
- "Draft the landing page for the Data Readiness Assessment."
- "Write two LinkedIn ads and two nurture emails from the landing page."
- "Review sample-data/ad-copy-sample.csv."

The skill is in [`.claude/skills/campaign-assistant/SKILL.md`](.claude/skills/campaign-assistant/SKILL.md). To use it for your own team, replace the files in [`knowledge/`](knowledge/) and [`rules/`](rules/) with yours: your go-to-market plan, templates, brand guidelines, audience, past results and asset abstracts.

## Use it in Microsoft Copilot

[`copilot/`](copilot/) has the same agent as Copilot instructions (paste-ready) and a setup guide: SharePoint knowledge folders, conversation starters and guardrail tests. Copilot can't run the Python checks, so the guide says what a person should double-check.

## The checks (command line)

Python 3 only, nothing to install.

```bash
python3 -m assistant brief knowledge/01-campaign-plans/2026-q3-data-readiness-master-brief.md
python3 -m assistant copy sample-data/ad-copy-sample.csv
python3 -m assistant keywords sample-data/keywords-sample.csv --negatives sample-data/negative-keywords.csv
python3 -m unittest discover -s tests
```

| Check | Runs on | What it catches on the sample data |
|---|---|---|
| `brief` | Master briefs | Tactic budgets add up to $130,000 vs. a $120,000 total; a tactic that starts before launch; no pipeline target; no owner for the nurture; [TBD] and [CONFIRM] placeholders |
| `copy` | Ads, emails and landing pages | Google headlines over 30 characters; too few headlines and descriptions; "3x" and "500+" claims that aren't approved proof points; avoid-list words ("best-in-class", "revolutionary"); wrong terminology ("quiz"); ALL CAPS and "!!" in an email subject |
| `keywords` | Keyword lists | Duplicates; keywords blocked by the negatives "free" and "jobs"; a 16-word keyword; a misspelled match type; competitor brand terms; one keyword in two ad groups |

Character limits live in [`rules/copy-limits.csv`](rules/copy-limits.csv) and brand words in [`rules/brand-words.csv`](rules/brand-words.csv). Platform limits change, so check them against current platform documentation.

## What's in the repo

| Folder | What it holds |
|---|---|
| `knowledge/00-strategy/` | A go-to-market plan, the starting point for a master brief |
| `knowledge/01-campaign-plans/` | A hand-written master brief with planted gaps |
| `knowledge/02-brief-templates/` | Master brief, paid search, paid social, email and landing page templates, plus an approved example |
| `knowledge/03-brand-and-channel/` | Voice, terminology, approved proof points, channel best practices |
| `knowledge/04-audience/` | Target account criteria, personas, competitors |
| `knowledge/05-performance/` | Creative performance log |
| `knowledge/06-assets/` | Asset abstracts for the assessment and the guide |
| `rules/` | Character limits and brand words used by the checks |
| `assistant/` | The Python checks |
| `sample-data/` | Ad copy, keywords and negatives with planted problems |
| `examples/` | Example outputs; `examples/drafts/` has the drafts as CSV files |
| `copilot/` | Copilot version |
| `tests/` | Tests |

## The B2B Campaign Lifecycle Toolkit

Five tools, one per step of a B2B campaign, from the brief to proving pipeline. Each works on its own; together they cover the whole cycle. All sample data is made up.

| Step | Tool | What it does |
|---|---|---|
| 1. Plan | **B2B Campaign Assistant** (this repo) | Draft the master brief, channel briefs, keywords, landing page and ad copy from your go-to-market plan, and check them before launch. |
| 2. Set up | [B2B Paid Media Planner](https://github.com/rachelhong-marketing/b2b-paid-media-planner) | Plan channels and retargeting, then build and check tracking links before launch. |
| 3. Test | [B2B Campaign Test Planner](https://github.com/rachelhong-marketing/b2b-campaign-test-planner) | Size tests on leads and MQLs, not clicks, and read the results. |
| 4. Report | [B2B Campaign Reporting Agent](https://github.com/rachelhong-marketing/b2b-campaign-reporting-agent) | Consolidate ad platform and CRM data into one file, check every channel and funnel stage for gaps, and draft insights. |
| 5. Prove | [B2B Pipeline Attribution Tool](https://github.com/rachelhong-marketing/b2b-pipeline-attribution-tool) | Check the CRM data can be trusted, then show sourced and influenced pipeline. |

## About the author

**Rachel Hong** has worked in B2B demand generation and marketing analytics for more than ten years, at marketing and advertising technology companies. She builds campaigns, reporting and the AI workflows that help marketing teams plan and measure them.

[LinkedIn](https://www.linkedin.com/in/rachelhongatbaruch/)
