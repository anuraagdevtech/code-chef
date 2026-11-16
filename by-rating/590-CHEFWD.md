[&larr; 589. Mountain](589-MOUNTAIN.md) &middot; [Index](README.md) &middot; [591. No Palindrome &rarr;](591-NOPALINDROME.md)

# 590. Chef World

> [`CHEFWD`](https://www.codechef.com/problems/CHEFWD) &middot; difficulty **2049** &middot; time limit **1s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Fibonacci convolution in closed form with fast doubling |
| **CodeChef tags** | `Mathematics`, `Modular Arithmetic`, `Sequences and Progression`, `Matrices`, `Matrix Multiplication`, `Modulo Multiplicative Inverse`, `Fibonacci Series`, `Matrix Exponentiation` |
| **Complexity class** | Logarithmic $O(\log n)$ |
| **Time** | $O(\log N)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef Ciel lives in a long street which can be thought as of x-axis of coordinate system.
Her house is at coordinate 0 whereas her restaurant is situated at coordinate **N**.
Usually Ciel goes from home to restaurant taking a step of size 1 or 2 in forward direction.
We all know how much Chef loves Fibonacci numbers.

But today, Ciel being little casual stepped in wrong direction on her way to her restaurant exactly once and of course she did not set her foot wrong at home.
Now she wonders how many ways she can reach her restaurant provided that she stepped wrong once but not at home.

 She does not go past her restaurant because it is altogether different world and once she reaches her restaurant she stops.

For example, if **N** is **3** then
**0** <span style="color:#808080;">-></span> **1** <span style="color:#808080;">-></span> **-1** <span style="color:#808080;">-></span> **0** <span style="color:#808080;">-></span> **1** <span style="color:#808080;">-></span> **3**,
**0** <span style="color:#808080;">-></span> **2** <span style="color:#808080;">-></span> **1** <span style="color:#808080;">-></span> **3**

are some possible ways where as
**0** <span style="color:#808080;">-></span> **-1** <span style="color:#808080;">-></span> **1** <span style="color:#808080;">-></span> **3**, (She did not set her foot wrong at her home)
**0** <span style="color:#808080;">-></span> **1** <span style="color:#808080;">-></span> **3**, (She sets her foot wrong direction exactly once)
**0** <span style="color:#808080;">-></span> **1** <span style="color:#808080;">-></span> **0** <span style="color:#808080;">-></span> **3**, (Her steps are always size 1 or 2)
**0** <span style="color:#808080;">-></span> **1** <span style="color:#808080;">-></span> **2** <span style="color:#808080;">-></span> **4** <span style="color:#808080;">-></span> **3**, (She does not go past her restaurant)
**0** <span style="color:#808080;">-></span> **1** <span style="color:#808080;">-></span> **2** <span style="color:#808080;">-></span> **3** <span style="color:#808080;">-></span> **2** <span style="color:#808080;">-></span> **3** (Once she reaches her restaurant, she stops)

are not.

**Input**

First line of input contains **T**, number of test cases which is at most 10000.
Then **T** lines follows each containing a positive integer **N** which is at most 1000000000000000 (10^15).

**Output**

Number of ways Ciel can reach her restaurant modulo 1000000007 (10^9+7).

## Constraints

- 1 <= T <= 10000.
- 1 <= N <= 10^15.

## Sample

**Sample input**

```
2
3
4
```

**Sample output**

```
18
44
```

## Approach

Let $w(d)$ be the number of ways to cover a distance $d$ with forward steps of 1 and 2; $w(d) = F_{d+1}$. A walk with exactly one wrong step is: walk forward from 0 to some point $p$ with $1 \le p \le N-1$ (not at home, and not at the restaurant, where she stops), step back by $s \in \{1, 2\}$, then walk forward from $p - s$ to $N$. The backward step may go below 0. So

$$\text{answer} = \sum_{p=1}^{N-1} w(p) \cdot \bigl(w(N - p + 1) + w(N - p + 2)\bigr).$$

For $N = 3$ this is $1 \cdot (3 + 5) + 2 \cdot (2 + 3) = 18$.

Both parts are convolutions of the Fibonacci sequence with itself, and $\sum_{i=0}^{m} F_i F_{m-i} = (m L_m - F_m) / 5$ with $L_m$ the Lucas numbers. The code evaluates the two full convolutions with this identity and subtracts the few boundary terms that correspond to $p = 0$ and $p = N$. The handful of Fibonacci numbers around index $N$ come from fast doubling, and the division by 5 is a modular inverse.

## Solution

```python
import sys


def main() -> None:
    MOD = 1000000007
    inv5 = pow(5, MOD - 2, MOD)

    def fib(n):
        a, b = (0, 1)
        for bit in bin(n)[2:]:
            c = a * ((2 * b - a) % MOD) % MOD
            d = (a * a + b * b) % MOD
            if bit == '0':
                a, b = (c, d)
            else:
                a, b = (d, (c + d) % MOD)
        return (a, b)
    out = []
    for n in list(map(int, sys.stdin.buffer.read().split()))[1:]:
        fib_n1, fib_n2 = fib(n + 1)
        fib_n3 = (fib_n1 + fib_n2) % MOD
        fib_n4 = (fib_n2 + fib_n3) % MOD
        c1 = ((n + 3) * (2 * fib_n4 - fib_n3) - fib_n3) * inv5 % MOD
        c2 = ((n + 4) * (2 * (fib_n3 + fib_n4) - fib_n4) - fib_n4) * inv5 % MOD
        out.append(str((c1 + c2 - 3 * fib_n2 - 2 * fib_n3 - 3 * fib_n1) % MOD))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- $N$ is far too large for a loop over positions - only the closed form is evaluated.
- The backward step from position 1 by two units lands on $-1$, which is allowed.
- $N = 1$ leaves no place for a wrong step and the formula gives 0.
- Intermediate values can be negative before the final reduction modulo $10^9 + 7$.

## Dry run

`N = 3`, with $w = 1, 1, 2, 3, 5$ for distances $0 \dots 4$.

- $p = 1$: one way to get there; back to 0 or $-1$, then 3 or 4 units forward: $1 \cdot (3 + 5) = 8$.
- $p = 2$: two ways; back to 1 or 0, then 2 or 3 units forward: $2 \cdot (2 + 3) = 10$.

Answer 18.

---

Same problem grouped by topic: [../docs/combinatorics/CHEFWD.md](../docs/combinatorics/CHEFWD.md)
