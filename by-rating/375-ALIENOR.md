[&larr; 374. Number Hunt](374-NUMHUNT.md) &middot; [Index](README.md) &middot; [376. Exam Cheating &rarr;](376-EXAMCHT.md)

# 375. ALIEN-OR

> [`ALIENOR`](https://www.codechef.com/problems/ALIENOR) &middot; difficulty **1639** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Single-bit values are necessary and sufficient |
| **CodeChef tags** | `Mathematics`, `Bit Manipulation`, `Algorithms`, `Bitwise Operation`, `Observation`, `Brute Force` |
| **Complexity class** | Product of two sizes $O(n m)$ |
| **Time** | $O(NK)$ per test case |
| **Space** | $O(K)$ |

## Question

You are given:
- positive integers $N$ and $K$ $(K \le N)$.
- an array $A$ of size $N$, where each element of the array is a **binary** string of length $K$;

For each $1\le j\lt 2^K$, your task is to find whether there exists a set of indices $\{i_1, i_2, \ldots, i_m\}$ $(1\le i_j, m \le N)$ such that:
- The decimal value of $(A_{i_1}$ $|$ $A_{i_2}$ $|$ $A_{i_3}$ $|$ $\ldots$ $|$ $A_{i_m})$ equals $j$, where $|$ denotes [bitwise OR](https://en.wikipedia.org/wiki/Bitwise_operation#:~:text=A%20bitwise%20OR%20is%20a) operation.

Print `YES` if a set of indices satisfying the given condition exists for **all** $1\le j\lt 2^K$. Otherwise, print `NO`.

**Input**

- The first line contains an integer $T$ denoting the number of test cases.
- The first line of each test case contains two integers $N$ and $K$.
- The $i$-th of the next $N$ lines contains the binary string $A_i$.

**Output**

For each test case, print `YES` if a set of indices satisfying the given condition exists for **all** $1\le j\lt 2^K$. Otherwise, print `NO`.

You may print each character of the string in uppercase or lowercase (for example, the strings `YES`, `yEs`, `yes`, and `yeS` will all be treated as identical).

## Constraints

- $1 \leq T \leq 50$
- $1 \leq N \leq 100$
- $1 \leq K \leq N$
- $|A_i| = K$
- $A_i \in \{0, 1\}$
- The sum of $N$ over all test cases won't exceed $500$.

## Sample

**Sample input**

```
3
2 2
01
10
4 3
000
010
011
100
6 3
000
001
010
011
100
101
```

**Sample output**

```
YES
NO
YES
```

<details><summary>Explanation</summary>

**Test case $1$:**
- $j = 1$ : The set of indices $\{1\}$ satisfies the condition as decimal value of $A_1 = 1 = j$.
- $j = 2$ : The set of indices $\{2\}$ satisfies the condition as decimal value of $A_2 = 2 = j$.
- $j = 3$ : The set of indices $\{1, 2\}$ satisfies the condition as decimal value of $(A_1$ $|$ $A_2) = 3 = j$.

**Test case $2$:** The set of indices for $j = 2, 3, 4, 6, 7$ are $\{2\}, \{3\}, \{4\}, \{2,4\},$ and $\{3, 4\}$ respectively.
However, there doesn't exist any set of indices for $j=1$ and $j=5$. Hence output is `NO`.

</details>

## Approach

The condition quantifies over all $2^K - 1$ targets, but it reduces to a check on $K$ of them.

**Necessity.** Consider the target $j = 2^b$, a single bit. An OR only ever adds bits, so every chosen $A_i$ must be a subset of $\{b\}$ — i.e. $0$ or $2^b$ — and at least one must be non-zero. So the array must literally **contain** the string with a single $1$ at position $b$, for every $b$.

**Sufficiency.** If all $K$ single-bit strings are present, any $j$ is the OR of the single bits in its own binary expansion, so every target is reachable.

So the whole problem is: does $A$ contain each of the $K$ powers of two? That reduces an apparent $2^K$ search to one pass over the input, which is what makes $K$ up to $100$ — and $2^K$ astronomically large — irrelevant. Note the all-zero string and any string with two or more bits set are useless for this test, though they are harmless.

The samples are built around it. Sample 1 has exactly `01` and `10`, so both single bits are present and the answer is `YES`. Sample 3 holds `001`, `010` and `100` among six strings, again `YES` — the extra multi-bit strings `011` and `101` add nothing. Sample 2 is the instructive failure: it has `010` and `100` but no `001`, so the target $j = 1$ is unreachable even though `011` *contains* that bit, and the answer is `NO`.

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
        rows = set(data[pos + 2:pos + 2 + n])
        pos += 2 + n
        # Only the K single-bit strings matter; everything else follows by OR.
        ok = all(("0" * b + "1" + "0" * (k - b - 1)).encode() in rows
                 for b in range(k))
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Only the $K$ single-bit strings matter.** An OR can never lose bits, so producing a value with exactly one bit set requires an element that *is* that single bit — and conversely, having all $K$ of them lets any $j$ be assembled from its own bits.
- **So the whole question reduces to $K$ membership tests**, not an enumeration of $2^K - 1$ targets.
- **The strings are built by position, not by integer value**, since each $A_i$ is a $K$-character string: bit $b$ corresponds to `0`*b + `1` + `0`*(K-b-1).
- **An all-zeros element is harmless but useless** — it contributes nothing to any OR, so its presence neither helps nor hurts.
- **A missing single bit is fatal** however many other strings are present: the second sample has $4$ distinct strings and still fails for want of `001`.
- **$j$ ranges over $1 \dots 2^K - 1$**, excluding $0$, which is why an all-zeros array is not required to be representable.
- **Sum of $N \leq 500$**, so a set of the raw byte strings is ample.

## Dry run

Second sample: $K = 3$ with strings `000`, `010`, `011`, `100`.

| bit | required string | present? |
|---:|---|:---:|
| 0 | `100` | yes |
| 1 | `010` | yes |
| 2 | `001` | **no** |

Output `NO`. The value $j = 1$ (binary `001`) is unreachable, since every element containing that bit — namely `011` — also carries another bit that no OR can remove.

---

Same problem grouped by topic: [../docs/bit-manipulation/ALIENOR.md](../docs/bit-manipulation/ALIENOR.md)
