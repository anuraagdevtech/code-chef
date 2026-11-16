---
topic: Simulation
subtopic: Simulate the admissions in exam-rank order until Chef chooses
time: $O(M \log M + \sum \text{list lengths})$ per test case
space: $O(N + M + \sum \text{list lengths})$
complexity_note: Auxiliary space excludes the buffered input and output.
---
The process is deterministic: students choose in the order of their exam ranks, and each takes the best-ranked college on their own list that still has its seat, or nothing if all of them are taken.

So sort the students by exam rank and simulate. For each student scan their list for the free college with the smallest rank value and mark it as taken. When Chef (student 1) is reached, print his college - or 0 if none on his list is free - and stop: students after him cannot affect his result.

Every list is scanned at most once, so the simulation is linear in the input size after the sort.

## Edge cases

- Chef may get no college at all: print 0.
- Rank 1 is the best, both for colleges and for students.
- A student whose colleges are all taken occupies nothing.
- The college ids in the lists are converted to 0-based indices.

## Dry run

First sample: college ranks `2 1` (college 2 is the best), student ranks `1 2` (Chef is first), both students list colleges 1 and 2.

Chef chooses first and takes the best college on his list, college 2.

Second sample: one college; Chef has exam rank 2 and the other student takes the college first. Chef gets nothing: 0.
