Day: 99 | Execution log | Date : 30/03/2026
Session Type: Micro Session

Topic: Efficient Waiting (Sleep + Wake)

Concept:
Threads should wait efficiently without consuming CPU using sleep-based mechanisms.

Problem:
Busy waiting (spin loops) wastes CPU resources.

Solution:
Use wait-notify mechanisms where threads sleep until a condition is met.

Key Insight:
Efficient synchronization avoids unnecessary CPU usage.

Systems Engineering Principle:
High-performance systems minimize resource waste by replacing active waiting with passive waiting.
