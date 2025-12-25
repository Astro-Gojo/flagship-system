Day 4 — Understanding Functions & Control Flow (Simulation)
Objective

To understand how functions work in a systems-oriented program:

Separation of sensing, decision-making, and output

Difference between defining a function and executing it

How control flow determines system behavior

Work Done

Learned the concept of functions as reusable system components

Implemented a simulated sensor function using random values

Implemented a decision function to determine system behavior based on sensor input

Implemented a display/output function to present system state

Understood that functions do not execute when defined, only when called

Modified the decision threshold to observe behavior change

Key Code Concepts Learned

def is used to define a function, not execute it

return sends data out of a function for use elsewhere

Functions help separate:

Data acquisition (sensor)

Decision logic (control)

Output/communication (display)

Control flow changes system behavior without changing structure

Experiment Performed

Changed decision threshold:

if sensor_value < 50:


to:

if sensor_value < 30:

Observation

The system behavior changed immediately

The light now turns ON only for lower sensor values

This demonstrated how decision logic alone can alter system output

Key Insight

Functions behave like system workers — they only act when called.
Changing logic inside a function changes system behavior without affecting the rest of the system.

Outcome

Clear understanding of function execution flow

Stronger intuition for systems-based programming

Prepared foundation for scaling into real hardware + AI integration