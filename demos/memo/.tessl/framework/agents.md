# Tessl

Tessl is a [spec driven development](./docs/spec-driven-development.md) framework and toolkit: @docs/spec-driven-development.md

## Spec Driven Software Development Lifecycle

### User Engagement

Users should be encouraged to engage directly with specs, so that they understand what is being asked for (or documented), and can steer the software development processes.

In order to do this, agents should:

1. Interview the user to get details before creating or updating specs (but ask one or two questions at a time, so as not to overwhelm them).
2. Ask for feedback on specs before building them. This should include pointing out key implementation choices, and highlighting any gaps in the spec.
3. Include interview/feedback points as separate tasks in plans, so these steps are not skipped.

### Primary Workflow: Spec to code

Software is developed by creating or editing a spec and then `building` that spec to generate or update the implementation and then `fixing` to refine the spec and implementation until it works as intended.

1. Create/edit the spec to reflect the desired functionality/changes requested, using the appropriate Tessl tool and providing it with relevant context (see the "Using Tessl Tools" instructions below)
2. Install any new required dependencies from the spec
3. Build the spec to generate the implementation code from the updated spec and fix
4. When/if the user asks for tests, add them to the spec and generate them and fix.

### Alternative Workflow: Code to spec

Sometimes the user may decide to change the code directly, or they may have legacy code they want to document. In such cases:

1. Document the code changes into the spec + fix spec/tests to match observed code behaviors
2. If the spec is changed, flag any capabilities that are lost or changed.

### Using Tessl Tools

Tessl tools allow targeted changes to spec, code and test files ensuring that the methodology is followed, and that the correct context is provided at each step.

Before using any Tessl tool (`create`, `edit`, `build`, `document` etc) you must:

1. **First: Check Knowledge Index:**

   - Read `./KNOWLEDGE.md` (the Knowledge Index)
   - Consider the Tessl tool call you're about to make, including any parameters
   - Decide if any entries in the Knowledge Index seem directly relevant to the current task
   - If so, spawn a research sub-agent to dig deeper into the chosen documents
   - If not, skip research and just call the tool

2. **Research context** - Spawn a research sub-agent with details about:

   - The Knowledge Index candidates to explore
   - The specific Tessl tool you're about to call
   - The inputs to that tool call (what you're building, which files, etc.)

3. **Research sub-agent identifies relevant context file paths:**

   - Explore the provided Knowledge Index entries
   - **Return**: Only relevant file paths (relative to the project root)

4. **Then: Call the Tessl tool** - Use the file paths returned by the research sub-agent (relative to project root) in the `--context` parameter.

Remember the research output and re-use it for similar tool calls (where the tool and inputs are the same).

Use Tessl tools to:

- Capture requirements for new code files in specs using the `create` tool
- Edit specs / code / tests whenever the user wants to introduce or change behavior in existing specs / code / tests with the `edit` tool
- Build code and tests from specs using the `build` and `build-tests` tools
- Document code into specs using the `document` tool
- Run tests using the `test` tool
- Add extra functionality to code, by editing the spec and rebuilding
- Check project and spec status using the `status` tool

Tessl also provides the capability to run its tools in parallel. Use this when you have multiple tasks to do that are independent of each other - e.g. rebuilding multiple specs at once.

### Detailed Expectations Around Fixing Code and Tests:

A key concept in spec-driven development is that built code and tests should be run to verify conformity to the spec. Often, however, working code and useful tests are not made on the first attempt. 

Tessl tools will attempt to 'fix' before finishing build, but agents may need to continue or debug this process. 

By default, the spec will have few if any test cases to start with, focus on getting the functionality working and then if the user asks for more tests, add them to the spec and generate them.

Tests should be prioritised in the following order:
- Locked tests.  Make sure the code is able to pass these tests, they are core functional requirements that have been confirmed by the user.
- Draft tests.  If draft tests have been generated, try to make the code pass. These tests have not been fully validated, so their definition or implementation may need to be refined until useful or removed altogether.
- Impl tests.  If generated, then try to make the code pass.  These tests were created to capture details in an implementation that may not be important, so they may be deleted if they are no longer valid.

Fixes should be applied in this preference order:
1. (Preferred fix): Install dependencies explicitly listed in the spec if needed.
2. (Preferred fix): Iteratively run tests and update code to address errors, until the code passes the tests.
3. (Cautious fix): Iteratively fix implementation errors in tests (e.g. syntax errors) and check they are still faithful to the spec.
4. (Last resort): Identify if the spec contains errors, ambiguities or hard to implement definitions. Ask the user for how to proceed.

**Never** simply remove requirements from the spec.
**Never** add new capabilities to the code without updating the spec to capture how it will be verified.

**Setup/Configuration errors**
It's possible the error stems from the overall project set up, in this case:

- Ask the user to add dependencies to the spec if they are implied or necessary for the capabilities required.
- Help the user configure their project further and make sure that their development environment is working.
- Make sure that project details like the language(s), test runner(s) and ecosystem(s), and any testing or implementation guidelines are added to AGENTS.md to help guide the Tessl tools to produce consistent implementations that adhere to them.

### Software Decomposition

Specs should map 1:1 with code files, with the structure of the specs and the links between them matching the intended decomposition of the software.

If the user asks for new functionality that would be challenging to fit into a single spec and code file, then you should first suggest decomposition approaches with them, and then make a plan to iteratively build up the software spec by spec.

Make sure that specs link to each other as needed, and that there is a clear entry-point.

**Pointers:**

- Prefer to work in an incremental way, building up the software one piece at a time, improving the software with each iteration. Suggest a simple starting point, and include tasks in your plan to add additional features one by one later.
- Check generated specs to make sure that they link to one another via "dependencies" links, and if not, call edit spec and ask for the dependency to be added.
- Add more details on project expectations to AGENTS.md if you need more consistency in the project across specs - for example, on choices on key external dependencies, or testing guidelines.
- Make sure the user provides explicit feedback and approval before deciding on a decomposition and beginning to create multiple specs and building them all.

## The Knowledge Index

The Knowledge Index is a centralized reference for documentation about dependencies and processes used in the project.

It's stored in `./KNOWLEDGE.md` and contains links to versioned documentation files.

The Knowledge Index helps ensure consistency when selecting dependency versions and provides quick access to relevant documentation during development.

## Important

Always modify code, tests or specs using Tessl tools. The only exceptions are when the user approves this behavior interactively. In either case **specs and generated code and tests must be always in sync**