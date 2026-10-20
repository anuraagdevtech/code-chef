---
topic: Big Integers
subtopic: Arbitrary-precision arithmetic
time: $O(n)$ big-integer multiplications per test case
space: $O(n \log n)$ bits for the result
---
The task is to print $n!$ for $n$ up to $100$. The arithmetic is trivial; the problem is the **size** of the answer. $100!$ has $158$ decimal digits, far beyond the $64$ bits of a `long long` — which is exactly what the problem's note about overflow in C is warning about.

In C or Java this is the classic "big number" exercise: store the result as an array of digits and implement multiplication by hand, carrying between positions. That is why the problem carries tags for arrays and implementation despite being arithmetic on the surface.

Python removes the obstacle entirely. Its `int` is arbitrary-precision by default, growing as needed and limited only by memory, so `math.factorial(n)` is both correct and fast. There is no overflow to guard against and no manual digit array to maintain.

Two practical notes. First, `math.factorial` is implemented in C and uses a divide-and-conquer product, so it comfortably beats a hand-rolled Python loop. Second, with $t$ up to $100$ and $n$ up to $100$ the inputs repeat heavily, so the factorials could be computed once into a lookup table — though at these bounds the direct call is already instant.

One modern wrinkle worth knowing: Python 3.11+ caps `int`-to-`str` conversion at $4300$ digits by default to avoid a quadratic-conversion denial of service. $100!$ is nowhere near that limit, so printing is unaffected here, but the ceiling is real for genuinely large outputs.
