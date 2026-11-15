"""Check ad and email copy against character limits, brand words and approved proof points."""
import csv
import re
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
LIMITS_FILE = ROOT / "rules" / "copy-limits.csv"
WORDS_FILE = ROOT / "rules" / "brand-words.csv"
GUIDELINES_FILE = ROOT / "knowledge" / "03-brand-and-channel" / "brand-and-channel-guidelines.md"

ERROR, WARN = "ERROR", "WARN"
CLAIM = re.compile(r"\b\d+(?:[.,]\d+)?(?:\s?%|x\b|\s?percent\b|\+)", re.I)


def _read(path):
    with open(path, newline="", encoding="utf-8-sig") as fh:
        return [{(k or "").strip().lower(): (v or "").strip() for k, v in r.items()} for r in csv.DictReader(fh)]


def load_limits(path=LIMITS_FILE):
    return {(r["channel"], r["field"]): r for r in _read(path)}


def load_words(path=WORDS_FILE):
    return _read(path)


def approved_claims(path=GUIDELINES_FILE):
    """Numbers (like 40%) that appear in the approved proof points table."""
    text = Path(path).read_text(encoding="utf-8") if Path(path).exists() else ""
    m = re.search(r"## Approved proof points(.*?)(\n## |\Z)", text, re.S)
    return {c.replace(" ", "").lower() for c in CLAIM.findall(m.group(1))} if m else set()


def check(rows, limits=None, words=None, claims=None):
    """rows: dicts with channel, ad, field, text. Returns {(channel, ad): [(level, field, message)]}."""
    limits = load_limits() if limits is None else limits
    words = load_words() if words is None else words
    claims = approved_claims() if claims is None else claims
    out = defaultdict(list)
    counts = defaultdict(int)
    seen = defaultdict(set)
    for r in rows:
        channel, ad, field, text = r["channel"].lower(), r["ad"], r["field"].lower(), r["text"]
        key = (channel, ad)
        counts[(channel, ad, field)] += 1
        rule = limits.get((channel, field))
        if rule is None:
            out[key].append((WARN, field, f"no character rule for {channel} / {field}. Check the field name."))
        else:
            mx = int(rule["max_chars"])
            if len(text) > mx:
                level = ERROR if rule["limit_type"] == "hard" else WARN
                kind = "limit" if rule["limit_type"] == "hard" else "recommended length"
                out[key].append((level, field, f"{len(text)} characters, over the {mx}-character {kind}: \"{text}\""))
        norm = text.lower().strip()
        if norm in seen[(channel, ad, field)]:
            out[key].append((WARN, field, f"repeats another {field} in this ad: \"{text}\""))
        seen[(channel, ad, field)].add(norm)
        low = text.lower()
        for w in words:
            term = w["term"].lower()
            pattern = r"(?<![a-z0-9])" + re.escape(term) + r"(?![a-z0-9])"
            if re.search(pattern, low):
                if w["type"] == "avoid":
                    out[key].append((WARN, field, f"'{w['term']}' is on the avoid list. {w['suggestion']}."))
                elif w["type"] == "needs-proof":
                    out[key].append((WARN, field, f"'{w['term']}' is a claim. {w['suggestion']}."))
                elif w["type"] == "terminology":
                    out[key].append((WARN, field, f"use '{w['suggestion']}' instead of '{w['term']}'."))
        for c in CLAIM.findall(text):
            if c.replace(" ", "").lower() not in claims:
                out[key].append((ERROR, field, f"'{c}' isn't an approved proof point. Add a source and get approval, or remove it."))
        if channel == "email" and field == "subject":
            if re.search(r"\b[A-Z]{4,}\b", text):
                out[key].append((WARN, field, "has a word in ALL CAPS."))
            if text.count("!") > 1:
                out[key].append((WARN, field, "has more than one exclamation mark."))
    for (channel, ad, field), n in counts.items():
        rule = limits.get((channel, field))
        if rule and rule.get("max_count") and n > int(rule["max_count"]):
            out[(channel, ad)].append((ERROR, field, f"{n} {field}s; the most allowed is {rule['max_count']}."))
    ads_by_channel = defaultdict(set)
    for r in rows:
        ads_by_channel[r["channel"].lower()].add(r["ad"])
    for (channel, field), rule in limits.items():
        need = int(rule["min_count"]) if rule.get("min_count") else 0
        for ad in sorted(ads_by_channel.get(channel, ())):
            have = counts.get((channel, ad, field), 0)
            if have < need:
                out[(channel, ad)].append((ERROR, field, f"only {have} {field}(s); at least {need} are required."))
    for r in rows:
        out.setdefault((r["channel"].lower(), r["ad"]), [])
    return dict(out)


def read_copy(path):
    rows = _read(path)
    missing = {"channel", "ad", "field", "text"} - set(rows[0].keys() if rows else [])
    if missing:
        raise ValueError(f"{path} is missing columns: {', '.join(sorted(missing))}")
    return rows
