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

## Edge cases

- **This is not a permutation.** Values may run up to $2N$, which is what gives the construction room: the pairs reach $4j - 2 \leq 2N - 2$.
- **The non-division at even positions is free.** The second member of each pair, $4j - 2$, is even while the next odd position holds $2j + 1$, which is odd — an even number can never divide an odd one, so the condition holds without any checking.
- **The division at odd positions is by construction**: $2j - 1$ divides $2(2j-1) = 4j - 2$.
- **An odd $N$ leaves a lone tail**, and position $N$ has no successor, so no condition applies to it. The value $N$ itself is used, and it is not among the odds already placed (those stop at $N - 2$), so distinctness holds.
- **For odd $N \geq 3$ the join is still valid**: the preceding value $2N - 4$ sits at an even position and exceeds $N$, so it cannot divide it.
- **$N = 1$** → a single element with no conditions at all.
- **This answer differs from the sample's** (`1 2 3 6` against `1 3 2 4`), and the statement allows any valid array, so a special judge checks the four conditions.

## Dry run

$N = 6$ gives $A = 1, 2, 3, 6, 5, 10$.

| $i$ | $A_i$ | $A_{i+1}$ | required | holds? |
|---:|---:|---:|---|:---:|
| 1 | 1 | 2 | $1 \mid 2$ | yes |
| 2 | 2 | 3 | $2 \nmid 3$ | yes |
| 3 | 3 | 6 | $3 \mid 6$ | yes |
| 4 | 6 | 5 | $6 \nmid 5$ | yes |
| 5 | 5 | 10 | $5 \mid 10$ | yes |

All six values distinct, and the largest is $10 \leq 2N = 12$.
