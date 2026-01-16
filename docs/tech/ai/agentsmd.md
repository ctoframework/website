---
tags:
  - llm
  - ai
  - coding-assistant
---

# Agents.MD

## What is `agents.md`?

`agents.md` is a lightweight, human-readable contract that defines how software agents should behave within a system.

### Purpose
- **Alignment:** Captures the agent’s goals, boundaries, and decision principles.
- **Consistency:** Standardises behaviour across environments and teams.
- **Governance:** Makes assumptions, constraints, and safety rules explicit and reviewable.

### Typical Contents
- **Role & scope:** What the agent is responsible for (and what it is not).
- **Capabilities & tools:** Which actions, APIs, or resources it may use.
- **Decision logic:** High-level policies, priorities, and escalation rules.
- **Constraints:** Security, compliance, and operational limits.
- **Lifecycle:** How the agent is initialised, monitored, and updated.

### Why it matters
By externalising intent and rules from code, `agents.md` improves transparency, auditability, and long-term maintainability of agent-driven systems.

## Agents.MD examples

- [Agency Swarm](https://github.com/VRSEN/agency-swarm/blob/main/AGENTS.md)
- [Oh-my-posh](https://github.com/JanDeDobbeleer/oh-my-posh/blob/main/AGENTS.md)
- [AWS HPC Recipes](https://github.com/aws-samples/aws-hpc-recipes/blob/main/AGENTS.md)
- [RabbitMQ server](https://github.com/rabbitmq/rabbitmq-server/blob/main/AGENTS.md)
- [AI Agents for Beginners](https://github.com/microsoft/ai-agents-for-beginners/blob/main/AGENTS.md)
- [Dart Code](https://github.com/Dart-Code/Dart-Code/blob/master/AGENTS.md)
- [Vercel Labs Agent-skills](https://github.com/vercel-labs/agent-skills/blob/main/AGENTS.md)
- [Sentry](https://github.com/getsentry/sentry/blob/master/AGENTS.md)
- [Cloudflare workers SDK](https://github.com/cloudflare/workers-sdk/blob/main/AGENTS.md)

## References

- https://agentsmd.net/agents-md-examples/
- https://github.blog/ai-and-ml/github-copilot/how-to-write-a-great-agents-md-lessons-from-over-2500-repositories/
- https://www.builder.io/blog/agents-md
- https://developers.openai.com/codex/guides/agents-md
- https://www.claude.com/blog/using-claude-md-files
