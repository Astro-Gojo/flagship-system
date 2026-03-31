Day: 99 | Execution log | Date : 30/03/2026
Session Type: Micro Session

Topic: Order Control using Shared Flag

Concept:
Execution order between threads can be controlled using a shared variable (flag).

Implementation Idea:
Threads wait until a condition is satisfied before proceeding.

Example:
while turn != expected_value:
    pass

Key Insight:
This approach enforces order but uses busy waiting, which wastes CPU resources.

Systems Engineering Principle:
Correctness and control must be balanced with efficien