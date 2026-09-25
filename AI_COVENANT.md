<!--
SPDX-FileCopyrightText: 2026 Jonathan Amme <https://github.com/nesnoj> © Reiner Lemoine Institut
SPDX-FileCopyrightText: super-repo v0.5.0 <https://github.com/rl-institut/super-repo>
SPDX-License-Identifier: CC0-1.0
-->

# AI Covenant

This covenant sets the rules for using AI tools (e.g. chat assistants, coding
agents, code completion, AI review bots) when contributing to this repository.
It applies to all contributions: code, documentation, issues, pull requests
(PR), reviews, discussions and any other project channel.

AI tools are welcome as long as they support human work and do not replace
human judgement and responsibility.

## Core Principle: You Own Your Contributions

**Everything you contribute is yours, regardless of what tools helped create it.**

When you submit anything created with AI assistance, you are its author and
you are responsible for:

- Understanding what you submit
- Verifying that it is correct, tested and appropriate
- Explaining and defending your choices during review
- Ensuring it follows the project standards (see [CONTRIBUTING.md](CONTRIBUTING.md))
- Removing unrelated changes that AI tools tend to introduce
- Ensuring it does not violate licenses, copyrights or other rights of third parties

Do not submit anything you cannot fully stand behind.

## Rules

### 1. Human in the loop

A human must review and approve every action that changes the repository or
speaks for a person in project channels.

- AI tools must not commit, push, open or comment on issues and PRs, or post
  in discussions and chats autonomously.
- You may let an AI tool draft text or changes, but you review and submit them
  yourself.
- Automated AI tools acting on behalf of the project (e.g. AI review bots)
  may only be enabled by the maintainers. They must be clearly recognisable as
  bots, may only comment and must never approve, merge, push or close.

### 2. No AI co-authorship

AI tools are not authors. Do not credit them in commits:

- No `Co-authored-by:`, `Assisted-by:`, `Generated-by:` or similar trailers
- No AI-specific prefixes, tags or markers in commit messages

Commit messages follow the regular conventions in [CONTRIBUTING.md](CONTRIBUTING.md).
Many AI tools add such trailers by default, so configure your tool accordingly.

### 3. Disclose what you do not fully understand

Routine use of AI tools does not need to be disclosed. **Disclosure is
required** if your contribution contains AI-proposed changes that you do not
fully understand. Name the tool and point to the affected parts in the PR
description (see the PR template), so reviewers can assess them accordingly.

In discussions, make clear whether an idea is an AI suggestion or your own
recommendation based on your expertise.

### 4. Good first issues are for humans

Issues labelled as good first issues are reserved for newcomers to learn the
project. **Using AI tools to solve them is forbidden**, i.e. to write the
code, tests, documentation or PR description. This applies to everyone,
including maintainers.

Using AI tools to learn is fine, e.g. to explain existing code, concepts or
error messages.

## AI-Assisted Reviews

AI review comments are automated suggestions, not human reviews.

- PR authors may resolve AI review comments without a response
- Human reviewers may use AI feedback to inform their own review
- Every PR requires the approval of a human reviewer

## What This Means in Practice

| Situation                                                    | Guidance                                                |
|--------------------------------------------------------------|---------------------------------------------------------|
| Writing code or docs with AI assistance                      | No disclosure needed, you own the result                |
| Submitting an AI-proposed change you fully understand        | No disclosure needed                                    |
| Submitting an AI-proposed change you do not fully understand | Disclose tool and affected parts in the PR              |
| Drafting an issue or PR description with AI                  | No disclosure needed, ensure it is accurate, no AI slop |
| Letting an agent commit, push or post without your review    | Not allowed                                             |
| AI tool adds a co-author trailer to a commit                 | Not allowed, remove it before pushing                   |
| Working on a good first issue                                | Do not use AI to solve it, only to learn                |
| Receiving AI review comments                                 | Address or resolve them at your discretion              |

## Enforcement

- Maintainers may close issues or PRs that violate this covenant with a
  comment pointing to the violated rule. You are welcome to reopen or resubmit
  once the issue is fixed. Minor violations such as co-author trailers are
  fixed on request instead.
- Repeated or deliberate violations are handled according to the enforcement
  guidelines of the [Code of Conduct](CODE_OF_CONDUCT.md).

---

*This covenant may evolve as AI tools and community needs change.
Feedback and suggestions are welcome.*

*It is inspired by the [LinkML AI Covenant](https://github.com/linkml/linkml/blob/main/AI_COVENANT.md)
and the [Apache Airflow Gen-AI Assisted contributions](https://github.com/apache/airflow/blob/main/contributing-docs/05_pull_requests.rst#gen-ai-assisted-contributions)
guidelines.*
