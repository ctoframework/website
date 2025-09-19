# Pets vs Cattle Analogy in Infrastructure Management

The **“pets vs cattle”** analogy is a way to describe two different approaches to managing servers or infrastructure.

## Pets

- **Definition**: Individual machines treated as unique and irreplaceable.
- **Characteristics**:
  - Each has a distinct name (e.g. _web-server-1_, _db-primary_).
  - If one fails, you fix it manually (apply patches, reboot, troubleshoot).
  - Custom configurations are common.
  - Scaling is limited and slower due to manual care.
- **Typical Use Cases**:
  - Legacy systems.
  - Highly specialised workloads that can’t be easily replicated.

## Cattle

- **Definition**: Large numbers of essentially identical machines that are disposable and interchangeable.
- **Characteristics**:
  - Machines are numbered or automatically named (e.g. _server-001_, _server-002_).
  - If one fails, it’s terminated and replaced automatically.
  - Configuration and deployment are automated.
  - Scaling is fast and horizontal.
- **Typical Use Cases**:
  - Cloud-native applications.
  - Container orchestration platforms.
  - Auto-scaling environments.

## Why It Matters

Moving from **pets** to **cattle**:

- Reduces operational overhead.
- Improves reliability and consistency.
- Enables rapid scaling and recovery.
- Aligns with infrastructure-as-code and immutable deployment practices.

In short, **“pets” require care and attention**, whereas **“cattle” can be replaced without disruption**. This mindset shift is key to modern infrastructure management.
