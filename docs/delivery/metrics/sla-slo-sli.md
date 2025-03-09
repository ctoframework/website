# SLA, SLO and SLI compared

In the context of service reliability and performance management, **SLA (Service Level Agreement), SLO (Service Level Objective), and SLI (Service Level Indicator)** are key concepts used to define, measure, and enforce service quality. While they are closely related, each serves a distinct role in ensuring reliable and predictable service delivery.

### **1. Service Level Indicator (SLI)**

An SLI is a **quantitative measure** of a system’s performance and reliability. It represents specific metrics that track service health, such as **latency, availability, error rate, or throughput**. These indicators provide insight into how well a service is performing from an operational perspective.

For example:

- **Availability SLI**: The percentage of successful requests over a given period.
- **Latency SLI**: The proportion of requests served within a specified response time threshold.

SLIs are the foundation upon which objectives and agreements are built.

### **2. Service Level Objective (SLO)**

An SLO is a **target value or range** for an SLI, defining an acceptable level of performance. It acts as an internal reliability benchmark for teams to maintain service quality before breaching contractual obligations.

For example:

- **Availability SLO**: 99.9% uptime over a month.
- **Latency SLO**: 95% of requests must be served within 200ms.

SLOs help guide engineering efforts, balancing reliability with operational costs and user expectations.

### **3. Service Level Agreement (SLA)**

An SLA is a **formal contract** between a service provider and its customers, specifying the promised level of service. It typically includes **SLOs**, along with consequences (such as refunds or credits) if the provider fails to meet them.

For example:

- **Availability SLA**: 99.9% uptime, with a penalty if downtime exceeds 43.8 minutes per month.
- **Support SLA**: A guaranteed response time of under 4 hours for critical incidents.

SLAs are **legally binding**, whereas SLOs are internal goals.

### **Comparison and Relationship**

| Concept             | Purpose                           | Scope            | Example                           |
| ------------------- | --------------------------------- | ---------------- | --------------------------------- |
| **SLI (Indicator)** | Measures service performance      | Low-level metric | 99.95% successful requests        |
| **SLO (Objective)** | Sets internal performance targets | Engineering goal | 99.9% uptime target               |
| **SLA (Agreement)** | Defines contractual obligations   | Customer-facing  | 99.9% uptime or financial penalty |

**Key Insights:**

- **SLIs are the raw data points**, SLOs set **acceptable limits** on them, and SLAs are **enforceable promises** based on those limits.
- **SLOs are stricter than SLAs** to provide a buffer before contractual breaches occur.
- While SLAs focus on external commitments, **SLOs help maintain reliability internally**, preventing SLA violations.
