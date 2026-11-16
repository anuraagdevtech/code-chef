[&larr; 692. Balanced Suffix](692-BALSUFF.md) &middot; [Index](README.md) &middot; [694. Treeversion &rarr;](694-TREEVERS.md)

# 693. Good Sequence

> [`GSEQ`](https://www.codechef.com/problems/GSEQ) &middot; difficulty **2451** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Longest chain of boundaries whose prefix value rises by exactly one |
| **CodeChef tags** | `Algorithms`, `Dynamic Programming`, `Greedy` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ expected per test case |
| **Space** | $O(N)$ |

## Question

Suppose you have a **binary** array $B$ of length $N$.
A sequence $x_1, x_2, \ldots, x_k$ is called *good* with respect to $B$ if it satisfies the following conditions:
- $1 \leq x_1 \lt x_2 \lt \ldots \lt x_k \leq N+1$
- For *every* pair $(i, j)$ such that $1 \leq i \lt j \leq k$, the subarray $B[x_i: x_j-1]$ contains $(j-i)$ more ones than zeros.
    - That is, if $B[x_i : x_j-1]$ contains $c_1$ ones and $c_0$ zeros, then $c_1 - c_0 = j-i$ must hold.

Here, $B[L: R]$ denotes the subarray consisting of elements $[B_L, B_{L+1}, B_{L+2}, \ldots, B_R]$.
Note that in particular, a sequence of size $1$ is always *good*.

For example, suppose $B = [0,1,1,0,1,1]$. Then,
- The sequence $[1,4,7]$ is a *good* sequence. The subarrays that need to be checked are $B[1:3], B[1:6]$ and $B[4:6]$, which all satisfy the condition.
- The sequence $[1, 5]$ is not *good*, because $B[1:4] = [0, 1, 1, 0]$ contains an equal number of zeros and ones (when it should contain one extra $1$).

Alice gave Bob a binary array $A$ of size $N$ and asked him to find the **longest** sequence that is *good* with respect to $A$. Help Bob find one such sequence.
If multiple possible longest sequences exist, you may print **any** of them.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the size of the binary array.
    - The second line contains $N$ space-separated numbers — $A_1 , A_2 , \ldots , A_N$.

**Output**

Each test case requires two lines of output:
- First, print on a new line a single integer $K$ — the maximum length of a sequence that is good with respect to $A$
- On the next line, print $K$ space-separated integers in **increasing order**, denoting the indices of one such sequence.

If there are multiple possible good sequences with maximum size, output any of them.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $0 \leq A_i \leq 1$
- The sum of $N$ over all test cases won't exceed $10^6$.

## Sample

**Sample input**

```
4
6
0 1 1 0 1 1
5
0 1 0 1 0
4
1 1 1 1
3
1 0 0
```

**Sample output**

```
4
2 5 6 7
2
4 5
5
1 2 3 4 5
2
1 2
```

<details><summary>Explanation</summary>

**Test case $1$:** We have $A = [0, 1, 1, 0, 1, 1]$. The sequence $[2, 5, 6, 7]$ requires us to check $6$ subarrays:
- $A[2:4] = [1, 1, 0]$ which has $c_1 - c_0 = 1$ and corresponds to $i = 1, j = 2$
- $A[2:5] = [1, 1, 0, 1]$ which has $c_1 - c_0 = 2$ and corresponds to $i = 1, j = 3$
- $A[2:6] = [1, 1, 0, 1, 1]$ which has $c_1 - c_0 = 3$ and corresponds to $i = 1, j = 4$
- $A[5:5] = [1]$, which has $c_1 - c_0 = 1$ and corresponds to $i = 2, j = 3$
- $A[5:6] = [1, 1]$, which has $c_1 - c_0 = 2$ and corresponds to $i = 2, j = 4$
- $A[6:6] = [1]$, which has $c_1 - c_0 = 1$ and corresponds to $i = 3, j = 4$

As you can see, all $6$ pairs satisfy the condition.

**Test case $2$:** The only subarray that needs to be checked is $A[4:4] = [1]$, which has $c_1 - c_0 = 1$ as needed. It can be verified that no good sequence of length greater than $2$ exists.

</details>

## Approach

Replace ones by $+1$ and zeros by $-1$ and let $h_x$ be the prefix sum just before position $x$ ($h_1 = 0$, defined for $x = 1 \dots N + 1$). The subarray $B[x_i : x_j - 1]$ has (ones $-$ zeros) $= h_{x_j} - h_{x_i}$.

The condition for all pairs is therefore $h_{x_j} - h_{x_i} = j - i$, which holds for all pairs as soon as it holds for consecutive ones: a good sequence is a chain of boundaries, increasing in position, whose heights go up by exactly 1 at each step.

Scan the boundaries from left to right. Let `best_at[v]` be the longest chain found so far that ends at a boundary of height $v$, together with that boundary. A chain ending at the current boundary of height $s$ extends the best chain ending at height $s - 1$, so its length is `best_at[s - 1] + 1`; store it if it improves `best_at[s]`, and remember the predecessor to rebuild the chain. The longest chain overall is the answer; its boundaries are printed in increasing order.

## Solution

```python
import sys


def solve(tokens):
    n = next(tokens)
    bits = [next(tokens) for _ in range(n)]
    best_at = {0: (1, 0)}
    previous = [-1] * (n + 1)
    height = 0
    best = (1, 0)
    for i, x in enumerate(bits, 1):
        height += 2 * x - 1
        v, j = best_at.get(height - 1, (0, -1))
        current = (v + 1, i)
        previous[i] = j
        if current[0] > best_at.get(height, (0, 0))[0]:
            best_at[height] = current
        if current[0] > best[0]:
            best = current
    chain = []
    j = best[1]
    while j >= 0:
        chain.append(j + 1)
        j = previous[j]
    return str(best[0]) + '\n' + ' '.join(map(str, reversed(chain)))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- A single boundary is always a good sequence, so the answer is at least 1.
- All ones: every boundary is used, length $N + 1$.
- Heights can be negative, so a dictionary is used.
- Several longest chains may exist, so the output is validated by a checker.

## Dry run

`A = [0, 1, 1, 0, 1, 1]`. Heights at boundaries 1-7: `0 -1 0 1 0 1 2`.

Chain lengths: boundary 1 (height 0): 1. Boundary 2 (height $-1$): 1. Boundary 3 (height 0): extends boundary 2, length 2. Boundary 4 (height 1): 3. Boundary 5 (height 0): 2. Boundary 6 (height 1): 3. Boundary 7 (height 2): 4.

One longest chain is `2 3 4 7` with heights $-1, 0, 1, 2$; the sample's `2 5 6 7` is another.

---

Same problem grouped by topic: [../docs/dynamic-programming/GSEQ.md](../docs/dynamic-programming/GSEQ.md)
