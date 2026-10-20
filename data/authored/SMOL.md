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
