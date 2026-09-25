**Day 266 — Execution Log | Date : 13/09/2026**



**Session:** Micro



**Topic:** At-Most-Once, At-Least-Once \& Exactly-Once



**Core Concepts:**

* Message/operation delivery semantics
* At-most-once
* At-least-once
* Exactly-once
* Duplicate processing
* Lost operations
* Idempotent consumers
* Reliable distributed processing



**What I Learned:**

* At-most-once attempts to avoid duplicate processing but can lose operations.
* At-least-once retries to reduce the chance of losing operations but can produce duplicates.
* Exactly-once behavior is difficult to guarantee across independently failing distributed components.
* Unique operation IDs, deduplication, durable state, and transactional mechanisms can help produce externally visible exactly-once-like behavior.
* At-least-once delivery combined with idempotent processing is often a practical reliability strategy.



**Core Trade-off:**

At-most-once

→ fewer duplicates

→ possible loss



At-least-once

→ fewer losses

→ possible duplicates



Exactly-once

→ ideal behavior

→ difficult to guarantee



**Key Systems Insight:**

Reliable systems often choose to tolerate duplicates and make them harmless rather than trying to eliminate every possibility of duplicate delivery.



**Connection:**

Retries → Idempotency → Delivery Semantics → Reliable Distributed Processing



**Foundation Principle:**

Don't assume perfect delivery; design the system to survive uncertainty.

