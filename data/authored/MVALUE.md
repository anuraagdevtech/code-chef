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

## Edge cases

- **The expression factors**: $ab + a - b = (a-1)(b+1) + 1$, which turns the search into maximising a product and makes the extremes the only candidates.
- **It is not symmetric**, so both orderings of a pair must be tried — on $5, 3, 2$ the best is $a = 5$ with $b = 3$ giving $17$, while swapping them gives $13$.
- **Negative values matter.** With $A_i$ down to $-10^9$, two large negatives can multiply to a large positive, so the smallest few elements are candidates alongside the largest few.
- **Three from each end is enough**, since $(a-1)$ and $(b+1)$ are each monotone in their argument and the two indices must differ — a margin of three covers every tie and exclusion.
- **The two elements must be distinct positions**, which the `i == j` guard enforces; distinct *values* are not required.
- **$N = 2$** leaves exactly two ordered pairs, both of which the window covers.
- **Products reach $10^{18}$**, past 32-bit and at the edge of 64-bit, though exact in Python.

## Dry run

Second sample: $A = 5, 3, 2$, sorted to $2, 3, 5$.

| $a$ | $b$ | $(a-1)(b+1) + 1$ |
|---:|---:|---:|
| 2 | 3 | $1 \cdot 4 + 1 = 5$ |
| 2 | 5 | $1 \cdot 6 + 1 = 7$ |
| 3 | 2 | $2 \cdot 3 + 1 = 7$ |
| 3 | 5 | $2 \cdot 6 + 1 = 13$ |
| 5 | 2 | $4 \cdot 3 + 1 = 13$ |
| 5 | 3 | $4 \cdot 4 + 1 = $ **17** |

Output `17`.
