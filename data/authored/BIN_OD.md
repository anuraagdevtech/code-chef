---
topic: Bit Manipulation
subtopic: Offline queries grouped by bit with prefix counts
time: $O(NB+Q)$ per test case for $B$ queried bits
space: $O(N+Q)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
An XOR bit is one exactly when its two input bits differ. For a query, if the two ranges have $a,b$ set bits and lengths $u,v$, the answer is $a(v-b)+(u-a)b$.

Group queries by their requested bit. Build one prefix-count array for that bit, answer all its queries, then discard it before processing the next bit. This uses linear memory instead of retaining a prefix array for every bit.

## Edge cases

- Bits are zero-based.
- Count pairs of indices, including repeated values separately.
- Preserve original query order after grouping.

## Dry run

In the first sample query, bit 1 has one set bit among `[1,2,4]` and one among `[2]`. The count is `1*0+2*1=2`.
