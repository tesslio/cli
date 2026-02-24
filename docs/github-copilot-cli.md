# Using Tessl with GitHub Copilot CLI

This guide covers how to install and use Tessl tiles with [GitHub Copilot CLI](https://github.com/github/copilot-cli).

## Prerequisites

- [GitHub Copilot CLI](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli) installed and authenticated
- [Tessl CLI](https://get.tessl.io) installed

## Quick Start

### 1. Install Tessl

```sh
curl -fsSL https://get.tessl.io | sh
```

### 2. Initialize Tessl for GitHub Copilot CLI

In your project directory, run:

```sh
tessl init --agent copilot-cli
```

This creates the necessary configuration files that GitHub Copilot CLI will automatically discover and use.

### 3. Install Tiles

Install tiles from the [Tessl Registry](https://tessl.io/registry):

```sh
tessl install <tile-name>
```

For example:
```sh
tessl install react
tessl install typescript
tessl install tessl-labs/spec-driven-development
```

## How It Works

When you run `tessl init --agent copilot-cli`, Tessl creates:

1. **`.tessl/` directory** - Contains installed tile content (skills, documentation, rules)
2. **`AGENTS.md`** - A context file that GitHub Copilot CLI automatically reads

GitHub Copilot CLI natively supports `AGENTS.md` files. The nearest `AGENTS.md` file in the directory tree takes precedence, allowing you to have project-wide and directory-specific configurations.

## File Structure

After initialization, your project will have:

```
your-project/
├── .tessl/
│   ├── tiles/           # Installed tile content
│   └── config.yaml      # Tessl configuration
├── AGENTS.md            # Auto-generated context for Copilot CLI
└── ... your project files
```

## Configuration Options

### Using AGENTS.md

The `AGENTS.md` file is automatically generated and updated when you install tiles. It contains:

- Project context and conventions
- Installed skill instructions
- Documentation references
- Rules and constraints

You can also manually edit `AGENTS.md` to add project-specific instructions that will be combined with tile content.

### Directory-Specific Context

For monorepos or projects with distinct subsections, you can place additional `AGENTS.md` files in subdirectories:

```
your-project/
├── AGENTS.md              # Root-level context
├── packages/
│   ├── frontend/
│   │   └── AGENTS.md      # Frontend-specific context
│   └── backend/
│       └── AGENTS.md      # Backend-specific context
```

GitHub Copilot CLI will use the nearest `AGENTS.md` based on your current working directory.

## Installing Tiles for Specific Directories

To install tiles for a specific directory:

```sh
cd packages/frontend
tessl install react
tessl install tailwind
```

## Viewing Installed Tiles

List all installed tiles:

```sh
tessl list
```

## Updating Tiles

Update all installed tiles to their latest versions:

```sh
tessl update
```

## Removing Tiles

Remove a tile:

```sh
tessl uninstall <tile-name>
```

## Alternative: Using GitHub's Instructions Format

If you prefer GitHub's native instruction format, Tessl can also output to `.github/copilot-instructions.md`:

```sh
tessl init --agent copilot-cli --format github-instructions
```

This creates instructions in the format that GitHub Copilot CLI reads from the `.github` directory.

## Troubleshooting

### Copilot CLI not reading instructions

1. Ensure you're in a directory where `AGENTS.md` exists or is in a parent directory
2. GitHub Copilot CLI caches instructions. Restart Copilot CLI or use `/resume SESSION-ID` to reload
3. Check that your `AGENTS.md` file is valid Markdown

### Tiles not appearing in context

1. Run `tessl list` to verify tiles are installed
2. Check that `AGENTS.md` references the installed tiles
3. Run `tessl init --agent copilot-cli` to regenerate the context file

## Next Steps

- Browse the [Tessl Registry](https://tessl.io/registry) for available tiles
- Read about [creating your own tiles](https://docs.tessl.io/authoring)
- Join the [Tessl Discord](https://tessl.co/4eV736y) for community support

## See Also

- [GitHub Copilot CLI Documentation](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/use-copilot-cli)
- [AGENTS.md Specification](https://agents.md/)
- [Tessl Documentation](https://docs.tessl.io)
