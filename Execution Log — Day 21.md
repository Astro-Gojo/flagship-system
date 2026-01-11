Day 21 – System Recovery & Resilience

Focus:
- Difference between ERROR and RECOVERY states
- Safe handling of repeated failures
- Recovery limits and system resilience

Key Learnings:
- ERROR state signals detection of an unsafe or unhandled condition.
- RECOVERY state actively attempts to adapt, retry, or degrade gracefully.
- Infinite retries are dangerous due to resource exhaustion and hidden failures.
- Recovery attempts must be limited using time-based, count-based, or condition-based rules.
- A resilient system adapts instead of panicking when failures occur.

Core Principle:
Resilience is defined not by avoiding failure, but by controlled recovery.
