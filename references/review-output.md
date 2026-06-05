# Review Output

Use this format for formal skill audits.

## Default Report

```markdown
**Findings**

1. **[P1] <title>**
   <file link if available>
   Why it matters:
   Fix:

2. **[P2] <title>**
   <file link if available>
   Why it matters:
   Fix:

**Verification**

- Ran:
- Not run:

**Recommended Next Step**

<one concrete action>
```

## Severity Examples

P1:

- description is too broad or does not describe trigger conditions
- references are required for correct behavior but not discoverable from `SKILL.md`
- package cannot validate or has malformed frontmatter
- adjacent skill boundaries are absent and likely to cause misrouting

P2:

- missing gotchas section
- no examples for a judgment-heavy workflow
- full workflow is required for narrow tasks
- no deterministic validator for easy structural checks
- metadata is stale

P3:

- naming could be clearer
- report wording could be tighter
- optional config could reduce repeated questions
- examples could cover one more edge case

## Improvement Summary

When edits are made, report:

- files changed
- validations run
- whether global installed copies were synced
- whether commit/push was done or still pending
