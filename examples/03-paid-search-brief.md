# Example output: paid search brief

> What the campaign assistant returns for "Draft the paid search brief for Q3 Clean Customer Data." Made-up campaign. It follows `knowledge/02-brief-templates/paid-search-brief-template.md`. The copy and keywords below passed `python3 -m assistant copy` and `python3 -m assistant keywords`.

**Before you use this:** the master brief's budget doesn't add up ($130,000 in tactics vs. a $120,000 total). The $30,000 below is from the tactics table. [CONFIRM]

## 1. Campaign link
- Master brief: 2026-q3-clean-customer-data-master-brief
- Funnel stage(s): Interest (playbook); Decision (demo, brand terms only)
- Launch and end dates: 2026-07-01 to 2026-09-30

## 2. Objective and KPIs
- Objective: Get searchers with duplicate customer data problems to download the Customer Data Cleanup Playbook.
- Primary KPI and target: Playbook downloads from search. [CONFIRM] The master brief has 600 downloads across all channels but no split by channel.
- Early-read metric (direction only): click-to-download rate

## 3. Audience and targeting
- Locations: United States, Canada
- Audience layers: target account list as an observation layer; remarketing list of playbook page visitors who didn't download
- Exclusions: current customer list; job seekers and students (see negatives)

## 4. Keywords
| Ad group | Theme | Example keywords | Match type |
|---|---|---|---|
| Duplicate customer data | The pain | duplicate customer records, customer data deduplication, merge duplicate customer records | Phrase |
| Cleanup plan | The offer | customer data cleanup, data cleanup plan, data cleanup checklist | Phrase |
| Data quality platform | The category | data quality platform, data quality software | Exact, phrase |

- Negative keywords: jobs, salary, course, free [CONFIRM: "free" also blocks searches like "free customer data cleanup guide", which fit our offer. Suggest removing "free" from the negatives.]
- Competitor terms: no. Brand guidelines require approval.

## 5. Ad copy (responsive search ad)
- Headlines (10, all 30 characters or fewer): Duplicate Customer Records? · Merge Duplicates in 30 Days · Free Customer Data Playbook · One Customer, One Record · Find and Merge Duplicates · Keep Duplicates From Returning · Cut Data Cleanup Time by 40% · Built for Data Leaders · Get the Free Cleanup Playbook · Reports That Finally Match
- Descriptions (4): "Find, merge and stop duplicate customer records with a free 30-day cleanup plan." · "Match rules, a safe merge order and a checklist for your team. Free playbook." · "Teams spend 30% of their week fixing data. Get the plan to stop the duplicates." · "Customers cut data cleanup time by 40%. Start with the free playbook."
- Display path: /duplicates/playbook
- Past learning applied: in 2025-Q4 a free offer ("Free Data Health Check") beat a demo offer on leads per click, and the 2026-Q1 demo CTA converted fewer leads. So the ads lead with the free playbook, not a demo.
- Left out on purpose: "based on 500+ customer cleanups" (no approved source).

## 6. Landing page and tracking
- Landing page: https://yoursite.example/cleanup-playbook
- UTM campaign: 2026-q3-clean-customer-data; `utm_term` from the keyword
- GCLID captured on the form: [CONFIRM] Needed to send MQLs back to Google Ads.

## 7. Budget, bidding and owner
- Budget: $30,000 [CONFIRM given the budget gap]
- Bid strategy: maximize conversions on playbook downloads at first; move to MQL-based bidding once offline conversions are flowing [CONFIRM]
- Owner: Paid search lead

## 8. Open questions
1. Which $10,000 comes out of the tactics budget? (Campaign owner)
2. What share of the 600 playbook downloads should come from search? (Campaign owner)
3. Remove "free" from the negative keyword list? (Paid search lead)
4. Is the GCLID hidden field on the playbook form? (Marketing ops)
