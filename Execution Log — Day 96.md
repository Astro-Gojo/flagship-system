**Day: 96 | Execution log | Date : 27/03/2026**

**Session Type:** Micro Session



**Topic:** Lock Scope vs Performance



**Concept:**

Even correct synchronization can lead to poor performance if locks are held too long.



**Issue:**

Long operations inside a lock block other threads unnecessarily.



**Example:**

time.sleep(2) inside critical section increases wait time for other threads.



**Fix:**

Keep critical sections minimal and move non-essential work outside the lock.



**Key Insight:**

Efficiency depends on minimizing time spent holding locks.



**Systems Engineering Principle:**

Design synchronization to balance correctness and performance.

