**Day 145 — Execution Log | Date : 15/05/2026**



**Session Type:** Core Session



**Topic:** Spinlocks



**Concept:**

A spinlock is a synchronization mechanism where a thread continuously checks a lock in a busy-wait loop until the lock becomes available.



**Key Learnings:**

* Spinlocks are based on busy waiting
* They provide low-latency synchronization for short waits
* Continuous spinning wastes CPU cycles
* Spinlocks are useful only when waiting times are expected to be very small



**Core Insight:**

Spinlocks trade CPU efficiency for faster synchronization response time.



**Outcome:**

* Strengthened understanding of low-level synchronization
* Connected busy waiting with practical lock design
* Improved reasoning about synchronization trade-offs and latency optimization

