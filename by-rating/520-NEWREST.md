[&larr; 519. Stacks](519-STACKS.md) &middot; [Index](README.md) &middot; [521. A temple of Snakes &rarr;](521-SNTEMPLE.md)

# 520. New Restaurant

> [`NEWREST`](https://www.codechef.com/problems/NEWREST) &middot; difficulty **1800** &middot; time limit **1s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Stirling numbers of the second kind times a falling factorial |
| **Complexity class** | Quadratic $O(n^2)$ |
| **Time** | $O(N_{\max}^2 + \sum \min(N, M, K))$ |
| **Space** | $O(N_{\max} + T)$ |

## Question

Chef Dengklek will open a new restaurant in the city. The restaurant will be open for N days. He can cook M different types of dish. He would like to cook a single dish every day, such that for the entire N days, he only cook at most K distinct types of dishes.

In how many ways can he do that?

**Input**

The first line contains a single integer T, the number of test cases. T test cases follow. Each test case consists of a single line consisting of three integers N, M, K.

**Output**

For each test case, output a single line consisting the number of different ways he can cook for the entire N days, modulo 1000000007.

**Constraints**

- 1 ≤ T ≤ 100

- 1 ≤ N ≤ 1000

- 1 ≤ M ≤ 1000000

- 1 ≤ K ≤ 1000

## Constraints

- 1 ≤ T ≤ 100
- 1 ≤ N ≤ 1000
- 1 ≤ M ≤ 1000000
- 1 ≤ K ≤ 1000

## Sample

**Sample input**

```
4
1 1 1
2 2 2
4 3 2
5 7 3
```

**Sample output**

```
1
4
45
5887
```

## Approach

Count the schedules that use exactly $j$ distinct dishes and sum over $j \le K$.

Using exactly $j$ dishes means splitting the $N$ days into $j$ non-empty groups (days with the same dish) and giving the groups distinct dishes. The number of splittings is the Stirling number of the second kind $S(N, j)$, and the dishes can be assigned in $M (M-1) \cdots (M-j+1)$ ways, so

$$\text{answer} = \sum_{j=1}^{\min(N, M, K)} S(N, j) \cdot M^{\underline{j}}.$$

The Stirling row is advanced in place with $S(n, j) = j \cdot S(n-1, j) + S(n-1, j-1)$; test cases are grouped by $N$ and answered when their row is reached. $M$ can be a million but only the first $\min(N, K)$ factors of the falling factorial are needed.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    cases = [(next(tokens), next(tokens), next(tokens)) for _ in range(next(tokens))]
    MOD = 1000000007
    most_days = max((n for n, m, k in cases), default=0)
    by_days = {}
    for i, c in enumerate(cases):
        by_days.setdefault(c[0], []).append((i, c[1], c[2]))
    stirling = [1] + [0] * most_days
    answers = [0] * len(cases)
    for n in range(1, most_days + 1):
        for j in range(n, 0, -1):
            stirling[j] = (stirling[j] * j + stirling[j - 1]) % MOD
        stirling[0] = 0
        for i, m, k in by_days.get(n, []):
            fall = 1
            total = 0
            for j in range(1, min(n, m, k) + 1):
                fall = fall * (m - j + 1) % MOD
                total = (total + fall * stirling[j]) % MOD
            answers[i] = total
    print('\n'.join(map(str, answers)))


if __name__ == "__main__":
    main()
```

## Edge cases

- $j$ cannot exceed $N$ (days), $M$ (dishes) or $K$ (limit).
- $K \ge N$ and $M \ge N$ gives all $M^N$ schedules.
- The in-place row update must run from high $j$ to low $j$.
- Everything is modulo $10^9 + 7$.

## Dry run

`N = 4, M = 3, K = 2`. $S(4, 1) = 1$, $S(4, 2) = 7$.

- one dish: $1 \cdot 3 = 3$
- two dishes: $7 \cdot (3 \cdot 2) = 42$

Answer 45.

---

Same problem grouped by topic: [../docs/combinatorics/NEWREST.md](../docs/combinatorics/NEWREST.md)
