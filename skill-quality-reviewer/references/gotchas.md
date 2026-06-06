# Gotchas

Use this when reviewing a skill starts to drift into generic writing advice or broad code review.

## Review Gotchas

- Do not review ordinary app code with this skill unless the artifact is itself a skill or skill resource.
- Do not treat every missing resource directory as a defect. Scripts, examples, references, and assets are useful only when they support reusable behavior.
- Do not reward long SKILL.md files just because they are comprehensive. Check whether details should move to references or examples.
- Do not rewrite the skill's purpose while reviewing quality. Fix trigger, structure, gotchas, validation, and examples before changing scope.
- Do not score a missing validator as P1 unless deterministic checks are clearly important.

## Editing Gotchas

- Do not add README, changelog, or installation guides inside a skill package.
- Do not put fixed output templates in `SKILL.md` when examples or assets would be cheaper to load conditionally.
- Do not make gotchas generic. They should capture mistakes agents are likely to make.
- Do not make description a marketing summary. It should describe concrete trigger conditions and adjacent-skill boundaries.
- Do not claim validation passed unless a script or concrete review was actually run.
