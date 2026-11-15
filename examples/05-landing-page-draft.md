# Example output: landing page draft

> What the campaign assistant returns for "Draft the landing page for the Data Readiness Assessment." Made-up campaign. Built from [`knowledge/06-assets/data-readiness-assessment-abstract.md`](../knowledge/06-assets/data-readiness-assessment-abstract.md), following `knowledge/02-brief-templates/landing-page-template.md`. The copy is also in [`drafts/landing-page-draft.csv`](drafts/landing-page-draft.csv) so the check can read it.

## Search result

**Data Readiness Assessment | Fernhill Software**  
Find out if your customer data is ready for AI. Take the free 3-minute assessment and get your score and the top three fixes.

## Hero

### Is your customer data ready for AI?

Take the 3-minute Data Readiness Assessment. Get a score from 0 to 100 and the three fixes that matter most, before your AI project starts.

**[ Take the assessment ]**

Image: the score gauge and a page of the sample report (not a stock photo).

## What you get

- Your readiness score from 0 to 100
- A score for each area: completeness, duplicates, consistency and governance
- The top three fixes to make first, ranked by impact
- A report you can download and share with your team

## How it works

1. Answer 15 questions about your customer data. It takes about 3 minutes.
2. See your score and the area holding you back most.
3. Get the full report with your top three fixes.

## Proof

> Teams spend 30% of their week fixing data (2025 customer survey, n=120)

## Form

- Work email
- First name
- Company
- Job title

Note under the button: "We'll show your score right away and email your full report."

[CONFIRM with sales operations: is company size needed on the form, or can it come from enrichment? Fewer fields usually means more completions.]

## After submit

- **Score under 50:** results page with the score, the top three fixes and a "Book your demo" button.
- **Score 50 or above:** results page with the score and the report download. The guide is added when it's published on 2026-08-03.

## Why it's written this way

- The headline asks the same question as LinkedIn ad A, which follows the performance log: question headlines beat statements on click-through rate in 2025-Q4 and 2026-Q1.
- No benchmark claim. The abstract says the assessment doesn't compare companies yet.
- One proof point only, from the approved list.

## Copy check result

`python3 -m assistant copy examples/drafts/landing-page-draft.csv`

```
Copy check: landing-page-draft.csv
1 of 1 ads pass the hard rules

landing-page / assessment-page  [OK]
```
