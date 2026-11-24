# B2B Campaign Assistant

> **B2B Campaign Lifecycle Toolkit**, step 2 of 7
>
> [1. Position](https://github.com/rachelhong-marketing/b2b-product-marketing-agent) → **2. Plan** → [3. Content](https://github.com/rachelhong-marketing/b2b-content-strategy-assistant) → [4. Set up](https://github.com/rachelhong-marketing/b2b-paid-media-planner) → [5. Test](https://github.com/rachelhong-marketing/b2b-campaign-test-planner) → [6. Report](https://github.com/rachelhong-marketing/b2b-campaign-reporting-agent) → [7. Prove](https://github.com/rachelhong-marketing/b2b-pipeline-attribution-tool)

An AI agent that helps a B2B marketing team plan and build a campaign, from the first idea to launch-ready copy. It brainstorms the campaign theme from your positioning (the Product Marketing Agent's `positioning.json` is the input), brand narrative and customer research, writes the master campaign plan and the master brief, then drafts the channel briefs, search keywords, landing page, and search, social and email copy. It checks every draft before anyone uses it, and reviews copy and keywords your team already wrote.

It follows a [campaign planning framework](framework/campaign-planning-framework.md) and works from the team's own plans, templates, brand rules, audience criteria and past results, not generic best practice. It runs as a Claude Code skill, with Python checks for anything that has to be exact (budget math, offer dates, character limits, approved claims, keyword rules). There's also a Microsoft Copilot version for teams that work in Microsoft 365.

All data here is made up. Fernhill Software is a fictional company.

## Why this exists

Most campaign problems start before the first ad is written. Teams jump to a theme before they've gathered the inputs, so it's either too product-led or too vague. Then the plan and briefs get written by hand, and the same mistakes slip through: budgets that don't add up, a persona sales doesn't sell to, a channel promoting a webinar that isn't published yet, a 34-character Google headline, a "3x faster" claim nobody can source.

A general AI assistant writes fluent drafts but invents numbers and ignores your rules. This agent is built the other way around: your files are the source of truth, the checks are code and run on every draft, and anything it can't trace gets marked `[MISSING]` or `[CONFIRM]`.

## What it does

| Phase | Step | You ask | You get |
|---|---|---|---|
| **Plan** | 1. Campaign themes | "Brainstorm Q3 campaign themes from our plan, brand narrative and research" | 2 or 3 theme options, each tied to the buyer assumption it challenges and the research behind it, scored on three tests, with a recommendation and an agenda for the team's brainstorm |
| | 2. Master campaign plan | "Write the Q3 campaign plan with option 1" | Goals and KPIs, audience priorities, theme, messaging pillars, offers by funnel stage, channel mix and budget, ABM plan, timeline and measurement |
| | 3. Master brief | "Turn the plan into the master brief" | The one-page hand-off to channel owners: audience, message, CTA, assets, tactics with budgets, owners and dates |
| | 4. Check a brief | "Check this master brief" | A summary plus open questions: gaps, budget and date conflicts, personas not in the audience file, unapproved claims, and who answers each one |
| **Brief** | 5. Channel briefs | "Draft the paid search brief" | A brief in your template, with targeting from your audience file and the past learning it applied |
| **Create** | 6. Keywords | "Brainstorm keywords for the search campaign" | Ad groups mapped to the brief, keywords with match types, and negatives, as a CSV ready to upload |
| | 7. Landing page | "Draft the landing page from the playbook abstract" | Page title, headline, what you get, how it works, proof, form and button, written to your template |
| | 8. Ad and email copy | "Write the search, LinkedIn, Meta and email copy" | Copy within every limit, using approved proof points and past learnings, with a tracking value per ad |
| **Review** | 9. Copy | "Review this LinkedIn copy" | Score (1-5), what works, what to fix with a rewrite that passes the limits, and risks |
| | 10. Keywords | "Check this keyword list" | Duplicates, keywords blocked by negatives, length and match type errors, competitor terms, and ad groups competing |

See the outputs on the sample campaign in [`examples/`](examples/):

1. [Campaign theme options](examples/01-campaign-themes.md), from the [go-to-market plan](knowledge/00-strategy/2026-h2-data-quality-gtm-plan.md), [brand narrative](knowledge/00-strategy/brand-narrative-2026.md) and [customer research](knowledge/00-strategy/customer-research-2026-h1.md)
2. [Master campaign plan](examples/02-master-campaign-plan.md)
3. [Master brief](examples/03-master-brief-draft.md)
4. [Master brief check](examples/04-master-brief-check.md), on a hand-written brief with planted problems
5. [Paid search brief](examples/05-paid-search-brief.md)
6. [Keyword draft](examples/06-keyword-draft.md)
7. [Landing page draft](examples/07-landing-page-draft.md), from the [asset abstract](knowledge/06-assets/customer-data-cleanup-playbook-abstract.md)
8. [Ad and email copy drafts](examples/08-copy-drafts.md)
9. [Copy review](examples/09-copy-review.md)

Every draft in steps 2, 3, 6, 7 and 8 passed the checks below; the check output is at the end of each example.

## Use it with Claude Code

Download the repo, open the folder in Claude Code, and ask:

- "Brainstorm campaign themes for Q3 from the strategy folder."
- "Write the Q3 Clean Customer Data campaign plan with option 1."
- "Turn the plan into the master brief."
- "Draft a paid social brief for LinkedIn."
- "Brainstorm keywords and negatives for the search campaign."
- "Draft the landing page for the Customer Data Cleanup Playbook."
- "Write two LinkedIn ads and two nurture emails from the landing page."
- "Review sample-data/ad-copy-sample.csv."

The skill is in [`.claude/skills/campaign-assistant/SKILL.md`](.claude/skills/campaign-assistant/SKILL.md). To use it for your own team, replace the files in [`knowledge/`](knowledge/) and [`rules/`](rules/) with yours: your go-to-market plan, brand narrative, research, templates, brand guidelines, audience, past results and asset abstracts.

## Use it in Microsoft Copilot

[`copilot/`](copilot/) has the same agent as Copilot instructions (paste-ready) and a setup guide: SharePoint knowledge folders, conversation starters and guardrail tests. Copilot can't run the Python checks, so the guide says what a person should double-check.

## The checks (command line)

Python 3 only, nothing to install.

```bash
python3 -m assistant plan examples/02-master-campaign-plan.md
python3 -m assistant brief knowledge/01-campaign-plans/2026-q3-clean-customer-data-master-brief.md
python3 -m assistant copy sample-data/ad-copy-sample.csv
python3 -m assistant keywords sample-data/keywords-sample.csv --negatives sample-data/negative-keywords.csv
python3 -m unittest discover -s tests
```

| Check | Runs on | What it catches |
|---|---|---|
| `plan` | Master campaign plans | Missing sections or fields; channel budgets that don't add up to the total; a channel that starts before the offer it promotes is ready; missing targets and owners |
| `brief` | Master briefs | On the sample: tactic budgets add up to $130,000 vs. a $120,000 total; a tactic that starts before launch; no pipeline target; no owner for the nurture; [TBD] and [CONFIRM] placeholders |
| `copy` | Ads, emails and landing pages | On the sample: Google headlines over 30 characters; too few headlines and descriptions; "3x" and "500+" claims that aren't approved proof points; avoid-list words ("best-in-class", "revolutionary"); wrong terminology ("ebook"); ALL CAPS and "!!" in an email subject |
| `keywords` | Keyword lists | On the sample: duplicates; keywords blocked by the negatives "free" and "jobs"; a 16-word keyword; a misspelled match type; competitor brand terms; one keyword in two ad groups |

Character limits live in [`rules/copy-limits.csv`](rules/copy-limits.csv) and brand words in [`rules/brand-words.csv`](rules/brand-words.csv). Platform limits change, so check them against current platform documentation.

## What's in the repo

| Folder | What it holds |
|---|---|
| `framework/` | The campaign planning framework the agent follows |
| `knowledge/00-strategy/` | Go-to-market plan, brand narrative and customer research: the inputs for themes and the plan |
| `knowledge/01-campaign-plans/` | A hand-written master brief with planted gaps |
| `knowledge/02-brief-templates/` | Theme, campaign plan, master brief, channel brief and landing page templates, plus an approved example |
| `knowledge/03-brand-and-channel/` | Voice, terminology, approved proof points, channel best practices |
| `knowledge/04-audience/` | Target account criteria, personas, competitors |
| `knowledge/05-performance/` | Creative performance log |
| `knowledge/06-assets/` | Asset abstracts for the playbook and the webinar |
| `rules/` | Character limits and brand words used by the checks |
| `assistant/` | The Python checks |
| `sample-data/` | Ad copy, keywords and negatives with planted problems |
| `examples/` | Example outputs; `examples/drafts/` has the drafts as CSV files |
| `copilot/` | Copilot version |
| `tests/` | Tests |

## The B2B Campaign Lifecycle Toolkit

Seven tools, one per step of a B2B campaign, from positioning to proving pipeline. Each works on its own; together they cover the whole cycle. All sample data is made up.

| Step | Tool | What it does |
|---|---|---|
| 1. Position | [B2B Product Marketing Agent](https://github.com/rachelhong-marketing/b2b-product-marketing-agent) | Define who you sell to and what you say: ideal customer profile, positioning, messaging pillars and proof points, checked for gaps before any campaign starts. |
| 2. Plan | **B2B Campaign Assistant** (this repo) | Turn the positioning into a campaign theme, write the campaign plan and master brief, then draft channel briefs, keywords, landing page and ad copy, all checked before launch. |
| 3. Content | [B2B Content Strategy Assistant](https://github.com/rachelhong-marketing/b2b-content-strategy-assistant) | Pick content topics inside the campaign theme from audience questions, news, competitors and keyword data, outline and check each piece so search and AI answer tools can quote it, and log whether AI answers cite you. |
| 4. Set up | [B2B Paid Media Planner](https://github.com/rachelhong-marketing/b2b-paid-media-planner) | Plan channels and retargeting, then build and check tracking links before launch. |
| 5. Test | [B2B Campaign Test Planner](https://github.com/rachelhong-marketing/b2b-campaign-test-planner) | Plan tests in waves, let the ad platform call the winner, check MQLs, and size tests when volume is small. |
| 6. Report | [B2B Campaign Reporting Agent](https://github.com/rachelhong-marketing/b2b-campaign-reporting-agent) | Consolidate ad platform and CRM data into one file, check every channel and funnel stage for gaps, and draft insights. |
| 7. Prove | [B2B Pipeline Attribution Tool](https://github.com/rachelhong-marketing/b2b-pipeline-attribution-tool) | Check the CRM data can be trusted, then show sourced and influenced pipeline. |

## About the author

**Rachel Hong** has worked in B2B demand generation and marketing analytics for more than ten years, at marketing and advertising technology companies. She builds campaigns, reporting and the AI workflows that help marketing teams plan and measure them.

[LinkedIn](https://www.linkedin.com/in/rachelhongatbaruch/)
