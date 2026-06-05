**Day 162 — Execution Log | Date : 01/06/2026**



**Session Type:** Core Session



**Topic:** Consistency vs Availability in Distributed Systems



**Concepts Learned:**

* Distributed systems often face trade-offs between consistency and availability.
* Consistency ensures users observe the same data view across servers.
* Availability ensures requests receive responses despite failures.
* Network issues can cause temporary disagreement between servers.
* Different applications prioritize consistency or availability based on requirements.



**Key Insights:**

* Banking systems usually prioritize consistency because correctness is critical.
* Social media and similar applications can often tolerate temporary inconsistency.
* Distributed systems introduce coordination challenges similar to thread synchronization, but across machines.
* Network latency and failures become major design considerations at scale.



**Systems Engineering Principle:**

Engineering decisions should be driven by system requirements rather than pursuing a single ideal property.

Different workloads require different trade-offs between:

* correctness
* responsiveness
* availability
* complexity



**Progression:**

Systems understanding expanded from:

* memory coordination between threads

→ visibility and ordering

→ coordination between machines

→ distributed consistency trade-offs

