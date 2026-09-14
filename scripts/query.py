#!/usr/bin/env python3
"""Tiny, zero-dependency browser for the Working Patterns corpus.

This is intentionally not a recommender. It exposes records and evidence links.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data"


def load(rel):
    return json.loads((DATA / rel).read_text(encoding="utf-8"))


def dump(value):
    print(json.dumps(value, indent=2, ensure_ascii=False))


def main():
    parser = argparse.ArgumentParser(description="Inspect the Working Patterns research corpus")
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("list", help="List human patterns")
    p = sub.add_parser("pattern", help="Show a pattern and its claims")
    p.add_argument("id")
    c = sub.add_parser("claim", help="Show one claim")
    c.add_argument("id")
    a = sub.add_parser("ai", help="Show a Pyragogy AI candidate")
    a.add_argument("id")
    s = sub.add_parser("source", help="Show one source")
    s.add_argument("id")
    args = parser.parse_args()

    patterns = load("patterns/patterns.json")["patterns"]
    claims = load("claims/claims.json")["claims"]
    sources = load("sources/sources.json")["sources"]
    ai = load("ai-patterns/candidates.json")["patterns"]

    if args.cmd == "list":
        for row in patterns:
            print(f"{row['pattern_id']}\t{row['pattern_maturity']}\t{row['name']}")
        return
    if args.cmd == "pattern":
        record = next((r for r in patterns if r["pattern_id"] == args.id), None)
        if not record:
            raise SystemExit(f"unknown pattern: {args.id}")
        linked = [c for c in claims if c["pattern_id"] == args.id]
        dump({"pattern": record, "claims": linked})
        return
    if args.cmd == "claim":
        record = next((r for r in claims if r["claim_id"] == args.id), None)
        if not record:
            raise SystemExit(f"unknown claim: {args.id}")
        dump(record)
        return
    if args.cmd == "ai":
        record = next((r for r in ai if r["pattern_id"] == args.id), None)
        if not record:
            raise SystemExit(f"unknown AI candidate: {args.id}")
        dump(record)
        return
    if args.cmd == "source":
        record = next((r for r in sources if r["source_id"] == args.id), None)
        if not record:
            raise SystemExit(f"unknown source: {args.id}")
        dump(record)


if __name__ == "__main__":
    main()
