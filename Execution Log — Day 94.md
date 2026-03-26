**Day: 94 | Execution log | Date : 25/03/2026**

**Session Type:** Micro Session



**Topic:** Incomplete Critical Section



**Concept:**

Protecting only part of a shared operation can still lead to incorrect behavior.



**Scenario:**

Increment operation is protected by a lock, but the condition check is outside the lock.



**Issue:**

Multiple threads may observe the same condition and execute the same action.



**Example:**

if counter == 100000:

&#x20;   print("Reached target")



**Key Insight:**

Critical section must include both state modification and dependent logic.



**Systems Engineering Principle:**

Partial synchronization can still lead to race conditions in system behavior.

