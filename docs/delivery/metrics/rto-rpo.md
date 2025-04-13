# RTO and RPO

### **Recovery Time Objective (RTO)**

**RTO** defines the **maximum acceptable time** that a system, application, or process can be **down after a failure or disaster** before causing significant impact to the business.

#### **ROT Example**

Suppose your e-commerce platform goes down due to a database failure.  
If the RTO is **2 hours**, the IT team must restore the platform within **120 minutes** to meet business continuity expectations.

- If recovery takes **1 hour 45 minutes**, you're within the RTO.
- If it takes **3 hours**, you've **missed the RTO**, and this may result in financial loss, SLA breaches, or reputational damage.

RTO is often driven by the **cost of downtime**. For instance, if your business loses **£10,000 per hour** of downtime, a **4-hour outage** equates to **£40,000** in direct losses.

---

### **Recovery Point Objective (RPO)**

**RPO** defines the **maximum tolerable amount of data loss**, measured in time. It indicates how far back in time your data recovery point can be from the moment of failure.

#### **RPO Example**

Let’s say you perform **hourly backups** of a customer database.

- If a system crashes at **12:45**, and the last backup was at **12:00**, you've lost **45 minutes** of data.
- If the RPO is **1 hour**, this loss is within acceptable limits.
- If the RPO is **15 minutes**, you've **exceeded** the RPO, and it may require alternative recovery strategies like real-time replication.

RPO is often tied to **data criticality**. For instance:

- A financial trading system may require an RPO of **0 seconds** (i.e., **zero data loss**) using real-time replication.
- An internal HR portal might have an RPO of **12 hours**, allowing for daily backups.

---

### **Summary Table**

| Term | Definition              | Quantitative Example                   | Business Impact           |
| ---- | ----------------------- | -------------------------------------- | ------------------------- |
| RTO  | Max downtime allowed    | Must recover within 2 hours            | Loss per hour: £10,000    |
| RPO  | Max data loss tolerable | Must not lose more than 1 hour of data | Lost transactions, rework |
