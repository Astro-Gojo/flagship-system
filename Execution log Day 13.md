Day 13 – System States & Verification Logic

Worked on understanding system-level states beyond basic if/else logic.

Key learnings:
- Understood that VERIFYING is a system state, not just a condition.
- Realized that VERIFYING exists to control transitions between states.
- Identified that a system must not stay in VERIFYING indefinitely.
- Defined exit conditions for VERIFYING:
  - Validation success → normal operational state
  - Validation failure → error or safe state
  - Timeout/uncertainty → forced transition to error/safe state

Clarified the difference between:
- Code-level decisions (if/elif/else)
- System-level behavior (states over time)

This helped solidify how real-world systems (authentication, sensors, services)
handle uncertainty before committing to actions.
