#!/usr/bin/env python3
"""Parse docs/ttp-matrix.md -> evidence/coverage.json (MITRE/NIST/SOC2 coverage)."""
import json, re, sys
from pathlib import Path

def parse_matrix(path: Path) -> list:
    rules = []
    for line in path.read_text().splitlines():
        m = re.match(r"^\|\s*(T\d[\d.]*)\s*\|", line)
        if not m: continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) >= 5:
            rules.append({"ttp": m.group(1), "technique": cells[1],
                          "rule": cells[2], "data_source": cells[3], "severity": cells[4]})
    return rules

def main():
    args = sys.argv[1:]
    matrix = Path(args[args.index("--matrix")+1] if "--matrix" in args else "docs/ttp-matrix.md")
    out = Path(args[args.index("--out")+1] if "--out" in args else "evidence/coverage.json")
    rules = parse_matrix(matrix)
    report = {
        "generated": __import__("datetime").datetime.utcnow().isoformat(),
        "total_rules": len(rules),
        "ttps_covered": sorted({r["ttp"] for r in rules}),
        "severity_counts": {s: sum(1 for r in rules if r["severity"].lower() == s)
                            for s in ("critical", "high", "medium", "low")},
        "rules": rules,
    }
    out.parent.mkdir(exist_ok=True)
    out.write_text(json.dumps(report, indent=2))
    print(f"Coverage report -> {out} ({len(rules)} rules, {len(report['ttps_covered'])} TTPs)")

if __name__ == "__main__":
    main()
