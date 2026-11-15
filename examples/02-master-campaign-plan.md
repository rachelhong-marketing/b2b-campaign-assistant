# Example output: master campaign plan

> What the campaign assistant returns for "Write the Q3 master campaign plan with Option 1 as the theme." Made-up campaign. Sources: the [theme options](01-campaign-themes.md), the [H2 go-to-market plan](../knowledge/00-strategy/2026-h2-data-quality-gtm-plan.md), the asset abstracts and the brand guidelines. It follows the [master campaign plan template](../knowledge/02-brief-templates/master-campaign-plan-template.md). Anything not in the sources is marked CONFIRM or MISSING; the plan check result is at the end.

# Master campaign plan: 2026-Q3 Clean Customer Data

## Campaign

- **Campaign name:** 2026-Q3 Clean Customer Data
- **Theme:** One customer, one record, and it stays that way
- **Product:** Fernhill Data Quality Platform
- **Launch date:** 2026-07-01
- **End date:** 2026-09-30
- **Owner:** Integrated Marketing
- **Total budget:** $120,000

## Goals and KPIs

| KPI | Target |
|---|---|
| Playbook downloads | 600 |
| MQLs (marketing qualified leads) | 180 |
| SALs (sales accepted leads) | 60 |
| Pipeline | [MISSING: the go-to-market plan says "TBD with sales operations"] |

## Audience priorities

- **Segments:** retail and financial services, 1,000 to 10,000 employees, United States and Canada. Manufacturing waits for H1 2027.
- **Personas:** data leader (decision maker), analytics leader (champion). Finance leaders approve late in the deal, so they get sales follow-up, not paid media.
- **Accounts:** the 400-account Q3 target list.
- **Exclusions:** current customers, late-stage open opportunities, competitors.

## Theme and why it works

Buyers treat duplicate records as a one-time cleanup project, and in 11 of 18 win/loss interviews the duplicates came back. This theme challenges that assumption. It matches the brand's 2026 direction (from cleanup project to habit) and the one position no competitor owns. It passed all three tests in the theme options: cross-channel, ownable and audience-specific.

## Messaging pillars

| Pillar | Message | Proof point (approved only) |
|---|---|---|
| Find them | See how many duplicate customer records you have | Teams spend 30% of their week fixing data |
| Merge them | One record per customer, without breaking your reports | Setup in under two weeks |
| Keep them out | Monitoring and an owner, so duplicates don't come back | Customers cut data cleanup time by 40% [CONFIRM: a proof point about monitoring itself would be stronger] |

For analytics leaders, lead with "your reports disagree because your records do" (theme Option 2).

## Offers by funnel stage

| Stage | Offer | Ready | Channels |
|---|---|---|---|
| Awareness | 30-second video: "One customer, five records" | 2026-07-01 | LinkedIn, display |
| Interest | Customer Data Cleanup Playbook | 2026-07-01 | LinkedIn, Google Search, Meta retargeting, email |
| Consideration | On-demand webinar: "How a regional bank cleaned up its customer records" | 2026-08-03 | Email, content syndication |
| Decision | Demo with a data specialist | Live | Email, sales follow-up |

## Channel mix and budget

The split is the go-to-market plan's H2 planning ratio applied to $120,000.

| Channel | Promotes | Budget | Share | Owner | Start | End |
|---|---|---|---|---|---|---|
| LinkedIn | Awareness, Interest | $48,000 | 40% | Paid social lead | 2026-07-01 | 2026-09-30 |
| Google Search | Interest | $30,000 | 25% | Paid search lead | 2026-07-01 | 2026-09-30 |
| Account-based display | Awareness | $18,000 | 15% | Paid media lead | 2026-07-01 | 2026-09-30 |
| Meta retargeting | Interest | $12,000 | 10% | Paid social lead | 2026-07-15 | 2026-09-30 |
| Content syndication | Consideration | $12,000 | 10% | Demand gen lead | 2026-08-03 | 2026-09-30 |
| Email nurture | Interest, Consideration, Decision | $0 | 0% | [MISSING: no email lead assigned for Q3] | 2026-07-01 | 2026-09-30 |

Meta starts two weeks after launch so there are site visitors to retarget. Content syndication waits for the webinar.

## ABM plan

- All 400 accounts: account-based display and LinkedIn matched audiences.
- Tier 1 accounts: industry versions of the playbook landing page (retail, financial services). [CONFIRM: the go-to-market plan has no account tiers; ABM and sales operations to set them]

## Timeline

Planning milestones suggested by the assistant. [CONFIRM with the campaign owner]

| Date | Milestone |
|---|---|
| 2026-06-15 | Creative and copy approved |
| 2026-06-24 | Tracking links checked with the launch checker (step 2) |
| 2026-07-01 | Launch: video, playbook, search, display, nurture |
| 2026-07-15 | Meta retargeting starts |
| 2026-08-03 | Webinar published; content syndication starts |
| 2026-08-17 | Read the LinkedIn headline test (step 3) |
| 2026-10-15 | Q3 report (step 4) |
| 2026-11-30 | Sourced and influenced pipeline read (step 5) |

## Measurement

- **Weekly, direction only:** spend, click-through rate, downloads by channel.
- **Monthly:** leads, MQLs, SALs, SQLs and cost per MQL by channel and asset, built and checked with the B2B Campaign Reporting Agent (step 4).
- **Tests:** one LinkedIn headline test, sized on MQLs with the B2B Campaign Test Planner (step 3).
- **Pipeline:** sourced and influenced pipeline 60 days after the end date, with the B2B Pipeline Attribution Tool (step 5).

## Risks and dependencies

- No pipeline target, so success can only be judged on MQLs and SALs for now.
- No email owner, and email carries three of the four funnel stages.
- The "keep them out" pillar has no proof point about monitoring.
- Meta retargeting depends on enough site traffic in the first two weeks.

## Open questions

| Question | Who answers |
|---|---|
| What's the pipeline target? | Sales operations, campaign owner |
| Who owns the email nurture? | Campaign owner |
| Can we approve a proof point about monitoring? | Product marketing |
| Which accounts are tier 1? | ABM, sales operations |
| Do the timeline dates work? | Campaign owner |

---

## Plan check result

`python3 -m assistant plan examples/02-master-campaign-plan.md`

```
Plan check: 02-master-campaign-plan.md
5 gaps, 0 conflicts

GAP      line 24: placeholder [MISSING: the go-to-market plan says "TBD with sales operations"]: | Pipeline | [MISSING: the go-to-market plan says "TBD with sales operations"] |
GAP      line 43: placeholder [CONFIRM: a proof point about monitoring itself would be stronger]: | Keep them out | Monitoring and an owner, so duplicates don't come back | Customers cut d
GAP      line 67: placeholder [MISSING: no email lead assigned for Q3]: | Email nurture | Interest, Consideration, Decision | $0 | 0% | [MISSING: no email lead as
GAP      line 74: placeholder [CONFIRM: the go-to-market plan has no account tiers; ABM and sales operations to set them]: - Tier 1 accounts: industry versions of the playbook landing page (retail, financial servi
GAP      line 78: placeholder [CONFIRM with the campaign owner]: Planning milestones suggested by the assistant. [CONFIRM with the campaign owner]
```

No conflicts: channel budgets add up to $120,000, and no channel starts before what it promotes is ready. The gaps are the open questions above.
