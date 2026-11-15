"""Command line: brief, copy, keywords."""
import argparse
from collections import Counter
from pathlib import Path

from . import brief, copy_rules as copy, keywords

ROOT = Path(__file__).resolve().parent.parent


def main(argv=None):
    ap = argparse.ArgumentParser(prog="assistant", description="Checks behind the B2B campaign assistant.")
    sub = ap.add_subparsers(dest="cmd", required=True)
    b = sub.add_parser("brief", help="find gaps and conflicts in a master brief (Markdown)")
    b.add_argument("path")
    c = sub.add_parser("copy", help="check ad and email copy (CSV: channel, ad, field, text)")
    c.add_argument("path")
    k = sub.add_parser("keywords", help="check a Google Ads keyword list (CSV: ad_group, keyword, match_type)")
    k.add_argument("path")
    k.add_argument("--negatives", help="negative keywords CSV (column: keyword)")
    k.add_argument("--competitors", default=str(ROOT / "knowledge" / "04-audience" / "competitors.csv"),
                   help="competitor brand terms CSV")
    a = ap.parse_args(argv)

    if a.cmd == "brief":
        text = Path(a.path).read_text(encoding="utf-8")
        found = brief.check(text)
        counts = Counter(level for level, _, _ in found)
        print(f"Brief check: {Path(a.path).name}")
        print(f"{counts.get('GAP', 0)} gaps, {counts.get('CONFLICT', 0)} conflicts\n")
        for level in ("CONFLICT", "GAP"):
            for lv, where, msg in found:
                if lv == level:
                    print(f"{lv:<9}{where}: {msg}")
        if not found:
            print("No gaps or conflicts found by the checks. Still read it for audience and message fit.")
        return 1 if found else 0

    if a.cmd == "copy":
        results = copy.check(copy.read_copy(a.path))
        bad = {k for k, v in results.items() if any(l == copy.ERROR for l, _, _ in v)}
        print(f"Copy check: {Path(a.path).name}")
        print(f"{len(results) - len(bad)} of {len(results)} ads pass the hard rules\n")
        for (channel, ad), issues in results.items():
            status = "FIX" if (channel, ad) in bad else ("CHECK" if issues else "OK")
            print(f"{channel} / {ad}  [{status}]")
            for level, field, msg in issues:
                print(f"  {level:<6}{field}: {msg}")
        return 1 if bad else 0

    rows = keywords.read(a.path)
    negs = keywords._read(a.negatives) if a.negatives else []
    comps = keywords.load_competitor_terms(a.competitors) if a.competitors and Path(a.competitors).exists() else []
    found = keywords.check(rows, negs, comps)
    errors = sum(1 for f in found if f[1] == keywords.ERROR)
    print(f"Keyword check: {Path(a.path).name}")
    print(f"{len(rows)} keywords, {errors} errors, {len(found) - errors} warnings\n")
    for row, level, kw, msg in found:
        print(f"{level:<6}row {row} '{kw}': {msg}")
    if not a.negatives:
        print("\nNegative keywords not checked. Add --negatives <file.csv>.")
    return 1 if errors else 0
