**Day 156 — Execution Log | Date : 26/05/2026**



**Session Type:** Core Session



**Topic:** NUMA (Non-Uniform Memory Access)



**Concepts Learned:**

* NUMA means memory access latency is not uniform across CPUs.
* Large systems divide memory into NUMA nodes associated with CPU sockets.
* Local memory access is faster than remote memory access.
* Poor NUMA awareness causes:

  * latency increases
  * scalability loss
  * bandwidth bottlenecks
* Thread affinity and memory affinity help maintain locality.



**Key Insights:**

* At large scale, data movement can become more expensive than computation itself.
* Memory locality becomes critical in multi-core and multi-socket systems.
* Efficient systems minimize remote memory access and optimize placement.
* Hardware architecture directly affects scalability and performance behavior.



**Systems Engineering Principle:**

Scalable systems engineering requires optimization of:

* computation
* memory locality
* communication cost
* data movement



**Progression:**

Concurrency understanding expanded from:

* cache behavior

→ hardware-aware synchronization

→ memory locality

→ NUMA-aware scalability thinking



