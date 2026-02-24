# Tessl

Tessl is an Agent Enablement Platform that gives your agents the context they're missing.

- Install usage docs for your favorite open source library from the Tessl Spec Registry
- Create your own internal docs and share with your team 

**Explore more in our [official documentation](https://docs.tessl.io)**.

Visit the [Registry](https://tessl.io/registry) to see which open source libraries we provide documentation for.

## Supported Agents

Tessl works with all major AI coding agents:

- **Claude Code** - `tessl init --agent claude-code`
- **GitHub Copilot CLI** - `tessl init --agent copilot-cli` ([setup guide](docs/github-copilot-cli.md))
- **Cursor** - `tessl init --agent cursor`
- **Gemini** - `tessl init --agent gemini`
- **Codex** - `tessl init --agent codex`

## Get started

1. Install Tessl:

```sh
curl -fsSL https://get.tessl.io | sh
```

2. Initialize for your agent:

```sh
tessl init --agent copilot-cli  # or: claude-code, cursor, gemini, codex
```

3. Install tiles from the registry:

```sh
tessl install react
tessl install typescript
```

4. Run your agent - it will automatically use the installed context

## Reporting Bugs

We love feedback. You can use the `tessl feedback` command to report issues or share feedback directly within Tessl, file a [GitHub issue](https://github.com/tesslio/cli/issues) or just email <support@tessl.io>.

## Connect on Discord

You are welcome to join the [Tessl Discord](https://tessl.co/4eV736y) to connect with other developers using Tessl.

## Terms and Conditions

- [Terms of Service](https://tessl.io/policies/terms)
- [Privacy Policy](https://tessl.io/policies/privacy-cookies)
