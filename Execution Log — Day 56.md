# Day 56 — Interrupts, Polling & Resilience

## Concept
Explored interrupt-driven vs polling architectures and why real systems use hybrid models.

## Key Insights
- Interrupts scale because CPU time depends on actual events, not constant checking.
- Polling increases cost linearly with number of inputs.
- Interrupt misuse can cause interrupt storms and starvation.
- Hybrid systems separate event detection (ISR) from work execution (main loop).
- Rate limiting and debouncing protect systems from noisy or excessive events.

## Engineering Shift
Started thinking in terms of fault tolerance, not just functionality.

## Status
Chunky session complete.
Main quest strengthened.
