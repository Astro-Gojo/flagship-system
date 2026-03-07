**Day 76 — Execution Log**



**Session Mode: Micro Session**

Time: ~10–15 min



**Topics:**

* Lock contention (review)
* CPU cores vs mutex bottleneck
* Lock granularity:

1. Coarse-grained locking
2. Fine-grained locking



**Key Insight:**

Concurrency performance improves when locks protect smaller independent data, allowing more threads to run in parallel.

