**Day 263 — Execution Log | Date : 10/09/2026**



**Session:** Micro



**Topic:** Saga Pattern — Distributed Transaction Alternative



**Core Concepts:**

* Distributed transaction decomposition
* Local transactions
* Partial completion
* Compensating transactions
* Eventual consistency
* Difference between rollback and compensation



**What I Learned:**

* A Saga breaks a large distributed workflow into smaller local transactions.
* Each service can commit its own local operation independently.
* If a later operation fails, previously completed operations may need compensation.
* Compensation is a new business operation rather than a literal database rollback.
* Example: a successful payment may be compensated by issuing a refund.
* Saga avoids some of the coordination and blocking problems associated with 2PC.
* The trade-off is that the system may temporarily exist in an intermediate state while compensation occurs.



**Failure Case:**

Order       ✅

Payment     ✅

Inventory   ✅

Shipping    ❌

&#x20;   ↓

Compensation

&#x20;   ↓

Inventory released

Payment refunded

Order cancelled



**Key Systems Insight:**

A distributed system cannot always erase completed side effects, so recovery may require new actions that compensate for old ones.



**Connection:**

2PC → Coordinator/Blocking → Saga → Local Transactions → Compensation



**Foundation Principle:**

When global rollback is impractical, recover through coordinated compensating actions.

