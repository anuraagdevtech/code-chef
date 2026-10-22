# 258. Jogging

> CodeChef problem code [`JOGGING`](https://www.codechef.com/problems/JOGGING) &middot; difficulty **1484** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | A doubling recurrence, taken modulo |
| **Time** | $O(\log N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Alice jogs everyday to keep herself fit and active. She noticed that she burns $X$ calories when jogging the first kilometer, and for $K > 1$, jogging the $K^{th}$ kilometer burns calories equivalent to the total number of calories burned while jogging the first $K-1$ kilometers.

What is the total number of calories that Alice burns after jogging for $N$ kilometers? The answer can be very large, so report it modulo $10^9 + 7$ ($1000000007$).

**Input**

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $N$ and $X$, as described in the problem statement.

**Output**

For each test case, output on a new line the total number of calories that Alice burns after jogging for $N$ kilometers, modulo $10^9 + 7$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^6$
- $1 \leq X \leq 100$

## Sample

**Sample input**

```
3
1 2
2 1
12548 1
```

**Sample output**

```
2
2
588809226
```

<details><summary>Explanation</summary>

**Test case $1$:** Alice only jogs one kilometer, which burns $2$ calories since $X = 2$.

**Test case $2$:** Alice jogs two kilometers. The first burns $X = 1$ calorie, and the second also burns $1$ calorie since the total amount burnt before this is $1$ calorie. So, the total is $1 + 1 = 2$ calories burned.

</details>

## Approach

Let $S_K$ be the total burned after $K$ kilometres. The $K$-th kilometre burns whatever was burned over the first $K-1$, so

$$S_K = S_{K-1} + S_{K-1} = 2\,S_{K-1}$$

Each kilometre **doubles the running total**, and with $S_1 = X$ this gives the closed form

$$S_N = X \cdot 2^{\,N-1} \pmod{10^9+7}$$

Recognising the recurrence as pure doubling is the whole step. Written out, the per-kilometre burns are $X, X, 2X, 4X, 8X, \ldots$ — note the second kilometre burns the same as the first, which is why the exponent is $N-1$ rather than $N$.

Computing $2^{N-1}$ by repeated multiplication would be $O(N)$ per query and far too slow at $N = 10^6$ with $T = 10^5$. Python's three-argument `pow(2, n - 1, MOD)` does modular exponentiation by squaring in $O(\log N)$.

The samples confirm the off-by-one: $N = 1$ gives $X \cdot 2^0 = X = 2$, and $N = 2$ gives $1 \cdot 2^1 = 2$ — the same total, because the second kilometre merely matches the first.

The modulus is prime, but no inverse is needed here — only a power. An alternative for many queries would be to precompute all powers of two up to $10^6$ once, making each query $O(1)$; at these bounds either is comfortable.

## Solution (Python)

```python
import sys

MOD = 10 ** 9 + 7


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Each kilometre doubles the running total, starting from x.
        out.append(str(x % MOD * pow(2, n - 1, MOD) % MOD))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(\log N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The $K$-th kilometre burns the *total* of the first $K-1$**, which doubles the running total each step: $X, 2X, 4X, \dots$, so the answer is $X \cdot 2^{N-1}$ with no recurrence to iterate.
- **$N = 1$** → just $X$, and $2^0 = 1$ gives it; writing $2^N$ would double every answer.
- **The exponent must be computed modularly.** At $N = 10^6$ the true value has over $300{,}000$ digits, so `pow(2, n - 1, MOD)` is essential rather than computing the power and reducing afterwards.
- **$X \leq 100$ is already below the modulus**, so the `x % MOD` is defensive rather than necessary.
- **The modulus is $10^9 + 7$**, and the product of two reduced values stays under $10^{18}$ — within 64-bit, and exact in Python.
- **$T$ up to $10^5$** with one modular exponentiation each, at $O(\log N)$.

## Dry run

| $N$ | $X$ | per-kilometre burn | total |
|---:|---:|---|---:|
| 1 | 2 | $2$ | `2` |
| 2 | 1 | $1, 1$ | `2` |
| 4 | 1 | $1, 1, 2, 4$ | 8 |

The totals after each kilometre are $X, 2X, 4X, 8X$ — the running sum doubles because the new kilometre equals everything before it.

> CodeChef tags: `Special`, `Mathematics`

---

Same problem in rating order (#282 of 486): [../../by-rating/282-JOGGING.md](../../by-rating/282-JOGGING.md)
