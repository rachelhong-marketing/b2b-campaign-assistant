# Example output: keyword draft

> What the campaign assistant returns for "Brainstorm keywords for the Q3 Clean Customer Data search campaign." Made-up campaign. Built from the master brief draft (message, pain points, industries) and the playbook abstract. The files are [`drafts/keywords-draft.csv`](drafts/keywords-draft.csv) and [`drafts/negative-keywords-draft.csv`](drafts/negative-keywords-draft.csv), ready to check or upload.

## How the ad groups map to the brief

| Ad group | Theme | Why it's here | Keywords |
|---|---|---|---|
| Duplicate customer data | The pain | The brief's first pain point: one customer, many records | 5 |
| Cleanup plan | The offer | People looking for a plan or checklist, which is what the playbook is | 5 |
| Reports don't match | The outcome | Analytics leaders whose reports don't agree | 4 |
| Data quality platform | The category | Buyers comparing tools; exact match on the head term to control cost | 4 |
| Industry | Our two industries | Retail and financial services searchers | 3 |

## Keywords

| Ad group | Keyword | Match type |
|---|---|---|
| Duplicate customer data | duplicate customer records | phrase |
| Duplicate customer data | customer data deduplication | phrase |
| Duplicate customer data | merge duplicate customer records | phrase |
| Duplicate customer data | remove duplicate records crm | phrase |
| Duplicate customer data | fix duplicate customer data | phrase |
| Cleanup plan | customer data cleanup | phrase |
| Cleanup plan | data cleanup plan | phrase |
| Cleanup plan | data cleanup checklist | phrase |
| Cleanup plan | free customer data cleanup guide | phrase |
| Cleanup plan | deduplication best practices | phrase |
| Reports don't match | single customer view | phrase |
| Reports don't match | customer data quality | phrase |
| Reports don't match | inconsistent customer data | phrase |
| Reports don't match | incomplete customer data | phrase |
| Data quality platform | data quality platform | exact |
| Data quality platform | data quality software | phrase |
| Data quality platform | enterprise data quality software | phrase |
| Data quality platform | data quality monitoring | phrase |
| Industry | retail customer data quality | phrase |
| Industry | banking customer data cleanup | phrase |
| Industry | financial services data quality | phrase |

## Negative keywords

jobs, job, salary, career, course, certification, training, internship, open source, definition. These keep out job seekers, students and people looking for free open source tools or definitions.

Not on the list: "free". The playbook is free, so people searching "free customer data cleanup guide" are a good fit. (The team's current negative list in `sample-data/` blocks "free"; the keyword review flags that.)

## What the assistant didn't do

- **Search volume and cost per click:** not estimated. Check each keyword in Google Keyword Planner before setting budgets. [CONFIRM]
- **Competitor terms:** none added. Brand guidelines require approval before bidding on Clearline Data, Datavault Pro or Purestream.
- **Manufacturing:** left out. The go-to-market plan moves it to H1 2027.

## Keyword check result

`python3 -m assistant keywords examples/drafts/keywords-draft.csv --negatives examples/drafts/negative-keywords-draft.csv`

```
Keyword check: keywords-draft.csv
21 keywords, 0 errors, 0 warnings
```
