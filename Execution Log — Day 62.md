Day 62 – Main Quest Execution Log

Focus: Concurrency \& Synchronization Foundations

Energy: 5–6/10

Session Type: Deep Systems Drill

🧠 Topics Covered:



1️⃣ Process (Systems Definition)

* A process = an executing program instance.
* Has its own:

\-Address space

\-Stack

\-Heap

\-Registers

* Isolation prevents memory interference.

correctly distinguished:

* “Set of instructions” (basic view)
* “System with state evolving over time” (systems view)



2️⃣ Threads

* Threads share process memory.
* They have:

\-Separate stacks

\-Shared heap/data segment

correctly identified:

* One process can contain multiple threads.
* Threads are like execution branches within a process.



3️⃣ Race Conditions

recognized:

* Shared variables between threads can cause undefined behavior.
* Conflicting operations lead to corruption.

Core idea reinforced: Race conditions are caused by concurrent access to shared state without synchronization.



4️⃣ Critical Section

Defined as:

Code region that must not be executed concurrently.

Important realization: A critical section is not protection itself. It is the vulnerable region.

Protection requires:

* Locks
* Interrupt disabling
* Atomic operations



5️⃣ Preemption

defined correctly:

Interrupting a running task so another task can run.

refined:

* Preemption is one source of concurrency.
* Interrupts introduce concurrency even on single-core systems.



6️⃣ Interrupt Disabling

learned;

Single-core:

* Disabling interrupts = prevents preemption.
* Enough for mutual exclusion.

Multi-core:

* Not enough.

* Other cores still run in parallel.

* Requires synchronization primitives.

Major conceptual milestone achieved here.



7️⃣ Spinlocks

Defined simply:

* Busy-wait lock.
* Used in kernel.
* Prevents parallel access across cores.

Critical insight learned: Spinlocks + Interrupt Disable are used together to prevent:

* Multi-core parallel access
* Same-core interrupt reentry
* Self-deadlock

That’s advanced OS-level understanding.



8️⃣ Mutex (New Term Introduced)

learned:

* Mutex = sleeping lock.
* Used in user-space or longer sections.
* Cannot be used in interrupt handlers (because interrupts cannot sleep).

This was my first exposure. That’s fine.



🔎 Conceptual Upgrades Today;

You moved from:

“Critical section prevents corruption”

To:

“Different sources of concurrency require different protection mechanisms.”

That is a systems-level upgrade.



🧭 Performance Assessment;

Strengths:

* Strong intuition.
* Good pattern recognition.
* Correct architectural reasoning on multi-core.
* Honest when unsure (very important).

Growth Edge:

* Vocabulary expansion phase.
* Cognitive load management.
* Avoid overextension late at night.



📊 System State;

Mental Load: High

Energy: Medium-low

Retention Risk: Slight (due to fatigue)

Recommendation:

* No more heavy abstractions tonight.
* Do soft core lightly.
* Push GitHub streak.
* Sleep.
