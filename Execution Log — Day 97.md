**Day: 97 | Execution log | Date : 28/03/2026**

**Session Type:** Micro Session



**Topic:** Thread Execution Order



**Concept:**

Locks ensure mutual exclusion but do not guarantee execution order.



**Observation:**

Even with correct synchronization, output may appear out of order.



**Reason:**

Thread scheduling is controlled by the operating system and is non-deterministic.



**Key Insight:**

Correctness and ordering are separate concerns in concurrent systems.



**Systems Engineering Principle:**

Synchronization ensures data integrity, not execution sequence.

