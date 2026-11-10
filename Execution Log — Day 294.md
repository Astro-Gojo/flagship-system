Execution Log — Day 294 | Date : 10/10/2026

Topic: Virtual Memory & Address Spaces

Session: Micro


Core Concepts:
- Virtual addresses are used by processes.
- Physical addresses identify actual RAM locations.
- MMU translates virtual addresses into physical addresses.
- OS manages mappings and memory permissions.
- Each process has its own virtual address space.

What I Learned:
- Different processes can use identical virtual addresses.
- Those addresses can map to different physical locations.
- Memory isolation prevents unauthorized access.
- Shared memory is possible through intentional mappings.

Key Systems Insight:
Virtual memory separates the addresses a program uses from the physical memory hardware.

Hardware Insight:
The Raspberry Pi's MMU handles address translation while Linux manages mappings and permissions.

Foundation Principle:
A process operates within its own virtual address space, with hardware-assisted translation and OS-managed protection.