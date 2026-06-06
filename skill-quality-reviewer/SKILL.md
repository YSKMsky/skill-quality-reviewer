---
name: skill-quality-reviewer
description: Use when reviewing, scoring, debugging, or improving a Codex/Claude-style skill folder, especially when checking trigger descriptions, progressive disclosure, gotchas, deterministic validation scripts, examples, workflow flexibility, or whether a skill is overbroad, overlong, or likely to mis-trigger. Do not use for normal code review unless the artifact under review is a skill.
---

# Skill Quality Reviewer

## Overview

Review skills as reusable operating systems, not prompt prose. Focus on whether another agent can trigger the skill correctly, load the right context cheaply, avoid known mistakes, validate fragile requirements deterministically, and produce a useful next action.

## First Action

1. Identify the target skill folder or `SKILL.md`.
2. Inspect the target file tree, `SKILL.md`, and `agents/openai.yaml` if present.
3. Read only the target references needed to explain a finding. Do not bulk-load every reference.
4. Run `scripts/audit-skill.py` with the target skill folder when local filesystem access is available.
5. If the user asks for improvements, make focused edits and rerun deterministic checks.
6. End with findings grouped by severity, verification run, and the smallest useful next step.

## Quality Gates

Read `references/quality-gates.md` when doing a full review or when deciding whether a problem is P1/P2/P3.

The high-signal gates are:

- Trigger description: clear "when to use", concrete contexts, and negative boundary.
- Progressive disclosure: concise `SKILL.md`, detailed references/examples/scripts loaded only when needed.
- Gotchas: concentrated record of mistakes agents actually make.
- Deterministic validation: scripts for checks that should not depend on natural-language memory.
- Workflow flexibility: enough structure to guide, not so much that it railroads narrow tasks.
- Examples: concrete user input, expected agent behavior, and "do not" cases.

## Review Workflow

1. Classify the review:
   - quick triage: inspect `SKILL.md`, file tree, and validator output
   - full audit: also inspect relevant references, examples, scripts, and metadata
   - improvement pass: edit the skill, run validation, and summarize the diff
2. Check the description first. A weak description can make the rest of the skill invisible or over-triggered.
3. Check structure next. `SKILL.md` should route to resources, not contain every detail.
4. Check gotchas and examples. They should capture non-obvious failure modes, not generic advice.
5. Check validation. Fragile requirements should be enforced by scripts where practical.
6. Check output behavior. The skill should tell agents what to produce, what to skip, and how to prove completion.
7. If editing, make the smallest changes that fix the observed failure mode.

## Severity

- P1: likely to prevent correct triggering, cause major overuse, hide critical context, or make the skill unreliable.
- P2: likely to waste tokens, create inconsistent behavior, or make future maintenance harder.
- P3: polish, naming, organization, or optional improvements that do not block usefulness.

## Output Format

Read `references/review-output.md` when the user asks for a formal review report.

Default shape:

- Findings first, grouped by severity.
- Each finding names the file/line when available.
- Each finding explains why it matters for future agent behavior.
- Then list concrete fixes, verification, and remaining risk.

## Self-Review Rule

When creating or modifying a skill, review the changed skill with this skill before claiming completion:

- Run deterministic validation when a script exists.
- Check whether the description is a trigger, not a summary.
- Check whether new details belong in references/examples/scripts instead of `SKILL.md`.
- Add or update gotchas only when they capture real failure modes.
- Report anything intentionally not fixed.

## Resources

- `scripts/audit-skill.py`: deterministic structural audit for a skill folder.
- `references/quality-gates.md`: detailed scoring standards.
- `references/gotchas.md`: common mistakes when reviewing or editing skills.
- `references/review-output.md`: report format and severity examples.
- `examples/review-examples.md`: compact review examples.
