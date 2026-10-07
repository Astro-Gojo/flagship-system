**Day 277 — Execution Log | Date : 23/09/2026**



**Session:** Micro



**Topic:** Reserved capacity, work conservation, controlled sharing



**Core Concepts:**

* Strict reservations improve predictability but may leave resources idle.
* Work-conserving systems try to use available capacity.
* Controlled sharing allows workloads to temporarily benefit from spare resources while preserving minimum guarantees.
* Scheduling policies can reclaim capacity when another workload needs it.



**What I Learned:**

* Resource sharing doesn't have to mean giving up isolation completely.
* Guaranteed minimum + opportunistic extra capacity provides a useful middle ground.



**Key Systems Insight:**

A workload can use spare capacity without being entitled to permanently own it.



**Trade-off:**

Better utilization comes with potentially less predictable performance for workloads using borrowed capacity.



**Foundation Principle:**

Good resource management balances utilization, isolation, and predictability.

