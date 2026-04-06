**Day 105 — Execution Log | Date : 05/04/2026**



**Session Type:** Micro Session



**Topic:** Control Mechanism (Slots Concept)



**Concept:**

System uses counters (empty\_slots, filled\_slots) to control producer and consumer behavior.



**Key Learnings:**

* empty\_slots = 0 → producer must wait
* filled\_slots = 0 → consumer must wait
* System must check conditions BEFORE allowing actions



**Mistake Identified:**

* Initially assumed producer could act before control
* Corrected to: control happens before execution



**Core Insight:**

System enforces rules before actions, not after.

