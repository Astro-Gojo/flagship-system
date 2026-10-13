**Day 280 — Execution Log | Date : 26/09/2026** 



**Topic:** Interrupts \& Preemption



**Session:** Micro



**Core Concepts:**

* Interrupts notify the processor about events requiring attention.
* Preemption allows the OS to suspend a running task.
* Interrupt handling and context switching are distinct operations.
* Long-running interrupt handlers can delay other work.



**What I Learned:**

* An interrupt may trigger a scheduling decision but does not necessarily cause a context switch.
* Preemption improves responsiveness but cannot eliminate delays caused by lengthy interrupt handling.



**Key Systems Insight:**

\- Interrupt handling is itself part of the system's critical execution path and must not become a bottleneck.



**Failure Modes:**

* Long interrupt handlers.
* Delayed interrupt processing.
* Excessive event-handling overhead.
* Increased scheduling latency.



**Hardware Insight:**

\- Hardware events and OS scheduling interact to determine how quickly software responds to external events.



**Foundation Principle:**

Interrupts provide event notification; preemption provides control over which task executes. Both contribute to responsiveness, but neither guarantees immediate completion.

