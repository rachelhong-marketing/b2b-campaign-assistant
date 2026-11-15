# Example output: ad and email copy drafts

> What the campaign assistant returns for "Write the search, LinkedIn, Meta and email copy from the assessment landing page." Made-up campaign. Built from the landing page draft and the asset abstracts, with past learnings from `knowledge/05-performance/creative-performance-log.csv`. All copy is in [`drafts/copy-draft.csv`](drafts/copy-draft.csv).

Character counts are the tool's, not the AI's.

## Google search ads

Headline 1 leads with the problem or the offer, per the guidelines. At least 8 distinct headlines per ad. "Free" follows the 2025-Q4 learning: a free tool offer beat a demo offer on leads per click.

### RSA-1 Data readiness

| Field | Text | Characters |
|---|---|---|
| headline | Is Your Data Ready for AI? | 26 |
| headline | Data Readiness Assessment | 25 |
| headline | Get Your Score in 3 Minutes | 27 |
| headline | Free 3-Minute Assessment | 24 |
| headline | See Your Top 3 Data Fixes | 25 |
| headline | Know Before Your AI Project | 27 |
| headline | Score Your Data From 0 to 100 | 29 |
| headline | Built for Data Leaders | 22 |
| headline | Fix Duplicate Customer Data | 27 |
| headline | Cut Data Cleanup Time by 40% | 28 |
| description | Find out if your customer data is ready for AI before you start. Takes 3 minutes. | 81 |
| description | Get a readiness score and the three fixes that matter most, ranked by impact. | 77 |
| description | Teams spend 30% of their week fixing data. See where yours stands. | 66 |
| description | Scores completeness, duplicates, consistency and governance. Free report. | 73 |
| path | data-readiness | 14 |
| path | assessment | 10 |

### RSA-2 Data quality for AI

| Field | Text | Characters |
|---|---|---|
| headline | Data Quality for AI | 19 |
| headline | Is Your Data AI-Ready? | 22 |
| headline | Trust the Data Your AI Uses | 27 |
| headline | Find Duplicates and Gaps | 24 |
| headline | Data Readiness Assessment | 25 |
| headline | Get Your Score in 3 Minutes | 27 |
| headline | Setup in Under Two Weeks | 24 |
| headline | Cut Data Cleanup Time by 40% | 28 |
| headline | Free 3-Minute Assessment | 24 |
| description | AI projects stall on duplicated, incomplete data. See where you stand in 3 minutes. | 83 |
| description | Customers cut data cleanup time by 40%. Start with a free readiness score. | 74 |
| description | Take the Data Readiness Assessment and get the top three fixes for your data. | 77 |
| path | ai-data | 7 |
| path | assessment | 10 |

## LinkedIn

Ad A uses a question headline (won on click-through rate twice in the performance log). Ad B uses a specific time promise (held up well on MQLs in 2026-Q1). Test one variable at a time: same image, different headline.

### LI-A question

| Field | Text | Characters |
|---|---|---|
| intro_text | AI projects stall when customer data is duplicated or incomplete. Find out if yours is ready in 3 minutes. | 106 |
| headline | Is your customer data ready for AI? | 35 |

### LI-B time promise

| Field | Text | Characters |
|---|---|---|
| intro_text | Get a readiness score for your customer data, plus the three fixes that matter most. It takes 3 minutes. | 104 |
| headline | Score your data's AI readiness in 3 minutes | 43 |

## Meta retargeting

For people who visited the assessment page but didn't finish.

### Meta-R1 retargeting

| Field | Text | Characters |
|---|---|---|
| primary_text | Still planning your AI project? Take the 3-minute Data Readiness Assessment and see what to fix first. | 102 |
| headline | Get your data readiness score | 29 |

## Email nurture

Email 1 goes to assessment takers who score under 50; Email 2 goes to those who score 50 or above, from 2026-08-03 when the guide is published. One CTA each.

### Email-1 score under 50

| Field | Text | Characters |
|---|---|---|
| subject | Your readiness score, and what to fix first | 43 |
| preheader | Walk through your top three fixes with a data specialist. | 57 |
| body | Hi {first name}, thanks for taking the Data Readiness Assessment. Your score shows a few areas to fix before an AI project can rely on this data, and your report ranks the top three. A data specialist can walk you through them, show how other teams fixed the same problems, and answer questions about your setup. Customers cut data cleanup time by 40%, and setup takes under two weeks. You can download your full report anytime from your results page. | 451 |
| cta | Book your demo | 14 |

### Email-2 guide

| Field | Text | Characters |
|---|---|---|
| subject | 5 signs your data isn't ready for AI | 36 |
| preheader | A quick self-check for each one, plus the first step to take. | 61 |
| body | Hi {first name}, your Data Readiness Assessment showed where your customer data stands today. Our new guide goes one step further: five signs your data isn't ready for AI, each with a quick self-check and one first step. The most common sign is the same customer showing up as several records. Teams spend 30% of their week fixing problems like this. The guide shows how to keep the fixes from wearing off. | 406 |
| cta | Read the guide | 14 |

## UTM content values

One `utm_content` per ad so the reporting agent (step 4) can tell them apart, for example `ready-rsa-1`, `ready-li-a-question`, `ready-li-b-time`, `ready-meta-r1`, `ready-email-1`, `ready-email-2`. Build and check the links with the launch checker in the B2B Paid Media Planner (step 2).

## Copy check result

`python3 -m assistant copy examples/drafts/copy-draft.csv`

```
Copy check: copy-draft.csv
7 of 7 ads pass the hard rules

google-search / RSA-1 Data readiness  [OK]
google-search / RSA-2 Data quality for AI  [OK]
linkedin / LI-A question  [OK]
linkedin / LI-B time promise  [OK]
meta / Meta-R1 retargeting  [OK]
email / Email-1 score under 50  [OK]
email / Email-2 guide  [OK]
```
