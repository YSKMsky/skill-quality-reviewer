#!/usr/bin/env python3
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


def parse_frontmatter(skill_md):
    text = skill_md.read_text(encoding="utf-8")
    errors = []
    data = {}
    if not text.startswith("---\n"):
        errors.append("SKILL.md must start with YAML frontmatter")
        return text, data, errors
    end = text.find("\n---\n", 4)
    if end == -1:
        errors.append("SKILL.md frontmatter must close with ---")
        return text, data, errors
    raw = text[4:end]
    if "<" in raw or ">" in raw:
        errors.append("YAML frontmatter contains < or >")
    if yaml:
        try:
            data = yaml.safe_load(raw) or {}
        except Exception as exc:
            errors.append(f"YAML frontmatter is invalid: {exc}")
    else:
        for line in raw.splitlines():
            if ":" in line:
                key, value = line.split(":", 1)
                data[key.strip()] = value.strip()
    return text, data, errors


def main():
    if len(sys.argv) != 2:
        print("usage: audit-skill.py <skill-folder>", file=sys.stderr)
        return 2

    root = Path(sys.argv[1]).resolve()
    errors = []
    warnings = []
    notes = []

    skill_md = root / "SKILL.md"
    if not skill_md.exists():
        errors.append("missing SKILL.md")
        print_report(root, errors, warnings, notes)
        return 1

    text, data, frontmatter_errors = parse_frontmatter(skill_md)
    errors.extend(frontmatter_errors)

    name = str(data.get("name", ""))
    desc = str(data.get("description", ""))
    if not name:
        errors.append("frontmatter missing name")
    if not desc:
        errors.append("frontmatter missing description")
    else:
        if not desc.startswith("Use when"):
            warnings.append("description should start with 'Use when'")
        if "Do not use" not in desc:
            warnings.append("description lacks a negative trigger boundary")
        if len(desc) > 700:
            warnings.append(f"description is long: {len(desc)} characters")

    words = len(re.findall(r"\S+", text))
    if words > 1200:
        warnings.append(f"SKILL.md is long: {words} words")
    else:
        notes.append(f"SKILL.md size OK: {words} words")

    for forbidden in [".DS_Store", "README.md", "CHANGELOG.md", "INSTALLATION_GUIDE.md"]:
        for path in root.rglob(forbidden):
            errors.append(f"forbidden file in skill package: {path.relative_to(root)}")

    referenced = sorted(set(re.findall(r"`((?:references|examples|scripts|assets)/[^`]+)`", text)))
    for ref in referenced:
        if not (root / ref).exists():
            warnings.append(f"referenced resource missing: {ref}")

    if not (root / "references").exists():
        warnings.append("no references directory; acceptable only for very small skills")
    if not any((root / d).exists() for d in ["examples", "references"]):
        warnings.append("no examples or references for progressive disclosure")
    if not list((root / "scripts").glob("*.py")) if (root / "scripts").exists() else True:
        warnings.append("no validation/helper scripts; acceptable only when no deterministic checks are useful")

    gotcha_files = list(root.glob("references/*gotcha*.md")) + list(root.glob("references/*pitfall*.md"))
    if not gotcha_files:
        warnings.append("no gotchas/pitfalls reference found")

    openai_yaml = root / "agents" / "openai.yaml"
    if openai_yaml.exists():
        notes.append("agents/openai.yaml present")
    else:
        warnings.append("agents/openai.yaml missing")

    print_report(root, errors, warnings, notes)
    return 1 if errors else 0


def print_report(root, errors, warnings, notes):
    result = {
        "skill": str(root),
        "errors": errors,
        "warnings": warnings,
        "notes": notes,
    }
    print(json.dumps(result, indent=2, ensure_ascii=False))


if __name__ == "__main__":
    raise SystemExit(main())
