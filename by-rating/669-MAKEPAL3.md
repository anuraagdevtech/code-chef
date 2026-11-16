[&larr; 668. Red Green Grids](668-REDGREEN.md) &middot; [Index](README.md) &middot; [670. Make that Array! &rarr;](670-SWAPGAME.md)

# 669. Palindrome In Making

> [`MAKEPAL3`](https://www.codechef.com/problems/MAKEPAL3) &middot; difficulty **2322** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Mirror differences, removed in signed layers |
| **CodeChef tags** | `Algorithms`, `Constructive`, `ad-hoc`, `Observation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

JJ has an array $A$ of length $N$. He can perform the following operation on $A$:
- Select any $L$, $R$ ($1 \le L \le R \le N$) and for each $i$ such that $L \le i \le R$, set $A_i := A_i + 1$.

JJ wants to make $A$ palindromic. Find the **minimum** number of moves to do so.

Note: An array is called a palindrome if it reads the same backwards and forwards, for e.g. $[1, 3, 3, 1]$ and $[6, 2, 6]$ are palindromic.

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

**Output**

For each test case, output the minimum number of moves to make $A$ palindromic.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \le A_i \le 10^9$
- Sum of $N$ over all test cases does not exceed $3 \cdot 10^5$.

## Sample

**Sample input**

```
3
6
2 6 4 3 4 1
2
1 10
3
1 10 1
```

**Sample output**

```
2
9
0
```

<details><summary>Explanation</summary>

**Test Case 1**: We can perform the following operations:
- $[2, 6, \underline{4, 3, 4, 1}] \xrightarrow{L = 3, R = 6} [2, 6, 5, 4, 5, 2]$
- $[2, 6, 5, \underline{4, 5}, 2] \xrightarrow{L = 4, R = 5} [2, 6, 5, 5, 6, 2]$

**Test Case 2:** We perform the operation on $(L = 1, R = 1)$ $9$ times after which array becomes $[10, 10]$.

**Test Case 3:** $A$ is already a palindrome.

</details>

## Approach

Let $d_i = A_i - A_{N+1-i}$ for the positions $i$ of the left half; the array is a palindrome when all $d_i$ are 0.

Adding 1 on a range that lies in the right half lowers $d$ by 1 on a contiguous range of mirrored indices, and a range in the left half raises $d$ by 1 on a contiguous range. A range that crosses the centre changes both members of the innermost pairs equally, so those cancel and the net effect is again $\pm 1$ on a contiguous range of $d$. Hence the task is: bring $d$ to zero with the fewest operations of the form "add $+1$ or $-1$ to a contiguous range".

Positive and negative parts must be handled by different kinds of operations, and inside a part of constant sign the classical layer argument applies: scanning from left to right, a new operation has to start whenever the magnitude rises above the previous one, so position $i$ costs $\max(0, |d_i| - |d_{i-1}|)$; when the sign changes, all $|d_i|$ layers are new.

## Solution

```python
import sys


def solve(tokens):
    n = next(tokens)
    values = [next(tokens) for _ in range(n)]
    previous = moves = 0
    for i in range(n // 2):
        delta = values[i] - values[-1 - i]
        moves += abs(delta) if delta * previous < 0 else max(0, abs(delta) - abs(previous))
        previous = delta
    return str(moves)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- Already a palindrome: 0.
- For odd $N$ the middle element has no partner and is ignored.
- A sign change between neighbours cannot share any operation.
- The count can be as large as $10^9$ per pair.

## Dry run

`A = [2, 6, 4, 3, 4, 1]`: $d = (2 - 1,\; 6 - 4,\; 4 - 3) = (1, 2, 1)$.

- $d_1 = 1$: one new layer (cost 1).
- $d_2 = 2$: one more layer than before (cost 1).
- $d_3 = 1$: fewer layers, nothing new.

Answer 2: one range covers all three pairs, a second covers only the middle pair.

---

Same problem grouped by topic: [../docs/greedy/MAKEPAL3.md](../docs/greedy/MAKEPAL3.md)
