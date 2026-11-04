**Day 290 — Execution Log | Date : 06/10/2026**



**Topic:** Deadlocks



**session:** Micro



**Core Concepts:**

* Deadlock occurs when threads become permanently blocked waiting for resources held by one another.
* Four necessary conditions: mutual exclusion, hold and wait, no preemption, circular wait.
* Global lock ordering prevents circular wait.
* Deadlock prevention, avoidance and detection are different strategies.



**What I Learned:**

* Resource acquisition order affects deadlock possibility.
* Timeout-based retries can prevent indefinite waiting.
* Poorly coordinated retries can cause livelock.



**Key Systems Insight:**

A system can avoid deadlock yet still fail to make useful progress. Eliminating blocking dependencies is not the same as guaranteeing forward progress.



**Failure Modes / Trade-offs:**

* Circular lock dependencies.
* Livelock from repeated retries.
* Starvation under unfair scheduling.
* Performance overhead from timeouts and retries.
* Incorrect recovery after partially completed operations.



**Hardware Insight:**

In the Raspberry Pi battery-monitoring application, multiple threads accessing sensor data and dashboard state must follow a consistent lock-acquisition order to avoid circular dependencies.



**Foundation Principle:**

Deadlock prevention requires breaking at least one necessary condition. Correct synchronization must also consider starvation, livelock and forward progress.

