**Day 268 — Execution Log | Date : 15/09/2026**



**Session:** core



**Topic:** Message Delivery \& Acknowledgement Semantics



**Core Concepts:**

* ACK / acknowledgement
* ACK timing
* At-most-once vs at-least-once delivery
* Visibility timeout / redelivery
* Processing-before-ACK vs ACK-before-processing
* Failure windows around acknowledgement
* Duplicate delivery
* Idempotent processing



**What I Learned:**

* An ACK tells the queue that processing has completed.
* If processing succeeds but the ACK is lost, the queue may redeliver the message.
* ACK-before-processing can cause lost work.
* Processing-before-ACK can cause duplicate processing after crashes.
* At-least-once delivery therefore commonly requires idempotent consumers.
* Idempotency does not prevent duplicates; it makes repeated execution safe.



**Key Systems Insight:**

* A distributed system often cannot know the true outcome of an operation after communication failure.
* The queue knows whether it received an ACK, not necessarily whether the external side effect happened.



**Failure Modes:**

* Crash before processing → redelivery.
* Processing succeeds + crash before ACK → possible duplicate.
* ACK succeeds + processing fails → possible lost work.
* Lost ACK → uncertain outcome and retry.



**Hardware Insight:**

* In an IoT pipeline, a battery measurement could be stored successfully while the acknowledgement is lost, causing the same measurement event to be delivered again.
* Unique measurement IDs and idempotent storage can prevent duplicate records.



**Connection / Progression:**

Queue → ACK → failure window → redelivery → duplicate → idempotency.



**Foundation Principle:**

An ACK confirms communication of completion, not necessarily the real-world outcome; failures around the ACK boundary require suitable delivery semantics and idempotent processing.

