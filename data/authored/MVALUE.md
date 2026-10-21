---
topic: Basic Math
subtopic: Factoring the expression, then checking the extremes
time: $O(N \log N)$ per test case
space: $O(N)$
---
The expression factors:

$$ab + a - b = (a-1)(b+1) + 1$$

so maximising it means maximising a **product of two shifted elements**, with $a$ and $b$ taken from distinct positions. That asymmetry matters — $a$ is shifted down and $b$ up — so the pair is ordered and both orders must be tried.

A product of two terms is largest when both factors are large positive or both are large negative, so the optimum uses only the array's extremes: $a$ wants either the maximum (to make $a-1$ big) or the minimum (to make $a-1$ very negative), and the same for $b$. Taking the three smallest and three largest entries of the sorted array and trying every ordered pair among them therefore suffices, in constant time after the sort — and taking three of each leaves room for the ties and duplicates that a two-of-each window could mishandle.

$$\text{answer} = 1 + \max_{i \neq j} (A_i - 1)(A_j + 1)$$

Note values can be negative, so the answer can be too, and the product reaches $10^{18}$ — `long long` territory in C++, free in Python.

The second sample shows the ordering effect: with $[5,3,2]$ the best is $a = 5$, $b = 3$ giving $4 \cdot 4 + 1 = 17$, while swapping them gives only $2 \cdot 6 + 1 = 13$. The first sample, $[2,2]$, uses the two equal elements at distinct positions for $1 \cdot 3 + 1 = 4$ — the values may repeat as long as the positions differ.
