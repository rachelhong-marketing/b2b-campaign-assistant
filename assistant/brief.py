"""Check a master brief (Markdown) for gaps and conflicts before channel briefs are written from it."""
import re
from datetime import date

PLACEHOLDER = re.compile(r"\[(TBD|TODO|CONFIRM[^\]]*|MISSING[^\]]*)\]|\bTBD\b", re.I)
GAP, CONFLICT = "GAP", "CONFLICT"

REQUIRED_FIELDS = ["campaign name", "product", "launch date", "end date", "owner", "total budget", "primary cta",
                   "primary message", "industries", "company size", "personas", "exclusions"]
REQUIRED_SECTIONS = ["objective", "kpis", "funnel stages", "tactics, budget and owners"]


def parse(text):
    """Return fields, tables and section text from a Markdown brief."""
    fields, tables, sections = {}, {}, {}
    current = None
    rows = []
    for line in text.splitlines():
        h = re.match(r"^##\s+(.+?)\s*$", line)
        if h:
            current = h.group(1).strip().lower()
            sections[current] = []
            continue
        if current is None:
            continue
        sections[current].append(line)
        f = re.match(r"^\s*-\s+\*\*(.+?):\*\*\s*(.*)$", line)
        if f:
            fields[f.group(1).strip().lower()] = f.group(2).strip()
        if line.strip().startswith("|"):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if all(re.fullmatch(r":?-+:?", c) for c in cells if c):
                continue
            tables.setdefault(current, []).append(cells)
    out_tables = {}
    for name, rows in tables.items():
        header = [h.lower() for h in rows[0]]
        out_tables[name] = [dict(zip(header, r + [""] * (len(header) - len(r)))) for r in rows[1:]]
    return fields, out_tables, {k: "\n".join(v).strip() for k, v in sections.items()}


def _money(v):
    num = re.sub(r"[^0-9.]", "", v or "")
    return float(num) if num else None


def _date(v):
    try:
        return date.fromisoformat((v or "").strip())
    except ValueError:
        return None


def check(text):
    """Return a list of (level, where, message)."""
    fields, tables, sections = parse(text)
    out = []

    for f in REQUIRED_FIELDS:
        v = fields.get(f)
        if v is None or not v.strip():
            out.append((GAP, f, "missing."))
    for s in REQUIRED_SECTIONS:
        body = sections.get(s)
        if body is None or not re.sub(r"[|\-\s:]", "", body):
            out.append((GAP, s, "section is missing or empty."))

    for n, line in enumerate(text.splitlines(), start=1):
        for m in PLACEHOLDER.finditer(line):
            out.append((GAP, f"line {n}", f"placeholder {m.group(0)}: {line.strip()[:90]}"))

    for row in tables.get("kpis", []):
        if row.get("kpi") and not row.get("target", "").strip():
            out.append((GAP, "kpis", f"'{row['kpi']}' has no target."))

    for row in tables.get("funnel stages", []):
        for col in ("key asset", "channels", "link"):
            if col in row and not row[col].strip():
                out.append((GAP, "funnel stages", f"{row.get('stage', '?')}: no {col}."))

    launch, end = _date(fields.get("launch date")), _date(fields.get("end date"))
    if launch and end and end < launch:
        out.append((CONFLICT, "dates", f"end date {end} is before launch date {launch}."))

    tactics = tables.get("tactics, budget and owners", [])
    total = 0.0
    for row in tactics:
        name = row.get("tactic", "?")
        if "owner" in row and not row["owner"].strip():
            out.append((GAP, "tactics", f"{name}: no owner."))
        amount = _money(row.get("budget"))
        if amount is None:
            out.append((GAP, "tactics", f"{name}: no budget."))
        else:
            total += amount
        start, stop = _date(row.get("start")), _date(row.get("end"))
        if launch and start and start < launch:
            out.append((CONFLICT, "tactics", f"{name} starts {start}, before the campaign launches ({launch})."))
        if end and stop and stop > end:
            out.append((CONFLICT, "tactics", f"{name} ends {stop}, after the campaign ends ({end})."))
        if start and stop and stop < start:
            out.append((CONFLICT, "tactics", f"{name} ends before it starts."))
    budget = _money(fields.get("total budget"))
    if tactics and budget is not None and abs(total - budget) > 0.5:
        out.append((CONFLICT, "budget", f"tactic budgets add up to ${total:,.0f}, but the total budget is ${budget:,.0f} "
                                        f"(a difference of ${total - budget:+,.0f})."))
    return out
