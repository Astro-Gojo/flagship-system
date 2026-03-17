**Day: 86 | Execution log | Date : 17/03/2026**

**Session Type: Micro Session**



**Topic: Spinlock using CAS**



**Concept:**

Spinlocks can be implemented using Compare-And-Swap (CAS).



**Implementation Idea:**

while CAS(lock, 0, 1) fails

&#x20;   keep trying



**Meaning:**

If lock is free (0), CAS sets it to 1 and thread enters.

If lock is taken (1), CAS fails and thread keeps retrying.



**Unlock:**

lock = 0



**Key Insight:**

CAS allows threads to compete for a lock using hardware-level atomic operations without OS involvement.



**Limitation:**

If many threads spin on the lock, CPU resources are wasted due to continuous retries.



**Systems Engineering Principle:**

Spinlocks are efficient only for very short critical sections and low contention scenarios.

