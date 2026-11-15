# Example output: paid search brief

> What the campaign assistant returns for "Draft the paid search brief for Q3 Data Readiness." Made-up campaign. It follows `knowledge/02-brief-templates/paid-search-brief-template.md`. The copy and keywords below passed `python3 -m assistant copy` and `python3 -m assistant keywords`.

**Before you use this:** the master brief's budget doesn't add up ($130,000 in tactics vs. a $120,000 total). The $30,000 below is from the tactics table. [CONFIRM]

## 1. Campaign link
- Master brief: 2026-q3-data-readiness-master-brief
- Funnel stage(s): Interest (assessment); Decision (demo, brand terms only)
- Launch and end dates: 2026-07-01 to 2026-09-30

## 2. Objective and KPIs
- Objective: Get searchers with data quality and AI readiness problems to take the Data Readiness Assessment.
- Primary KPI and target: Assessment completions from search. [CONFIRM] The master brief has 600 completions across all channels but no split by channel.
- Early-read metric (direction only): click-to-completion rate

## 3. Audience and targeting
- Locations: United States, Canada
- Audience layers: target account list as an observation layer; remarketing list of assessment page visitors who didn't finish
- Exclusions: current customer list; job seekers and students (see negatives)

## 4. Keywords
| Ad group | Theme | Example keywords | Match type |
|---|---|---|---|
| Data readiness | AI readiness | data readiness assessment, ai data readiness, is my data ready for ai | Phrase |
| Data quality for AI | The problem | data quality for ai, customer data quality, duplicate customer data | Phrase |
| Data quality platform | The category | data quality platform, data quality software | Exact, phrase |

- Negative keywords: jobs, salary, course, free [CONFIRM: "free" also blocks searches like "free data readiness assessment", which fit our offer. Suggest removing "free" from the negatives.]
- Competitor terms: no. Brand guidelines require approval.

## 5. Ad copy (responsive search ad)
- Headlines (10, all 30 characters or fewer): Is Your Data Ready for AI? · Free Data Readiness Assessment · Get Your Score in 3 Minutes · Know Before Your AI Project · Cut Data Cleanup Time by 40% · Data Quality Platform · Setup in Under Two Weeks · Find Gaps Before They Cost You · Duplicates Slowing Your AI? · See the 3 Fixes That Matter
- Descriptions (3): "Find out if your customer data is ready for AI. Take the free 3-minute assessment." · "See where duplicates and gaps will slow your AI projects down and what to fix first." · "Customers cut data cleanup time by 40%. Start with a free readiness score."
- Display path: /data-readiness/assessment
- Past learning applied: in 2025-Q4 a free tool offer ("Free Data Health Check") beat a demo offer on leads per click, and the 2026-Q1 demo CTA converted fewer leads. So the ads lead with the free assessment, not a demo.
- Left out on purpose: "500+ companies" (no approved source).

## 6. Landing page and tracking
- Landing page: https://yoursite.example/assessment
- UTM campaign: 2026-q3-data-readiness; `utm_term` from the keyword
- GCLID captured on the form: [CONFIRM] Needed to send MQLs back to Google Ads.

## 7. Budget, bidding and owner
- Budget: $30,000 [CONFIRM given the budget gap]
- Bid strategy: maximize conversions on assessment completions at first; move to MQL-based bidding once offline conversions are flowing [CONFIRM]
- Owner: Paid search lead

## 8. Open questions
1. Which $10,000 comes out of the tactics budget? (Campaign owner)
2. What share of the 600 assessment completions should come from search? (Campaign owner)
3. Remove "free" from the negative keyword list? (Paid search lead)
4. Is the GCLID hidden field on the assessment form? (Marketing ops)
