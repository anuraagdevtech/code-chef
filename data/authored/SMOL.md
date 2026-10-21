---
topic: Number Theory
subtopic: Modulo, with a zero-divisor guard
time: $O(1)$ per test case
space: $O(1)$
---
Repeatedly subtracting $K$ from $N$ while staying non-negative lands on exactly the remainder:

$$N \bmod K$$

That is what the modulo operator *means* — the smallest non-negative value reachable by subtracting multiples of $K$. Looping the subtractions would be correct but hopeless at $N$ up to $10^9$ with $K = 1$; the modulo is $O(1)$.

The case that makes this more than a one-liner is **$K = 0$**, which the constraints explicitly allow. Subtracting zero changes nothing, so the answer is $N$ itself — and `n % 0` raises `ZeroDivisionError` in Python (and is undefined behaviour in C). So the guard is not defensive padding; without it the program crashes on valid input.

The samples do not include $K = 0$, which is exactly why it is worth reading the constraints rather than trusting the examples. A solution tested only against the three given cases passes locally and fails on submission.

Sample case 3 covers the other easily-missed case: $K > N$, where no subtraction is possible at all and the answer is $N$ unchanged. The modulo handles that without a branch, since $2 \bmod 5 = 2$.

Sample case 2 is the exact-division case, reaching $0$.

## Edge cases

- **$K = 0$ is permitted by the constraints** and would raise `ZeroDivisionError`. With a step of zero no subtraction changes anything, so the answer is $N$ itself — this guard is the whole problem.
- **$K > N$** (the third row, $N = 2$ with $K = 5$): no subtraction is possible without going negative, and `n % k` already returns $N$, so no extra branch is needed.
- **$K$ divides $N$** (the second row): the result is $0$, the smallest whole number reachable.
- **$N$ is at least $1$**, so a $0$ answer only ever arises from exact divisibility.
- **$T$ up to $10^5$** with constant work per case; the input is read in one buffered call.

## Dry run

| $N$ | $K$ | path | output |
|---:|---:|---|---:|
| 5 | 2 | $5 \to 3 \to 1$ | `1` |
| 4 | 4 | $4 \to 0$ | `0` |
| 2 | 5 | cannot subtract | `2` |

A fourth, unsampled case: $N = 7$, $K = 0$ stays at `7` instead of crashing.
