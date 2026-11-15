import io
import unittest
from contextlib import redirect_stdout
from pathlib import Path

from assistant import brief, copy_rules, keywords, cli

ROOT = Path(__file__).resolve().parent.parent
BRIEF = ROOT / "knowledge" / "01-campaign-plans" / "2026-q3-clean-customer-data-master-brief.md"
COPY = ROOT / "sample-data" / "ad-copy-sample.csv"
KW = ROOT / "sample-data" / "keywords-sample.csv"
NEG = ROOT / "sample-data" / "negative-keywords.csv"
COMP = ROOT / "knowledge" / "04-audience" / "competitors.csv"


class Brief(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.found = brief.check(BRIEF.read_text())
        cls.text = " ".join(m for _, _, m in cls.found)

    def test_budget_conflict(self):
        self.assertIn("$130,000", self.text)
        self.assertIn("$120,000", self.text)

    def test_planted_gaps(self):
        self.assertIn("Content syndication starts 2026-06-15", self.text)
        self.assertIn("'Pipeline' has no target", self.text)
        self.assertIn("Nurture (4 emails): no owner", self.text)
        self.assertIn("[TBD]", self.text)
        self.assertIn("[CONFIRM source]", self.text)

    def test_complete_brief_is_clean(self):
        clean = BRIEF.read_text()
        clean = clean.replace("[CONFIRM source]", "(2025 benchmark study)").replace("[TBD]", "https://yoursite.example/bank-webinar")
        clean = clean.replace("| Pipeline | |", "| Pipeline | $1,200,000 |").replace("| $0 | |", "| $0 | Email lead |")
        clean = clean.replace("$25,000 | Demand gen lead | 2026-06-15", "$15,000 | Demand gen lead | 2026-07-15")
        self.assertEqual(brief.check(clean), [])

    def test_missing_field(self):
        found = brief.check(BRIEF.read_text().replace("- **Owner:** Integrated Marketing\n", ""))
        self.assertIn(("GAP", "owner", "missing."), found)


class Copy(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.r = copy_rules.check(copy_rules.read_copy(COPY))

    def msgs(self, key):
        return " ".join(m for _, _, m in self.r[key])

    def test_hard_limits(self):
        self.assertIn("32 characters, over the 30-character limit", self.msgs(("google-search", "RSA-1")))
        self.assertIn("only 2 headline(s)", self.msgs(("google-search", "RSA-2")))
        self.assertIn("only 1 description(s)", self.msgs(("google-search", "RSA-2")))

    def test_claims(self):
        self.assertIn("'3x' isn't an approved proof point", self.msgs(("google-search", "RSA-2")))
        self.assertIn("'500+' isn't an approved proof point", self.msgs(("google-search", "RSA-1")))
        self.assertNotIn("40%", self.msgs(("google-search", "RSA-1")))          # approved
        self.assertEqual(self.r[("linkedin", "Image-B")][0][0], "WARN")          # 30% approved; only 'ebook'

    def test_brand_words_and_email(self):
        self.assertIn("avoid list", self.msgs(("google-search", "RSA-2")))
        email2 = self.msgs(("email", "Email-2"))
        self.assertIn("ALL CAPS", email2)
        self.assertIn("'#1' is a claim", email2)

    def test_clean_ads(self):
        self.assertEqual(self.r[("meta", "Retarget-1")], [])
        self.assertEqual(self.r[("email", "Email-1")], [])


class Keywords(unittest.TestCase):
    def test_sample(self):
        found = keywords.check(keywords.read(KW), keywords._read(NEG), keywords.load_competitor_terms(COMP))
        text = " ".join(m for *_, m in found)
        self.assertIn("duplicate of row 2", text)
        self.assertIn("blocked by the negative keyword 'free'", text)
        self.assertIn("blocked by the negative keyword 'jobs'", text)
        self.assertIn("Google Ads allows 80 characters and 10 words", text)
        self.assertIn("match type 'exacct'", text)
        self.assertEqual(text.count("competitor brand term"), 2)
        self.assertIn("in 2 ad groups", text)


class Commands(unittest.TestCase):
    def test_exit_codes(self):
        with redirect_stdout(io.StringIO()):
            self.assertEqual(cli.main(["brief", str(BRIEF)]), 1)
            self.assertEqual(cli.main(["copy", str(COPY)]), 1)



class Drafts(unittest.TestCase):
    """The example drafts must pass the same checks the assistant runs on its own work."""
    DRAFTS = ROOT / "examples" / "drafts"

    def test_master_brief_draft_has_no_conflicts(self):
        found = brief.check((ROOT / "examples" / "01-master-brief-draft.md").read_text())
        self.assertEqual([f for f in found if f[0] == brief.CONFLICT], [])
        gaps = " ".join(m for _, _, m in found)
        self.assertIn("[MISSING: the plan says", gaps)
        self.assertIn("[MISSING: no email lead", gaps)

    def test_copy_drafts_pass(self):
        for name in ("copy-draft.csv", "landing-page-draft.csv"):
            results = copy_rules.check(copy_rules.read_copy(self.DRAFTS / name))
            issues = [(k, i) for k, v in results.items() for i in v]
            self.assertEqual(issues, [], name)

    def test_keyword_draft_passes(self):
        rows = keywords.read(self.DRAFTS / "keywords-draft.csv")
        negs = keywords._read(self.DRAFTS / "negative-keywords-draft.csv")
        found = keywords.check(rows, negs, keywords.load_competitor_terms(COMP))
        self.assertEqual(found, [])

    def test_landing_page_needs_three_bullets(self):
        rows = [{"channel": "landing-page", "ad": "p", "field": f, "text": t} for f, t in
                [("meta_title", "Title"), ("meta_description", "Desc"), ("headline", "Head"), ("cta", "Go"),
                 ("bullet", "One")]]
        msgs = " ".join(m for _, _, m in copy_rules.check(rows)[("landing-page", "p")])
        self.assertIn("only 1 bullet(s); at least 3", msgs)


if __name__ == "__main__":
    unittest.main()
