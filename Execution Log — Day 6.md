Day 6 — Execution Log

Focus: Deep understanding of functions, variables, and main() execution flow
Status: Conceptual clarity achieved


What I worked on:

-Revisited the existing simulated sensor–light system (no new features added)

-Focused entirely on understanding:

  *Function calls vs function definitions

  *Role of main() as an execution entry point

  *Difference between function names and variable names

  *Why multiple outputs appeared earlier due to repeated function calls


Key Learnings:

-Functions do not run automatically; they only run when called

-main() is not special in Python, but acts as a clear control point for execution

-Variable names like sensor and state are local containers, not fixed concepts

-get_sensor_value() is a function; sensor_value is just a variable holding its return

-Calling sensor functions multiple times generates new values each time

-Incorrect placement of function calls can cause unintended multiple executions


Conceptual Breakthrough:

-Earlier confusion came from regenerating sensor values unintentionally

-Centralizing execution inside main() ensures:

  *Single sensor read

  *Consistent decision logic

  *Predictable output

-Understood why structured programs scale better than linear scripts


Outcome:

-No new code added

-Existing code now fully understood

-Mental model corrected from “shortest way” to “scalable architecture”

-Ready to extend system complexity safely in future days


Next Steps:

-Continue Python fundamentals (functions, parameters, scope)

-Apply same structured thinking to future hardware simulations

-Maintain no-zero-day rule through learning documentation
