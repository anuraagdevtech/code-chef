# 377. Charges

> [`CHARGES`](https://www.codechef.com/problems/CHARGES) &middot; difficulty **1645** &middot; time limit **3s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Local update of an adjacency count |
| **CodeChef tags** | `Data Structures`, `Algorithms`, `String`, `Observation`, `Implementation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N + K)$ per test case |
| **Space** | $O(N)$ |

## Question

There are $N$ subatomic particles lined up in a row. There are two types: protons and electrons. Protons have a positive charge and are represented by $1$, while electrons have a negative charge and are represented by $0$.

Our current understanding of physics gives us a way to predict how the particles will be spaced out, if we know their charges. Two adjacent particles will be separated by $1$ unit if they have opposite charges, and $2$ units if they have the same charge.

When Chef is not in the kitchen, he is doing physics experiments on subatomic particles. He is testing the hypothesis by having $N$ particles in a row, and he will change the charge of a particle $K$ times. In the $i$-th update, he will change the charge of the $Q_i$-th particle. After each update, find the distance between the first and last particle.

**Note:** Each update is persistent for further updates.

**Input**
- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains three lines of input.
- The first line contains two integers $N$, $K$.
- The second line contains a string $S$ of length $N$, where $S_i$ represents the initial charge on $i$-th particle.
- The third line contains $K$ integers $Q_1, Q_2, \ldots, Q_K$, the positions of the changed particles.

**Output**
For each test case, output $K$ lines, where the $i$-th line contains the answer after the updates $Q_1,\ldots, Q_i$ have been made.

**Constraints**
- $1 \leq T \leq 5$
- $1 \leq N, K \leq 10^5$
- $S$ contains only $0$ and $1$ characters.
- $1 \leq Q_i \leq N$
- The sum of $K$ over all testcases is at most $2 \cdot 10^5$

**Subtasks**
**Subtask #1 (100 points):** original constraints

## Constraints

- $1 \leq T \leq 5$
- $1 \leq N, K \leq 10^5$
- $S$ contains only $0$ and $1$ characters.
- $1 \leq Q_i \leq N$
- The sum of $K$ over all testcases is at most $2 \cdot 10^5$

## Sample

**Sample input**

```
1
3 3
010
2 1 3
```

**Sample output**

```
4
3
2
```

<details><summary>Explanation</summary>

**Update 1:** After reversing the parity of particle $2$, the new configuration is $000$. Since all the particles have a similar charge, each is separated from the previous by a distance of $2$ units. So the location of particle $3$ is $2 + 2 = 4$ units from the first particle.

**Update 2:** After reversing the parity of particle $1$, the new configuration is $100$. Here, the charges of particles $1$ and $2$ differ, so they are separated by $1$ unit. The charges of particles $2$ and $3$ agree, so they are separated by $2$ units. So, the location of particle $3$ is $1 + 2 = 3$ units from the first particle.

**Update 3:** After reversing the charge of particle $3$, the new configuration is $101$. Here, particles $1$ and $2$ are separated by $1$ unit and particles $2$ and $3$ are separated by $1$ unit. So the location of particle $3$ is $1 + 1 = 2$ units from the first particle.

</details>

## Approach

The total length is a sum over the $N-1$ adjacent pairs, each worth $1$ or $2$. Writing $m$ for the number of pairs with **opposite** charges,

$$\text{distance} = 2(N-1) - m$$

so the whole state collapses to a single counter, and each query needs only the change in $m$.

Flipping particle $q$ changes nothing except the two pairs it belongs to, $(q-1, q)$ and $(q, q+1)$ — both of which **invert**: a matching pair becomes opposite and vice versa. So remove those pairs' contributions from $m$, flip the character, and add them back. That is $O(1)$ per update, with the ends handled by simply having fewer pairs.

Recomputing the whole string after each query would be $O(NK) = 10^{10}$; the local update makes it $O(N + K)$. No segment tree or difference array is needed, because a point flip touches a bounded number of pairs.

Updates are **persistent**, so the string must be mutated in place rather than re-read from the input each time — which also means the same position may be flipped twice and return to its original charge.

The sample runs all three cases. `010` starts with both pairs opposite, so $m = 2$ and the distance is $2 \cdot 2 - 2 = 2$. Flipping position $2$ gives `000` with $m = 0$ and distance $4$ — the maximum, since same-charge neighbours repel further. Flipping position $1$ makes `100`, with one opposite pair, giving $3$. Flipping position $3$ makes `101`, both pairs opposite again, back to $2$.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        s = bytearray(data[pos + 2])
        queries = data[pos + 3:pos + 3 + k]
        pos += 3 + k
        opposite = sum(s[i] != s[i + 1] for i in range(n - 1))
        base = 2 * (n - 1)
        for tok in queries:
            q = int(tok) - 1
            # Only q's own two pairs change, and both of them invert.
            for j in (q - 1, q):
                if 0 <= j < n - 1:
                    opposite -= s[j] != s[j + 1]
            s[q] ^= 1
            for j in (q - 1, q):
                if 0 <= j < n - 1:
                    opposite += s[j] != s[j + 1]
            out.append(str(base - opposite))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The total length is $2(N-1) - (\text{opposite pairs})$.** Each of the $N-1$ gaps costs $2$ for a matching pair and $1$ for an opposite one, so counting the opposite pairs and subtracting is enough.
- **A flip touches only two gaps** — the ones on either side of the flipped particle — and both invert, which is what makes each query $O(1)$ instead of a rescan.
- **The flips are cumulative.** Query $2$ then $1$ then $3$ in the sample operate on a string that keeps changing, so the state must be mutated rather than recomputed from the original.
- **The ends have only one adjacent gap**, which the `0 <= j < n - 1` guard handles for $Q = 1$ and $Q = N$.
- **The old contributions must be removed before the flip and the new ones added after**, or the delta is computed against a stale character.
- **$N = 1$** has no gaps at all, so the length is $0$ for every query.
- **Sum of $K \leq 2 \cdot 10^5$**: a `bytearray` for in-place flips and XOR with $1$ to toggle between the byte codes for `0` and `1`.

## Dry run

$N = 3$, $S = $ `010`, so $2(N-1) = 4$.

| query | string after | opposite pairs | length |
|---:|---|---:|---:|
| flip 2 | `000` | 0 | `4` |
| flip 1 | `100` | 1 | `3` |
| flip 3 | `101` | 2 | `2` |

The last state has both gaps opposite, so each costs $1$.

---

Same problem grouped by topic: [../docs/arrays/CHARGES.md](../docs/arrays/CHARGES.md)
