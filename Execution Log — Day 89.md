**Day: 89 | Execution log | Date : 20/03/2026**



**Session Type: Standard Session**



**Topic: Lock-Free Programming (Introduction)**



**Concept:**

Lock-free programming avoids traditional locks by using atomic operations like Compare-And-Swap (CAS).



**Working Principle:**

Threads attempt operations optimistically.

If a conflict occurs, the operation fails and is retried.



**Example:**

do:

&#x20;   old = counter

while CAS(counter, old, old + 1) fails



**Key Insight:**

Lock-free systems avoid blocking, deadlocks, and reduce contention compared to locks.



**Tradeoff:**

Threads may retry multiple times, leading to CPU usage due to repeated attempts.



**Systems Engineering Principle:**

Lock-free design improves scalability but requires careful handling of retries and correctness.

