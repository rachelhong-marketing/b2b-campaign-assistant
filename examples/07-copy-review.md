# Example output: copy review

> What the campaign assistant returns for "Review sample-data/ad-copy-sample.csv." Made-up campaign. The ERROR and WARN items come from `python3 -m assistant copy`; the scores and rewrites come from the assistant, and every rewrite was re-checked.

## Summary
5 of 7 ads pass the hard rules. Both Google ads need fixes before launch; four ads have warnings.

## google-search / RSA-1: Score 4/5
Strong problem-first headlines and approved proof points. Two headlines are over the limit, and one uses an unapproved claim.
- **What works:** "Is Your Data AI-Ready?" matches the master brief's message; "Cut Data Cleanup Time by 40%" is an approved proof point; 8 headlines give the system options.
- **What to fix:**
  - "Benchmark Against 500+ Companies" (32 characters, and "500+" has no approved source) → **"See How Your Data Compares"** (26)
  - "Know Before Your AI Project Starts" (34) → **"Know Before Your AI Project"** (27)
- **Risks:** none after the fixes.

## google-search / RSA-2: Score 1/5
Not launchable: too few headlines and descriptions, an over-limit headline, hype words and an unapproved "3x" claim.
- **What works:** "Free Data Readiness Assessment" is the right offer (a free tool beat a demo offer in 2025-Q4).
- **What to fix:**
  - "The Best-in-Class Data Quality Tool" (35, avoid list, wrong product term) → **"Data Quality Platform"** (21)
  - "Revolutionary AI-powered data cleansing that delivers 3x faster results for your team." → **"Find duplicates and gaps before they slow your AI projects. Free 3-minute assessment."** (85)
  - Add at least one more headline and one more description, or merge this ad into RSA-1.
- **Risks:** "3x faster" has no source. Remove it unless product marketing approves one.

## linkedin / Video-A: Score 4/5
- **What works:** question opening matches what won in 2025-Q4 and 2026-Q1 (question headlines beat statements on CTR).
- **What to fix:** the intro text is 169 characters, so the CTA is cut off on desktop. → **"Is your data ready for AI? Most teams find out only after a project stalls. Get your score in 3 minutes."** (104)

## linkedin / Image-B: Score 3/5
- **What works:** "30% of their week" is an approved proof point.
- **What to fix:** "quiz" isn't brand terminology. → Headline: **"Take the 3-minute Data Readiness Assessment"** (43)

## email / Email-2: Score 2/5
- **What to fix:** ALL CAPS, two exclamation marks, and "#1" with no source. → Subject: **"5 signs your data isn't ready for AI"** (36). Move the current preheader text into the body and use the preheader for the benefit: "A 3-minute check shows which fixes matter most."
- **Risks:** "#1 guide" is a ranking claim that needs a named source.

## meta / Retarget-1 and email / Email-1: Score 4/5
Pass all checks. Retarget-1 fits a retargeting audience ("Still wondering...").
