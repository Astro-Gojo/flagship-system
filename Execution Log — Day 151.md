**Day 151 — Execution Log**



**Session Type:** Normal Session **| Date : 21/05/2026**



**Topic:** Condition Variables (Efficient Waiting \& Coordination)



**Concepts Learned**



* Condition variables allow threads to sleep efficiently until a state changes.
* Busy waiting wastes CPU resources during long waits.
* Condition variables are used together with mutexes for safe coordination.
* wait(condition, mutex) atomically:

  * releases the mutex
  * puts the thread to sleep
  * reacquires mutex after wake-up
* Threads must recheck conditions after waking using while(condition).



**Key Insights**



* Mutex handles safety; condition variables handle efficient waiting.
* Efficient systems avoid continuous polling when progress is impossible.
* Sleeping threads preserve CPU efficiency and scalability.
* Wake-ups are not always trustworthy; conditions must be revalidated.



**Systems Engineering Principle**



Efficient concurrent systems coordinate thread execution using safe sleep/wake mechanisms instead of wasting CPU on constant checking.



**Progression**



Concurrency understanding expanded from:

* mutual exclusion

→ coordination

→ efficient waiting behavior

