# Chaos Engineering

**Chaos Engineering** is the discipline of intentionally introducing failure into systems to learn how they behave under stress. The goal is not to break things for fun, but to build confidence that systems will survive real-world incidents.

It assumes failure is inevitable and treats resilience as something that must be *proven*, not assumed.

---

## The core idea
Chaos Engineering is built around a simple belief:

> Systems don’t fail in theory — they fail in production, under pressure.

Instead of waiting for outages to reveal weaknesses, chaos experiments surface them early, safely, and deliberately.

---

## How it works

A typical chaos experiment follows a tight loop:

1. **Define steady state** – What “normal” looks like (latency, error rates, throughput)
2. **Form a hypothesis** – What should happen if a component fails
3. **Introduce failure** – Kill instances, add latency, block dependencies, expire credentials
4. **Observe the outcome** – Does the system degrade gracefully or collapse?
5. **Learn and improve** – Fix weaknesses, update assumptions, repeat

The emphasis is on learning, not heroics.

---

## What Chaos Engineering is good at

Chaos Engineering excels at:

- Exposing hidden dependencies and single points of failure
- Validating redundancy and failover paths
- Improving incident response and operational confidence
- Turning unknown risks into known, manageable ones

It shifts resilience from hope to evidence.

---

## What Chaos Engineering is *not*

Common misconceptions:

- **Not** random destruction in production
- **Not** a replacement for testing, monitoring, or reliability engineering
- **Not** reckless when done properly

Well-run chaos experiments are scoped, observable, and reversible.

---

## Why it matters now

Modern systems are:

- Distributed by default
- Dependent on third parties
- Changing continuously

Traditional testing cannot model the combinatorial failure modes these systems create. Chaos Engineering embraces that complexity instead of pretending it can be fully controlled.

## References

- [Chaos Monkeys from Netflix, on Github](https://github.com/Netflix/chaosmonkey/)
- [Chaos Mesh](https://github.com/chaos-mesh/chaos-mesh), Chaos engineering platform for Kubernetes
- [Chaos Engineering](https://en.wikipedia.org/wiki/Chaos_engineering) article on the Wikipedia
- [Chaos Engineering](https://www.ibm.com/think/topics/chaos-engineering) article on IBM