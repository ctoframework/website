# Goodhart’s Law in Software Engineering

## **Definition**
**"When a measure becomes a target, it ceases to be a good measure."**

At its core, Goodhart’s Law highlights a fundamental risk in managing complex systems: once a specific metric is used to guide behaviour or assess success, it can distort the very process it was intended to monitor.

In software engineering, where systems are complex and team dynamics are intricate, this law has particularly potent implications. Metrics are essential—they help track progress, ensure accountability, and inform decisions—but if misapplied, they can lead to perverse incentives and outcomes that diverge from the original goal.

---

## **Why This Happens**

People respond to incentives. When a metric is elevated to the status of a target, individuals and teams begin optimising for it—often at the expense of broader, harder-to-measure goals like code quality, team cohesion, system reliability, or customer satisfaction.

---

## **Examples in Software Engineering**

### **1. Lines of Code (LoC)**
- **Intent:** Measure productivity.  
- **Consequence:** Developers may write verbose or unnecessarily complex code to appear productive. The result is a bloated codebase, higher maintenance costs, and degraded performance.  
- **Better alternative:** Emphasise value delivered, such as completed features or reduced technical debt, alongside peer-reviewed code quality assessments.

### **2. Velocity in Agile (Story Points Completed per Sprint)**
- **Intent:** Track team throughput.  
- **Consequence:** Teams may inflate estimates or split tasks unnaturally to boost their numbers, undermining the integrity of sprint planning. Worse, velocity becomes a competitive metric rather than a planning tool.  
- **Better alternative:** Use velocity as a *team-internal* planning guide, and combine it with qualitative retrospectives and customer feedback.

### **3. Number of Deployments**
- **Intent:** Encourage continuous delivery and faster iteration.  
- **Consequence:** Teams might deploy frequently without meaningful changes or skip thorough testing, leading to an increase in post-deployment issues and instability.  
- **Better alternative:** Monitor *deployment success rate* and *time to resolve production issues* alongside deployment frequency.

### **4. Bug Closure Rate**
- **Intent:** Track responsiveness to issues.  
- **Consequence:** Engineers may prioritise trivial bugs that are easy to fix to inflate closure stats, while critical but complex issues remain neglected.  
- **Better alternative:** Weight bug fixes by severity and impact, and track time-to-resolution for high-priority issues.

---

## **How to Use Metrics Wisely**

1. **Recognise proxy indicators:** Understand that most software metrics are proxies—not end goals. Treat them as signals, not scorecards.
2. **Balance metrics with judgement:** Quantitative data should be combined with qualitative assessments, like code reviews, user feedback, and retrospectives.
3. **Watch for metric saturation:** Over time, metrics can lose their effectiveness as people learn how to game them. Periodically re-evaluate whether a metric is still serving its purpose.
4. **Avoid metric monoculture:** No single metric can capture the complexity of software development. Use a dashboard of diverse metrics to maintain a holistic view.
5. **Align metrics with values, not just outputs:** For example, if maintainability is a core value, measure things like cyclomatic complexity or pull request review depth—not just feature throughput.
