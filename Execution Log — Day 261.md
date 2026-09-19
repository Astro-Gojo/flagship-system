**Day 261 — Execution Log | Date : 08/09/2026** 



**Session:** Micro



**Topic:** Prepared State vs Committed State



**Core Concepts:**

* Prepare state
* Commit state
* Intermediate transaction state
* Coordinator decision
* Atomic transaction coordination



**What I Learned:**

* PREPARED means a participant is ready to commit if instructed.
* COMMITTED means the final commit decision has been made and applied.
* A participant replying YES during Phase 1 does not mean the global transaction has committed.
* The intermediate prepared state allows the coordinator to coordinate the global decision.
* However, remaining prepared while waiting for the coordinator contributes to 2PC's blocking problem.



**Key Systems Insight:**

A system can be ready to perform an action without that action having been globally authorized yet.



**Connection:**

Prepare → Coordinator Decision → Commit

and

Replicated ≠ Committed → Prepared ≠ Committed



**Foundation Principle:**

Readiness is not completion.

