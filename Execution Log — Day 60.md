# Day 60 — Priority Inversion, Deadlocks & RTOS Stability

## Main Quest — Real-Time Systems Deepening

### 1. Priority Inversion
Learned how a low-priority task holding a resource can block a high-priority task, causing deadline violations.

### 2. Priority Inheritance
Understood the RTOS solution:
Temporarily boost the priority of the resource-holding task to prevent medium-priority interference.

Key Insight:
Real-time systems are defined by timing guarantees, not just correctness.

---

### 3. Deadlocks
Studied deadlock conditions (Coffman conditions):
- Mutual exclusion
- Hold and wait
- No preemption
- Circular wait

Key Insight:
Deadlocks are harder to detect than race conditions because they fail silently — the system appears frozen rather than corrupted.

---

## Systems Growth
Progressed from:
Interrupts → Concurrency → Race Conditions → Critical Sections → Priority Inversion → Deadlocks

Understanding now includes:
- Preemption effects
- Scheduling dynamics
- Resource contention
- Timing guarantees
- System liveness vs safety

Status:
Main quest advancing into RTOS-level reasoning.
