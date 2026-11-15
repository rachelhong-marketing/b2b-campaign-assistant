# Example output: landing page draft

> What the campaign assistant returns for "Draft the landing page for the Customer Data Cleanup Playbook." Made-up campaign. Built from [`knowledge/06-assets/customer-data-cleanup-playbook-abstract.md`](../knowledge/06-assets/customer-data-cleanup-playbook-abstract.md), following `knowledge/02-brief-templates/landing-page-template.md`. The copy is also in [`drafts/landing-page-draft.csv`](drafts/landing-page-draft.csv) so the check can read it.

## Search result

**Customer Data Cleanup Playbook | Fernhill Software**  
A free 30-day plan to find, merge and stop duplicate customer records. Get the Customer Data Cleanup Playbook.

## Hero

### One customer, one record. Here's the 30-day plan.

The free Customer Data Cleanup Playbook shows how to find duplicate customer records, merge them safely and keep them from coming back.

**[ Get the playbook ]**

Image: the playbook cover and the one-page checklist (not a stock photo).

## What you get

- How to measure how many duplicate records you have
- Match rules for "same customer" across your CRM, billing and support systems
- A safe order to merge records without breaking your reports
- How to assign an owner so duplicates don't come back
- A one-page checklist to share with your team

## How it works

1. Fill in the short form.
2. Get the playbook by email and download it right away.
3. Start with week one: measure your duplicates.

## Proof

> Teams spend 30% of their week fixing data (2025 customer survey, n=120)

## Form

- Work email
- First name
- Company
- Job title

Note under the button: "We'll email you the playbook. You can also download it on the next page."

[CONFIRM with sales operations: is company size needed on the form, or can it come from enrichment? Fewer fields usually means more downloads.]

## After submit

- **Thank-you page:** the download link, plus "Want help with week one? Book a demo with a data specialist."
- **From 2026-08-03:** add the bank webinar to the thank-you page.

## Why it's written this way

- The headline uses the campaign's message ("One customer, one record") and a specific time promise, which held up well on MQLs in 2026-Q1.
- No "based on 500+ cleanups" claim. The abstract says the playbook isn't based on a count of customer projects.
- One proof point only, from the approved list.

## Copy check result

`python3 -m assistant copy examples/drafts/landing-page-draft.csv`

```
Copy check: landing-page-draft.csv
1 of 1 ads pass the hard rules

landing-page / playbook-page  [OK]
```
