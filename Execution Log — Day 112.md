**Day 112 — Execution Log | Date : 12/04/2026**



**Session Type:** Core Session



**Topic:** Priority Inversion



**Concept:**

Priority inversion occurs when a high-priority thread is indirectly blocked by a lower-priority thread due to resource locking and scheduling behavior.



**Scenario Learned:**

Low-priority thread holds mutex

High-priority thread waits for it

Medium-priority thread runs continuously

Low-priority thread cannot release mutex



**Key Problem:**

High-priority thread gets delayed due to scheduling interference



**Solution:**

Priority inheritance → temporarily boosts low-priority thread



**Core Insight:**

System correctness alone is not enough; scheduling interactions can break expected behavior.



**Outcome:**

Understood interaction between synchronization and scheduling

Learned real-world failure case

Strengthened OS-level system thinking

