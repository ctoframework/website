# SOLID Principles

SOLID is a set of five principles in object-oriented programming that help developers write maintainable, scalable, and flexible code. The principles were introduced by Robert C. Martin (Uncle Bob) and are commonly applied in software design, particularly in agile and clean code practices.

## The SOLID Principles:

### 1. **S - Single Responsibility Principle (SRP)**

**A class should have only one reason to change.**

- Each class should only have **one responsibility** or function.
- This makes code easier to understand, maintain, and test.
- **Example:** Instead of a `Report` class handling both data storage and printing, split it into `ReportData` (handles data) and `ReportPrinter` (handles printing).

---

### 2. **O - Open/Closed Principle (OCP)**

**Software entities (classes, modules, functions) should be open for extension but closed for modification.**

- You should be able to **extend** functionality without modifying existing code.
- This is often achieved using **inheritance** and **interfaces**.
- **Example:** Instead of modifying a `PaymentProcessor` class to handle new payment methods, define an interface `PaymentMethod` and implement different payment classes (`CreditCard`, `PayPal`, etc.).

---

### 3. **L - Liskov Substitution Principle (LSP)**

**Objects of a derived class must be substitutable for objects of the base class without altering correctness.**

- A subclass should **extend** the behavior of a parent class, not break it.
- **Example:** If `Bird` has a `fly()` method, then a `Penguin` subclass should not override it in a way that causes errors. Instead, `Bird` should be redesigned to separate flying and non-flying birds.

---

### 4. **I - Interface Segregation Principle (ISP)**

**Clients should not be forced to depend on interfaces they do not use.**

- Large, general-purpose interfaces should be **split** into smaller, specific ones.
- **Example:** Instead of having one `Worker` interface with methods `work()` and `eat()`, separate it into `Workable` and `Eatable`, so that a `Robot` class doesn’t need to implement `eat()`.

---

### 5. **D - Dependency Inversion Principle (DIP)**

**High-level modules should not depend on low-level modules. Both should depend on abstractions.**

- Instead of depending on **concrete implementations**, depend on **abstractions (interfaces or abstract classes)**.
- **Example:** A `DatabaseService` class should depend on a `DatabaseInterface`, so it can switch from MySQL to PostgreSQL without changing the high-level logic.

---

## Benefits

- Improves **code maintainability** and **scalability**.
- Reduces **tight coupling**, making it easier to modify or extend code.
- Enhances **testability**, as smaller, single-purpose classes are easier to unit test.
