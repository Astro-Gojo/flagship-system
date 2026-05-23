**Day 152 — Execution Log | Date : 22/05/2026**



**Session Type:** Normal Session



**Topic:** Thread Pools \& Worker Reuse



**Concepts Learned:**

* Thread pools reuse worker threads instead of repeatedly creating/destroying them.
* Worker threads continuously pull tasks from a shared task queue.
* Condition variables allow workers to sleep efficiently until tasks arrive.
* Thread pools improve:

  * scalability
  * latency
  * resource stability
  * performance efficiency
* Excessive thread creation causes scheduler and context-switch overhead.



**Key Insights:**

* Efficient systems reuse expensive resources whenever possible.
* Too many threads can reduce performance despite increasing concurrency.
* CPU-bound workloads usually align closer to CPU core count.
* I/O-bound workloads can support more threads because many threads spend time waiting.



**Systems Engineering Principle:**

Scalable systems balance concurrency carefully to maximize throughput without overwhelming hardware or schedulers.



**Progression:**

Concurrency understanding expanded from:

* synchronization

→ efficient waiting

→ worker reuse

→ scalability-aware thread management

