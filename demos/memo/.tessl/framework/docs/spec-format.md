# Spec Format

Specs are markdown files with some annotations for parsing. Typically one spec is written for each module.

They can contain the following sections, empty sections can be omitted:

- Name.
  - Short overview to explain overall purpose.
- Target.
  - Relative link to the code file this spec targets.
- Capabilities.
  - Headings for each capability with an optional description.
    - List of test definitions for each capability, with relative links to the test files where they will be implemented.
- API.
  - Description of the module's API that code and tests will be written to conform to.
- Dependencies.
  - List of dependencies the spec has on other modules and external libraries.

A further explanation of each is provided below.

## Target

Should contain a relative link to the code file that will contain the code this spec targets. This can be one of two flavors:

- [@generate](./relative/path/to/code/file) or
- [@describe](./relative/path/to/code/file)

@generate is used where the spec is the primary artifact and the linked code will be generated (and regenerated) from the spec. This is the default.
@describe is used to provide a wrapper to an existing code file, where the code is the primary artifact. This is provided to allow the spec to act as a reference material. The spec will be updated to match code changes.

A spec may contain multiple links if multiple code files are generated from or described by the spec, but it is best practice to have one spec for one code file.

## Capabilities

List of capabilities of the module.

Each capability:

- Should be precise and concise.
- Should explicitly describe the _intent_ of the capability, rather than describing the approach.
- Can optionally have a short description under the title to explain the capability in more detail.

Each capability should be followed by a list of requirements.

Each requirement:

- Should be concise, precise and opinionated on specific behaviors.
- Can cover internal logic or external behavior.
- Requirements can be converted into test cases by adding a corresponding [@test](./relative/path/to/test/file) annotation.  Test cases must have clearly defined inputs and outputs, as well as setup/mocking notes if needed.

Example:

```markdown
Reverses any string. Preserves capitalization and whitespaces during reversal.

- "hello" becomes "olleh" [@test](./relative/path/to/test/file)
- "Hello, world!" becomes "!dlrow ,olleH" [@test](./relative/path/to/test/file_impl) { .impl }
```

## API

- Describe the external interface for the module, including function signatures and parameters with types.
- Must be wrapped in code block with a language identifier, with an { .api } tag on the block.
- Should be an appropriate format for the language, and should be consistent with any project configuration provided.

## Dependencies

List of dependencies on other specs, files or external libraries that the module is expected to have. No other dependencies should be assumed, unless explicitly specified in the project configuration or in a user goal. Links can either be to the spec for the module if available, or directly to the code itself if the spec is not available.

- Each lists what is expected from the dependency and has a link to the dependency.
- New dependencies should only be added when explicitly requested by the user.

- The whole section can be skipped if there are no requirements.
- Each requirement should have a @use link.
- For local dependencies, the link will be a relative path, for example [@use](./relative/path/to/dependency-spec)
- For external dependencies a package name will be used, for example [@use](package-name)
- For code dependencies, the link will be a relative path, for example [@use](./relative/path/to/code-file).

Example dependencies:

```markdown
# Dependencies

## Code Dependency Example

Description of the requirements for the module.
[@use](./relative/path/to/code-file)

## Spec Dependency Example

Description of the requirements for the module.
[@use](./relative/path/to/dependency-spec)

## External Dependency Example

Description of the requirements for the module.
[@use](package-name)
```

## Content tags

Sections of the spec can be annotated with tags to explain the prioritization and level of editing that is appropriate.  They are most often used for annotating specific tests.

Rules for applying tags:
- By default, do not add tags.
- Tags applied to a section will apply to all tests in the section.
- Tests must not have more than one kind. e.g: you should not have a test marked as `impl` and `locked`, or a section marked with both `impl` and a test marked with `locked`.
- Tests files must not mix test kinds. e.g: you should not have untagged and `locked` tests in the same test file.
- Locked content must never be edited unless instructed to do so by the user.
- Content must never be tagged as locked unless explicitly requested by the user.

### Untagged (default)

Untagged content is the standard and is considered draft.

Untagged test cases 
- **Purpose**: Regular test cases that can be modified during development as necessary.
- **Annotation**: No special class required (default behavior)
- **Priority**: Medium priority, they can be changed during the development flow as the spec is refined

Example:
```markdown
- "hello" becomes "olleh" [@test](./relative/path/to/test/file)
```


### Locked { .locked }

Locked tags capture core functional requirements that should remain stable over time. They represent critical test cases that define the essential behavior of the module that have been confirmed by the user.

- **Purpose**: Capture core functional requirements that should remain stable over time
- **Annotation**: `{ .locked }` class on individual tests or section headers
- **Priority**: High priority, they are applied deliberately by the user after reviews have been completed.

Examples:
```markdown
- "hello" becomes "olleh" [@test](./relative/path/to/test/file) { .locked }

### Core functionality { .locked }
- "test1" becomes "1tset" [@test](./relative/path/to/test/file1)
- "test2" becomes "2tset" [@test](./relative/path/to/test/file2)
```

### Implementation { .impl }

Implementation tags are used to mark incidental implementation by-products rather than user-specified capabilities. They have lower priority and can be changed more freely.

- **Purpose**: Cover implementation details that were not explicitly specified by the user.
- **Annotation**: `{ .impl }` class on individual tests or section headers
- **Priority**: Lower priority, they should be more freely changed if user requirements change.

Examples:
```markdown
- "Hello" becomes "olleH" [@test](./relative/path/to/test/file) { .impl }

### Implementation details { .impl }
- Edge case behavior [@test](./relative/path/to/test/file1)
- Performance characteristics [@test](./relative/path/to/test/file2)
```


## Example spec (with placeholders for the api details)

````markdown
# String Reverser

String reverser. Switches the order of characters in a string.

## Target

[@generate](./relative/path/to/code/file)

## Capabilities

### Reverses a string.

- "hello" becomes "olleh" [@test](./relative/path/to/test/file1)
- "iPhone 5 Samsung" becomes "gnusmaS 5 enohPi" [@test](./relative/path/to/test/file2)

### Reverses within a delimiter.

Delimiter is optional, but if provided, reversing only happens between each delimited block, with block order preserved.

- ("hello friend", " ") becomes "olleh dneirf" [@test](./relative/path/to/test/file4)

### Efficient implementation

- Uses a single pass buffer approach.
- Doesn't modify the original string.


## API

```{{LANGUAGE}} { .api }

{{API_CODE}}

```

````