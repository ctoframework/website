# Quality Assurance Metrics

Quality Assurance (QA) metrics and KPIs help assess the effectiveness of testing processes, defect management, and overall software quality.

---

## 1. Test Coverage Metrics

- **Code Coverage** – The percentage of the code executed during automated tests (unit, integration, system tests).
- **Requirement Coverage** – The percentage of requirements covered by test cases.
- **Test Case Coverage** – The percentage of test cases executed out of the total planned.

---

## 2. Defect Management Metrics

- **Defect Density** – Number of defects per thousand lines of code (KLOC), indicating software stability.
- **Defect Leakage** – Percentage of defects found in production versus total defects found during testing.

  **Formula:**

\[
\text{Defect Leakage} = \left( \frac{\text{Defects found in production}}{\text{Total defects found in testing}} \right) \times 100
\]

- **Defect Removal Efficiency (DRE)** – Measures how effectively defects are caught during testing.

  **Formula:**

\[
\text{DRE} = \left( \frac{\text{Defects found before release}}{\text{Total defects found (before + after release)}} \right) \times 100
\]

- **Defect Severity Index** – Tracks the impact of defects based on severity levels (critical, major, minor).
- **Reopened Defects** – The number of defects that were marked as fixed but reoccurred, indicating testing effectiveness.

---

## 3. Test Execution Metrics

- **Test Pass Rate** – The percentage of passed test cases compared to the total executed.
- **Test Fail Rate** – The percentage of failed test cases out of the total executed.
- **Test Case Effectiveness** – Percentage of test cases that detected defects, measuring how well tests identify issues.
- **Blocked Test Cases** – Number of test cases that could not be executed due to unresolved issues.

---

## 4. Automation & Efficiency Metrics

- **Test Automation Coverage** – Percentage of test cases automated versus total test cases.
- **Test Execution Time** – The total time taken to execute tests, useful for optimizing automation.
- **Mean Time to Detect (MTTD)** – The average time taken to identify a defect after it is introduced.
- **Mean Time to Resolve (MTTR)** – The average time taken to fix and verify a defect after detection.
