**Day 285 — Execution Log | Date : 01/10/2026**



**Topic:** Race Conditions \& Shared State



**Session:** Micro



**Core concepts:**

* Threads can share memory and access the same variables.
* Multi-step operations can interleave in unsafe ways.
* A lost update occurs when concurrent modifications overwrite one another.
* Race conditions can occur on single-core and multicore systems.



**What I learned:**

* An increment is not necessarily an indivisible operation.
* The OS can switch between threads between individual steps.
* Correctness may depend on the ordering of concurrent operations.



**Failure modes:**

* Lost updates.
* Inconsistent shared state.
* Timing-dependent bugs that are difficult to reproduce.



**Hardware insight:**

Multiple cores can access shared memory concurrently, but even one core can experience unsafe interleavings between threads.



**Connection:**

Processes and threads → concurrency and parallelism → shared state → race conditions → synchronization.



**Foundation principle:**

Shared operations must be coordinated whenever unsafe interleavings could violate program correctness.

