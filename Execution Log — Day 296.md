**Execution Log — Day 296 | Date : 12/10/2026**



**Topic:** Page Faults \& Demand Paging



**Session:** Micro



**Core Concepts:**

* Page faults.
* Demand paging.
* Storage-backed page loading.
* Page-table updates.
* Thrashing.



**What I Learned:**

* Page faults require OS intervention.
* Pages can be loaded from storage into RAM when needed.
* Demand paging avoids loading unused pages unnecessarily.
* Excessive page faults can degrade system performance.
* Storage I/O latency can become a major bottleneck.



**Key Systems Insight:**

A powerful CPU cannot compensate for a system constantly waiting on slow storage operations.



**Hardware Insight:**

On the Raspberry Pi, excessive page faults can cause storage I/O to become a bottleneck, particularly when using a microSD card.



**Foundation Principle:**

Memory management must balance RAM utilization, storage I/O, and execution performance.

