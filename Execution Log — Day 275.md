**Day 275 — Execution Log | Date : 21/09/2026**



**Topic:** Resource Isolation \& Noisy Neighbors



**Session:** Micro



**Core concepts:**

* A noisy neighbor is a workload that consumes disproportionate shared resources and affects other workloads.
* Resource limits define maximum usage; reservations set aside or guarantee capacity, subject to the platform.
* Logical process isolation does not eliminate competition for physical hardware.
* Scheduling and resource controls help protect important workloads.



**What I learned:**

* CPU scheduling, resource limits, priorities, and workload placement can reduce interference.
* Heavy work can be scheduled during less demanding periods.
* Critical monitoring tasks can receive higher priority, while optional inference work can be limited or deferred.



**Key systems insight:**

\- Separate processes can still compete for the same CPU cores, cache, and memory bandwidth.



**Failure modes and trade-offs:**

* CPU limits reduce interference but do not guarantee real-time deadlines.
* High-priority work can still be delayed by other bottlenecks.
* Strict resource limits can reduce overall throughput if capacity remains unused.



**Hardware insight:**

\- In the Raspberry Pi battery-monitoring system, ML inference can delay sensor processing if both compete for CPU time. Limiting inference concurrency or prioritizing monitoring helps reduce that risk.



**Foundation principle:**

Resource isolation and scheduling control competition for shared hardware, reducing the impact of noisy workloads and helping protect important services.

