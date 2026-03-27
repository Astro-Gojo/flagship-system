**Day: 95 | Execution log | Date : 26/03/2026**

**Session Type:** Micro Session



**Topic:** Complete Critical Section



**Concept:**

A critical section must include both the update of shared data and any dependent logic.



**Issue:**

Protecting only the variable update can still lead to incorrect behavior when condition checks are outside the lock.



**Fix:**

Include both update and condition check inside the lock.



**Example:**

with lock:

&#x20;   counter += 1

&#x20;   if counter == 100000:

&#x20;       print("Reached target")



**Key Insight:**

Synchronization must cover all operations that depend on shared state.



**Systems Engineering Principle:**

Correctness requires protecting both state modification and decision logic.

