---
topic: Constructive
subtopic: Blocks that only close at the right moment
time: $O(N)$ per test case
space: $O(N)$
---
A prefix of length $L$ is a permutation exactly when it contains precisely $\{1, \ldots, L\}$. The required lengths $A_1 < A_2 < \cdots < A_K = N$ therefore cut the array into **blocks**: positions $A_{i-1}+1 \ldots A_i$ must hold exactly the values $A_{i-1}+1 \ldots A_i$, since everything smaller is already used up by the earlier prefixes.

That fixes *which* values go in each block. The only freedom is their order inside it — and that order must ensure **no prefix ending strictly inside a block is a permutation**.

The trick is to place each block's **largest value first**. Then any prefix that stops partway through the block already contains that largest value $A_i$ but is shorter than $A_i$, so it cannot be a permutation of $\{1, \ldots, L\}$ for its own length $L$ — it holds a value too big. Only at the block's end, where length and maximum finally agree, does it close.

So each block is emitted as $A_i$, then $A_{i-1}+1, A_{i-1}+2, \ldots, A_i - 1$.

Blocks of size $1$ need no care: the single position is both the start and the end, and the prefix there is required to be a permutation anyway.

For the sample $N = 8$ with $A = [3,6,7,8]$, this yields `3 1 2 | 6 4 5 | 7 | 8`. The published answer, `2 3 1 6 4 5 7 8`, orders the first block differently — both are valid, so **any correct permutation is accepted** and this is judged by a checker.

The guarantee $A_K = N$ means the blocks exactly tile the array, so no leftover values remain.
