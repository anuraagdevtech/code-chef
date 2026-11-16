[&larr; 575. MasterChef](MCHEF.md) &middot; [Index](../../README.md) &middot; [577. Coin Partition &rarr;](COINPART.md)

# 576. Permutation Split

> CodeChef problem code [`PERMSPL`](https://www.codechef.com/problems/PERMSPL) &middot; difficulty **2996** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Subset sum of inversion-graph degrees |
| **Time** | $O(N^2+NI/w)$ word operations per test case for $I$ total inversions |
| **Space** | $O(N+I/w)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

For a sequence of positive integers $A_1, A_2, \ldots, A_K$, let's define the number of inversions in it as the number of pairs of integers $(i, j)$ such that $1 \le i \lt j \le K$ and $A_i \gt A_j$.

You are given a permutation $P_1, P_2, \ldots, P_N$ of the integers $1$ through $N$. Determine if it is possible to partition this permutation into two subsequences (possibly empty or non-contiguous) such that:
- Each element of $P$ appears in exactly one of these subsequences.
- The numbers of inversions in one subsequence is equal to the number of inversions in the other subsequence.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $P_1, P_2, \ldots, P_N$.

**Output**
For each test case, print a single line containing the string `"YES"` if it is possible to partition the permutation in a given way or `"NO"` if it is impossible.

**Constraints**
- $1 \le N \le 100$
- $1 \le P_i \le N$ for each valid $i$
- $P_1, P_2, \ldots, P_N$ are pairwise distinct
- the sum of $N$ over all test cases does not exceed $200$

**Subtasks**
**Subtask #1 (20 points):** $N \le 16$

**Subtask #2 (80 points):** original constraints

## Constraints

- $1 \le N \le 100$
- $1 \le P_i \le N$ for each valid $i$
- $P_1, P_2, \ldots, P_N$ are pairwise distinct
- the sum of $N$ over all test cases does not exceed $200$

## Sample

**Sample input**

```
4
1
1
3
3 2 1
4
4 3 2 1
5 
1 4 3 2 5
```

**Sample output**

```
YES
NO
YES
NO
```

<details><summary>Explanation</summary>

**Example case 1:** We can split $(1)$ into $(1)$ and $()$. There are $0$ inversions in each of these sequences.

**Example case 3:** We can split $(4, 3, 2, 1)$ into $(4, 3)$ and $(2, 1)$. There is $1$ inversion in each of them. Note that this is not the only solution ? we could also split the permutation into sequences $(4, 1)$ and $(3, 2)$.

</details>

## Approach

Form the inversion graph: each permutation position is a vertex, and each inversion is an undirected edge. Let $I$ be the total edge count. If positions are partitioned into $S$ and its complement, then `sum(degree[u] for u in S) - I` equals the number of internal inversions in $S$ minus the number in the complement; crossing edges cancel.

Therefore equal inversion counts are possible exactly when some subset of vertex degrees sums to $I$. Compute degrees by testing all pairs, then solve this subset-sum question with an integer bitset capped at $I$. Empty subsequences are naturally included.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        p = [int(next(tokens)) for _ in range(n)]
        degree = [0]*n
        inversions = 0
        for i in range(n):
            for j in range(i+1,n):
                if p[i] > p[j]:
                    degree[i] += 1
                    degree[j] += 1
                    inversions += 1
        reachable = 1
        mask = (1 << (inversions+1))-1
        for d in degree:
            reachable |= (reachable << d)&mask
        out.append('YES' if reachable >> inversions&1 else 'NO')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N^2+NI/w)$ word operations per test case for $I$ total inversions
- **Space:** $O(N+I/w)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- With no inversions, the empty subset already reaches target zero.
- Degrees count inversion partners on both sides of a position.
- Merely checking that the total inversion count is even is insufficient.

## Dry run

For `[3,2,1]`, every vertex has degree two, but the target is three inversions, which no subset of degrees reaches. For `[4,3,2,1]`, target six is reached by choosing two vertices of degree three.

> CodeChef tags: `Algorithms`, `Dynamic Programming`, `Constructive`

---

Same problem in rating order (#714 of 735): [../../by-rating/714-PERMSPL.md](../../by-rating/714-PERMSPL.md)
