# Example output: copy review

> What the campaign assistant returns for "Review sample-data/ad-copy-sample.csv." Made-up campaign. The ERROR and WARN items come from `python3 -m assistant copy`; the scores and rewrites come from the assistant, and every rewrite was re-checked.

## Summary
5 of 7 ads pass the hard rules. Both Google ads need fixes before launch; three more ads have warnings.

## google-search / RSA-1: Score 4/5
Strong problem-first headlines and approved proof points. Two headlines are over the limit, and one uses an unapproved claim.
- **What works:** "Duplicate Customer Records?" matches the master brief's first pain point; "Cut Data Cleanup Time by 40%" is an approved proof point; 8 headlines give the system options.
- **What to fix:**
  - "Based on 500+ Customer Cleanups" (31 characters, and "500+" has no approved source) → **"Get the Free Cleanup Playbook"** (29)
  - "Stop Duplicates From Coming Back" (32) → **"Keep Duplicates From Returning"** (30)
- **Risks:** none after the fixes.

## google-search / RSA-2: Score 1/5
Not launchable: too few headlines and descriptions, an over-limit headline, hype words, wrong terms and an unapproved "3x" claim.
- **What works:** "Free Customer Data Playbook" is the right offer (a free offer beat a demo offer in 2025-Q4).
- **What to fix:**
  - "The Best-in-Class Data Quality Tool" (35, avoid list, wrong product term) → **"Data Quality Platform"** (21)
  - "Revolutionary data cleansing tool that removes dupes 3x faster for your whole team." → **"Find, merge and stop duplicate customer records with a free 30-day cleanup plan."** (80)
  - Add at least one more headline and one more description, or merge this ad into RSA-1.
- **Risks:** "3x faster" has no source. Remove it unless product marketing approves one.

## linkedin / Video-A: Score 4/5
- **What works:** question opening matches what won in 2025-Q4 and 2026-Q1 (question headlines beat statements on CTR).
- **What to fix:** the intro text is 162 characters, so the CTA is cut off on desktop. "Most mid-size companies" is also a claim with no source. → **"Is the same customer in your CRM five times? Get the free 30-day plan to find, merge and stop duplicate records."** (112)

## linkedin / Image-B: Score 3/5
- **What works:** "30% of their week" is an approved proof point.
- **What to fix:** "ebook" isn't brand terminology. → Headline: **"Download the Customer Data Cleanup Playbook"** (43)

## email / Email-2: Score 2/5
- **What to fix:** ALL CAPS, two exclamation marks, and "#1" with no source. → Subject: **"How a regional bank cleaned up its records"** (42). Customer story subject lines got the most clicks in the 2026-Q1 nurture. Use the preheader for the benefit: "30 minutes, on demand: match rules, merge order and who owns it now."
- **Risks:** "#1 guide" is a ranking claim that needs a named source.

## meta / Retarget-1 and email / Email-1: Score 4/5
Pass all checks. Retarget-1 fits a retargeting audience ("Still merging duplicate records by hand?").
