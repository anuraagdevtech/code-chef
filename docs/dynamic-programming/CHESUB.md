[&larr; 697. Search for 404](CS2023_404.md) &middot; [Index](../../README.md) &middot; [703. Merging Binary Strings &rarr;](MERGEBS.md)

# 701. K-Subarrays

> CodeChef problem code [`CHESUB`](https://www.codechef.com/problems/CHESUB) &middot; difficulty **2306** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Two arrays per count - subarray still open, or best so far |
| **Time** | $O(N \cdot K)$ per test case |
| **Space** | $O(K)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

You are given two integers $N$ and $K$, and an array $A$ of $N$ integers. You have to choose $K$ disjoint non-empty subarrays such that the score is maximized.

The score is calculated as follows:
$$
\mathrm{Score}= \sum_{i=1}^{K} \mathrm{Sum}[i] \cdot i,
$$

where $\mathrm{Sum}[i]$ denotes sum of elements of $i$-th subarray. By the $i$-th subarray, we mean the $i$-th one in the order from left to right.

Find the maximum score that can be achieved.

**Note:** The subarrays are not required to cover the whole array. It is allowed for some elements of $A$ to belong to none of the subarrays.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line of each test case contains $N$ space-separated integers $A_1,A_2,\dots,A_N$.

**Output**
For each test case, print a single line containing one integer ― the maximum score.

**Constraints**
- $1 \le T \le 1000$
- $1 \le N \le 10^5$
- $1 \le K \le \min(100,N)$
- $-10^6 \le A_i \le 10^6$
- The sum of $N$ over all test cases does not exceed $10^5$

**Subtasks**
- **Subtask #1 (15 points)**: $K=1$
- **Subtask #2 (35 points):** $K=2$
- **Subtask #3 (50 points):** Original constraints

## Constraints

- $1 \le T \le 1000$
- $1 \le N \le 10^5$
- $1 \le K \le \min(100,N)$
- $-10^6 \le A_i \le 10^6$
- The sum of $N$ over all test cases does not exceed $10^5$

## Sample

**Sample input**

```
2
5 2
1 2 -1 3 1
5 2
-1 2 11 -23 12
```

**Sample output**

```
11
37
```

<details><summary>Explanation</summary>

- **Test Case 1:** One way to choose $2$ disjoint non-empty subarrays is:

$S_1 = [1,2]$ and $S_2 = [3,1]$

The score is $3\cdot 1 + 4\cdot 2 =11$, which is the maximum possible.

- **Test Case 2:** One way to choose $2$ disjoint non-empty subarrays is:

$S_1 = [2,11]$ and $S_2 = [12]$

The score is $13\cdot 1+12\cdot 2 = 37$, which is the maximum possible.

</details>

## Approach

Process the array from left to right and keep, for every $j \le K$:

- `end[j]`: the best score when the $j$-th subarray ends exactly at the current element;
- `best[j]`: the best score using $j$ subarrays within the prefix processed so far.

For a new element $x$, the $j$-th subarray ending here either extends the $j$-th subarray that ended at the previous element, or starts fresh after the best arrangement of $j - 1$ subarrays in the earlier prefix; in both cases $x$ is added with weight $j$:

$$\text{end}[j] = \max(\text{end}[j],\; \text{best}[j-1]) + j \cdot x, \qquad \text{best}[j] = \max(\text{best}[j],\; \text{end}[j]).$$

Updating $j$ from $K$ down to 1 ensures that `best[j-1]` still refers to the prefix before the current element, so the subarrays stay disjoint. The answer is `best[K]`.

## Solution (Python)

```python
import sys


def solve(tokens):
    n, k = (next(tokens), next(tokens))
    values = [next(tokens) for _ in range(n)]
    NEG = -10 ** 30
    best = [NEG] * (k + 1)
    end = best.copy()
    best[0] = 0
    for value in values:
        for j in range(k, 0, -1):
            end[j] = max(end[j], best[j - 1]) + j * value
            best[j] = max(best[j], end[j])
    return str(best[k])


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(N \cdot K)$ per test case
- **Space:** $O(K)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Exactly $K$ non-empty subarrays are required, so `best[K]` may be negative.
- Elements may be skipped between subarrays.
- Unreachable states use a large negative sentinel that never wins a maximum.
- The weights make the order of subarrays matter - later ones count more.

## Dry run

`A = [1, 2, -1, 3, 1]`, `K = 2`. Values of (`best[1]`, `best[2]`) after each element:

| element | end[1] | best[1] | end[2] | best[2] |
|---:|---:|---:|---:|---:|
| 1 | 1 | 1 | - | - |
| 2 | 3 | 3 | 5 | 5 |
| -1 | 2 | 3 | 3 | 5 |
| 3 | 5 | 5 | 9 | 9 |
| 1 | 6 | 6 | 11 | 11 |

Answer 11: `[1, 2]` with weight 1 and `[3, 1]` with weight 2.

> CodeChef tags: `Data Structures`, `Arrays`, `Algorithms`, `Dynamic Programming`, `DP Approach`, `Greedy`

---

Same problem in rating order (#664 of 735): [../../by-rating/664-CHESUB.md](../../by-rating/664-CHESUB.md)
