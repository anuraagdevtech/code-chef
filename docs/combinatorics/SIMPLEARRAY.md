[&larr; 704. Red Green Grids](REDGREEN.md) &middot; [Index](../../README.md) &middot; [719. Weird Values &rarr;](WRDVLS.md)

# 708. Potato to Gold

> CodeChef problem code [`SIMPLEARRAY`](https://www.codechef.com/problems/SIMPLEARRAY) &middot; difficulty **2326** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Independent choices per pair of complementary remainders |
| **Time** | $O(N + K)$ per test case |
| **Space** | $O(K)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

You are given an array $A$ of $N$ integers and an integer $K$. Find the number of (**possibly empty**) [subsequences](https://en.wikipedia.org/wiki/Subsequence) of $A$ such that no two elements in the subsequence have a sum that is divisible by $K$.

Two subsequences are considered distinct if they are made up of different indices. For example, $A = [1, 2, 1, 2]$ contains $[1, 2]$ as a subsequence three times, and all $3$ must be counted separately in the answer.

More formally,
- Let $S = \{x_1, x_2, \ldots, x_m\}$ be a (possibly empty) set such that $1 \leq x_1 \lt x_2 \lt \ldots \lt x_m \leq N$.
- $S$ is said to be *good* if $A_{x_i} + A_{x_j}$ is not divisible by $K$ for any $1 \leq i \lt j \leq m$. In particular, any subsequence of size $\leq 1$ is *good*.
- Your task is to count the number of *good* sets.

Since the answer can be very large, print it modulo $10^9 + 7$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space separated integers, $N$ and $K$.
    - The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$

**Output**

For each test case, output on a new line number of subsequences satisfying the condition, modulo $10^9 + 7$.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 10^5$
- $1 \leq K \leq 5 \cdot 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ and $K$ over all test cases won't exceed $10^6$.

## Sample

**Sample input**

```
3
3 4
4 5 7
5 4
1 2 3 4 5
5 3
1 2 3 4 5
```

**Sample output**

```
6
20
14
```

<details><summary>Explanation</summary>

**Test case $1$:** Here, $K = 4$. There are $8$ subsequences of the array, and they are considered as follows:
- $[]$: the empty subsequence. It satisfies the condition.
- $[4], [5], [7]$: size $1$ subsequences, all are good.
- $[4, 5]$: good, because $4+5 = 9$ is not a multiple of $4$
- $[4, 7]$: good, because $4+7 = 11$ is not a multiple of $4$
- $[5, 7]$: not good, because $5+7=12$ is a multiple of $4$.
- $[4, 5, 7]$: not good, again because it contains $5$ and $7$.

So, $6$ of the subsequences are good.

</details>

## Approach

Two elements have a sum divisible by $K$ exactly when their remainders $r$ and $s$ satisfy $r + s \equiv 0 \pmod K$. So group the elements by remainder; a conflict only ever involves the classes $r$ and $K - r$.

- Remainder 0 (and remainder $K/2$ when $K$ is even) conflicts with itself: at most one element of the class may be chosen, $c + 1$ possibilities.
- For $0 < r < K/2$ the classes $r$ and $K - r$ conflict with each other but not internally: choose any subset of one class or any subset of the other. That is $2^{c_r} + 2^{c_{K-r}} - 1$ possibilities, the empty choice being counted once.

Different pairs of classes are independent, so the answer is the product of these factors; the empty subsequence is included automatically.

## Solution (Python)

```python
import sys


def solve(tokens):
    n, k = (next(tokens), next(tokens))
    count = [0] * k
    for _ in range(n):
        count[next(tokens) % k] += 1
    MOD = 1000000007
    answer = count[0] + 1
    for residue in range(1, (k + 1) // 2):
        answer = answer * (pow(2, count[residue], MOD) + pow(2, count[k - residue], MOD) - 1) % MOD
    if k % 2 == 0:
        answer = answer * (count[k // 2] + 1) % MOD
    return str(answer)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(N + K)$ per test case
- **Space:** $O(K)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $K = 1$: every pair conflicts, so the answer is $N + 1$.
- $K = 2$: both classes are self-conflicting.
- Equal values at different indices are different elements.
- Powers of two are taken modulo $10^9 + 7$.

## Dry run

`A = [4, 5, 7]`, `K = 4`: remainders `0, 1, 3`.

- remainder 0: one element, factor $1 + 1 = 2$.
- pair (1, 3): one element each, factor $2 + 2 - 1 = 3$.

Answer $2 \cdot 3 = 6$ - all subsets except those containing both 5 and 7.

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#672 of 735): [../../by-rating/672-SIMPLEARRAY.md](../../by-rating/672-SIMPLEARRAY.md)
