**Day 289 — Execution Log | Date : 05/10/2026**



**Topic:** Condition Variables



**session:** Micro



**Core Concepts:**

* Condition variables allow threads to wait for a shared condition.
* They are commonly used together with mutexes.
* wait() releases the associated mutex while blocking and reacquires it before returning.
* Notifications wake waiting threads, but do not guarantee the condition is true.



**What I Learned:**

* Busy waiting wastes CPU time through repeated condition checking.
* Blocking allows the processor to execute other runnable work.
* Conditions should be checked in a while loop after waking.
* Spurious wakeups and competition between consumers make rechecking necessary.



**Key Systems Insight:**

A notification is not the source of truth. Shared state is. A thread must verify that the condition it needs is actually satisfied.



**Failure Modes / Trade-offs:**

* Lost wakeups from incorrect synchronization.
* Spurious wakeups.
* Incorrect condition checking.
* Deadlocks caused by improper mutex handling.



**Hardware Insight:**

In the Raspberry Pi battery-monitoring application, a consumer thread can sleep until the sensor acquisition thread updates the shared data buffer and signals that new readings may be available.



**Foundation Principle:**

Condition variables let threads sleep until shared state may have changed, avoiding unnecessary busy waiting. The condition must always be checked again after waking.

