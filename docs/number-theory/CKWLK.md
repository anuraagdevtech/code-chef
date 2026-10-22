# 376. Cakewalk

> CodeChef problem code [`CKWLK`](https://www.codechef.com/problems/CKWLK) &middot; difficulty **1474** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Prime factorisation into a two-variable range test |
| **Time** | $O(\log N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

You are playing EVE Online. Initially, you have one dollar, but you have somehow acquired two cheat codes. The first cheat code multiplies the amount of money you own by $10$, while the second one multiplies it by $20$. The cheat codes can be used any number of times.

You want to have exactly $N$ dollars. Now you are wondering: can you achieve that by only using some sequence of cheat codes?

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$.

**Output**
- For each test case, print a single line containing the string `"Yes"` if you can make exactly $N$ dollars or `"No"` otherwise.

**Constraints**
- $1 \le T \le 100$
- $1 \le N \le 10^{18}$

## Constraints

- $1 \le T \le 100$
- $1 \le N \le 10^{18}$

## Sample

**Sample input**

```
4
200
90
1000000000000
1024000000000
```

**Sample output**

```
Yes
No
Yes
No
```

## Approach

Order does not matter, so a sequence of cheats is just a count of each: applying $\times 10$ $a$ times and $\times 20$ $b$ times gives

$$N = 10^a \cdot 20^b = 2^{a + 2b} \cdot 5^{a + b}$$

So $N$ must be $2^x 5^y$ with no other prime factor, and we need non-negative integers $a, b$ with $x = a + 2b$ and $y = a + b$. Subtracting gives $b = x - y$ and then $a = y - b = 2y - x$. Both must be non-negative, which is a single sandwich:

$$y \leq x \leq 2y$$

So the test is: strip every factor of $2$ and of $5$ from $N$; the remainder must be $1$; and the two exponents must satisfy that inequality. The lower bound says there are at least as many $2$s as $5$s (every cheat contributes at least one of each), and the upper bound says no more than twice as many (even using $\times 20$ exclusively).

Both samples that fail do so for different reasons, which is the point of the pair. $90 = 2 \cdot 3^2 \cdot 5$ leaves $9$ behind, so the factorisation itself is wrong. But $1024000000000 = 2^{19} \cdot 5^{9}$ is a clean $2$-$5$ number and still fails, because $19 > 18 = 2y$ — it has one factor of $2$ too many, so no combination of cheats produces it.

Meanwhile $200 = 2^3 \cdot 5^2$ satisfies $2 \leq 3 \leq 4$ (take $a = 1, b = 1$), and $10^{12} = 2^{12} 5^{12}$ satisfies $12 \leq 12 \leq 24$ (take $a = 12, b = 0$). Note $N = 1$ is also `Yes`, by using no cheats at all.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        twos = fives = 0
        while n % 2 == 0:
            n //= 2
            twos += 1
        while n % 5 == 0:
            n //= 5
            fives += 1
        # a = 2y - x and b = x - y must both be non-negative.
        out.append("Yes" if n == 1 and fives <= twos <= 2 * fives else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(\log N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Factorising into twos and fives turns the puzzle into two linear bounds.** Using $\times 10$ $a$ times and $\times 20$ $b$ times gives $2^{a+2b} 5^{a+b}$, so with $t$ twos and $f$ fives we need $a = 2f - t$ and $b = t - f$ — both non-negative, i.e. $f \leq t \leq 2f$.
- **Any other prime factor is fatal.** The second row, $90 = 2 \cdot 3^2 \cdot 5$, has the right shape in twos and fives but leaves $9$ behind, so the residue must be checked against $1$.
- **Too many twos fails** even with no stray primes: the last row is $2^{19} 5^9$, and $19 > 2 \cdot 9$, so no choice of $a, b$ works.
- **$N = 1$** → zero twos and zero fives, so $0 \leq 0 \leq 0$ holds and the answer is `Yes` with no cheat codes used.
- **Both bounds are non-strict**, and the extremes correspond to using only one code: $t = f$ means all $\times 10$, and $t = 2f$ means all $\times 20$ (the third row sits on $t = f$).
- **$N$ up to $10^{18}$**: the two division loops run at most about $60$ and $26$ times, so no general factorisation is needed.

## Dry run

| $N$ | factorisation | twos $t$ | fives $f$ | residue | $f \leq t \leq 2f$ | output |
|---:|---|---:|---:|---:|:---:|---|
| 200 | $2^3 5^2$ | 3 | 2 | 1 | $2 \leq 3 \leq 4$ ✓ | `Yes` |
| 90 | $2 \cdot 3^2 \cdot 5$ | 1 | 1 | **9** | — | `No` |
| $10^{12}$ | $2^{12} 5^{12}$ | 12 | 12 | 1 | $12 \leq 12 \leq 24$ ✓ | `Yes` |
| $1024 \cdot 10^9$ | $2^{19} 5^9$ | 19 | 9 | 1 | $19 \leq 18$ **✗** | `No` |

For $200$: $a = 2(2) - 3 = 1$ and $b = 3 - 2 = 1$, so one $\times 10$ and one $\times 20$.

---

Same problem in rating order (#272 of 486): [../../by-rating/272-CKWLK.md](../../by-rating/272-CKWLK.md)
