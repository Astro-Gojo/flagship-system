**Day: 93 | Execution log | Date : 24/03/2026**

**Session Type:** Micro Session



**Topic:** System Scaling with Threads



**Concept:**

Increasing the number of threads increases total system workload.



**Experiment:**

3 threads, each performing 50000 increments.



**Calculation:**

Total increments = 3 × 50000 = 150000



**Observation:**

With proper synchronization (mutex), the system produces correct results.



**Key Insight:**

System output depends on the combined work of all concurrent threads.



**Systems Engineering Principle:**

Scalability requires understanding how multiple components contribute to total system behavior.

