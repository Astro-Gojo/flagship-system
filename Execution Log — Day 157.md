**Day 157 — Execution Log | Date : 27/05/2026**



**Session Type:** Core Session



**Topic:** Amdahl’s Law \& Limits of Parallel Scalability



**Concepts Learned:**

* Amdahl’s Law explains the limits of parallel speedup.
* Sequential portions of a system limit maximum scalability.
* Adding more CPUs mainly improves the parallelizable portion of workloads.
* Real-world bottlenecks include:

  * lock contention
  * sequential coordination
  * centralized shared resources
* Excessive parallelism introduces coordination and synchronization overhead.



**Key Insights:**

* Scalability bottlenecks matter more than raw hardware power.
* Optimizing bottlenecks can improve entire system throughput.
* Parallel systems eventually hit diminishing returns.
* Coordination overhead can reduce performance despite additional hardware.



**Systems Engineering Principle:**

Efficient scalable systems minimize:

* sequential bottlenecks
* shared coordination
* synchronization overhead

while maximizing independent parallel execution.



**Progression:**

Concurrency understanding expanded from:

* memory locality

→ hardware-aware scaling

→ bottleneck analysis

→ theoretical limits of parallelism

