# Quality Gates

Use these gates to review a skill. Prefer findings that explain how a future agent would misbehave.

## 1. Trigger Description

The description is the trigger surface.

Good:

- starts with concrete "Use when" conditions
- names artifact types or task contexts
- includes negative boundaries when adjacent skills could conflict
- does not summarize the whole workflow as a shortcut

Bad:

- "Helps with documents"
- broad persona language
- only says what the skill does, not when it should trigger
- no "do not use" boundary for adjacent skills

P1 when the skill may not trigger or may trigger for too many unrelated tasks.

## 2. Progressive Disclosure

The skill should use the file system as context routing.

Good:

- `SKILL.md` stays concise and routes to references/scripts/examples
- resource loading conditions are explicit
- long details live outside `SKILL.md`
- examples and gotchas are separate when they grow

Bad:

- everything is in `SKILL.md`
- references exist but are not mentioned from `SKILL.md`
- reference files are loaded "just in case"
- duplicate rules appear in several places

P1 when context bloat or missing references will change behavior.

## 3. Gotchas

Gotchas are high-signal memory of failure modes.

Good gotchas:

- describe mistakes agents actually make
- are specific and enforceable
- include "do not" or "first check" wording
- protect the lower bound of output quality

Bad gotchas:

- generic advice
- broad taste preferences without concrete failure mode
- long essays
- rules that duplicate common sense

P2 when gotchas are missing but the rest of the workflow is usable.

## 4. Deterministic Validation

Use scripts for checks that should not vary between agents.

Good candidates:

- YAML/frontmatter parse
- required files exist
- description length and trigger wording
- forbidden files such as `.DS_Store` or skill-package `README.md`
- JSON/config validity
- referenced paths exist

Do not script judgment-heavy review. Use scripts to catch structural issues, then use reasoning for design quality.

P1 when fragile package validity depends only on natural-language instructions.

## 5. Workflow Flexibility

A good skill guides without railroading.

Good:

- defines when to skip stages
- distinguishes app-level versus feature-level work
- lets agents proceed on low-risk reversible tasks
- says when to ask the user

Bad:

- always requires the full process
- asks for approval on low-impact details
- turns examples into mandatory rules
- prevents agent judgment

P2 when the skill is correct but unnecessarily slow or token-heavy.

## 6. Examples

Examples show the skill in motion.

Good examples include:

- user says
- agent should
- do not
- expected artifact or verification

Bad examples are too abstract, too long, or only show successful output without failure boundaries.

P2 when agents may understand the rules but struggle to apply them.

## 7. Output And Completion

The skill should define what "done" means.

Good:

- output shape is clear
- verification is named
- skipped work is explicit
- unresolved risks are surfaced

Bad:

- ends with vague summaries
- hides unverified claims
- lacks severity or acceptance criteria

P2 when users receive inconsistent reviews.
