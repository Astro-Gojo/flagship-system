**Day 283 — Execution Log** 



**Topic:** Processes vs Threads



**Session:** Micro



**Core concepts:**

* Processes have separate virtual address spaces by default.
* Threads are execution paths within a process.
* Threads share process memory and many process-level resources.
* Each thread has its own execution state and stack.



**What I learned:**

* Shared memory makes communication convenient.
* Concurrent access to shared data can cause interference and incorrect results.
* Processes generally offer stronger fault isolation, while threads often make sharing cheaper and simpler.



**Trade-offs:**

* Processes: stronger isolation, but communication can require explicit IPC.
* Threads: convenient sharing, but synchronization becomes important.



**Hardware insight:**

Multiple threads may execute on different CPU cores, but sharing memory does not automatically make concurrent access safe.



**Key systems insight:**

Shared state is convenient only when its concurrent access is managed correctly.



**Foundation principle:**

Processes separate execution environments; threads share an environment, making coordination essential.

