[Index](../../README.md)

# 40. Small factorials

> CodeChef problem code [`FCTRL2`](https://www.codechef.com/problems/FCTRL2) &middot; difficulty **420** &middot; time limit **0.235294s**

| | |
|---|---|
| **Topic** | Big Integers |
| **Technique** | Arbitrary-precision arithmetic |
| **Time** | $O(n)$ big-integer multiplications per test case |
| **Space** | $O(n \log n)$ bits for the result |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

You are asked to calculate factorials of some small positive integers.

**Input**

An integer t, 1<=t<=100, denoting the number of testcases, followed by t lines, each containing a single integer n, 1 <= n <= 100

**Output**

For each integer n given at input, display a line with the value of n!

**Note:** For larger numbers, their factorial can overflows any available numeric data type in C.

## Constraints

- $1 \leq t \leq 100$
- $1 \leq n \leq 100$

## Sample

**Sample input**

```
4
1
2
5
3
```

**Sample output**

```
1
2
120
6
```

## Approach

The task is to print $n!$ for $n$ up to $100$. The arithmetic is trivial; the problem is the **size** of the answer. $100!$ has $158$ decimal digits, far beyond the $64$ bits of a `long long` — which is exactly what the problem's note about overflow in C is warning about.

In C or Java this is the classic "big number" exercise: store the result as an array of digits and implement multiplication by hand, carrying between positions. That is why the problem carries tags for arrays and implementation despite being arithmetic on the surface.

Python removes the obstacle entirely. Its `int` is arbitrary-precision by default, growing as needed and limited only by memory, so `math.factorial(n)` is both correct and fast. There is no overflow to guard against and no manual digit array to maintain.

Two practical notes. First, `math.factorial` is implemented in C and uses a divide-and-conquer product, so it comfortably beats a hand-rolled Python loop. Second, with $t$ up to $100$ and $n$ up to $100$ the inputs repeat heavily, so the factorials could be computed once into a lookup table — though at these bounds the direct call is already instant.

One modern wrinkle worth knowing: Python 3.11+ caps `int`-to-`str` conversion at $4300$ digits by default to avoid a quadratic-conversion denial of service. $100!$ is nowhere near that limit, so printing is unaffected here, but the ceiling is real for genuinely large outputs.

## Solution (Python)

```python
import math
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    # Python ints are arbitrary precision, so 100! needs no manual big-num code.
    out = [str(math.factorial(int(data[1 + i]))) for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(n)$ big-integer multiplications per test case
- **Space:** $O(n \log n)$ bits for the result

## Edge cases

- **$n = 1$**: $1! = 1$. The lower bound here is $1$, so $0!$ never arises, but `math.factorial(0)` would correctly give $1$ anyway.
- **$n = 100$**, the upper bound: $100!$ has $158$ digits. This is the whole point of the problem — a 64-bit integer overflows at $21!$, so any fixed-width type is unusable and C/C++ solutions must implement big-number multiplication by hand.
- **No floating point.** A `double` can hold $100!$ only approximately, and the answer has to be exact to the last digit, so `math.exp`/`lgamma` style shortcuts are wrong here.
- Python's integers are arbitrary precision, so the "big integer" part of the problem disappears entirely.

## Dry run

| $n$ | product | output |
|---:|---|---:|
| 1 | $1$ | `1` |
| 2 | $1 \times 2$ | `2` |
| 5 | $1 \times 2 \times 3 \times 4 \times 5$ | `120` |
| 3 | $1 \times 2 \times 3$ | `6` |

The values arrive out of order and are independent, so each is answered on its own.

> CodeChef tags: `Data Structures`, `Arrays`, `Mathematics`, `Algorithms`

---

Same problem in rating order (#1 of 486): [../../by-rating/001-FCTRL2.md](../../by-rating/001-FCTRL2.md)
