#!/usr/bin/env python3
"""Subrosa repo validator — enforces the suite's own integrity rules.

Checks (stdlib only, no dependencies):
  1. Cross-references: every backticked `*.md` path in README, skills/, and
     taxonomy/ must resolve — repo-relative, file-relative, or (inside a
     skill) skill-root-relative, per the suite's path conventions.
  2. Skill frontmatter: every skills/<name>/SKILL.md carries YAML frontmatter
     with `name:` matching its directory and a non-empty `description:`.
  3. Currency Protocol: every taxonomy record carries a `Current as of` date
     (derived artifacts, stubs, and HISTORICAL records are exempt); records
     older than one quarter are reported as STALE (warning — statutes rot,
     builds shouldn't break by clock).
  4. [UNVERIFIED] census: per-file counts, reported for drift tracking.

Exit 1 on structural failures (broken refs, bad frontmatter, missing
Current-as-of). Staleness and the census are informational.
"""
import datetime
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
REF = re.compile(r"`([A-Za-z0-9._/-]+\.md)`")
STALE_DAYS = 92  # one quarter, per the Currency Protocol
CURRENCY_EXEMPT = {  # derived artifacts, stubs, historical records
    "regulatory-taxonomy--floor.md",
    "regulatory-taxonomy--conflicts.md",
    "regulatory-taxonomy--arch-rollup.md",
    "regulatory-taxonomy--stubs.md",
    "regulatory-taxonomy--vn-pdpd.md",
}

failures: list[str] = []
warnings: list[str] = []


def check_references() -> int:
    checked = 0
    files = [ROOT / "README.md", ROOT / "NAMING.md"]
    files += sorted(ROOT.glob("skills/**/*.md")) + sorted(ROOT.glob("taxonomy/*.md"))
    for md in files:
        rel = md.relative_to(ROOT)
        for m in REF.finditer(md.read_text()):
            ref = m.group(1)
            if "*" in ref:
                continue
            candidates = [ROOT / ref, md.parent / ref]
            if ref.startswith("--"):  # taxonomy sibling shorthand
                candidates.append(md.parent / ("regulatory-taxonomy" + ref))
            if rel.parts[0] == "skills":  # skill-root-relative convention
                candidates.append(ROOT / rel.parts[0] / rel.parts[1] / ref)
            checked += 1
            if not any(c.exists() for c in candidates):
                failures.append(f"broken ref in {rel}: `{ref}`")
    return checked


def check_frontmatter() -> int:
    n = 0
    for skill_dir in sorted((ROOT / "skills").iterdir()):
        if not skill_dir.is_dir():
            continue
        n += 1
        skill = skill_dir / "SKILL.md"
        if not skill.exists():
            failures.append(f"{skill_dir.name}: missing SKILL.md")
            continue
        head = skill.read_text().split("---")
        if len(head) < 3:
            failures.append(f"{skill_dir.name}: no frontmatter block")
            continue
        fm = head[1]
        name = re.search(r"^name:\s*(\S+)", fm, re.M)
        desc = re.search(r"^description:\s*(.+)", fm, re.M)
        if not name or name.group(1) != skill_dir.name:
            failures.append(f"{skill_dir.name}: frontmatter name mismatch")
        if not desc or not desc.group(1).strip():
            failures.append(f"{skill_dir.name}: missing description")
    return n


def check_currency() -> int:
    today = datetime.date.today()
    n = 0
    for rec in sorted(ROOT.glob("taxonomy/regulatory-taxonomy--*.md")):
        if rec.name in CURRENCY_EXEMPT:
            continue
        n += 1
        text = rec.read_text()
        line = next((l for l in text.splitlines() if "urrent as of" in l), None)
        if line is None:
            failures.append(f"{rec.name}: no 'Current as of' header (Currency Protocol rule 1)")
            continue
        m = re.search(r"20\d\d-\d\d-\d\d", line)
        if not m:
            failures.append(f"{rec.name}: 'Current as of' has no parseable date")
            continue
        age = (today - datetime.date.fromisoformat(m.group(0))).days
        if age > STALE_DAYS:
            warnings.append(f"STALE ({age}d): {rec.name} — re-check before advisory use")
    return n


def census() -> None:
    total = 0
    rows = []
    for md in sorted(ROOT.glob("taxonomy/*.md")):
        c = md.read_text().count("[UNVERIFIED")
        if c:
            rows.append((c, md.name))
            total += c
    print(f"[UNVERIFIED] census: {total} flags in {len(rows)} files")
    for c, name in sorted(rows, reverse=True)[:5]:
        print(f"  {c:3d}  {name}")


def main() -> int:
    print(f"references checked: {check_references()}")
    print(f"skills checked:     {check_frontmatter()}")
    print(f"records checked:    {check_currency()}")
    census()
    for w in warnings:
        print(f"WARN: {w}")
    if failures:
        print(f"\nFAILURES ({len(failures)}):")
        for f in failures:
            print(f"  {f}")
        return 1
    print("\nOK — all structural checks pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
