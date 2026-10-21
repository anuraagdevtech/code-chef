---
topic: Arrays
subtopic: Frequency combined with value
time: $O(N)$ per test case
space: $O(N)$
---
The rule that every tower **except the one landed on** rises by $1$ after each jump is what makes this collapse.

Suppose Pushpa lands first on a tower of height $h$. Every other tower is now $h' + 1$. To jump next he needs a tower currently at $h + 1$, so he needs $h' + 1 = h + 1$ — that is, $h' = h$. After that jump he stands at height $h+1$, every untouched tower has risen twice, and the same argument gives $h'' = h$ again.

So **every tower he ever visits had the same original height**. If a height $h$ occurs $c$ times, he lands on one of them and jumps $c - 1$ more times, gaining a metre each jump, finishing at

$$h + c - 1$$

The answer maximises that over all distinct heights:

$$\max_h \bigl(h + \mathrm{count}(h) - 1\bigr)$$

The trade-off between the two terms is the point, and sample case 1 shows both sides. With heights $[1,2,1,3]$, the value $1$ appears twice for $1 + 1 = 2$, while the lone $3$ gives $3 + 0 = 3$ — so the tallest single tower beats the repeated short one. On an input like $[1,1,1,1]$ the frequency would win instead.

Sample case 2 is a single tower: one landing, no jumps, final height $2$.

A `Counter` gives the frequencies in one pass; heights reach $10^9$, so hashing rather than an array indexed by height is essential.

## Edge cases

- **Frequency can beat raw height.** With heights $2, 1, 1, 1$ the tallest tower reaches only $2$, while the three $1$s stack to $1 + 3 - 1 = 3$ — so taking $\max(H)$ is wrong even though the sample does not expose it.
- **A single tower** ($N = 1$, the second row): the count is $1$ and the answer is $H_1$ exactly, which is what the $-1$ in $h + c - 1$ ensures.
- **All heights distinct**: every count is $1$, so the answer degenerates to $\max(H)$.
- **$H_i$ up to $10^9$** while counts are at most $N = 10^5$, so the sum stays small and no overflow concern arises.
- Grouping by height is the whole trick: towers of *different* heights never combine, so the maximum is taken over groups rather than over the array.

## Dry run

First sample: heights $1, 2, 1, 3$.

| height | count $c$ | reach $h + c - 1$ |
|---:|---:|---:|
| 1 | 2 | 2 |
| 2 | 1 | 2 |
| 3 | 1 | **3** |

Output `3`. Note the two $1$s reach as high as the lone $2$.
