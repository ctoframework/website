# Threat modelling

Threat modeling is a structured approach used in cybersecurity to identify, assess, and mitigate security threats in applications, systems, or networks. It helps organizations proactively address potential security risks by analyzing vulnerabilities and designing appropriate defenses.

### Importance

- Identifies security weaknesses early in development.
- Helps prioritize security efforts based on risk levels.
- Reduces costs associated with fixing security issues later.
- Enhances overall security posture by applying defensive measures.

### Key components

- Assets – What needs protection? (e.g., data, servers, user credentials)
- Threats – What could go wrong? (e.g., data breaches, denial-of-service attacks)
- Attackers – Who might attack? (e.g., hackers, insiders, competitors)
- Vulnerabilities – Where are the weaknesses? (e.g., unpatched software, weak encryption)
- Mitigations – How can we defend against threats? (e.g., encryption, access controls)

### Common Threat Modeling Methodologies

#### STRIDE (Microsoft) – Identifies six types of threats:

- Spoofing (impersonation)
- Tampering (unauthorized modification)
- Repudiation (denying actions)
- Information Disclosure (data leaks)
- Denial of Service (disrupting availability)
- Elevation of Privilege (unauthorized access)

#### DREAD – Helps assess risk impact using five factors:

- Damage potential
- Reproducibility
- Exploitability
- Affected users
- Discoverability

#### PASTA (Process for Attack Simulation and Threat Analysis) – A risk-centric approach aligning security with business objectives.

#### OCTAVE (Operationally Critical Threat, Asset, and Vulnerability Evaluation) – Focuses on organizational risk assessment.

#### Kill Chain (MITRE ATT&CK Framework) – Models attacker tactics and techniques in different stages of an attack.

### Threat Modeling Process

- Define Scope & Objectives – Determine what needs to be protected and why.
- Identify Assets & Dependencies – List important assets and their dependencies.
- Analyze Threats & Vulnerabilities – Identify potential attack vectors.
- Assess Risk & Prioritize Threats – Rank threats based on impact and likelihood.
- Develop & Implement Mitigations – Apply security measures to reduce risks.
- Review & Update – Continuously update threat models to address new threats.

### Who Should Perform Threat Modeling?

- Security teams
- Developers
- Architects
- Risk management teams
- DevOps teams

## Tools

- [OWASP Threat Dragon](https://www.threatdragon.com/)
