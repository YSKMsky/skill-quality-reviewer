# Review Examples

## Broad Description

User says:

```text
Review this skill. It helps with frontend work.
```

Finding:

```markdown
**[P1] Description is too broad to trigger reliably**
The description says the skill "helps with frontend work" but does not name concrete trigger conditions or negative boundaries. Future agents may load it for any UI task or miss it when the user asks for design-to-code work.

Fix: Rewrite the description to start with "Use when..." and include concrete contexts plus "Do not use..." boundaries for adjacent design, testing, and backend skills.
```

## Missing Progressive Disclosure

User says:

```text
The SKILL.md is 3000 words and includes API docs, examples, and policy text.
```

Finding:

```markdown
**[P1] SKILL.md contains details that should be progressively disclosed**
The skill forces every triggered task to load examples and API details even when only the routing rules are needed. This increases context cost and makes agents more likely to miss the core flow.

Fix: Keep the core workflow and reference loading map in SKILL.md. Move API details, examples, and gotchas to one-level references.
```

## No Validation Script

User says:

```text
This skill requires JSON output in a fixed schema.
```

Finding:

```markdown
**[P2] Fixed schema is documented but not validated**
The skill asks agents to produce a fixed JSON shape, but there is no script to validate the output. Future agents may produce plausible but invalid JSON.

Fix: Add a small validator script and make the skill run it before claiming completion.
```
