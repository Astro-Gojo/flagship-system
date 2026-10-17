**Day 282 — Execution Log | Date : 28/09/2026**



**Topic:** Interrupts, Preemption \& Kernel Execution



**Session:** Micro



**Core concepts:**

* Interrupts notify the processor about events requiring attention.
* Preemption allows the OS to suspend a running task.
* Context switching preserves and restores execution state when tasks change.
* An interrupt does not necessarily trigger a context switch.



**What I learned:**

* The scheduler may allow the current task to continue after an interrupt.
* A high-priority task can still experience delays when blocked or waiting for a resource.
* Responsiveness depends on interrupt handling, scheduling, resource availability, and execution overhead.



**Failure modes:**

* Long interrupt handlers.
* Lock contention and blocked tasks.
* Scheduling latency and excessive overhead.



**Key systems insight:**

Priority influences scheduling, but it cannot make unavailable resources immediately available.



**Foundation principle:**

Interrupt handling, scheduling, and context switching cooperate to manage CPU execution, but none alone guarantees immediate responsiveness.

