**Day 106 — Execution Log | Date : 06/04/2026**

**Session Type:** Micro Session



**Topic:** Mutex vs Coordination



**Concept:**

Mutex ensures only one thread accesses shared resource at a time.



**Limitation:**

* Mutex does NOT manage:

  * buffer full condition
  * buffer empty condition



**Key Insight:**

* Mutex = safety (no race condition)
* Coordination = when threads should act



**Core Principle:**

Correct systems require both mutual exclusion and coordination.



**Outcome:**

* Understood limitation of mutex
* Recognized need for additional control mechanisms

