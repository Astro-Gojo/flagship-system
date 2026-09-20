**Day 262 — Execution Log | Date : 09/09/2026**



**Session:** Micro



**Topic:** 2PC Trade-offs and 2PC vs Consensus



**Core Concepts:**

* Distributed transaction coordination
* Coordinator dependency
* Blocking
* Communication rounds
* Latency
* Consensus vs transaction coordination
* Raft vs 2PC



**What I Learned:**

* 2PC helps coordinate a transaction across multiple participants.
* It requires communication between participants and a coordinator.
* This adds communication overhead and latency.
* Coordinator failure can cause blocking.
* Raft and 2PC are both distributed coordination mechanisms but solve different problems.
* Raft focuses on achieving safe agreement over replicated state/history.
* 2PC focuses on coordinating whether a distributed transaction commits or aborts.



**Key Systems Insight:**

Different distributed protocols can look superficially similar because they coordinate machines, while actually solving very different problems.



**Comparison:**

Raft

&#x20;↓

"What state/command should

the cluster agree on?"



2PC

&#x20;↓

"Can this distributed

transaction commit?"



**Connection:**

Consensus/Raft → Distributed Transactions → 2PC → Saga



**Foundation Principle:**

Distributed coordination is not one problem; different protocols exist because they solve different coordination problems.

