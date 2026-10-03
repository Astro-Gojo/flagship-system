**Day 273 — Execution Log | Date : 19/09/2026**



**Session:** Normal



**Topic:** Rate Limiting \& Admission Control



**Core Concepts:**

* Rate limiting
* Admission control
* Traffic control
* Capacity-aware acceptance
* Request cost
* Priority-aware processing
* Queueing latency
* Sustained overload



**What I Learned:**

* Rate limiting controls how quickly traffic is allowed to enter a system.
* Rate limiting does not increase computational efficiency; it controls workload to protect available capacity.
* A queue can absorb temporary bursts but sustained excess traffic causes backlog growth.
* Growing queues can increase queueing latency and eventually create resource pressure.
* Admission control evaluates whether work can safely be accepted based on current system conditions.
* Admission decisions can consider CPU, memory, queue depth, request cost, priority, and other resource constraints.
* A request can be within its rate limit while still being rejected by admission control because the system is currently overloaded.



**Key Systems Insight:**

Rate limiting looks primarily at incoming traffic rate; admission control looks at whether the system can safely handle additional work right now.



**Failure Modes / Trade-offs:**

* Excessive rate limiting can unnecessarily restrict legitimate traffic.
* Large queues can protect against short bursts but increase latency when backlog persists.
* Admission control may reject useful work, but this can protect critical functionality during overload.
* Per-client limits can provide better fairness than a single global limit.



**Hardware Insight:**

* An edge device such as the Raspberry Pi can use admission control to reject/defer expensive optional ML or analytics work while preserving safety-critical monitoring.
* Resource-aware decisions are particularly useful when compute and memory are limited.



**Connection / Progression:**

Rate Limiting → Admission Control → Backpressure → Load Shedding → Graceful Degradation → Circuit Breaking



**Foundation Principle:**

Don't accept more work simply because someone requested it; accept work according to what the system can safely sustain.

