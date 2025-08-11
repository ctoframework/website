## Exponential Backoff

Exponential backoff is a strategy for handling retries in systems where repeated, immediate attempts risk making a problem worse—such as when a service is under high load, a network link is unreliable, or a shared resource is congested.

Instead of retrying at fixed intervals, the wait time between retries grows exponentially. This reduces the chance of overloading the system and allows time for transient issues to resolve.

### Mathematical Model

The wait time before the _n_-th retry can be expressed as:

\[
t_n = t_0 \times 2^{n}
\]

Where:

- \( t*n \) = wait time before the \_n*-th retry
- \( t_0 \) = base delay (e.g., 1 second)
- \( n \) = retry attempt count starting from 0

For example, with \( t_0 = 1 \) second:

| Retry Attempt \(n\) | Delay \(t_n\)             | Cumulative Wait Time |
| ------------------- | ------------------------- | -------------------- |
| 0                   | \(1 \times 2^{0} = 1\) s  | 1 s                  |
| 1                   | \(1 \times 2^{1} = 2\) s  | 3 s                  |
| 2                   | \(1 \times 2^{2} = 4\) s  | 7 s                  |
| 3                   | \(1 \times 2^{3} = 8\) s  | 15 s                 |
| 4                   | \(1 \times 2^{4} = 16\) s | 31 s                 |

![Exponential backoff](/images/diagrams/exponential-backoff.png)

### Jitter

In many implementations, a random “jitter” is added to the wait time to prevent multiple clients from synchronising their retries and causing a surge. This can be represented as:

\[
t_n = \text{random}(0, t_0 \times 2^{n})
\]

### Why It Works

By growing the retry intervals exponentially, the approach turns retry load growth from linear (or constant) into a curve that quickly stretches out over time, avoiding a “retry storm” that could collapse a struggling service.

It is widely used in distributed systems, API calls, and database connections to balance responsiveness with stability, especially under fault conditions.
