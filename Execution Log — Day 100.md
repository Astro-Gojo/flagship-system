**Day: 100 | Execution log | Date : 31/03/2026**



**Session Type:** Consolidation + Application



**Topic:** Concurrent System Design



**Concept:**

Designing a correct concurrent system requires proper synchronization of both state updates and dependent logic.



**Scenario:**

Multiple threads update a shared counter and trigger an action when a condition is met.



**Correct Design:**

with lock:

&#x20;   counter += 1

&#x20;   if counter == 100000:

&#x20;       print("Done")



**Key Insights:**

\- Race conditions occur without synchronization.

\- Critical sections must include both state modification and dependent checks.

\- Correctness requires full protection of shared state interactions.



**Systems Engineering Principle:**

Reliable system design depends on combining correctness, synchronization scope, and controlled execution logic.

