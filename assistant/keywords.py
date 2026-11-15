"""Check a Google Ads keyword list: length, match types, duplicates, negatives that block keywords, competitor terms."""
import csv
import re
from collections import defaultdict

ERROR, WARN = "ERROR", "WARN"
MATCH_TYPES = {"exact", "phrase", "broad"}
SYMBOLS = set("!@%^*()={};~<>?\\|,")


def _read(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        return [{(k or "").strip().lower(): (v or "").strip() for k, v in r.items()} for r in csv.DictReader(fh)]


def norm(kw):
    kw = kw.strip().strip('"').strip("[]")
    return re.sub(r"\s+", " ", kw.lower())


def load_competitor_terms(path):
    terms = []
    for r in _read(path):
        for t in r.get("brand_terms", "").split(";"):
            if t.strip():
                terms.append((t.strip().lower(), r.get("competitor", "")))
    return terms


def check(keywords, negatives=(), competitor_terms=()):
    """keywords: dicts with ad_group, keyword, match_type. Returns list of (row, level, keyword, message)."""
    out = []
    first_seen = {}
    groups_for = defaultdict(set)
    neg = [norm(n["keyword"]) for n in negatives if n.get("keyword")]
    for i, r in enumerate(keywords, start=2):
        kw, mt, group = r.get("keyword", ""), r.get("match_type", "").lower(), r.get("ad_group", "")
        n = norm(kw)
        if not n:
            out.append((i, ERROR, kw, "empty keyword."))
            continue
        if len(n) > 80 or len(n.split()) > 10:
            out.append((i, ERROR, kw, f"too long ({len(n)} characters, {len(n.split())} words). Google Ads allows "
                                      "80 characters and 10 words."))
        bad = sorted({c for c in n if c in SYMBOLS})
        if bad:
            out.append((i, WARN, kw, f"has symbols Google Ads may reject or ignore: {' '.join(bad)}"))
        if mt not in MATCH_TYPES:
            out.append((i, ERROR, kw, f"match type '{r.get('match_type', '')}' should be exact, phrase or broad."))
        if (n, mt) in first_seen:
            out.append((i, ERROR, kw, f"duplicate of row {first_seen[(n, mt)]} ({mt} match)."))
        else:
            first_seen[(n, mt)] = i
        groups_for[n].add(group)
        words = n.split()
        for ng in neg:
            nw = ng.split()
            if any(words[j:j + len(nw)] == nw for j in range(len(words) - len(nw) + 1)):
                out.append((i, ERROR, kw, f"blocked by the negative keyword '{ng}', so it will never show."))
        flagged = set()
        for term, comp in competitor_terms:
            if comp not in flagged and re.search(r"(?<![a-z0-9])" + re.escape(term) + r"(?![a-z0-9])", n):
                flagged.add(comp)
                out.append((i, WARN, kw, f"competitor brand term ({comp}). Needs approval before bidding."))
    for n, groups in groups_for.items():
        if len(groups) > 1:
            rows = [i for i, r in enumerate(keywords, start=2) if norm(r.get("keyword", "")) == n]
            out.append((rows[-1], WARN, n, f"in {len(groups)} ad groups ({', '.join(sorted(groups))}). "
                                           "They'll compete with each other; keep it in one."))
    return sorted(out, key=lambda x: x[0])


def read(path):
    rows = _read(path)
    missing = {"keyword", "match_type"} - set(rows[0].keys() if rows else [])
    if missing:
        raise ValueError(f"{path} is missing columns: {', '.join(sorted(missing))}")
    return rows
