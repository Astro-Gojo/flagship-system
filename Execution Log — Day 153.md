**Day 153 — Execution Log | Date : 23/05/2026**



**Session Type:** Core Session



**Topic:** Reader–Writer Locks (Read-Heavy Optimization)



**Concepts Learned:**

* Reader–Writer locks allow:

  * multiple concurrent readers
  * exclusive writers
* RW locks improve scalability in read-heavy systems.
* Normal mutexes unnecessarily block parallel readers.
* Writer starvation can occur if readers continuously dominate access.
* RW locks introduce additional coordination complexity and overhead.



**Key Insights:**

* Efficient systems maximize safe parallelism whenever possible.
* RW locks are especially powerful on multi-core systems because many readers can execute simultaneously across CPU cores.
* Synchronization mechanisms must match workload characteristics:

  * read-heavy
  * write-heavy
  * contention level
  * hardware parallelism



**Systems Engineering Principle:**

Concurrency optimization is about balancing:

* safety
* scalability
* coordination overhead
* hardware utilization



**Progression:**

Concurrency understanding expanded from:

* efficient waiting

→ worker reuse

→ scalable coordination

→ read-parallel optimization

