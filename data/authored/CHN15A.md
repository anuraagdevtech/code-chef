---
topic: Number Theory
subtopic: Divisibility after a uniform shift
time: $O(N)$ per test case
space: $O(1)$
---
Every minion's characteristic value gains the same $K$, and a minion mutates when the result is divisible by $7$. So the answer counts the values satisfying

$$(A_i + K) \equiv 0 \pmod 7$$

a single pass with a counter, in $O(N)$ time and $O(1)$ space.

Because the shift is uniform, there is a neater way to see it. The condition rearranges to

$$A_i \equiv -K \pmod 7$$

so the qualifying minions are exactly those whose *original* value already sits in one fixed residue class mod $7$. Computing `(-k) % 7` once per test case and comparing each `a % 7` against it does the same work with one modulo per element instead of an addition and a modulo — and, more usefully, it shows that $K$ only ever matters through $K \bmod 7$. Adding $K = 10$ and adding $K = 3$ produce identical answers.

The direct form `(a + k) % 7 == 0` is used below because it mirrors the statement; at these bounds the difference is immaterial. Note that Python's `%` always returns a non-negative result for a positive modulus, so `(-k) % 7` is well behaved — in C it would not be.

Walking the sample: $K = 10$ against $[2, 4, 1, 35, 1]$ gives $12, 14, 11, 45, 11$, of which only $14$ is a multiple of $7$ — one mutation.

## Edge cases

- **$K$ may exceed $7$** (it is $10$ in the sample), so it is not pre-reduced. Adding it and then taking the remainder handles that automatically; reducing $K$ first would also work but is an extra step to get wrong.
- **A value already divisible by $7$** counts only when $K$ is too — the shift is uniform, so the test is equivalently $v \equiv -K \pmod 7$.
- **$N = 1$**: a single minion.
- **Values up to $10^5$ and $K$ up to $100$**: the sum stays small, so no overflow.
- The shift applies to every value equally, which is what turns "will become divisible" into a plain residue count.

## Dry run

$N = 5$, $K = 10$, values $2, 4, 1, 35, 1$:

| value | $v + K$ | $\bmod 7$ | counts? |
|---:|---:|---:|:---:|
| 2 | 12 | 5 | no |
| 4 | 14 | 0 | **yes** |
| 1 | 11 | 4 | no |
| 35 | 45 | 3 | no |
| 1 | 11 | 4 | no |

One minion qualifies, so `1`. Note $35$ is divisible by $7$ on its own and still fails, because $K$ is not.
