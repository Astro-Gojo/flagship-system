**Day 75 – Execution Log**

**Main Quest — Software Core (Concurrency / Threading)**



**Topics Covered**

* Race Conditions (review)
* volatile vs synchronization (review)
* Mutex contention
* Performance slowdown due to lock contention





**1. Race Condition Review**

**Concept:**

A race condition happens when multiple threads access and modify shared data at the same time without synchronization, causing unpredictable or incorrect results.

**My Answer:**

race conditions create mismatching of data, causes confusion, overloads CPU and halts movements of threads.

**Correction:**

The key problem is:

* Incorrect or unpredictable data results

Example:



count = 5



Thread A reads 5

Thread B reads 5



Thread A writes 6

Thread B writes 6



Expected result: 7

Actual result: 6

This happens because the operations interleave improperly.





**2. Why volatile Cannot Fix Race Conditions**

**Concept:**

volatile only guarantees visibility, not atomicity.

**Meaning:**

* It ensures threads see the latest value
* But it does not stop multiple threads from modifying it simultaneously

**My Answer:**

volatile does only improves the visibility condition of a thread.

**Evaluation:**

Correct core idea.

Just remember:



volatile = visibility

mutex/atomic = safety





**3. Mutex Contention and Performance**

**Question:**

Why would a program become slower if too many threads fight over the same mutex?

**My Answer:**

threads queue waiting for the lock which causes slower performance.

**Correct Explanation:**

A mutex allows only one thread at a time to access the protected section.

If many threads try to acquire the same mutex:



Thread 1 → running

Thread 2 → waiting

Thread 3 → waiting

Thread 4 → waiting

...



Even on a multi-core CPU, most threads remain blocked.

This causes:

* CPU idle time
* thread context switching
* reduced parallelism





**4. Multi-Core Lock Contention Scenario**

**Scenario:**

20 threads

1 shared mutex

8 CPU cores



C**orrect Answer**:

B — Most threads spend time waiting for the lock.

Even though the CPU has 8 cores, only one thread can hold the mutex.

So the mutex becomes a bottleneck.

**Analogy:**



8-lane highway

1 toll booth



Traffic builds up.





**Key Principles Learned Today**

**1. Race Condition**

Multiple threads modifying shared data without synchronization.

**2. Volatile**

Improves visibility, not safety.

**3. Mutex**

Ensures mutual exclusion (only one thread enters critical section).

**4. Lock Contention**

Too many threads fighting for one mutex reduces performance.





**Mental Model Built**

Concurrency performance depends on:



parallel work

\+ minimal shared locks

\+ proper synchronization



If threads share too many locks:



parallelism collapses





**Progress Status**

**Main Quest Progress**

* Concurrency fundamentals strengthening
* Understanding synchronization trade-offs
* Beginning to reason about system performance

My thinking is improving even if wording isn't perfect, which is exactly how deep systems knowledge forms.





**Streak Status**

Day completed: 75

GitHub log: Ready

