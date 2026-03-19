**Day: 88 | Execution log | Date : 19/03/2026**

**Session Type: Micro Session**



**Topic: Lock Selection Strategy**



**Concept:**

Different synchronization mechanisms should be chosen based on expected waiting time.



**Cases:**

1\. Short critical section → Spinlock

2\. Long critical section → Mutex (sleep)

3\. Unknown/mixed workload → Hybrid (spin + sleep)



**Key Insight:**

All locks provide correctness, but choosing the right one determines system performance.



**Example:**

For a shared resource with \~200 ms wait time, a mutex is preferred over a spinlock to avoid CPU waste.



**Systems Engineering Principle:**

Synchronization design must consider both correctness and efficiency.

