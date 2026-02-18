# Day 59 — Race Conditions & Critical Sections

## Concept
Studied race conditions in interrupt-driven systems.

## Key Insight
Interrupts introduce asynchronous preemption, which can break atomicity and cause non-deterministic behavior.

## Engineering Understanding
- Shared data between main loop and ISR can cause race conditions.
- Disabling interrupts protects critical sections.
- Overusing this technique increases latency and harms real-time guarantees.

## Status
Main quest continued.
Understanding of concurrency deepened.
