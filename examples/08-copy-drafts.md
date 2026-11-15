# Example output: ad and email copy drafts

> What the campaign assistant returns for "Write the search, LinkedIn, Meta and email copy from the playbook landing page." Made-up campaign. Built from the landing page draft and the asset abstracts, with past learnings from `knowledge/05-performance/creative-performance-log.csv`. All copy is in [`drafts/copy-draft.csv`](drafts/copy-draft.csv).

Character counts are the tool's, not the AI's.

## Google search ads

Headline 1 leads with the problem or the offer, per the guidelines. At least 8 distinct headlines per ad. "Free" follows the 2025-Q4 learning: a free offer beat a demo offer on leads per click.

### RSA-1 Duplicate customer data

| Field | Text | Characters |
|---|---|---|
| headline | Duplicate Customer Records? | 27 |
| headline | Merge Duplicates in 30 Days | 27 |
| headline | Free Customer Data Playbook | 27 |
| headline | One Customer, One Record | 24 |
| headline | Find and Merge Duplicates | 25 |
| headline | Keep Duplicates From Returning | 30 |
| headline | Cut Data Cleanup Time by 40% | 28 |
| headline | Built for Data Leaders | 22 |
| headline | Get the Free Cleanup Playbook | 29 |
| headline | Reports That Finally Match | 26 |
| description | Find, merge and stop duplicate customer records with a free 30-day cleanup plan. | 80 |
| description | Match rules, a safe merge order and a checklist for your team. Free playbook. | 77 |
| description | Teams spend 30% of their week fixing data. Get the plan to stop the duplicates. | 79 |
| description | Customers cut data cleanup time by 40%. Start with the free playbook. | 69 |
| path | duplicates | 10 |
| path | playbook | 8 |

### RSA-2 Cleanup plan

| Field | Text | Characters |
|---|---|---|
| headline | Customer Data Cleanup Plan | 26 |
| headline | A 30-Day Data Cleanup Plan | 26 |
| headline | Free Customer Data Playbook | 27 |
| headline | Data Cleanup Checklist | 22 |
| headline | Merge Records Without Errors | 28 |
| headline | Setup in Under Two Weeks | 24 |
| headline | Cut Data Cleanup Time by 40% | 28 |
| headline | One Customer, One Record | 24 |
| headline | Built for Data Leaders | 22 |
| description | A step-by-step plan to clean up customer records in 30 days. Download it free. | 78 |
| description | Customers cut data cleanup time by 40%. See how in the free cleanup playbook. | 77 |
| description | Measure, match, merge and monitor. Get the free Customer Data Cleanup Playbook. | 79 |
| path | data-cleanup | 12 |
| path | playbook | 8 |

## LinkedIn

Ad A uses a question headline (won on click-through rate twice in the performance log). Ad B uses a specific time promise (held up well on MQLs in 2026-Q1). Test one variable at a time: same image, different headline.

### LI-A question

| Field | Text | Characters |
|---|---|---|
| intro_text | Is the same customer in your CRM five times? Get the free 30-day plan to find, merge and stop duplicate records. | 112 |
| headline | One customer, five records? | 27 |

### LI-B time promise

| Field | Text | Characters |
|---|---|---|
| intro_text | Clean up duplicate customer records in 30 days. The free playbook gives you match rules, a safe merge order and a checklist. | 124 |
| headline | Merge duplicate customer records in 30 days | 43 |

## Meta retargeting

For people who visited the playbook page but didn't download it.

### Meta-R1 retargeting

| Field | Text | Characters |
|---|---|---|
| primary_text | Still merging duplicate records by hand? The free Customer Data Cleanup Playbook has a 30-day plan. | 99 |
| headline | Get the cleanup playbook | 24 |

## Email nurture

Email 1 goes to playbook downloads from target accounts. Email 2 goes to everyone in the nurture from 2026-08-03, when the webinar is published; it leads with a customer story, which got the most clicks in the 2026-Q1 nurture. One CTA each.

### Email-1 target accounts

| Field | Text | Characters |
|---|---|---|
| subject | Your 30-day plan, and a faster way to start | 43 |
| preheader | Walk through your duplicate records with a data specialist. | 59 |
| body | Hi {first name}, thanks for downloading the Customer Data Cleanup Playbook. Week one is about measuring how many duplicate records you have. A data specialist can do that step with you on your own data, show how other teams set their match rules, and answer questions about your systems. Customers cut data cleanup time by 40%, and setup takes under two weeks. The playbook stays in your inbox if you'd rather start on your own. | 428 |
| cta | Book your demo | 14 |

### Email-2 webinar

| Field | Text | Characters |
|---|---|---|
| subject | How a regional bank cleaned up its records | 42 |
| preheader | 30 minutes, on demand: match rules, merge order and who owns it now. | 68 |
| body | Hi {first name}, the playbook gives you the plan. This webinar shows it working. A regional bank's data lead walks through how they found their duplicate customer records, agreed on match rules with finance and marketing, and merged records without breaking month-end reports. Teams spend 30% of their week fixing data. This is how one team got that time back. | 360 |
| cta | Watch the webinar | 17 |

## UTM content values

One `utm_content` per ad so the reporting agent (step 4) can tell them apart, for example `playbook-rsa-1`, `playbook-li-a-question`, `playbook-li-b-time`, `playbook-meta-r1`, `playbook-email-1`, `webinar-email-2`. Build and check the links with the launch checker in the B2B Paid Media Planner (step 2).

## Copy check result

`python3 -m assistant copy examples/drafts/copy-draft.csv`

```
Copy check: copy-draft.csv
7 of 7 ads pass the hard rules

google-search / RSA-1 Duplicate customer data  [OK]
google-search / RSA-2 Cleanup plan  [OK]
linkedin / LI-A question  [OK]
linkedin / LI-B time promise  [OK]
meta / Meta-R1 retargeting  [OK]
email / Email-1 target accounts  [OK]
email / Email-2 webinar  [OK]
```
