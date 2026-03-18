**Day: 87 | Execution log | Date : 18/03/2026**

**Session Type: Micro Session**



**Topic: Hybrid Mutex (Spin + Sleep)**



**Concept:**

Real-world mutex implementations combine spinning and sleeping.



**Working:**

Thread first spins for a short time trying to acquire the lock.

If the lock is not acquired, the thread goes to sleep using OS scheduling.



**Key Insight:**

Spinning is fast for short waits.

Sleeping is efficient for long waits.



**Systems Engineering Principle:**

Efficient synchronization balances CPU usage and responsiveness by combining hardware-level spinning with OS-level scheduling.

