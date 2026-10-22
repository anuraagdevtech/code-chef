[&larr; 271. Palindrome Pain](PALINPAIN.md) &middot; [Index](../../README.md) &middot; [292. Chef and squares &rarr;](CHSQR.md)

# 284. Prefix Permutation

> CodeChef problem code [`PREFPERM`](https://www.codechef.com/problems/PREFPERM) &middot; difficulty **1532** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Blocks that only close at the right moment |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

You are given an array $A$ of length $K$. Find any permutation $P$ of length $N$ such that only the prefixes of length $A_i$ ($1 \le i \le K$) form a permutation.

Under the given constraints, it is guaranteed that there exists at least one permutation which satisfies the given condition.

If there are multiple solutions, you may print any.

Note: A permutation of length $N$ is an array where every element from $1$ to $N$ occurs exactly once.

**Input**

- The first line of the input contains a single integer $T$ - the number of test cases.
- The first line of each test case contains two integers $N$ and $K$ - the length of the permutation to be constructed and the size of the array $A$ respectively.
- The second line of each test case contains $K$ space-separated integers $A_1, A_2, \dots, A_K$ denoting the array $A$.

**Output**

For each test case, print a single line containing $N$ space-separated integers $P_1, \dots, P_{N}$ $(1 \le P_i \le N)$. If there are multiple solutions, you may print any.

## Constraints

- $1 \le T \le 10^5$
- $1 \le K \le N \le 10^5$
- $1 \le A_1 \lt A_2 \lt ... \lt A_K = N$
- the sum of $N$ over all test cases does not exceed $5 \cdot 10^5$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
3
8 4
3 6 7 8
7 1
7
5 5
1 2 3 4 5
```

**Sample output**

```
2 3 1 6 4 5 7 8
4 6 1 5 2 7 3
1 2 3 4 5
```

<details><summary>Explanation</summary>

**Test case-1:** $[2, 3, 1, 6, 4, 5, 7, 8]$ is valid permutation because
- Prefix of length $3 = [2, 3, 1]$ is a permutation.
- Prefix of length $6 = [2, 3, 1, 6, 4, 5]$ is a permutation.
- Prefix of length $7 = [2, 3, 1, 6, 4, 5, 7]$ is a permutation.
- Prefix of length $8 = [2, 3, 1, 6, 4, 5, 7, 8]$ is a permutation.
- None of the other prefixes form a permutation.

</details>

## Approach

A prefix of length $L$ is a permutation exactly when it contains precisely $\{1, \ldots, L\}$. The required lengths $A_1 < A_2 < \cdots < A_K = N$ therefore cut the array into **blocks**: positions $A_{i-1}+1 \ldots A_i$ must hold exactly the values $A_{i-1}+1 \ldots A_i$, since everything smaller is already used up by the earlier prefixes.

That fixes *which* values go in each block. The only freedom is their order inside it — and that order must ensure **no prefix ending strictly inside a block is a permutation**.

The trick is to place each block's **largest value first**. Then any prefix that stops partway through the block already contains that largest value $A_i$ but is shorter than $A_i$, so it cannot be a permutation of $\{1, \ldots, L\}$ for its own length $L$ — it holds a value too big. Only at the block's end, where length and maximum finally agree, does it close.

So each block is emitted as $A_i$, then $A_{i-1}+1, A_{i-1}+2, \ldots, A_i - 1$.

Blocks of size $1$ need no care: the single position is both the start and the end, and the prefix there is required to be a permutation anyway.

For the sample $N = 8$ with $A = [3,6,7,8]$, this yields `3 1 2 | 6 4 5 | 7 | 8`. The published answer, `2 3 1 6 4 5 7 8`, orders the first block differently — both are valid, so **any correct permutation is accepted** and this is judged by a checker.

The guarantee $A_K = N$ means the blocks exactly tile the array, so no leftover values remain.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        a = [int(v) for v in data[pos + 2:pos + 2 + k]]
        pos += 2 + k
        perm = []
        prev = 0
        for end in a:
            # Largest value first, so no prefix closes before the block ends.
            perm.append(end)
            perm.extend(range(prev + 1, end))
            prev = end
        out.append(" ".join(map(str, perm)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **Putting the block's largest value first is what prevents an early close.** Within the block $(\text{prev}, \text{end}]$, the prefix cannot be a permutation until every value up to `end` has appeared — and since `end` itself leads, no intermediate prefix has its maximum equal to its length.
- **Only the listed prefixes may be permutations**, so the construction must block all the others — which is exactly what the leading maximum achieves, block by block.
- **The listed lengths close automatically**: after finishing block $i$, the values seen are precisely $1 \dots A_i$.
- **$A_K = N$ is guaranteed**, so the blocks tile the whole array and nothing is left over.
- **A block of size $1$** contributes just its own value, as the third sample row does throughout — giving the identity permutation when every prefix must be good.
- **$K = 1$** means only the full array may be a permutation, so one big block runs from $1$ to $N$ with $N$ in front.
- **This answer differs from the sample's** at $N = 8$ (`3 1 2 6 4 5 7 8` against `2 3 1 6 4 5 7 8`); both have good prefixes at exactly $3, 6, 7, 8$, so a special judge checks which prefixes close.

## Dry run

First sample: $N = 8$ with $A = 3, 6, 7, 8$ gives $P = 3, 1, 2, 6, 4, 5, 7, 8$.

| prefix length | values seen | permutation? |
|---:|---|:---:|
| 1 | $\{3\}$ | no |
| 2 | $\{1,3\}$ | no |
| 3 | $\{1,2,3\}$ | **yes** |
| 4 | $\{1,2,3,6\}$ | no |
| 5 | $\{1,2,3,4,6\}$ | no |
| 6 | $\{1,\dots,6\}$ | **yes** |
| 7 | $\{1,\dots,7\}$ | **yes** |
| 8 | $\{1,\dots,8\}$ | **yes** |

Exactly the four listed lengths close.

> CodeChef tags: `Algorithms`

---

Same problem in rating order (#317 of 486): [../../by-rating/317-PREFPERM.md](../../by-rating/317-PREFPERM.md)
