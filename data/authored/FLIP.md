---
topic: Strings
subtopic: Two independent parity classes
time: $O(|A|)$ per test case
space: $O(|A|)$
---
Look carefully at which positions an operation touches. Choosing a substring starting at index $i$ with odd length, the inverted bits are the ones at odd positions *within* the substring — that is, the global indices $i, i+2, i+4, \ldots$, ending at the substring's last index because the length is odd.

So an operation flips a **contiguous run inside one parity class** and never mixes the two. The even-indexed positions and the odd-indexed positions are entirely independent problems.

Within a class, we must flip exactly the positions where $A$ and $B$ differ, and each operation flips one contiguous block of that class. The minimum number of blocks covering a set exactly is its number of **maximal runs** — merging across a non-differing position would flip something that already matches.

So the answer is the run count in the even class plus the run count in the odd class, both computed in a single pass.

Sample case 1, `100001` against `110111`, differs at indices $1, 3, 4$. In the even class $(0,2,4)$ only index $4$ differs — one run. In the odd class $(1,3,5)$ indices $1$ and $3$ differ, and they are *adjacent within that class*, so also one run. Total $2$.

That adjacency is the subtlety: globally, indices $1$ and $3$ have index $2$ between them, but index $2$ belongs to the other class and does not break the run.

Sample case 3, `000` to `111`, differs everywhere: one run in each class, giving $2$ — not $1$, since no single operation spans both parities.
