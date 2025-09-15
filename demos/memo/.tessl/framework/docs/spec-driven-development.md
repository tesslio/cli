# Spec Driven Development (SDD)

Spec driven development places specs at the center of the software development lifecycle. Specs are considered the canonical source of truth when they are verifiable. Code is considered disposable when it can be reliably regenerated from a spec.

Specs capture _intent_, and may contain or link to files containing the API and test cases. Over time specs are updated to add new features or requirements, and code is regenerated to align with the specs.

Each spec usually maps 1:1 to a code file. Larger units are composed of multiple linked specs (via dependencies), mirroring decomposition. A linked set of specs with their code and tests is a **tile** or **Tessl tile**. Projects may contain multiple tiles.

## Specs

- Follow the [Spec Format](./spec-format.md)
- Used to capture all user intent
- MUST NOT be modified without explicit user instruction or review
- Together reflect the expected software decomposition with local spec dependencies mirroring targeted local code files, and with links to external dependencies

## Code

- Follow language and ecosystem requirements specified in AGENTS.md, and APIs and requirements in spec
- Can be edited or rebuilt by tools or agents
- Makes good use of dependencies explicitly linked in spec - following dependency APIs if provided and without reimplementing functionality
- Doesn't use dependencies not explicitly listed in the spec

## Tests

- Follow the test runner requirements specified in AGENTS.md
- Can be edited or rebuilt by tools or agents
- Each test implements exactly one test definition from the spec, and only verifies that exact case
- Assumes code complies exactly with the defined APIs
- Can be tagged to indicate prioritization: draft (default), locked, impl