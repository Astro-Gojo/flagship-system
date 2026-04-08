**Day 107 — Execution Log  | Date : 07/04/2026**



**Session Type:** Core Session



**Topic:** Semaphores (Synchronization \& Coordination)



**Concept:**

Semaphore is a synchronization mechanism that uses a counter to control access and coordinate between threads.



**Core Operations:**

* WAIT → decreases value or blocks if 0
* SIGNAL → increases value and may wake waiting threads



**Application (Producer–Consumer):**

* Producer → WAIT(empty), SIGNAL(full)
* Consumer → WAIT(full), SIGNAL(empty)



**Key Understanding:**

* Semaphore controls when a thread can proceed
* Mutex ensures safe access to shared resource



**Important Insight:**

* WAIT on value = 0 → thread is blocked (no resource available)
* SIGNAL wakes up waiting threads



**System Principle:**

Coordination (semaphore) + Safety (mutex) = Correct concurrent system



**Outcome:**

* Understood real synchronization mechanism
* Connected theory to system behavior
* Strengthened concurrency design thinking

