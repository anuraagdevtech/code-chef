---
topic: Conditionals & Case Work
subtopic: Counting flags instead of enumerating cases
time: $O(1)$ per test case
space: $O(1)$
---
Chef refills when **at least two** of the three bottles are empty. Each $B_i$ is $1$ for full and $0$ for empty, so an empty bottle is a zero.

The naive route is to enumerate the eight possible triples, or to write a chain of `or`s covering each pair that could be empty. Both work but scale badly and are easy to get wrong. The cleaner framing: count the empties and compare against the threshold.

Because the values are exactly $0$ and $1$, the number of *full* bottles is just $B_1 + B_2 + B_3$, so the number of empty ones is $3 - (B_1 + B_2 + B_3)$. The refill condition "at least two empty" becomes

$$3 - (B_1 + B_2 + B_3) \geq 2 \quad\Longleftrightarrow\quad B_1 + B_2 + B_3 \leq 1$$

In words: Chef fills up exactly when **at most one** bottle is full — which is just the problem's own second sentence read from the other side. Encoding a 0/1 flag array as a sum is a trick worth keeping; it turns case analysis into arithmetic.
