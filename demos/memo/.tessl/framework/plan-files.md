# Plan Files

**CRITICAL: Create a plan file EVERY TIME you make a plan:**

1. Create a new plan file in the `plans/` directory at the root of the project.
2. Plan filename format: `YYYY-MM-DD_HH-mm-ss_descriptive-name.plan.md`
   - Example: `2025-08-25_14-37-12_user-authentication.plan.md`
3. Keep the plan file in sync with your own native task tracking tool.
4. Update the plan file IMMEDIATELY after completing EACH task. Do NOT batch updates.

## Plan File Structure

### Format
A plan file is a markdown document (`.plan.md`) that records tasks to achieve a goal, and acts as an audit trail of the plan.

### Components
1. **Header**: Overall goal and any relevant background context
2. **Task List**: Markdown checkboxes for each task
   - `- [ ]` for pending tasks
   - `- [x]` for completed tasks
3. **User Tasks**: Mark with `{ @user }` directive for user-completed tasks
4. **Task Outputs**: Document results as blockquotes after each task

## Rules for Executing Plans with Plan Files

### 1. Task Documentation
After completing each task, document comprehensively:

- **Update status**: Change checkbox from `[ ]` to `[x]`
- **Add output**: Create detailed blockquote on new line after task
- **Document tool calls**: For EVERY tool call (MCP, Bash, Edit, etc.), include:
  - Tool name
  - COMPLETE, VERBATIM parameters (do not summarize), EXCEPTION: do summarize parameters containing file contents
  - Use markdown code blocks for multi-line string parameters (e.g. prompts)
  - Summary of tool output
- **Include every step in the task**: Document every tool call needed to complete the task
- **Use separators**: Add `---` and a newline between multiple tool calls in same task
- **Include full journey**: Document the complete process, including diagnostics and debugging:
  - ALL problems encountered with specific details
  - Each fix attempt and rationale
  - Every diagnostic tool used (exact tool name, summary of parameters and output)
  - Summary of outcome, including initial state (e.g., "7 tests failed out of 12") and final state (e.g., "All 11 tests passing")
- **Always link to project files**: Include markdown links to any created/read/update/deleted project files:
  - link text: file path relative to the project root
  - link href: file path relative to the plan file

### 2. Plan Updates
- Modify the plan and plan file as needed when requirements change
- Add new tasks or remove irrelevant ones
- Document reasons for significant changes

### 3. User Task Handling
For tasks marked with `{ @user }`:

- **Stop immediately**: Present task to user exactly as written
- **Wait for response**: Act on any instructions in user responses
- **Don't assume**: Only complete user tasks when explicitly told the task is done
- **Document accurately**:
  - Record only what actually happened
  - NEVER add details about what the user did unless they explicitly provide those details

## Best Practices
1. Tasks should be:
  - **Specific**: Clear, actionable completion criteria
  - **Atomic**: One logical unit of work per task
  - **Logically Ordered**: Arrange in execution sequence
  - **Well Sized**: Break down complex goals into incremental atomic tasks

2. Add `{ @user }` tasks strategically to:
  - Delegate tasks requiring user action
  - Get feedback at critical decision points

## Example

````markdown
# Plan: Implement User Authentication

Add secure user authentication with email/password login.

## Tasks

- [x] Create user model spec with email, password hash, and timestamps
  > **MCP** `tessl - create`
  > - spec: specs/models/user.spec.md
  > - prompt:
  >   ```
  >   Create a User model with the following fields:
  >   - id: string (UUID)
  >   - email: string (unique, required)
  >   - passwordHash: string (required)
  >   - createdAt: Date
  >   - updatedAt: Date
  >
  >   Include methods for:
  >   - Password hashing and verification using bcrypt
  >   - Email validation
  >   - Safe JSON serialization (excludes passwordHash)
  >   ```
  >
  > Created [specs/models/user.spec.md](../specs/models/user.spec.md)
  > Model spec created successfully with all required fields and methods.

- [x] Build user model from spec
  > **MCP** `tessl - build`
  > - spec: ["specs/models/user.spec.md"]
  >
  > Generated:
  > - [src/models/user.ts](../src/models/user.ts)
  >
  > Build completed successfully, no errors.
  > ---
  >
  > **Bash** `npm run build`
  > Build failed with TypeScript errors: missing import extensions
  > ---
  >
  > **Edit** `src/models/user.ts`
  > - old_string: import { SomeType } from './types'
  > - new_string: import { SomeType } from './types.js'
  >
  > Updated [src/models/user.ts](../src/models/user.ts).
  > Fixed import to include .js extension for ESM compatibility.
  > ---
  >
  > **MCP** `tessl - document`
  > - spec: specs/models/user.spec.md
  > - includeImplDetails: true
  >
  > Synced [code](../src/models/user.ts) behavior to [spec](../specs/models/user.spec.md)

- [ ] Add database migration for users table
- [ ] Create authentication service spec
- [ ] Implement login endpoint
- [ ] Add session management
- [ ] Test authentication flow { @user }
````