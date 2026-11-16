[&larr; 678. Two Averages](678-TWOAVG.md) &middot; [Index](README.md) &middot; [680. Chandelier &rarr;](680-CHANDWEIGHT.md)

# 679. Chef and Riffles

> [`RIFFLES`](https://www.codechef.com/problems/RIFFLES) &middot; difficulty **2360** &middot; time limit **2s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | A riffle is multiplication by two modulo N - 1 |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N + \log K)$ per test case |
| **Space** | $O(N)$ for the output |

## Question

Let $f$ be a [permutation](https://en.wikipedia.org/wiki/Permutation) of length $N$, where $N$ is **even**. The *riffle* of $f$ is defined to be the permutation
$$g = (f(1), f(3), \ldots, f(N-1), f(2), f(4), \ldots, f(N))$$

You are given two integers $N$ and $K$. Output the resultant permutation when you riffle the identity permutation of length $N$, $K$ times.

The identity permutation of length $N$ is ${\sigma}_N = (1, 2, \ldots, N)$

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line of input, containing two space-separated integers $N$ and $K$.

**Output**

For each test case, output the answer permutation as $N$ space-separated integers in a new line.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 3 \cdot 10^5$
- $1 \leq K \leq 10^9$
- $N$ is even
- The sum of $N$ across test cases does not exceed $3 \cdot 10^5$

**Subtasks**

- **Subtask 1 (30 points):** $N$ is a power of $2$
- **Subtask 2 (70 points):** Original constraints

## Sample

**Sample input**

```
3
6 1
8 2
14 452
```

**Sample output**

```
1 3 5 2 4 6
1 5 2 6 3 7 4 8
1 10 6 2 11 7 3 12 8 4 13 9 5 14
```

<details><summary>Explanation</summary>

**Test case $1$:** Performing the riffle on $\sigma_6 = (1, 2, 3, 4, 5, 6)$ once results in $(1, 3, 5, 2, 4, 6)$, by definition.

**Test case $2$:** The process goes as follows:
- Performing the riffle on $(1, 2, 3, 4, 5, 6, 7, 8)$ results in $(1, 3, 5, 7, 2, 4, 6, 8)$
- Performing the riffle on $(1, 3, 5, 7, 2, 4, 6, 8)$ results in $(1, 5, 2, 6, 3, 7, 4, 8)$

</details>

## Approach

Use 0-based positions. After one riffle, position $i$ in the first half holds the old element from position $2i$, and position $N/2 + i$ holds the old element from position $2i + 1$. Both cases are described by one formula: position $i < N - 1$ reads from position $2i \bmod (N - 1)$, and the last position reads from itself.

Applying this $K$ times, position $i$ ends up reading from position $i \cdot 2^K \bmod (N - 1)$ of the original arrangement. The original arrangement is the identity, so the answer at 0-based position $i$ is

$$(i \cdot 2^K \bmod (N - 1)) + 1 \quad (i < N - 1), \qquad N \text{ at the last position}.$$

$2^K \bmod (N - 1)$ is one modular exponentiation.

## Solution

```python
import sys


def solve(tokens):
    n, k = (next(tokens), next(tokens))
    multiplier = pow(2, k, n - 1)
    return ' '.join((str(i * multiplier % (n - 1) + 1) for i in range(n - 1))) + ' ' + str(n)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- $N = 2$: the modulus is 1, everything maps to position 0, and the permutation stays `1 2`.
- $K$ up to $10^9$ is no problem for fast exponentiation.
- The first and the last element never move.
- The riffle has a period dividing the order of 2 modulo $N - 1$, but it is not needed.

## Dry run

`N = 8, K = 2`: $2^2 \bmod 7 = 4$.

Positions $0 \dots 6$ read from $0, 4, 1, 5, 2, 6, 3$, giving the values `1 5 2 6 3 7 4`, and the last position holds 8.

Output `1 5 2 6 3 7 4 8`.

---

Same problem grouped by topic: [../docs/number-theory/RIFFLES.md](../docs/number-theory/RIFFLES.md)
