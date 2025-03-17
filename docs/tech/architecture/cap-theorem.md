---
tags:
  - theorem
  - cap
  - brewers-theorem
---

# CAP Theorem

As a CTO, you need to balance trade-offs between **Consistency, Availability, and Partition Tolerance** when designing distributed systems. The **CAP theorem** formulated by computer scientist [Eric Brewer](<https://en.wikipedia.org/wiki/Eric_Brewer_(scientist)>) states that in any distributed system, you can only guarantee **two out of three** properties at any given time.

## Breaking Down CAP

### 1. **Consistency (C)**

Every node in the system always has the latest data. A read request will return the most recent write.

- **Implication**: Strong consistency often means sacrificing availability (e.g., using leader-based replication).
- **Example**: Traditional relational databases (e.g., PostgreSQL with strong ACID properties).

### 2. **Availability (A)**

Every request gets a response, even if some nodes are down. However, the response may not be the most recent version of the data.

- **Implication**: Prioritizing availability means some nodes might serve stale data.
- **Example**: NoSQL databases like Cassandra or DynamoDB favor availability over strict consistency.

### 3. **Partition Tolerance (P)**

The system continues to function despite network partitions (i.e., some nodes can't communicate with others).

- **Implication**: Any practical distributed system must be partition-tolerant, so the trade-off is usually between **C and A**.
- **Example**: If a data center loses connectivity, does the system halt (favoring C) or keep serving responses (favoring A)?

## Real-World Considerations

| **Industry/System**                           | **CAP Preference**                           | **Example**                                                                              |
| --------------------------------------------- | -------------------------------------------- | ---------------------------------------------------------------------------------------- |
| **Financial systems** (banking, transactions) | **CP (Consistency + Partition Tolerance)**   | A payment system must not allow double spending, even if it means temporary downtime.    |
| **E-commerce & social media**                 | **AP (Availability + Partition Tolerance)**  | Amazon or Facebook can serve slightly stale data, but the site must always be available. |
| **Hybrid architectures**                      | **Eventual Consistency (balancing C and A)** | AWS DynamoDB (AP with eventual consistency but configurable strong consistency).         |
