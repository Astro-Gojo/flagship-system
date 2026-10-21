**Day 284 — Execution Log | Date : 30/09/2026**



**Topic:** Concurrency vs Parallelism



**Session:** Micro



**Core concepts:**

* Concurrency allows multiple tasks to make progress over overlapping periods.
* Parallelism means multiple tasks execute simultaneously.
* A single CPU core can support concurrency through interleaving.
* Multiple cores can execute independent tasks in parallel.



**What I learned:**

* Adding CPU cores doesn't guarantee faster execution.
* Sequential work limits potential speedup.
* Synchronization overhead, lock contention, and memory bandwidth can limit performance.



**Key systems insight:**

Improving one resource doesn't remove every bottleneck. Overall performance depends on the entire workload and its constraints.



**Foundation principle:**

Concurrency organizes overlapping work; parallelism enables simultaneous execution. More cores help only when the workload can use them effectively.

