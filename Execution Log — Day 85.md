
**Day: 85 Date : 16/03/2026**

**Session Type: Micro Session**



**Topic: Compare-And-Swap (CAS)**



**Concept:**

CAS is a CPU atomic instruction used to safely update shared memory.



**Operation:**

CAS(memory, expected, new)



**Behavior:**

If memory == expected → update to new

Else → operation fails.



**Key Property:**

The comparison and update happen atomically in hardware.



**Implication:**

When multiple threads attempt CAS simultaneously, only one succeeds while others fail and retry.



**Systems Engineering Insight:**

CAS enables lock-free synchronization mechanisms and reduces the need for mutex locks in simple shared-state updates.

