# Versioning

Versioning is the practice of assigning unique identifiers to successive releases of software or systems so that changes can be tracked, communicated, and managed with clarity. It provides a shared language across engineering, product, and operations teams, making it easier to understand what has changed, how significant those changes are, and how they affect compatibility or deployment.

Effective versioning helps with:

- **Predictability**: Teams can infer the impact of an update before reading a changelog.
- **Coordination**: Multiple services, libraries, and components can evolve together without unexpected breakage.
- **Governance**: Release processes become more disciplined, enabling safer roll-outs and roll-backs.
- **Long-term maintenance**: Older branches or major lines of a product can be supported with explicit clarity.

Several established schemes provide structure for assigning version identifiers:

## Semantic Versioning
Semantic Versioning, often written as *MAJOR.MINOR.PATCH*, ties the version number to the scope of change.  
- A **major** increment indicates incompatible API or behaviour changes.  
- A **minor** increment signals new features added in a backwards-compatible way.  
- A **patch** increment reflects backwards-compatible bug fixes.  
This approach is widely used in libraries and platforms where dependency management is critical.

## Calendar Versioning
Calendar Versioning encodes the release date into the version itself, for example *2025.03* or *25.3.1*. It suits products with regular or time-based release cycles, and makes it immediately clear how recent a version is. It is common in operating systems, infrastructure software, and tools with predictable cadences.

## Zer0ver
Zer0ver extends the idea that software in continuous flux may never truly be “stable” and therefore keeps the major version at zero. Everything remains *0.x.x*, signalling that breaking changes are expected at any time. It is sometimes adopted by early-stage projects or experimental tools.

Choosing a versioning approach depends on the release discipline of the organisation, the stability guarantees expected by users or downstream systems, and how tightly coupled the software is within a larger ecosystem. The key is consistency: once a scheme is selected, applying it rigorously builds trust and reduces operational risk.

## Serial / Incremental Versioning
A simple, linear increment such as *1, 2, 3…* or *build-1247*.  
It does not encode meaning about compatibility or release content; it simply reflects the order of builds.  
Often used in internal tooling, automated build pipelines, and firmware.

## Build Metadata / Revision-Based Versioning
Versions are derived from source control metadata, for example:
- The Git commit hash  
- The number of commits since a tag  
- A CI build number  

Examples might look like: *1.4.0+githash*, *r10234*, or *10.2.5-build.341*.  
This approach works well for continuous delivery, allowing each build to be traced precisely to source code.

## Epoch-Based Versioning
Some packaging systems (such as Debian) support an **epoch**, a leading integer that overrides all other comparison rules.  
For example: *2:1.4.0* supersedes *1:9.9.9*.  
Epochs are rarely used unless a project needs to reset or correct a broken versioning sequence.

## Alphanumeric / Name-Based Versioning
Some teams use codenames or a combination of names and numbers, for example:
- Ubuntu’s *Bionic Beaver*, *Focal Fossa*  
- Android’s dessert-themed releases  
- Internal project tracks named after places or themes  

These usually run in parallel with a numeric version, but occasionally stand alone.

## Date + Sequence Hybrid
A structured but flexible format such as:
- *2025.03.15.1* (date plus build of the day)  
- *2025.3-beta.2* (calendar-based with additional stability markers)  

This works well for systems with multiple releases on the same day or complex branching models.

## External references

- [Semantic versioning](https://semver.org/)
- [Calendar versioning](https://calver.org/)
- [Zer0ver](https://0ver.org/)
