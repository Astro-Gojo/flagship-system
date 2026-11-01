**Day 288 — Execution Log | Date : 04/10/2026**



**Topic:** Semaphores



**session:** Micro 



**Core Concepts:**

* Semaphore maintains a counter representing available permits.
* Wait/acquire obtains a permit or blocks when none is available.
* Signal/release returns a permit.
* Binary semaphores represent two states; counting semaphores support multiple permits.



**What I Learned:**

* Semaphores can control access to a limited resource pool.
* Multiple threads can hold permits simultaneously.
* A permit must be released correctly after its intended use.
* Mutexes and semaphores have different ownership and coordination semantics.



**Key Systems Insight:**

Synchronization must reflect the resource's actual constraints. Allowing concurrent access is useful only when the underlying resource supports it.



**Failure Modes / Trade-offs:**

* Permit leaks.
* Incorrect over-release.
* Starvation.
* Deadlocks caused by flawed synchronization designs.



**Hardware Insight:**

A semaphore can limit concurrent operations on a shared resource in the Raspberry Pi battery-monitoring system. However, an I²C bus requiring serialized transactions needs suitable bus-level synchronization rather than simply allowing multiple concurrent operations.



**Foundation Principle:**

A semaphore manages resource availability through permits. Correct synchronization requires acquiring and releasing permits consistently.

