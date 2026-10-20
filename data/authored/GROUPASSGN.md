---
topic: Basic Math
subtopic: Pairing by reflection
time: $O(1)$ per test case
space: $O(1)$
---
The groups pair $1$ with $2N$, $2$ with $2N-1$, and so on. Every such pair sums to the same constant:

$$1 + 2N = 2 + (2N - 1) = \cdots = 2N + 1$$

So a student with roll number $X$ is partnered with

$$2N + 1 - X$$

Recognising the **constant sum** is what turns this from a case analysis into one subtraction. There is no need to work out which group $X$ falls into, nor whether $X$ sits in the first half or the second — the formula is symmetric and handles both. Sample case 2 has $X = 1$ in the first half giving $6$, and sample case 3 has $X = 4$ in the second half giving $3$; the same expression covers each.

This "reflect about the midpoint" pattern appears constantly: reversing an array maps index $i$ to $n - 1 - i$, and the arithmetic is identical once the indexing base is accounted for. Here the roll numbers start at $1$, which is why the constant is $2N + 1$ rather than $2N$.

A useful sanity check is that applying the formula twice returns the original roll number, as a pairing must — partnership is symmetric.

With $N$ up to $10^8$ there are up to $2 \times 10^8$ students, so constructing the groups explicitly is out of the question; the closed form is the only workable approach.
