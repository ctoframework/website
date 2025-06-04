# The C4 Model: Visualising Software Architecture

The C4 Model, created by [Simon Brown](https://c4model.com), is a structured approach to visualising software architecture across multiple levels of detail. It provides a clear and consistent way to describe the static structure of a system in a way that is understandable by both technical and non-technical stakeholders.

The name **C4** stands for four hierarchical diagram types:

1. **Context**
2. **Container**
3. **Component**
4. **Code**

This model supports better communication, documentation, and design discussions, particularly in complex, distributed systems.

---

## 1. System Context Diagram

The **System Context Diagram** shows the system in scope and how it interacts with users and other systems. It answers the question: _"What does the system do, and who does it interact with?"_

### Purpose:

- High-level overview for all audiences.
- Helps frame the boundaries and relationships of the system.

```mermaid
flowchart TB

subgraph personalBankingCustomer[Personal Banking Customer]
    h1[-Person-]:::type
    d1[A customer of the bank, with \n personal bank accounts]:::description
end
personalBankingCustomer:::person

subgraph internetBankingSystem[Internet Banking System]
    h2[-Software System-]:::type
    d2[Allows customers to view \n information about their bank \n banks, and make payments]:::description
end
internetBankingSystem:::internalSystem

subgraph mainframeBankingSystem[Mainframe Banking System]
    h3[-Software System-]:::type
    d3[Stores all of the core banking \n information about customers, \n accounts, transactions etc]:::description
end
mainframeBankingSystem:::externalSystem

subgraph emailSystem[Email System]
    h4[-Software System-]:::type
    d4[The internal Microsoft Exchange \n email system]:::description
end
emailSystem:::externalSystem

personalBankingCustomer--Views account \n balances, and \n makes payments \n using-->internetBankingSystem
internetBankingSystem--Gets accounts \n information from, \n and makes \n payments using-->mainframeBankingSystem
internetBankingSystem--Sends emails using--> emailSystem
emailSystem--Sends emails to-->personalBankingCustomer

%% Element type definitions

classDef person fill:#08427b
classDef internalSystem fill:#1168bd
classDef externalSystem fill:#999999

classDef type stroke-width:0px, color:#fff, fill:transparent, font-size:12px
classDef description stroke-width:0px, color:#fff, fill:transparent, font-size:13px
```

---

## 2. Container Diagram

The **Container Diagram** zooms into the system, showing the main containers (applications, services, databases, etc.) and how they interact. A container here is something that executes code or stores data.

### Purpose:

- Understand the technology stack and responsibilities.
- Clarify how the system is decomposed at a high level.

```mermaid
flowchart TB

subgraph personalBankingCustomer[Personal Banking Customer]
    h1[-Person-]:::type
    d1[A customer of the bank, with \n personal bank accounts]:::description
end
personalBankingCustomer:::person

personalBankingCustomer--Visits bigbank.com using HTTPS-->webApplication
personalBankingCustomer--Views account \n balancs, and \n makes payments \n using-->singlePageApplication
personalBankingCustomer--Views account \n balancs, and \n makes payments \n using-->mobileApp

subgraph internetBankingSystem[Internet Banking System]
    subgraph webApplication[Web Application]
        direction LR
        h2[Container: Java and Spring MVC]:::type
        d2[Delivers the static content and the \n Internet banking single page \n application]:::description
    end
    webApplication:::internalContainer

    subgraph singlePageApplication[Single Page Application]
        direction LR
        h3[Container: JavaScript and Angular]:::type
        d3[Provides all of the Internet banking \n fuctionality to customers via their \n web browser]:::description
    end
    singlePageApplication:::internalContainer

    subgraph mobileApp[Mobile App]
        direction LR
        h4[Container: Xamarin]:::type
        d4[Provides a limited subset of the \n Internet banking functionality to \n customers via their mobile device]:::description
    end
    mobileApp:::internalContainer

    subgraph apiApplication[API Application]
        direction LR
        h5[Container: Java and Spring MVC]:::type
        d5[Provides Internet banking \n functionality via a JSON/HTTP API]:::description
    end
    apiApplication:::internalContainer

    subgraph database[Database]
        direction LR
        h6[Container: Oracle Database Schema]:::type
        d6[Stores user registration information, \n hashed authentication credentials, \n access logs, etc]:::description
    end
    database:::internalContainer

    webApplication--Delivers to the \n customer's web \n browser-->singlePageApplication
    singlePageApplication--Makes API calls to-->apiApplication
    mobileApp--Makes API calls to-->apiApplication
    apiApplication--Reads from and \n writes to-->database
end

apiApplication--Sends emails using-->emailSystem
apiApplication--Makes API calls to-->mainframeBankingSystem

subgraph mainframeBankingSystem[Mainframe Banking System]
    h98[-Software System-]:::type
    d98[Stores all of the core banking \n information about customers, \n accounts, transactions etc]:::description
end
mainframeBankingSystem:::externalSystem

subgraph emailSystem[Email System]
    h99[-Software System-]:::type
    d99[The internal Microsoft Exchange \n email system]:::description
end
emailSystem:::externalSystem

emailSystem--Sends emails to-->personalBankingCustomer

%% Element type definitions

classDef person fill:#08427b
classDef internalContainer fill:#1168bd
classDef externalSystem fill:#999999

classDef type stroke-width:0px, color:#fff, fill:transparent, font-size:12px
classDef description stroke-width:0px, color:#fff, fill:transparent, font-size:13px
```

_Note: In a full C4 diagram, these containers would be drawn within a system boundary box to indicate they belong to the same system._

---

## 3. Component Diagram

The **Component Diagram** drills down into a single container, detailing its internal components (services, modules, controllers, etc.) and their relationships.

### Purpose:

- Understand the major building blocks of a container.
- Support modularity and team boundaries.

```mermaid
flowchart TB

subgraph singlePageApplication[Single Page Application]
    direction LR
    h3[Container: JavaScript and Angular]:::type
    d3[Provides all of the Internet banking\nfuctionality to customers via their\nweb browser]:::description
end
singlePageApplication:::internalContainer

subgraph mobileApp[Mobile App]
    direction LR
    h4[Container: Xamarin]:::type
    d4[Provides a limited subset of the\nInternet banking functionality to\ncustomers via their mobile device]:::description
end
mobileApp:::internalContainer

subgraph database[Database]
    direction LR
    h6[Container: Oracle Database Schema]:::type
    d6[Stores user registration information, \n hashed authentication credentials, \n access logs, etc]:::description
end
database:::internalContainer

subgraph mainframeBankingSystem[Mainframe Banking System]
    h98[-Software System-]:::type
    d98[Stores all of the core banking \n information about customers, \n accounts, transactions etc]:::description
end
mainframeBankingSystem:::externalSystem

subgraph emailSystem[Email System]
    h99[-Software System-]:::type
    d99[The internal Microsoft Exchange \n email system]:::description
end
emailSystem:::externalSystem

singlePageApplication--Make API calls to-->signInController
singlePageApplication--Make API calls to-->resetPasswordController
singlePageApplication--Make API calls to-->accountsSummaryController
mobileApp--Make API calls to-->signInController
mobileApp--Make API calls to-->resetPasswordController
mobileApp--Make API calls to-->accountsSummaryController

subgraph apiApplication[API Application]
    subgraph signInController[Sign In Controller]
        direction LR
        h10[Component: Spring MVC Rest Controller]:::type
        d10[Allows users to sign in to the Internet \n Banking System]:::description
    end
    signInController:::internalComponent

    subgraph resetPasswordController[Reset Password Controller]
        direction LR
        h20[Component: Spring MVC Rest Controller]:::type
        d20[Allows users to reset their passwords \n with a single use URL]:::description
    end
    resetPasswordController:::internalComponent

    subgraph accountsSummaryController[Accounts Summary Controller]
        direction LR
        h30[Component: Spring MVC Rest Controller]:::type
        d30[Provides customers with a summary \n of their bank accounts]:::description
    end
    accountsSummaryController:::internalComponent

    subgraph securityComponent[Security Component]
        direction LR
        h40[Component: Spring Bean]:::type
        d40[Provides functionality related to \n signing in, changing passwords, etc]:::description
    end
    securityComponent:::internalComponent

    subgraph emailComponent[Email Component]
        direction LR
        h50[Component: Spring Bean]:::type
        d50[Sends emails to users]:::description
    end
    emailComponent:::internalComponent

    subgraph mainframeBankingSystemFacade[Mainframe Banking System Facade]
        direction LR
        h60[Component: Spring Bean]:::type
        d60[A facade onto the mainframe \n banking system]:::description
    end
    mainframeBankingSystemFacade:::internalComponent

    signInController--Uses-->securityComponent
    resetPasswordController--Uses-->securityComponent
    resetPasswordController--Uses-->emailComponent
    accountsSummaryController--Uses-->mainframeBankingSystemFacade
end

securityComponent--Reads from and \n writes to-->database
emailComponent--Sends email using-->emailSystem
mainframeBankingSystemFacade--Uses-->mainframeBankingSystem

%% Element type definitions

classDef person fill:#08427b
classDef internalContainer fill:#1168bd
classDef internalComponent fill:#4b9bea
classDef externalSystem fill:#999999

classDef type stroke-width:0px, color:#fff, fill:transparent, font-size:12px
classDef description stroke-width:0px, color:#fff, fill:transparent, font-size:13px
```

---

## 4. Code (Class) Diagram

The **Code Diagram** is the most granular level, usually auto-generated. It shows the internal structure of a component using classes, interfaces, and their relationships.

### Purpose:

- Reference for developers.
- Explores implementation-level detail.

```mermaid
classDiagram
    class Controller {
        +handleRequest()
    }
    class Service {
        +process()
    }
    class Repository {
        +fetchData()
    }

    Controller --> Service
    Service --> Repository
```

---

## Why Use C4?

- Encourages **clear communication** across teams.
- Helps **standardise documentation** practices.
- Adaptable for various audiences — from business leaders to engineers.
- Complements agile and DevOps practices by making architecture _visible_ and _evolvable_.

---

## Summary

| Level     | Focus                               | Audience                          |
| --------- | ----------------------------------- | --------------------------------- |
| Context   | External interactions               | Broad (technical + non-technical) |
| Container | Applications & data stores          | Architects, engineers             |
| Component | Logical structure within containers | Engineers, developers             |
| Code      | Class-level detail                  | Developers                        |

## References

- [Wikipedia](https://en.wikipedia.org/wiki/C4_model)
