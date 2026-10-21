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

## Edge cases

- **Putting the block's largest value first is what prevents an early close.** Within the block $(\text{prev}, \text{end}]$, the prefix cannot be a permutation until every value up to `end` has appeared — and since `end` itself leads, no intermediate prefix has its maximum equal to its length.
- **Only the listed prefixes may be permutations**, so the construction must block all the others — which is exactly what the leading maximum achieves, block by block.
- **The listed lengths close automatically**: after finishing block $i$, the values seen are precisely $1 \dots A_i$.
- **$A_K = N$ is guaranteed**, so the blocks tile the whole array and nothing is left over.
- **A block of size $1$** contributes just its own value, as the third sample row does throughout — giving the identity permutation when every prefix must be good.
- **$K = 1$** means only the full array may be a permutation, so one big block runs from $1$ to $N$ with $N$ in front.
- **This answer differs from the sample's** at $N = 8$ (`3 1 2 6 4 5 7 8` against `2 3 1 6 4 5 7 8`); both have good prefixes at exactly $3, 6, 7, 8$, so a special judge checks which prefixes close.

## Dry run

First sample: $N = 8$ with $A = 3, 6, 7, 8$ gives $P = 3, 1, 2, 6, 4, 5, 7, 8$.

| prefix length | values seen | permutation? |
|---:|---|:---:|
| 1 | $\{3\}$ | no |
| 2 | $\{1,3\}$ | no |
| 3 | $\{1,2,3\}$ | **yes** |
| 4 | $\{1,2,3,6\}$ | no |
| 5 | $\{1,2,3,4,6\}$ | no |
| 6 | $\{1,\dots,6\}$ | **yes** |
| 7 | $\{1,\dots,7\}$ | **yes** |
| 8 | $\{1,\dots,8\}$ | **yes** |

Exactly the four listed lengths close.
