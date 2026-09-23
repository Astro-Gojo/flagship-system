**Day 264 — Execution Log | Date : 11/09/2026**



**Session:** Micro



**Topic:** Saga Coordination Models (Orchestration \& Choreography)



**Core Concepts:**

* Saga orchestration
* Saga choreography
* Central coordinator
* Event-driven communication
* Workflow visibility
* Distributed coordination complexity
* Scalability of system interactions



**What I Learned:**

* Orchestration uses a central component to control the Saga workflow.
* The orchestrator explicitly tells services which step to perform.
* This makes the overall workflow easier to visualize and reason about.
* Choreography distributes coordination across services using events.
* Services react to events and trigger subsequent actions.
* Choreography removes the need for one central workflow controller.
* However, as the number of services and event relationships grows, understanding the global workflow becomes increasingly difficult.



**Key Insight From Reasoning:**

Reacting to two events is fundamentally easier to reason about than reacting to two hundred events.



**Key Systems Insight:**

Reducing centralized coordination does not remove complexity—it can move the complexity into the interactions between services.



**Connection:**

Saga → Orchestration → Choreography → Event-driven Systems



**Foundation Principle:**

Distributed control can reduce central dependency while increasing global reasoning complexity.

