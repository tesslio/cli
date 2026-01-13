# Tessl CLI Non-Interactive Mode Research

**Purpose**: Document what's needed to ensure AI agents can use the Tessl CLI tool in non-interactive mode.

**Research Date**: 2026-01-13

**Slack Thread**: https://tesslio.slack.com/archives/C09T27C7QR2/p1768320103833899

---

## Executive Summary

The Tessl CLI (`@tessl/cli`) already has **partial non-interactive support**, but several commands still require user interaction. To fully support AI agent usage, additional work is needed to ensure all commands can run without prompts.

### Current State

| Status | Description |
|--------|-------------|
| ✅ Already Supported | `--yes` flag exists for `tessl install --project-dependencies` |
| ✅ Already Supported | JSON logs sent to stderr in non-interactive mode |
| ✅ Already Supported | CLI installation no longer blocks in non-interactive shells |
| ✅ Already Supported | Interactive tool picker has been removed |
| ⚠️ Needs Work | `tessl init` has interactive prompts for agent selection |
| ⚠️ Needs Work | `tessl auth` uses WorkOS device flow (browser-based) |
| ⚠️ Needs Work | Some commands prompt for input when parameters are omitted |

---

## Commands Analysis

### 1. `tessl init`

**Current Behavior**: Interactive prompts during initialization
- Prompts user to select: Tessl Framework vs Spec Registry only
- Prompts for agent setup (Cursor, Claude Code, etc.)
- Prompts for MCP configuration

**Non-Interactive Requirements**:
- Add `--framework` / `--no-framework` flag to skip Tessl Framework prompt
- Add `--agent <name>` flag (already exists, needs to be fully non-interactive)
- Add `--skip-agent-setup` flag to skip agent configuration prompts
- Add `--yes` or `--non-interactive` flag for default selections

**Recommended Changes**:
```bash
# Should work without prompts:
tessl init --agent cursor --project-dependencies skip --yes
tessl init --no-framework --skip-agent-setup
```

### 2. `tessl auth`

**Current Behavior**: Uses WorkOS device flow (opens browser)

**Non-Interactive Requirements**:
- Support `TESSL_AUTH_TOKEN` environment variable for CI/CD
- `tessl auth token` command exists for generating API keys
- Need documentation on using tokens in non-interactive environments

**Recommended Changes**:
```bash
# For CI/CD environments:
export TESSL_AUTH_TOKEN=<token>
tessl install --project-dependencies --yes
```

### 3. `tessl install`

**Current Behavior**: Mostly non-interactive
- `--yes` flag available for `--project-dependencies`
- May prompt for tile selection when multiple matches

**Non-Interactive Requirements**:
- Extend `--yes` flag to all install operations
- Add `--select-all` or `--select-first` for tile selection prompts

**Already Working**:
```bash
tessl install --project-dependencies --yes
tessl install tessl/[email protected]  # Explicit version, no prompts
```

### 4. `tessl search`

**Current Behavior**: May prompt to initialize or install after showing results

**Non-Interactive Requirements**:
- Add `--quiet` or `--no-prompt` flag to suppress post-search prompts
- JSON output option for scripting: `--output json`

### 5. `tessl publish`

**Current Behavior**: May prompt for confirmation

**Non-Interactive Requirements**:
- Add `--yes` flag to confirm publish without prompts
- Ensure all required metadata can be passed via CLI flags

### 6. `tessl workspace create`

**Current Behavior**: Prompts for name if omitted

**Non-Interactive Requirements**:
- Make name a required positional argument OR
- Fail with clear error if name not provided (instead of prompting)

### 7. `tessl mcp`

**Current Behavior**: Runs MCP server (already non-interactive)

**Status**: ✅ Already works for AI agents

---

## Recommendations for Full Non-Interactive Support

### Priority 1: Global Non-Interactive Flag

Add a global `--non-interactive` flag that:
- Disables all prompts across all commands
- Uses sensible defaults when decisions are needed
- Fails with clear error messages when required input is missing

```bash
tessl --non-interactive init --agent cursor
```

### Priority 2: Environment Variable

Implement `TESSL_NON_INTERACTIVE=1` environment variable:
- Automatically enables non-interactive mode
- Useful for CI/CD pipelines and agent environments
- Should be detectable: `process.stdout.isTTY` check

```bash
export TESSL_NON_INTERACTIVE=1
tessl init
```

### Priority 3: Extend `--yes` Flag

Extend the existing `--yes` flag to work with all commands:
- Currently only works with `tessl install --project-dependencies`
- Should work with `init`, `publish`, `workspace create`, etc.

### Priority 4: JSON Output Mode

Add `--output json` flag for programmatic parsing:
- Output structured data instead of formatted text
- Essential for AI agents parsing command output
- Errors should also be JSON formatted

```bash
tessl search react --output json
```

### Priority 5: Auth Token Support

Document and improve token-based authentication:
- Clear documentation for `TESSL_AUTH_TOKEN` usage
- Support for `--token` flag as alternative to env var
- Token validation without browser flow

---

## Implementation Checklist

### Code Changes Needed in `tesslio/m`

1. [ ] Add global `--non-interactive` flag to CLI entry point
2. [ ] Add `TESSL_NON_INTERACTIVE` environment variable detection
3. [ ] Extend `--yes` flag to `tessl init`
4. [ ] Add `--skip-agent-setup` flag to `tessl init`
5. [ ] Add `--output json` flag to commands that output data
6. [ ] Ensure all prompts check for non-interactive mode before prompting
7. [ ] Add TTY detection (`process.stdout.isTTY`) as automatic non-interactive trigger
8. [ ] Update error messages to be clear when required input is missing in non-interactive mode
9. [ ] Add `--yes` flag to `tessl publish` and `tessl workspace create`
10. [ ] Document all non-interactive usage patterns

### Testing Requirements

1. [ ] Test all commands in non-TTY environment (pipe output to file)
2. [ ] Test with `CI=true` environment variable set
3. [ ] Test with Docker/containerized environments
4. [ ] Test with AI agent (Claude Code, Cursor) automation

---

## Existing Non-Interactive Patterns to Follow

The CLI already has some non-interactive patterns that can be extended:

### Pattern 1: `--yes` Flag (from `tessl install`)
```typescript
if (options.yes || !process.stdout.isTTY) {
  // Skip prompt, use default
} else {
  // Show interactive prompt
}
```

### Pattern 2: JSON Logging
The CLI already sends JSON logs to stderr in non-interactive mode - this pattern should be extended to command output.

### Pattern 3: TTY Detection
Some commands already check for TTY availability - this should be consistent across all commands.

---

## References

- [Tessl CLI Commands Documentation](https://docs.tessl.io/reference/cli-commands)
- [Tessl Changelog](https://docs.tessl.io/changelog)
- [Quick Start Guide](https://docs.tessl.io/introduction-to-tessl/quick-start-guide-tessl-framework)
- [Tessl GitHub Organization](https://github.com/tesslio)
- [npm package: @tessl/cli](https://www.npmjs.com/package/@tessl/cli)

---

## Notes

- The `tesslio/m` repository (CLI source) is private; this research is based on public documentation and CLI behavior
- Current CLI version: 0.57.2
- Node.js requirement: >= 22.0.0
