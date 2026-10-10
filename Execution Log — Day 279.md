**Day 279 — Execution Log | Date : 25/09/2026** 



**Session:** Micro



**Topic:** Context switching and scheduling overhead



**Core Concepts:**

* The OS saves one task's execution context and restores another's.
* Context switching enables multitasking.
* Excessive switching consumes CPU time and can disturb cache/locality.
* Scheduling must balance fairness, responsiveness, and overhead.



**What I Learned:**

More frequent switching isn't automatically better.

Fairness must be achieved without wasting excessive CPU capacity.



**Key Systems Insight:**

The scheduler is itself part of the system's overhead.



**Connection:**

Resource contention → scheduling → priority/fairness → CPU affinity → context switching.



**Foundation Principle:**

Context switching enables sharing, but excessive switching reduces useful work.

