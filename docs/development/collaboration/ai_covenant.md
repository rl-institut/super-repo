# AI Covenant

This repository is following the [AI Covenant](https://github.com/rl-institut/super-repo/blob/production/AI_COVENANT.md). <br>
It defines how AI tools (e.g. chat assistants, coding agents, AI review bots) may be used when contributing.

The core principle is: **You own your contributions**, regardless of what tools helped create them. <br>
The main rules are:

- **Human in the loop:** AI tools must not commit, push or post in issues, PRs or other channels autonomously.
- **No AI authorship:** Commit under your own name, never under an AI tool or bot account. No `Co-authored-by:`, `Assisted-by:` or similar trailers and no AI markers in commit messages.
- **Disclosure:** Routine AI use needs no disclosure, but AI-proposed changes you do not fully understand must be disclosed in the PR description.
- **Good first issues:** Issues labelled `other: good first issue 🌱` are reserved for newcomers and must not be solved with AI tools.

## Guidance for AI agents

The 📝 `AGENTS.md` file provides guidance for AI coding agents working in the repository,
including the commands, conventions and the rules of the AI Covenant. <br>
📝 `CLAUDE.md` is a symlink to 📝 `AGENTS.md`, so that Claude Code uses the same guidance.

## Agent skills

Skills for AI agents can be added to the repository in 📝 `.agents/skills/<skill-name>/SKILL.md`. <br>
To make a skill available to Claude Code, add a symlink in 📝 `.claude/skills/`:

💻 `ln -s ../../.agents/skills/<skill-name> .claude/skills/<skill-name>`

!!! warning "Symlinks on Windows"
    Git checks out symlinks as plain text files on Windows, unless symlinks are enabled
    (Developer Mode and 💻 `git config core.symlinks true`).

!!! note "Used Icons"
    🐙 GitHub | 💠 git | 📝 File | 💻 Command Line
