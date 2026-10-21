---
topic: Sorting
subtopic: Counting sort over a small value range
time: $O(N + V)$ per test case with $V = 100$
space: $O(V)$
---
The values are confined to $1 \ldots 100$, which is the signal to use a **counting sort** rather than a comparison sort.

Tally how many times each value occurs in one pass, then emit each value that many times in increasing order. That is $O(N + V)$ — linear in the input — against the $O(N \log N)$ lower bound that applies to comparison sorts. The small, known value range is exactly the extra information that lets the bound be beaten.

Space is $O(V)$, a fixed $100$ counters regardless of how large $N$ grows.

With $N$ up to $10^6$ the practical concern is less the sorting than the **I/O**: reading a million tokens with per-line parsing and printing them one at a time would dominate the runtime. Reading the whole stream at once and emitting a single joined write is what keeps this fast.

The sample shows both the distinct case, $[7,2,9,10,1] \to [1,2,7,9,10]$, and the duplicate case, $[3,7,7,3] \to [3,3,7,7]$ — duplicates simply emit their value repeatedly, which counting sort handles naturally without any tie-breaking.

Note that Python's built-in `sorted` would also pass comfortably here; the point of the problem is to practise the counting technique, and the counting version is genuinely faster at this size.
