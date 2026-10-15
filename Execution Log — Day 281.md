**Day 281 — Execution Log | Date : 27/09/2026**



**Topic:** User Mode vs Kernel Mode



**Session:** Micro



**Core Concepts:**

* User mode restricts application privileges.
* Kernel mode provides the OS with elevated privileges.
* System calls provide controlled entry points to kernel services.
* Hardware privilege mechanisms and OS policies help protect resources.



**What I Learned:**

* Applications normally request OS-managed services instead of directly performing privileged hardware operations.
* The user/kernel boundary helps contain application errors and unauthorized operations.
* Kernel and driver vulnerabilities can still compromise system protection.



**Key Systems Insight:**

\- Security depends on both hardware-enforced boundaries and correct OS implementation.



**Failure Modes:**

* Kernel vulnerabilities.
* Faulty or vulnerable device drivers.
* Incorrect permission checks.
* Excessive privileges or insecure interfaces.



**Hardware Insight:**

\- On the Raspberry Pi, a Python application can use Linux interfaces to interact with sensors while the OS and drivers manage protected hardware operations.



**Foundation Principle:**

Privilege separation limits what applications can do, but protection ultimately depends on the correctness of the mechanisms enforcing that boundary.

