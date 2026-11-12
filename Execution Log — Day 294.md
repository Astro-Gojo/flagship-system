Execution Log — Day 294 | Date : 10/10/2026

Topic: Paging & Page Tables

Session: Micro

Core Concepts:
- Virtual memory is divided into pages.
- Physical memory is divided into frames.
- Page tables map virtual pages to physical frames.
- Pages can occupy non-contiguous physical frames.

What I Learned:
- Paging enables flexible physical memory allocation.
- Processes don't require one continuous block of RAM.
- Paging reduces external fragmentation.
- Internal fragmentation can still occur.

Key Systems Insight:
Physical memory allocation doesn't need to follow the logical arrangement of a process's virtual address space.

Hardware Insight:
The MMU uses page-table mappings to translate addresses. The OS manages those mappings and their permissions.

Foundation Principle:
Paging separates logical memory organization from physical RAM placement.
