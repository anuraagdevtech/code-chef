# 111. Construct N

> CodeChef problem code [`CONN`](https://www.codechef.com/problems/CONN) &middot; difficulty **860** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Parity plus a threshold |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

You are given an integer $N$. Find if it is possible to represent $N$ as the sum of several(possibly zero) $2$'s and several(possibly zero) $7$'s.

Formally, find if there exist two integers $X, Y \ (X, Y \ge 0)$ such that $2 \cdot X + 7\cdot Y = N$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line containing an integer $N$.

**Output**

For each test case, print on a new line `YES` if it is possible to represent $N$ as the sum of several(possibly zero) $2$'s and several(possibly zero) $7$'s and `NO` otherwise.

You may print each character of the string in either uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes`, and `YES` will all be treated as identical).

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^8$

## Sample

**Sample input**

```
4
2
5
7
11
```

**Sample output**

```
YES
NO
YES
YES
```

<details><summary>Explanation</summary>

**Test case $1$:** $2 \cdot 1 + 7\cdot 0 = 2$.

**Test case $2$:** It is impossible to express $5$ as a sum of several $2$'s and $7$'s.

**Test case $3$:** $2 \cdot 0 + 7\cdot 1 = 7$.

**Test case $4$:** $2 \cdot 2 + 7\cdot 1 = 11$.

</details>

## Approach

We need non-negative $X, Y$ with $2X + 7Y = N$. Split on the parity of $N$.

**$N$ even.** Take $Y = 0$ and $X = N/2$. Always works, so every even $N$ is representable — including $N = 2$ itself.

**$N$ odd.** The term $2X$ is always even, so $7Y$ must be odd, which forces $Y$ to be odd. The cheapest odd choice is $Y = 1$, leaving $N - 7$ to be covered by $2$s. Since $N$ is odd, $N - 7$ is even, so it splits into $2$s exactly — provided it is not negative. Hence odd $N$ works precisely when $N \geq 7$.

Larger odd $Y$ never helps: $Y = 3$ consumes $21$, so if that leaves a valid remainder then $Y = 1$ certainly did too. Trying the smallest qualifying $Y$ is enough.

Putting it together:

$$\text{YES} \iff N \text{ is even, or } N \geq 7$$

The only `NO` answers are the odd numbers below $7$: $1, 3, 5$. Sample case 2 is $N = 5$, and $N = 1$ and $N = 3$ fail the same way.

This is a small instance of the **Chicken McNugget / Frobenius** problem. Because $\gcd(2, 7) = 1$, all sufficiently large $N$ are representable, and the largest unrepresentable value is $2 \cdot 7 - 2 - 7 = 5$ — exactly matching the analysis above. With $N$ up to $10^8$, a search over $Y$ would be needlessly slow; the closed condition is $O(1)$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Even n splits into 2s. Odd n needs one 7, so it must reach 7.
        out.append("YES" if n % 2 == 0 or n >= 7 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **$N = 7$**, the smallest odd value that works: one $7$ and nothing else, so `YES`. This is the boundary.
- **$N = 5$**, the largest odd failure: too small to contain a $7$, and no combination of even parts can reach an odd total, so `NO`. The sample has both sides of the boundary.
- **$N = 1, 3$**: `NO` for the same reason.
- **$N = 2$**: a single $2$, so `YES`.
- The reasoning in one line: an even $N$ splits entirely into $2$s, while an odd $N$ needs at least one odd part — and the only odd part available is $7$, leaving an even remainder. So odd $N$ works exactly when $N \geq 7$.

## Dry run

| $N$ | parity | reaches 7? | construction | output |
|---:|---|:---:|---|---|
| 2 | even | — | $2$ | `YES` |
| 5 | odd | no | impossible | `NO` |
| 7 | odd | yes | $7$ | `YES` |
| 11 | odd | yes | $7 + 2 + 2$ | `YES` |

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#109 of 486): [../../by-rating/109-CONN.md](../../by-rating/109-CONN.md)
