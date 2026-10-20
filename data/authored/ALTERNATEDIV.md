---
topic: Constructive
subtopic: Pairing k with 2k
time: $O(N)$ per test case
space: $O(N)$
---
The conditions alternate: positions $(1,2), (3,4), (5,6), \ldots$ must divide, and the links between those pairs — positions $(2,3), (4,5), \ldots$ — must **not**.

So treat the array as consecutive pairs and make each pair a multiple relation. The clean choice is to put an **odd** number at each odd position and its **double** at the even position after it:

$$A_{2j-1} = 2j-1, \qquad A_{2j} = 2(2j-1) = 4j-2$$

giving $1, 2,\ 3, 6,\ 5, 10,\ 7, 14, \ldots$

Each required divisibility holds by construction. Each required **non**-divisibility holds too: the link runs from $A_{2j} = 4j-2$ to $A_{2j+1} = 2j+1$, and for $j \geq 2$ the first exceeds the second, so it cannot divide it; for $j = 1$ it is $2 \nmid 3$.

Distinctness falls out from parity: the odd positions hold odd numbers, while the even positions hold numbers of the form $4j-2$, all $\equiv 2 \pmod 4$. The two families never collide, and within each family the values strictly increase.

The bound is satisfied with room to spare. The largest value used is $N$ when $N$ is odd, and $2N - 2$ when $N$ is even — both within $2N$.

Odd $N$ simply ends on a lone odd number with no partner, which is fine since the final element has no condition after it. $N = 1$ emits a single value.

**Any valid array is accepted**, so this is judged by a checker — the sample prints `1 3 2 4` for $N = 4$ where this construction gives `1 2 3 6`, both legitimate.
