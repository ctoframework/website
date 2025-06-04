# Error Budgets

An _error budget_ is a powerful concept used to balance innovation and reliability in software systems. It originates from the principles of Site Reliability Engineering (SRE) and is particularly useful for aligning operations and development teams around service expectations and system stability.

## What Is an Error Budget?

Every service has a **Service Level Objective (SLO)** — a defined target for system performance or availability (e.g., 99.9% uptime). The error budget is the **difference between perfect reliability (100%) and the SLO**. If your SLO is 99.9%, the error budget is 0.1%. This 0.1% represents the _maximum acceptable amount of failure_ over a given period, such as a month.

In simple terms, it answers: **"How much failure is acceptable?"**

## Why It Matters

The key benefit of an error budget is that it introduces a **quantitative, business-aligned tolerance for risk**. This prevents over-engineering and allows teams to:

- Ship new features faster, as long as reliability remains within agreed thresholds.
- Pause releases and focus on stability when the error budget is consumed or trending toward exhaustion.
- Foster accountability between engineering and operations by framing reliability as a shared, measurable goal.

## Practical Application

1. **Monitoring and Enforcement**: Track error budget consumption via metrics tied to SLOs (e.g., latency, uptime, error rate). When consumption nears limits, automated alerts or deployment freezes can be triggered.

2. **Decision-Making Lever**: Use error budgets as a gate for releasing high-risk changes. If the budget is healthy, move fast. If not, stabilise before proceeding.

3. **Postmortems and Prioritisation**: When incidents occur, evaluate how much error budget was burned. This helps inform whether follow-up work is required, and how urgent it is.

4. **Engineering Culture Shift**: Encourages a mindset where reliability is treated as a feature — with trade-offs that can be discussed and managed.
