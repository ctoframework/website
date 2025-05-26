---
title: DORA metrics
---

# SPACE Metrics: A Comprehensive Model for Engineering Productivity

Traditional engineering metrics have often focused too narrowly on output—such as lines of code or velocity points—without capturing the complexity of modern software development. The **SPACE framework**, introduced by researchers from GitHub, Microsoft, and academia, addresses this by offering a multidimensional model for assessing developer productivity.

Rather than looking at a single number, SPACE advocates measuring across five dimensions:

---

## 1. Satisfaction and Well-being

This dimension is qualitative by nature, but it can be quantified through surveys and engagement analytics.

**Example Metrics:**
- Developer satisfaction score (e.g., on a 5-point Likert scale, gathered monthly)
- eNPS (Employee Net Promoter Score) – e.g., +35 may indicate a healthy team
- Burnout risk surveys – % of team reporting high stress or low energy

**Why it matters:**  
A team that is demoralised or burnt out will not sustain performance over time, even if activity appears high in the short term.

---

## 2. Performance

This is about *outcomes*, not activity. It includes value delivery, impact on users, and alignment with business objectives.

**Example Metrics:**
- Customer impact per engineer – e.g., number of customer issues resolved per quarter
- Feature adoption rate – e.g., % increase in usage after a new feature release
- Incident resolution quality – e.g., % of P1 incidents resolved with no regression in 30 days

**Why it matters:**  
These are tangible signs that engineering efforts are contributing real value, not just generating activity.

---

## 3. Activity

Activity is the most traditionally measured dimension but must be contextualised carefully. On its own, it’s insufficient.

**Example Metrics:**
- Commits per engineer per week – e.g., median of 25–40
- Pull requests merged per sprint
- Code review volume – e.g., number of reviews completed or time spent reviewing

**Caveat:**  
An increase in commits or PRs isn’t always positive—it might indicate churn or fragmented work. Combine with other dimensions to interpret correctly.

---

## 4. Communication and Collaboration

Collaboration is essential, especially in distributed or cross-functional teams. It can be measured through workflow efficiency and team interaction patterns.

**Example Metrics:**
- Pull request review turnaround time – e.g., target <24 hours
- Ratio of collaborative PRs – PRs with more than one reviewer or contributor
- Cross-team dependencies resolved per sprint

**Why it matters:**  
Delays or bottlenecks in collaboration often become the hidden tax that slows down engineering organisations.

---

## 5. Efficiency and Flow

This dimension evaluates how easily engineers can make uninterrupted progress on meaningful work.

**Example Metrics:**
- Lead time for change (from code commit to production) – e.g., target <1 day for high-performing teams
- Deployment frequency – daily or weekly is typical for modern teams; elite teams may deploy multiple times per day (cf. DORA metrics)
- Work-in-progress (WIP) limits exceeded – signal for too much context switching

**Why it matters:**  
Inefficiencies—such as waiting on approvals, dealing with flaky CI/CD pipelines, or frequent interruptions—are major productivity drains, even if other metrics look healthy.

---

## Practical Application

Leaders who successfully implement SPACE typically do the following:

- **Blend qualitative and quantitative data** – e.g., combine developer sentiment surveys with DORA metrics to see if changes in process are improving both flow and morale.
- **Avoid weaponising metrics** – measurements should guide conversations, not enforce quotas.
- **Visualise trends over time** – a dashboard showing the SPACE dimensions monthly can surface systemic issues before they escalate.

---

## Summary Table of Sample Metrics by Dimension

| SPACE Dimension           | Metric Example                                  | Target/Context                      |
|---------------------------|--------------------------------------------------|-------------------------------------|
| Satisfaction & Well-being | Developer satisfaction survey (1–5)             | ≥4.0 sustained                      |
| Performance               | Feature adoption within 30 days                 | +15% usage growth                   |
| Activity                  | Pull requests merged per sprint                 | 5–10 per engineer, context-dependent|
| Communication & Collaboration | PR review turnaround time                    | <24 hours                           |
| Efficiency & Flow         | Lead time for change                            | <1 day (DORA elite)                 |
