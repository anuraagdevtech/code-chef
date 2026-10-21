---
topic: Number Theory
subtopic: Parity invariant
time: $O(1)$ per test case
space: $O(1)$
---
Let $a$ be the number of problems Alice solves and $b$ the number Bob solves. Tracking both counts:

$$\text{Alice} = N - a + 3b, \qquad \text{Bob} = M + a - b$$

Setting them equal and rearranging:

$$N - M = 2a - 4b = 2(a - 2b)$$

The right side is always **even**, so the two can only level up when $N - M$ is even — that is, when $N$ and $M$ share a parity. Conversely, whenever the difference is even a suitable $(a, b)$ exists, so the condition is exactly

$$N \equiv M \pmod 2$$

Looking for what the operations preserve is again the fastest route. Each of Alice's solves changes the difference $N - M$ by $-2$, and each of Bob's changes it by $+4$; both are even, so the **parity of the difference is invariant**. Starting from an odd difference, no sequence of moves can ever reach zero.

Sample case 3 is the odd case: $N = 2$, $M = 3$ differ by $1$, so `NO`. The others all have even differences, including case 4 where they are already equal and no moves are needed.

Note the problem never requires the counts to stay non-negative, nor that the problems actually be solvable — "in any arbitrary manner" licenses treating $a$ and $b$ as free non-negative integers. That generality is what makes the parity condition sufficient as well as necessary.

## Edge cases

- **$N = M$**: the difference is $0$, which is even, so `YES`.
- **$N < M$** (the second row, $1$ and $5$): the difference is negative. Python's `%` returns a non-negative remainder so the parity test still works, but a language where the modulo follows the sign of the dividend needs care — `-1 % 2` can be `-1` there, and comparing it against $0$ then fails.
- **Both odd or both even** → `YES`; **mixed parity** → `NO`.
- Every move changes $N - M$ by an even amount, so its parity is invariant — which is why the answer depends on nothing else and no simulation is needed.

## Dry run

| $N$ | $M$ | $N - M$ | even? | output |
|---:|---:|---:|:---:|---|
| 4 | 2 | 2 | yes | `YES` |
| 1 | 5 | $-4$ | yes | `YES` |
| 2 | 3 | $-1$ | no | `NO` |
| 2 | 2 | 0 | yes | `YES` |

Row 2 is the negative-difference case.
