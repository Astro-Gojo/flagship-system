Execution Log — Day 17

Topic: Errors, Faults, Failures & Uncertain Input Handling
Objective: Understand failure theory and design safe system behavior under uncertainty

1. Conceptual Understanding

Learned Definitions (Corrected):

-Fault: An internal defect in hardware or software (exists even if system appears fine).

-Error: An incorrect internal state or value caused by a fault.

-Failure: Observable inability of the system to perform its intended function.

Key Chain Identified:

FAULT → ERROR → FAILURE

This clarified how issues propagate inside real systems.


2. Failure Identification

Identified Realistic System Failures:

-Sensor returns no data (timeout).

-Sensor returns out-of-range values.

-System remains stuck in VERIFYING state.

-Rapid state oscillation due to unstable input.

-Loss of communication with hardware components.

Focus shifted from causes to observable system behavior.


3. Failure Handling Design (Task A)

Chosen Failure: Bad / Unrecognized Input


Detection Strategy:

-Validate input against known state conditions.

-Apply time-based checks.

-Treat unrecognized or unstable input as uncertain.

Handling Logic:

Uncertain Input
   ↓
VERIFYING (recheck / stabilize / time window)
   ↓
Still invalid?
   ↓
ERROR state (safe handling)


System Behavior Decision:

-Do not guess.

-Retry and wait for clarity.

-Escalate only after verification fails.


4. Safety Principle Learned

Why Guessing is Dangerous:

-Acting on uncertain input can cause unsafe or irreversible outcomes.

-In engineered systems, a wrong action is worse than no action.

Core Rule Adopted:

Silence is safer than incorrect action.


5. System Design Rule Finalized

Canonical Rule:

“When input is uncertain, the system must verify or wait — never guess.”

This rule now governs all state transitions under uncertainty.


6. Personal Insight (Engineering Alignment)

-Recognized existing real-life habit of planning for failure as a form of reliability engineering.

-Identified main improvement area as precision of expression, not logic or reasoning.

-Began translating intuition into formal system rules.