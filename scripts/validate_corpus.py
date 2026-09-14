#!/usr/bin/env python3
"""Zero-dependency integrity gate for the Working Patterns corpus.

The validator checks structural and epistemic-reference integrity. It does not
pretend to determine whether a research claim is true.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"

PATTERN_ID = re.compile(r"^WP-C\d{3}$")
CLAIM_ID = re.compile(r"^WP-C\d{3}-CL\d{2}$")
CASE_ID = re.compile(r"^K\d{2}$")
SOURCE_ID = re.compile(r"^(?:SC\d{3}|S\d{2})$")
STUDY_ID = re.compile(r"^WP-ST\d{3}$")
AI_ID = re.compile(r"^WP-AI\d{3}$")

MATURITY = {"candidate", "documented", "corroborated", "contested", "revised", "retired"}
SCOPE = {"narrow-context", "multi-context", "cross-domain"}
MECHANISM = {"proposed", "plausible", "evidenced", "contested"}
RELATIONS = {"supports", "complicates", "contradicts", "context-only"}

errors: list[str] = []
warnings: list[str] = []


def load(path: Path):
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except Exception as exc:
        errors.append(f"{path.relative_to(ROOT)}: cannot parse JSON: {exc}")
        return {}


def unique(records, key, label):
    seen = set()
    for row in records:
        value = row.get(key)
        if not value:
            errors.append(f"{label}: missing {key}")
            continue
        if value in seen:
            errors.append(f"{label}: duplicate {key} {value}")
        seen.add(value)
    return seen


patterns = load(DATA / "patterns" / "patterns.json").get("patterns", [])
claims = load(DATA / "claims" / "claims.json").get("claims", [])
cases = load(DATA / "cases" / "cases.json").get("cases", [])
sources = load(DATA / "sources" / "sources.json").get("sources", [])
studies = load(DATA / "studies" / "studies.json").get("studies", [])
ai_patterns = load(DATA / "ai-patterns" / "candidates.json").get("patterns", [])
genealogy = load(DATA / "genealogy" / "relations.json").get("relations", [])

pattern_ids = unique(patterns, "pattern_id", "patterns")
unique(claims, "claim_id", "claims")
case_ids = unique(cases, "case_id", "cases")
source_ids = unique(sources, "source_id", "sources")
study_ids = unique(studies, "study_id", "studies")
unique(ai_patterns, "pattern_id", "ai-patterns")
unique(genealogy, "relation_id", "genealogy")

component_ids = set()
for p in patterns:
    pid = p.get("pattern_id", "")
    if not PATTERN_ID.match(pid):
        errors.append(f"pattern: invalid pattern_id {pid!r}")
    if p.get("pattern_maturity") not in MATURITY:
        errors.append(f"{pid}: invalid pattern_maturity {p.get('pattern_maturity')!r}")
    if p.get("evidence_scope") not in SCOPE:
        errors.append(f"{pid}: invalid evidence_scope {p.get('evidence_scope')!r}")
    if p.get("mechanism_status") not in MECHANISM:
        errors.append(f"{pid}: invalid mechanism_status {p.get('mechanism_status')!r}")
    if not p.get("problem"):
        errors.append(f"{pid}: missing problem")
    for c in p.get("components", []):
        cid = c.get("component_id")
        if not cid or not cid.startswith(pid + "-"):
            errors.append(f"{pid}: invalid component_id {cid!r}")
        elif cid in component_ids:
            errors.append(f"duplicate component_id {cid}")
        else:
            component_ids.add(cid)
        if "pattern_maturity" in c and c["pattern_maturity"] not in MATURITY:
            errors.append(f"{cid}: invalid component maturity")
        if "evidence_scope" in c and c["evidence_scope"] not in SCOPE:
            errors.append(f"{cid}: invalid component evidence scope")

for c in claims:
    cid = c.get("claim_id", "")
    pid = c.get("pattern_id")
    if not CLAIM_ID.match(cid):
        errors.append(f"claim: invalid claim_id {cid!r}")
    if pid not in pattern_ids:
        errors.append(f"{cid}: unknown pattern_id {pid!r}")
    if pid and not cid.startswith(pid + "-CL"):
        errors.append(f"{cid}: claim ID does not match pattern {pid}")
    if c.get("relation") not in RELATIONS:
        errors.append(f"{cid}: invalid evidence relation {c.get('relation')!r}")
    for component in c.get("component_ids", []):
        if component not in component_ids:
            errors.append(f"{cid}: unknown component_id {component!r}")
    sid = c.get("source_id")
    if sid is not None and sid not in source_ids:
        errors.append(f"{cid}: unknown source_id {sid!r}")
    kid = c.get("case_id")
    if kid is not None and kid not in case_ids:
        errors.append(f"{cid}: unknown case_id {kid!r}")
    if sid is None and c.get("verification") != "SYN":
        errors.append(f"{cid}: source-less claim must be explicitly synthetic (SYN)")
    if not c.get("locator"):
        errors.append(f"{cid}: missing locator")
    if not c.get("limitations"):
        warnings.append(f"{cid}: no limitation text")

for case in cases:
    kid = case.get("case_id", "")
    if not CASE_ID.match(kid):
        errors.append(f"case: invalid case_id {kid!r}")
    for sid in case.get("source_ids", []):
        if sid not in source_ids:
            errors.append(f"{kid}: unknown source_id {sid!r}")
    if not case.get("limitations"):
        warnings.append(f"{kid}: no limitation text")

for source in sources:
    sid = source.get("source_id", "")
    if not SOURCE_ID.match(sid):
        errors.append(f"source: invalid source_id {sid!r}")
    if not source.get("url"):
        errors.append(f"{sid}: missing URL")
    if source.get("licence_status") is None:
        errors.append(f"{sid}: missing licence_status")

for study in studies:
    stid = study.get("study_id", "")
    if not STUDY_ID.match(stid):
        errors.append(f"study: invalid study_id {stid!r}")
    for sid in study.get("source_ids", []):
        if sid not in source_ids:
            errors.append(f"{stid}: unknown source_id {sid!r}")
    for kid in study.get("case_ids", []):
        if kid not in case_ids:
            errors.append(f"{stid}: unknown case_id {kid!r}")
    if not study.get("independence_notes"):
        warnings.append(f"{stid}: independence_notes empty")

for p in ai_patterns:
    pid = p.get("pattern_id", "")
    if not AI_ID.match(pid):
        errors.append(f"ai-pattern: invalid pattern_id {pid!r}")
    if p.get("pattern_maturity") != "candidate":
        errors.append(f"{pid}: AI research seed must remain candidate until an evidence cycle changes it")
    if p.get("evidence_status") != "research-agenda":
        errors.append(f"{pid}: AI research seed must declare evidence_status=research-agenda")
    for human_id in p.get("human_pattern_links", []):
        if human_id not in pattern_ids:
            errors.append(f"{pid}: unknown human_pattern_link {human_id!r}")

resolvable = source_ids | study_ids
for rel in genealogy:
    rid = rel.get("relation_id", "?")
    for side in ("left", "right"):
        value = rel.get(side)
        if value not in resolvable:
            errors.append(f"{rid}: {side} reference {value!r} is not a source or study ID")
    if not rel.get("decision"):
        errors.append(f"{rid}: missing classification decision")

# The corpus should never silently collapse evidence into a score.
for path in [DATA / "patterns" / "patterns.json", DATA / "claims" / "claims.json"]:
    text = path.read_text(encoding="utf-8")
    if re.search(r'"(?:confidence|evidence|quality)_score"\s*:', text):
        errors.append(f"{path.relative_to(ROOT)}: aggregate evidence/confidence scoring is prohibited in v0.1")

print(
    "Working Patterns integrity gate: "
    f"{len(patterns)} human patterns, {len(claims)} claims, {len(cases)} cases, "
    f"{len(sources)} sources, {len(studies)} studies/syntheses, {len(ai_patterns)} AI candidates, "
    f"{len(genealogy)} genealogy relations"
)
for warning in warnings:
    print(f"WARNING: {warning}")
if errors:
    for error in errors:
        print(f"ERROR: {error}", file=sys.stderr)
    sys.exit(1)
print("OK: corpus references and epistemic enums are internally consistent")
