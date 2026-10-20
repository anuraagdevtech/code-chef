---
topic: Basic Math
subtopic: Counting odd and even positions
time: $O(1)$ per test case
space: $O(1)$
---
Episodes are numbered $1$ to $N$. Odd-numbered ones run $B$ minutes and even-numbered ones run $A$, so the total is

$$B \cdot (\text{odd count}) + A \cdot (\text{even count})$$

Among $1 \ldots N$ there are $\lceil N/2 \rceil = \lfloor (N+1)/2 \rfloor$ odd numbers and $\lfloor N/2 \rfloor$ even ones. Note the asymmetry: the odds get the extra episode when $N$ is odd, because the sequence *starts* at $1$. Writing both counts as $N/2$ would silently lose an episode on every odd $N$.

Two further traps sit in the wording. The indexing is **one-based**, so episode $1$ is odd and takes $B$; a zero-based reading swaps the roles entirely. And the input order is $N, A, B$ with $A$ attached to *even* episodes, which is the reverse of the order the two durations are naturally read in. Binding $A$ to the odd count is the most likely bug here, and sample case 3 would not catch it — with $N = 4$ the counts are equal, so $20 \cdot 2 + 30 \cdot 2 = 100$ either way. Sample case 2 is the one that discriminates: $N = 2$ gives one odd and one even episode for $4 + 3 = 7$, and case 1 with $N = 1$ gives $B$ alone.

A loop over the episodes would also work at $N \leq 60$, but the closed form is $O(1)$ and makes the parity structure explicit.
