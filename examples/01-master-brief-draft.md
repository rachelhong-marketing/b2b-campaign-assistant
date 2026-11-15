# Example output: master brief draft

> What the campaign assistant returns for "Draft the master brief for the Q3 Data Readiness program from the H2 go-to-market plan." Made-up campaign. Sources: `knowledge/00-strategy/2026-h2-data-quality-gtm-plan.md`, the asset abstracts in `knowledge/06-assets/`, the brand guidelines and the audience file. It follows `knowledge/02-brief-templates/master-brief-template.md`. Anything not in the sources is marked CONFIRM or MISSING; the brief check result is at the end.

# Master brief: 2026-Q3 Data Readiness

## Campaign

- **Campaign name:** 2026-Q3 Data Readiness
- **Product:** Fernhill Data Quality Platform
- **Launch date:** 2026-07-01
- **End date:** 2026-09-30
- **Owner:** Integrated Marketing
- **Total budget:** $120,000
- **Primary CTA:** Take the 3-minute Data Readiness Assessment

## Objective

Create new pipeline from the 400 Q3 target accounts in retail and financial services. Get data and analytics leaders to take the Data Readiness Assessment, then move those who score under 50 to a demo with a data specialist.

## KPIs

| KPI | Target |
|---|---|
| Assessment completions | 600 |
| MQLs (marketing qualified leads) | 180 |
| SALs (sales accepted leads) | 60 |
| Pipeline | [MISSING: the plan says "TBD with sales operations"] |

## Audience

- **Industries:** Retail, Financial Services
- **Company size:** 1,000 to 10,000 employees
- **Regions:** United States and Canada
- **Personas:** VP of Data and Head of Data Engineering (decision maker); Director of Analytics and BI Director (champion). Finance leaders join late in the deal, so they're not targeted in paid media.
- **Target accounts:** 400 accounts on the Q3 target account list
- **Exclusions:** Current customers, late-stage open opportunities, competitors

## Pain points

- AI projects stall because customer data is duplicated, incomplete or spread across systems.
- Teams spend about 30% of their week fixing data instead of using it.
- Leaders find out their data isn't ready only after an AI project fails.

## Message

- **Primary message:** Know if your data is ready for AI before you start.
- **Reasons to believe:**
  - Teams spend 30% of their week fixing data (2025 customer survey, n=120)
  - Customers cut data cleanup time by 40% (2025 customer survey, n=120)
  - Setup in under two weeks (implementation records, 2025 median)

## Creative concept and tone

- **Concept:** "Ready or not": the readiness score shown as a gauge, so every ad shows what the reader gets. [CONFIRM with the creative team: the plan doesn't set a concept]
- **Tone:** Plain, confident, practical. No hype (brand guidelines).

## Funnel stages

| Stage | Key asset | Channels | Link |
|---|---|---|---|
| Awareness | 30-second video: "Is your data AI-ready?" | LinkedIn, display | https://yoursite.example/ready-video |
| Interest | Data Readiness Assessment (3 minutes) | LinkedIn, Google Search, Meta retargeting | https://yoursite.example/assessment |
| Consideration | Guide: "5 signs your data isn't ready for AI" | Email nurture, content syndication | https://yoursite.example/guide |
| Decision | Demo with a data specialist | Email, sales follow-up | https://yoursite.example/demo |

## Tactics, budget and owners

Budgets use the plan's H2 channel split on the $120,000 total.

| Tactic | Channel | Budget | Owner | Start | End |
|---|---|---|---|---|---|
| Video and single image ads | LinkedIn | $48,000 | Paid social lead | 2026-07-01 | 2026-09-30 |
| Search ads | Google Search | $30,000 | Paid search lead | 2026-07-01 | 2026-09-30 |
| Account-based display | Display | $18,000 | Paid media lead | 2026-07-01 | 2026-09-30 |
| Retargeting | Meta | $12,000 | Paid social lead | 2026-07-15 | 2026-09-30 |
| Content syndication | Content syndication | $12,000 | Demand gen lead | 2026-08-03 | 2026-09-30 |
| Nurture (4 emails) | Email | $0 | [MISSING: no email lead assigned for Q3] | 2026-07-01 | 2026-09-30 |

Why two start dates differ from launch:
- Meta retargeting starts 2026-07-15 so there are two weeks of site visitors to retarget. [CONFIRM]
- Content syndication promotes the guide, which isn't published until 2026-08-03.

## Content calendar

| Week of | What goes live |
|---|---|
| 2026-07-01 | Assessment page, LinkedIn video and single image ads, Google Search, display, nurture for assessment takers |
| 2026-07-15 | Meta retargeting |
| 2026-08-03 | Guide published; content syndication starts; guide added to the nurture |

## Open questions

| Question | Who answers |
|---|---|
| What's the pipeline target? | Sales operations, campaign owner |
| Who owns the email nurture? | Campaign owner |
| Do we keep the "Ready or not" concept? | Creative team, product marketing |
| Is two weeks of traffic enough to start Meta retargeting? | Paid social lead |
| Should finance leaders get a late-stage email track? | Product marketing |

---

## Brief check result

`python3 -m assistant brief examples/01-master-brief-draft.md`

```
Brief check: 01-master-brief-draft.md
4 gaps, 0 conflicts

GAP      line 28: placeholder [MISSING: the plan says "TBD with sales operations"]: | Pipeline | [MISSING: the plan says "TBD with sales operations"] |
GAP      line 55: placeholder [CONFIRM with the creative team: the plan doesn't set a concept]: - **Concept:** "Ready or not": the readiness score shown as a gauge, so every ad shows wha
GAP      line 78: placeholder [MISSING: no email lead assigned for Q3]: | Nurture (4 emails) | Email | $0 | [MISSING: no email lead assigned for Q3] | 2026-07-01 
GAP      line 81: placeholder [CONFIRM]: - Meta retargeting starts 2026-07-15 so there are two weeks of site visitors to retarget. 
```

No conflicts: the tactic budgets add up to the $120,000 total and every tactic runs inside the campaign dates. The four gaps are the open questions above, marked on purpose so nobody mistakes a guess for a decision.
