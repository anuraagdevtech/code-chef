[&larr; 623. Counting Mobiles](MOBCNT.md) &middot; [Index](../../README.md) &middot; [661. SUM OR &rarr;](AWESUM_OR.md)

# 643. Parity Permutation

> CodeChef problem code [`PARPER`](https://www.codechef.com/problems/PARPER) &middot; difficulty **2066** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Index parity classes must be uniform in value parity |
| **Time** | $O(N)$ per test case |
| **Space** | $O(\max N)$ for factorials |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

You are given an array $A$ of length $N$ containing **distinct** integers and an integer $K$ (either $0$ or $1$).

Your task is to find the total number of permutations of array $A$ such that for **all** pairs $(i, j)$
with $1 \leq i \lt j \leq N$, and $(i + j)$ being an **odd** number:
- $(A_i+A_j) \% 2$ $= K$

You should output the count of such permutations modulo $10^9+7$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $K$, as mentioned in statement.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots ,A_N$ — the elements of the array.

**Output**

For each test case, output on a new line, the total number of permutations of array $A$ satisfying the conditions, modulo $10^9 + 7$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- $0 \leq K \leq 1$
- The sum of $N$ over all test cases won't exceed $5\cdot 10^5$.

## Sample

**Sample input**

```
3
5 0
6 10 1 4 8
4 0
17 13 21 3
3 1
1 2 3
```

**Sample output**

```
0
24
2
```

<details><summary>Explanation</summary>

**Test Case $1$:** There is no permutation that satisfies the required conditions.

**Test Case $2$:** All the permutations of the array satisfy the required conditions.

**Test Case $3$:** Two permutations satisfy the conditions. They are:
- $[1,2,3]$: The pairs under consideration are $(1, 2)$ and $(2, 3)$. Here $(A_1+A_2) \% 2 = 1 = K$. Similarly $(A_2+A_3) \% 2 = 1 = K$.
- $[3,2,1]$ The pairs under consideration are $(1, 2)$ and $(2, 3)$. Here $(A_1+A_2) \% 2 = 1 = K$. Similarly $(A_2+A_3) \% 2 = 1 = K$.

</details>

## Approach

A pair of positions with odd $i + j$ consists of one odd position and one even position, and every such pair is constrained. So the condition says: for every odd position $i$ and every even position $j$, $A_i + A_j \equiv K \pmod 2$.

- $K = 0$: every odd-position value has the same parity as every even-position value. For $N \ge 2$ both classes are non-empty, so all values must share one parity; then every permutation works: $N!$, otherwise 0.
- $K = 1$: all odd positions hold one parity and all even positions the other. There are $\lceil N/2 \rceil$ odd positions and $\lfloor N/2 \rfloor$ even ones. If the number of odd values $o$ equals $\lceil N/2 \rceil$ the odd values can fill the odd positions, in $o! \cdot (N - o)!$ ways; if $o = \lfloor N/2 \rfloor$ they can fill the even positions, again $o! \cdot (N - o)!$ ways. For even $N$ with $o = N/2$ both placements exist and the count doubles.

For $N = 1$ there is no pair and the single permutation counts.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    cases = []
    largest = 0
    for _ in range(next(tokens)):
        n = next(tokens)
        k = next(tokens)
        odd = sum((next(tokens) % 2 for _ in range(n)))
        cases.append((n, k, odd))
        largest = max(largest, n)
    fact = [1] * (largest + 1)
    MOD = 10 ** 9 + 7
    for i in range(1, largest + 1):
        fact[i] = fact[i - 1] * i % MOD
    for n, k, odd_count in cases:
        if n == 1:
            answer = 1
        elif k == 0:
            answer = fact[n] if odd_count == 0 or odd_count == n else 0
        else:
            answer = fact[odd_count] * fact[n - odd_count] * ((odd_count == (n + 1) // 2) + (odd_count == n // 2)) % MOD
        out.append(str(answer))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(\max N)$ for factorials
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $N = 1$: answer 1 regardless of $K$.
- The values are distinct, so permutations of the array are counted without any division.
- Even $N$ with exactly half odd values gives the factor 2 for $K = 1$.
- Only parities of the values are used.

## Dry run

`N = 3, K = 1, A = [1, 2, 3]`: two odd values, and there are $\lceil 3/2 \rceil = 2$ odd positions.

The odd values go to positions 1 and 3 ($2!$ ways) and the even value to position 2 ($1!$): answer 2 - `[1, 2, 3]` and `[3, 2, 1]`.

`N = 4, K = 0, A = [17, 13, 21, 3]`: all odd, so all $4! = 24$ permutations work.

> CodeChef tags: `Algorithms`, `Constructive`

---

Same problem in rating order (#595 of 735): [../../by-rating/595-PARPER.md](../../by-rating/595-PARPER.md)
