---
title: DORA metrics
---

# Understanding DORA Metrics: Measuring Software Delivery Performance

DORA metrics, developed by the **DevOps Research and Assessment** (DORA) team, offer a research-backed framework for measuring and improving software delivery performance. These four metrics provide clear, actionable insight into both the **velocity** and **stability** of software engineering teams.

## The Four DORA Metrics

### 1. **Deployment Frequency**

**What it measures**:  
How often an organisation successfully releases to production.

**Why it matters**:  
Frequent deployments indicate smaller, incremental changes that are easier to review, test, and roll back if needed. It reflects a team's ability to deliver value rapidly and respond to market or customer needs.

**Quantitative benchmarks (2023 State of DevOps Report):**

- **Elite performers**: Deploy on demand or multiple times per day
- **High performers**: Deploy between once per day and once per week
- **Medium performers**: Deploy between once per week and once per month
- **Low performers**: Deploy less than once per month

**Example**:  
A high-performing e-commerce company might deploy code updates 5–10 times per day, enabling rapid experimentation and customer feedback loops.

---

### 2. **Lead Time for Changes**

**What it measures**:  
The time it takes for a commit to reach production. This includes coding, testing, review, and deployment.

**Why it matters**:  
Shorter lead times mean faster iteration and the ability to adapt quickly to user feedback or changing business requirements. It also points to efficient pipelines and reduced friction in the delivery process.

**Quantitative benchmarks:**

- **Elite performers**: Less than one day
- **High performers**: Between one day and one week
- **Medium performers**: Between one week and one month
- **Low performers**: More than one month

**Example**:  
A SaaS platform with streamlined CI/CD processes may have an average lead time of 6 hours from code commit to production deployment.

---

### 3. **Change Failure Rate**

**What it measures**:  
The percentage of deployments that result in a service incident, rollback, or require hotfixes.

**Why it matters**:  
Lower change failure rates signify better quality code, stronger testing, and reliable deployment practices. It ensures that velocity doesn’t come at the cost of reliability.

**Quantitative benchmarks:**

- **Elite performers**: 0–15%
- **High performers**: 16–30%
- **Medium performers**: 31–45%
- **Low performers**: 46–60% or more

**Example**:  
An infrastructure team releasing microservices updates with a 5% failure rate indicates strong automation, canary deployments, and observability practices.

---

### 4. **Mean Time to Restore (MTTR)**

**What it measures**:  
The average time it takes to restore service after a failure that impacts users.

**Why it matters**:  
MTTR reflects system resilience and operational readiness. A low MTTR suggests that failures are detected quickly and remediated effectively — a critical capability for maintaining service-level objectives.

**Quantitative benchmarks:**

- **Elite performers**: Less than one hour
- **High performers**: Less than one day
- **Medium performers**: Between one day and one week
- **Low performers**: More than one week

**Example**:  
A digital banking app with strong incident response practices may recover from critical service outages within 30 minutes on average.

---

## Why DORA Metrics Matter

These metrics provide a **balanced view** of performance, ensuring that speed does not compromise stability. They also serve as a **common language** between technical and business stakeholders, helping bridge strategy and execution.

By tracking DORA metrics over time, organisations can:

- Identify bottlenecks in the delivery pipeline
- Justify investments in tooling, automation, or process improvement
- Align engineering performance with customer satisfaction and business goals
- Benchmark against industry standards

## References

- [Wikipedia](https://en.wikipedia.org/wiki/DevOps_Research_and_Assessment#DORA_Four_Key_Metrics)
