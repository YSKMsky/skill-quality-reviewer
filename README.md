# Skill Quality Reviewer

Codex skill for auditing and improving other skills against reusable quality gates: trigger descriptions, progressive disclosure, gotchas, validation scripts, examples, and workflow flexibility.

## What This Is

`skill-quality-reviewer` is a meta-skill for reviewing Codex/Claude-style skill folders.

It treats a skill as a reusable operating system for future agents, not as prompt prose. The goal is to identify whether another agent can trigger the skill correctly, load only the context it needs, avoid known mistakes, validate fragile requirements, and produce useful findings or improvements.

## When To Use It

Use this skill when you want to:

- review a new or existing skill folder
- check whether a skill description triggers correctly
- find overbroad, overlong, or under-specified skill instructions
- audit progressive disclosure across `SKILL.md`, `references/`, `examples/`, `scripts/`, and `assets/`
- identify missing gotchas or weak failure-mode coverage
- decide whether deterministic validation scripts are needed
- improve a skill without turning it into a long prompt
- self-review a skill while creating or editing it

Do not use it for normal code review unless the artifact under review is itself a skill.

## Core Quality Gates

The reviewer checks seven high-signal gates:

1. **Trigger description**
   - The description should say when the skill should trigger.
   - It should include concrete contexts and negative boundaries.

2. **Progressive disclosure**
   - `SKILL.md` should stay concise.
   - Details should live in references, examples, scripts, or assets and be loaded only when needed.

3. **Gotchas**
   - A good skill records the mistakes agents are likely to make.
   - Gotchas should be specific, actionable, and based on real failure modes.

4. **Deterministic validation**
   - Structural checks should be scripted when possible.
   - YAML, required files, referenced paths, JSON config, and forbidden files should not depend on memory.

5. **Workflow flexibility**
   - The skill should guide agents without forcing every task through the full process.
   - Narrow tasks should be able to skip irrelevant stages.

6. **Examples**
   - Examples should show user input, expected agent behavior, and "do not" cases.
   - They help future agents apply rules in realistic situations.

7. **Output and completion**
   - The skill should define what a good result looks like.
   - It should name verification, skipped work, and unresolved risks.

## Skill Structure

```text
skill-quality-reviewer/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── examples/
│   └── review-examples.md
├── references/
│   ├── gotchas.md
│   ├── quality-gates.md
│   └── review-output.md
└── scripts/
    └── audit-skill.py
```

## Review Workflow

The default review flow is:

```text
Identify target skill
→ Inspect SKILL.md and file tree
→ Run deterministic audit script
→ Check description and loading structure
→ Check gotchas, examples, and validation
→ Report findings by severity
→ Apply focused improvements if requested
→ Re-run validation
```

## Severity Model

Findings use three severity levels:

| Severity | Meaning |
| --- | --- |
| P1 | Likely to prevent correct triggering, cause major overuse, hide critical context, or make the skill unreliable. |
| P2 | Likely to waste tokens, create inconsistent behavior, or make future maintenance harder. |
| P3 | Polish, naming, organization, or optional improvements that do not block usefulness. |

## Deterministic Audit

Run the audit script against a skill folder:

```bash
skill-quality-reviewer/scripts/audit-skill.py path/to/skill-folder
```

The script checks:

- `SKILL.md` exists
- YAML frontmatter is parseable
- `name` and `description` exist
- description starts with `Use when`
- description includes a negative trigger boundary
- `SKILL.md` length is reasonable
- referenced resources exist
- forbidden files are absent
- gotchas/pitfalls reference exists
- `agents/openai.yaml` exists

Example:

```bash
skill-quality-reviewer/scripts/audit-skill.py ios-app-workflow
```

Output is JSON with `errors`, `warnings`, and `notes`.

## Example Finding

```markdown
**[P1] Description is too broad to trigger reliably**

The description says the skill "helps with frontend work" but does not name concrete trigger conditions or negative boundaries. Future agents may load it for unrelated UI work or miss it when design-to-code work is requested.

Fix: Rewrite the description to start with "Use when..." and include concrete contexts plus "Do not use..." boundaries for adjacent design, testing, and backend skills.
```

## Installation

Copy the skill folder into your Codex skills directory:

```bash
~/.codex/skills/skill-quality-reviewer
```

Then invoke it explicitly:

```text
Use $skill-quality-reviewer to review this skill folder and identify triggering, progressive disclosure, gotchas, validation, and workflow issues.
```

## Suggested GitHub Description

```text
Codex skill for auditing and improving other skills against reusable quality gates: triggers, progressive disclosure, gotchas, validation, examples, and workflow flexibility.
```
