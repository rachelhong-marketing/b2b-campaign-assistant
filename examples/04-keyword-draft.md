# Example output: keyword draft

> What the campaign assistant returns for "Brainstorm keywords for the Q3 Data Readiness search campaign." Made-up campaign. Built from the master brief draft (message, personas, industries) and the assessment abstract. The files are [`drafts/keywords-draft.csv`](drafts/keywords-draft.csv) and [`drafts/negative-keywords-draft.csv`](drafts/negative-keywords-draft.csv), ready to check or upload.

## How the ad groups map to the brief

| Ad group | Theme | Why it's here | Keywords |
|---|---|---|---|
| Data readiness | The offer | Interest: people already looking for a readiness check | 6 |
| Data quality for AI | The problem | Data leaders planning AI who know data is the risk | 5 |
| Duplicate customer data | The pain | The most common sign in the guide: one customer, many records | 4 |
| Data quality platform | The category | Buyers comparing tools; exact match on the head term to control cost | 4 |
| Industry | Our two industries | Retail and financial services searchers | 3 |

## Keywords

| Ad group | Keyword | Match type |
|---|---|---|
| Data readiness | data readiness assessment | phrase |
| Data readiness | ai data readiness | phrase |
| Data readiness | ai readiness assessment | phrase |
| Data readiness | is my data ready for ai | phrase |
| Data readiness | data readiness for ai | phrase |
| Data readiness | free data readiness assessment | phrase |
| Data quality for AI | data quality for ai | phrase |
| Data quality for AI | data quality for machine learning | phrase |
| Data quality for AI | prepare data for ai | phrase |
| Data quality for AI | ai data preparation | phrase |
| Data quality for AI | customer data quality | phrase |
| Duplicate customer data | duplicate customer records | phrase |
| Duplicate customer data | customer data deduplication | phrase |
| Duplicate customer data | fix duplicate customer data | phrase |
| Duplicate customer data | incomplete customer data | phrase |
| Data quality platform | data quality platform | exact |
| Data quality platform | data quality software | phrase |
| Data quality platform | enterprise data quality software | phrase |
| Data quality platform | data quality monitoring | phrase |
| Industry | retail customer data quality | phrase |
| Industry | banking data quality | phrase |
| Industry | financial services data quality | phrase |

## Negative keywords

jobs, job, salary, career, course, certification, training, internship, open source, definition. These keep out job seekers, students and people looking for free open source tools or definitions.

Not on the list: "free". The assessment is free, so people searching "free data readiness assessment" are a good fit. (The team's current negative list in `sample-data/` blocks "free"; the copy review flags that.)

## What the assistant didn't do

- **Search volume and cost per click:** not estimated. Check each keyword in Google Keyword Planner before setting budgets. [CONFIRM]
- **Competitor terms:** none added. Brand guidelines require approval before bidding on Clearline Data, Datavault Pro or Purestream.
- **Manufacturing:** left out. The go-to-market plan moves it to H1 2027.

## Keyword check result

`python3 -m assistant keywords examples/drafts/keywords-draft.csv --negatives examples/drafts/negative-keywords-draft.csv`

```
Keyword check: keywords-draft.csv
22 keywords, 0 errors, 0 warnings
```
