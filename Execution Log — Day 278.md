**Day 278 — Execution Log | Date : 24/09/2026**



**Session:** Micro



**Topic:** CPU affinity, CPU pinning, workload placement



**Core Concepts:**

* CPU affinity restricts where a process/thread can execute.
* Pinning can reduce direct CPU contention.
* Dedicated CPU placement can improve predictability and locality.
* Excessive pinning can leave resources underutilized.



**What I Learned:**

CPU isolation isn't free.

Restricting workload movement can sacrifice flexibility.



**Key Systems Insight:**

Isolation and utilization are often competing goals.



**Hardware Insight:**

Software scheduling decisions directly affect physical CPU-core utilization.



**Foundation Principle:**

CPU affinity trades flexibility for isolation, locality, and potentially predictability.

