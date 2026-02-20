Execution Log — Day 61 (Main Quest)

Domain:

Operating Systems — Scheduling \& Real-Time Systems



Topics Covered:

1️⃣ Mechanical Context Switching

* CPU state components:

\-Program Counter

\-Registers

\-Stack Pointer

\-Flags

* Saving state to PCB
* Loading next task’s state
* Hardware-level overhead



2️⃣ Context Switch Cost

* Register save/restore cycles
* Cache disruption
* Pipeline flush
* CPU time lost to overhead
* Trade-off between responsiveness and switching cost



3️⃣ Preemption vs Context Switch

* Preemption → Scheduling decision
* Context Switch → Mechanism execution
* Relationship: Preemption triggers context switch



4️⃣ Time Slice Trade-offs

* Smaller slice → More responsive, more overhead
* Larger slice → Less overhead, lower responsiveness
* Deterministic balancing in RTOS



5️⃣ Priority Inversion (Reinforced)

* Low-priority task holding resource
* High-priority task blocked
* Medium-priority task executing
* Leads to deadline violation
* Dangerous in real-time systems



6️⃣ Real-Time System Principle

* Real-time ≠ fast
* Real-time = deterministic + deadline guarantee
* Preemption required for critical task execution



Cognitive Notes:

* Retrieval difficulty observed
* Recognition strong
* Recall strengthening through repetition
* Concept consolidation improved during session
