# Root Cause Analysis (RCA)

## What is Root Cause Analysis?

**Root Cause Analysis (RCA)** is a systematic approach used to identify the underlying cause(s) of a problem, failure, or defect. Instead of just addressing symptoms, RCA aims to find and eliminate the fundamental reason the issue occurred, preventing recurrence.

---

## Key Principles of RCA

1. **Focus on Cause, Not Just Symptoms** – RCA seeks to uncover why a problem happened, not just how it manifested.
2. **Data-Driven Approach** – Uses evidence, facts, and logic rather than assumptions.
3. **Systematic and Structured** – Follows a step-by-step methodology.
4. **Prevention-Oriented** – Aims to implement corrective actions to avoid future occurrences.

---

## RCA Process Steps

1. **Identify the Problem** – Define the issue clearly (what happened, where, when, and how).
2. **Gather Data and Evidence** – Collect relevant information, logs, reports, witness statements, etc.
3. **Determine Root Causes** – Use analytical techniques to trace the issue back to its origin.
4. **Implement Corrective Actions** – Develop solutions that address root causes rather than symptoms.
5. **Monitor and Verify Effectiveness** – Ensure implemented actions prevent recurrence.

---

## Common RCA Techniques

![Ishiwaka (fishbone) diagram](/images/diagrams/fishbone-diagram-ishikawa.png)

- **5 Whys** – Repeatedly ask "Why?" to dig deeper into the root cause.
- **Fishbone Diagram (Ishikawa)** – Categorizes causes into groups (e.g., People, Process, Equipment).
- **Failure Mode and Effects Analysis (FMEA)** – Evaluates potential failure points systematically.
- **Fault Tree Analysis (FTA)** – Uses a logical tree structure to map out cause-and-effect relationships.
- **Pareto Analysis** – Identifies the most significant causes using the 80/20 rule.

---

## Example of RCA in Action

**Problem:** A website experiences frequent downtime.

1. **Why?** The server crashes.
2. **Why?** High CPU usage overloads the system.
3. **Why?** A poorly optimized database query is running continuously.
4. **Why?** A recent software update introduced inefficient indexing.
5. **Why?** The update was not thoroughly tested before deployment.

**Root Cause:** Inadequate testing process before software updates.  
**Solution:** Implement a robust testing protocol before deployment.

## References

- [Five whys on Wikipedia](https://en.wikipedia.org/wiki/Five_whys)
