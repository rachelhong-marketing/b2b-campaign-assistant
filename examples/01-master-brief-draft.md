# Example output: master brief draft

> What the campaign assistant returns for "Draft the master brief for the Q3 Clean Customer Data program from the H2 go-to-market plan." Made-up campaign. Sources: `knowledge/00-strategy/2026-h2-data-quality-gtm-plan.md`, the asset abstracts in `knowledge/06-assets/`, the brand guidelines and the audience file. It follows `knowledge/02-brief-templates/master-brief-template.md`. Anything not in the sources is marked CONFIRM or MISSING; the brief check result is at the end.

# Master brief: 2026-Q3 Clean Customer Data

## Campaign

- **Campaign name:** 2026-Q3 Clean Customer Data
- **Product:** Fernhill Data Quality Platform
- **Launch date:** 2026-07-01
- **End date:** 2026-09-30
- **Owner:** Integrated Marketing
- **Total budget:** $120,000
- **Primary CTA:** Download the free Customer Data Cleanup Playbook

## Objective

Create new pipeline from the 400 Q3 target accounts in retail and financial services. Get data and analytics leaders to download the Customer Data Cleanup Playbook, then move downloads from target accounts to a demo with a data specialist.

## KPIs

| KPI | Target |
|---|---|
| Playbook downloads | 600 |
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

- The same customer shows up as several records across the CRM, billing and support systems.
- Teams spend about 30% of their week fixing data instead of using it.
- Reports don't match, so leaders stop trusting the numbers.

## Message

- **Primary message:** One customer, one record. Clean up duplicate customer data for good.
- **Reasons to believe:**
  - Teams spend 30% of their week fixing data (2025 customer survey, n=120)
  - Customers cut data cleanup time by 40% (2025 customer survey, n=120)
  - Setup in under two weeks (implementation records, 2025 median)

## Creative concept and tone

- **Concept:** "One customer, five records": the same person shown as five slightly different records, then merged into one. It uses the video's title so every ad looks like one campaign. [CONFIRM with the creative team: the plan doesn't set a concept]
- **Tone:** Plain, confident, practical. No hype (brand guidelines).

## Funnel stages

| Stage | Key asset | Channels | Link |
|---|---|---|---|
| Awareness | 30-second video: "One customer, five records" | LinkedIn, display | https://yoursite.example/records-video |
| Interest | Customer Data Cleanup Playbook (gated guide) | LinkedIn, Google Search, Meta retargeting | https://yoursite.example/cleanup-playbook |
| Consideration | On-demand webinar: "How a regional bank cleaned up its customer records" | Email nurture, content syndication | https://yoursite.example/bank-webinar |
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
- Content syndication promotes the webinar, which isn't published until 2026-08-03.

## Content calendar

| Week of | What goes live |
|---|---|
| 2026-07-01 | Playbook page, LinkedIn video and single image ads, Google Search, display, nurture for playbook downloads |
| 2026-07-15 | Meta retargeting |
| 2026-08-03 | Webinar recording published; content syndication starts; webinar added to the nurture |

## Open questions

| Question | Who answers |
|---|---|
| What's the pipeline target? | Sales operations, campaign owner |
| Who owns the email nurture? | Campaign owner |
| Do we keep the "One customer, five records" concept? | Creative team, product marketing |
| Is two weeks of traffic enough to start Meta retargeting? | Paid social lead |
| Should finance leaders get a late-stage email track? | Product marketing |

---

## Brief check result

`python3 -m assistant brief examples/01-master-brief-draft.md`

```
Brief check: 01-master-brief-draft.md
4 gaps, 0 conflicts

GAP      line 28: placeholder [MISSING: the plan says "TBD with sales operations"]: | Pipeline | [MISSING: the plan says "TBD with sales operations"] |
GAP      line 55: placeholder [CONFIRM with the creative team: the plan doesn't set a concept]: - **Concept:** "One customer, five records": the same person shown as five slightly differ
GAP      line 78: placeholder [MISSING: no email lead assigned for Q3]: | Nurture (4 emails) | Email | $0 | [MISSING: no email lead assigned for Q3] | 2026-07-01 
GAP      line 81: placeholder [CONFIRM]: - Meta retargeting starts 2026-07-15 so there are two weeks of site visitors to retarget. 
```

No conflicts: the tactic budgets add up to the $120,000 total and every tactic runs inside the campaign dates. The four gaps are the open questions above, marked on purpose so nobody mistakes a guess for a decision.
