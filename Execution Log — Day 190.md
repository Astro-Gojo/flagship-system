**Day 190 — Execution Log | Date : 29/06/2026**



**Session Type:** Core Session



**Topic:** Consistent Hashing



**Concepts Learned:**

* Consistent Hashing
* Circular Hash Ring
* Data Redistribution
* Server Addition and Removal
* Minimal Data Movement



**Key Insights:**

* Simple modulo-based sharding causes massive data migration when the number of shards changes.
* Consistent hashing maps both data and servers onto a logical ring.
* Only a small subset of data moves when servers are added or removed.
* Efficient scaling is as important as raw performance.



**Systems Engineering Principle:**

A scalable system is not one that can merely grow—it is one that can grow without forcing unnecessary disruption.



**Progression:**

Horizontal Scaling → Sharding → Routing → Consistent Hashing

