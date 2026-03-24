**Day: 92 | Execution log | Date : 23/03/2026**

Session Type: Micro Session

Topic: Modifying Concurrent System

Concept:
Changing loop iterations affects total operations but not correctness when synchronization is applied.

Experiment:
Reduced loop count from 100000 to 50000 per thread.

Observation:
With 2 threads:
Total increments = 50000 + 50000 = 100000

Key Insight:
Mutex ensures correctness regardless of number of operations.

Systems Engineering Principle:
System output depends on total workload across all concurrent actors, not just individual components.


