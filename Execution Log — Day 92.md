**Day: 92 | Execution log | Date : 22/03/2026**

**Session Type: Build Session**



**Topic: Basic Concurrent System (Race Condition + Mutex)**



**Concept:**

A shared counter accessed by multiple threads can lead to race conditions.



**Observation:**

Without synchronization, multiple threads interfere with each other, producing incorrect results.



**Example:**

counter += 1 is not atomic and can be interrupted.



**Fix:**

Using a mutex ensures only one thread accesses the critical section at a time.



with lock:

&#x20;   counter += 1



**Key Insight:**

Race conditions are correctness issues and do not disappear by reducing execution frequency.



**Systems Engineering Principle:**

Correctness must be guaranteed regardless of probability of failure.

