# Common estimation methods

## 1. SWAG (Scientific Wild-Ass Guess)

- **Description**: A rough, experience-based guess that lacks detailed analysis.
- **When to Use**:
  - Early-stage discussions when little information is available.
  - When a quick ballpark figure is needed.
  - Informal or exploratory planning.
- **Example**:  
  _"This project might take around six months, but we need more details to be sure."_

## 2. ROM (Rough Order of Magnitude)

- **Description**: A high-level estimate with a broad accuracy range (typically ±50% or more).
- **When to Use**:
  - Initial feasibility studies.
  - Budgeting and executive decision-making.
  - Before detailed scope or requirements are available.
- **Example**:  
  _"This project will cost between $500K and $1M."_

## 3. T-Shirt Sizing (XS, S, M, L, XL, XXL, etc.)

- **Description**: Uses broad size categories instead of precise numbers, often based on complexity or effort.
- **When to Use**:
  - Agile development and backlog grooming.
  - When detailed effort estimation isn't practical.
  - Relative comparisons between tasks rather than absolute time estimates.
- **Example**:  
  _"Feature A is a Medium, but Feature B is an XL, so it will take significantly longer."_

## 4. Three-Point Estimation (PERT: Program Evaluation and Review Technique)

- **Description**: Uses three estimates—Optimistic (O), Pessimistic (P), and Most Likely (M)—to calculate an expected value using the formula:  
  \[
  E = \frac{O + 4M + P}{6}
  \]
- **When to Use**:
  - When uncertainty needs to be factored into planning.
  - For more accurate and risk-aware estimates.
- **Example**:  
  _"Best case: 3 days, worst case: 10 days, most likely: 6 days. Expected time = (3 + 4×6 + 10) ÷ 6 ≈ 6.2 days."_

## 5. Story Points (Agile Estimation)

- **Description**: Assigns effort values to user stories based on complexity, risk, and unknowns, often using Fibonacci-like sequences (1, 2, 3, 5, 8, etc.).
- **When to Use**:
  - Agile teams working with Scrum or Kanban.
  - When estimating development effort without tying it directly to time.
- **Example**:  
  _"This user story is a 5 because it's more complex than a 3 but not as large as an 8."_

## Choosing the Right Estimation Method

| **Method**         | **Accuracy** | **Best Used For**                            |
| ------------------ | ------------ | -------------------------------------------- |
| SWAG               | Very Low     | Quick ballpark figures, informal discussions |
| ROM                | Low          | Early feasibility, budget planning           |
| T-Shirt Sizing     | Medium       | Agile backlog sizing, high-level estimates   |
| Three-Point (PERT) | High         | Risk-aware estimation, detailed planning     |
| Story Points       | Medium-High  | Agile development, effort-based planning     |
