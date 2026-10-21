---
topic: Bit Manipulation
subtopic: Single-bit values are necessary and sufficient
time: $O(NK)$ per test case
space: $O(K)$
---
The condition quantifies over all $2^K - 1$ targets, but it reduces to a check on $K$ of them.

**Necessity.** Consider the target $j = 2^b$, a single bit. An OR only ever adds bits, so every chosen $A_i$ must be a subset of $\{b\}$ — i.e. $0$ or $2^b$ — and at least one must be non-zero. So the array must literally **contain** the string with a single $1$ at position $b$, for every $b$.

**Sufficiency.** If all $K$ single-bit strings are present, any $j$ is the OR of the single bits in its own binary expansion, so every target is reachable.

So the whole problem is: does $A$ contain each of the $K$ powers of two? That reduces an apparent $2^K$ search to one pass over the input, which is what makes $K$ up to $100$ — and $2^K$ astronomically large — irrelevant. Note the all-zero string and any string with two or more bits set are useless for this test, though they are harmless.

The samples are built around it. Sample 1 has exactly `01` and `10`, so both single bits are present and the answer is `YES`. Sample 3 holds `001`, `010` and `100` among six strings, again `YES` — the extra multi-bit strings `011` and `101` add nothing. Sample 2 is the instructive failure: it has `010` and `100` but no `001`, so the target $j = 1$ is unreachable even though `011` *contains* that bit, and the answer is `NO`.
