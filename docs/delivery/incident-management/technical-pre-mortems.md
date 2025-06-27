---
title: Technical pre-mortems
---

# Pre-Mortem: Engineering Failure Before It Happens

## Overview

A **pre-mortem** is a structured technical exercise where you assume your project has already failed—completely and irreversibly. The goal is to explore, in detail, what could have caused that failure _before_ any lines of code are shipped or infrastructure is provisioned.

This isn't about speculative doom. It’s about applying the same rigour to failure analysis _before_ delivery as we would _after_ an outage. You run a root-cause analysis in reverse—anticipating systemic collapse rather than responding to it.

---

## Why Technical Teams Should Use It

In complex systems, failure rarely comes from a single bug or misstep. It’s usually a cascading chain of overlooked risks, hidden coupling, unclear ownership, or misaligned priorities.

Pre-mortems help surface these issues early:

- **Architectural fragility**: “We assumed the system could scale horizontally, but never validated cross-region failover.”
- **Dependency risk**: “This new service has four upstream integrations, none with formal SLAs.”
- **Operational blind spots**: “No one considered how observability would work across the new event pipeline.”
- **Tech-debt pressure**: “We knew the legacy interface wasn’t fit for purpose, but kept punting refactoring.”

It creates space to think beyond ‘green builds’ and ‘on-time delivery’, and instead asks: _Would this system survive production-grade traffic, real-world constraints, and political pressure from stakeholders?_

---

## How to Run a Technical Pre-Mortem

### 1. Set the Failure Scenario

- “It’s six months from now. The rollout failed. We’ve missed our objectives. What went wrong?”
- Use a real, consequential project—re-architectures, platform migrations, or product launches.

### 2. Gather Cross-Disciplinary Input

- Involve architects, senior engineers, SREs, product and programme leads.
- Ensure representation from both build-time (engineering) and run-time (operations) teams.

### 3. Decompose the Failure

- Individually, people write down everything that might have contributed to the hypothetical failure:
  - Critical bugs, race conditions, memory leaks.
  - Misestimated load or traffic spikes.
  - Flawed rollout strategy (e.g. no blue/green or canary).
  - Misalignment between infra readiness and feature delivery.
  - Poor incident response or lack of observability.

### 4. Map Risks to Systems

- Cluster causes by component, service boundary, or layer in the stack.
- Use diagrams or architecture maps to locate systemic weak points.

### 5. Prioritise and Mitigate

- Rank the top failure modes by likelihood and blast radius.
- Design mitigations: automated rollback, feature flags, chaos testing, performance baselines, better monitoring.
- Feed findings into backlog, architecture reviews, or deployment checklists.

---

## When It’s Most Valuable

- **Before launching high-risk systems**: distributed architecture, zero-downtime migrations, or anything critical to revenue or reputation.
- **During planning for quarterly OKRs**: to sanity-check strategic bets.
- **As part of architectural decision records (ADRs)**: to validate trade-offs and assumptions before committing to long-term paths.

---

## Cultural Benefits for Engineering Orgs

Technical pre-mortems foster a culture of _failure-aware design_. They reward teams for thinking in systems, acknowledging uncertainty, and preparing for reality—not just ideal execution paths.

They also build muscle for incident readiness. Teams who have gamed out plausible failure scenarios in advance are vastly more effective under pressure.

# References

- [Wikipedia](https://en.wikipedia.org/wiki/Pre-mortem)
- [Technical post-mortems](./technical-post-mortems.md)
