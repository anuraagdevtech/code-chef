---
topic: Arrays
subtopic: Which multisets have all pairwise differences equal
time: $O(N)$ per test case
space: $O(N)$
---
Ask what the surviving array can look like. If it keeps three distinct values $a < b < c$, then $c - a$ is strictly larger than both $b - a$ and $c - b$, so the pairwise differences cannot all agree. Hence the survivors are one of only two shapes:

- **all equal** — every pairwise difference is $0$, and any number of copies is fine;
- **at most two elements** — there is then at most one pair, so "all differences equal" holds vacuously.

So the best we can keep is

$$\max\bigl(\text{largest frequency},\ \min(N, 2)\bigr)$$

and the answer is $N$ minus that.

Both branches are needed, and the samples separate them. Case 2, $[2,5,1,2,2]$, has three copies of $2$ — keeping them beats keeping any two elements, so the answer is $5 - 3 = 2$. Case 1, $[1,2]$, has no repeats at all, but two elements are always legal, so nothing is deleted.

Case 3, $[1,2,1,2]$, is the tie: the largest frequency is $2$ and the two-element option is also $2$, so either works and the answer is $4 - 2 = 2$.

The $\min(N, 2)$ guard matters for $N = 1$, where only one element exists to keep.

A `Counter` gives the modal frequency in one pass. Values reach $10^9$, so hashing rather than an indexed array is the right structure, and with $\sum N = 5 \times 10^5$ the single pass is what keeps this comfortable.
