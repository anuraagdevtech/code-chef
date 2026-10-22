[&larr; 75. Presents for Cheffina](PRESENTS.md) &middot; [Index](../../README.md) &middot; [78. Possible Victory &rarr;](T20MCH.md)

# 76. Small Factorial

> CodeChef problem code [`FLOW018`](https://www.codechef.com/problems/FLOW018) &middot; difficulty **700** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Factorials within fixed-width limits |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Write a program to find the factorial value of any number entered by the user.

**Input**

The first line contains an integer **T**, the total number of testcases. Then **T** lines follow, each line contains an integer **N**.

**Output**

For each test case, display the factorial of the given number **N** in a new line.

## Constraints

- 1 **≤** **T** **≤** 1000
- 0 **≤** **N** **≤** 20

## Sample

**Sample input**

```
3 
3 
4
5
```

**Sample output**

```
6
24
120
```

## Approach

Print $N!$ for $0 \leq N \leq 20$. In Python the whole solution is `math.factorial(n)`.

The bound of $20$ is chosen deliberately. $20! = 2{,}432{,}902{,}008{,}176{,}640{,}000 \approx 2.4 \times 10^{18}$, which still fits in a signed 64-bit integer (whose ceiling is about $9.22 \times 10^{18}$) — but $21!$ is roughly $5.1 \times 10^{19}$ and overflows it. So this problem is the largest factorial a C `long long` can hold, and it is the counterpart to Small Factorials, where $N$ reaches $100$ and genuine big-number arithmetic is unavoidable.

In Python the distinction is invisible, since `int` grows as needed. The lesson is to recognise *why* a problem setter picks $20$ rather than $25$: the bound is telling you which integer type the intended solution uses.

The edge case is $N = 0$. By definition $0! = 1$, not $0$, and `math.factorial(0)` returns $1$ correctly. A hand-written loop seeded with `result = 1` also gets this right, whereas one seeded with `result = n` does not.

With $T$ up to $1000$ and $N$ capped at $20$, the inputs repeat heavily, so a precomputed table of the $21$ possible answers would avoid recomputation entirely — an easy win in a hotter loop, though unnecessary at this scale.

## Solution (Python)

```python
import math
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    # 0! is 1; math.factorial handles that without a special case.
    out = [str(math.factorial(int(data[1 + i]))) for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **$N = 0$**: $0! = 1$. The lower bound here is $0$, unlike the sibling problem where it is $1$, and `math.factorial(0)` returns $1$ without a special case — a hand-rolled `for i in range(1, n+1)` loop also gets this right only because the empty product is $1$.
- **$N = 20$**, the upper bound: $20! = 2{,}432{,}902{,}008{,}176{,}640{,}000$, which just fits in a signed 64-bit integer (limit about $9.22 \times 10^{18}$). **$21!$ would not**, and that is precisely why the bound is $20$ — the problem is calibrated so a `long long` suffices.
- **$N = 1$**: $1$.
- In Python the bound is irrelevant, since integers are arbitrary precision.

## Dry run

| $N$ | product | output |
|---:|---|---:|
| 3 | $1 \times 2 \times 3$ | `6` |
| 4 | $6 \times 4$ | `24` |
| 5 | $24 \times 5$ | `120` |

> CodeChef tags: `Basic Programming Concepts`, `Mathematics`, `Basic Math`, `Algorithms`, `CPP`

---

Same problem in rating order (#62 of 486): [../../by-rating/062-FLOW018.md](../../by-rating/062-FLOW018.md)
