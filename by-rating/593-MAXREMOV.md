[&larr; 592. Strategy for the World Cup](592-WORLDCUP.md) &middot; [Index](README.md) &middot; [594. Tetris &rarr;](594-SPCP6.md)

# 593. Max Range Queries

> [`MAXREMOV`](https://www.codechef.com/problems/MAXREMOV) &middot; difficulty **2057** &middot; time limit **1.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Net gain of removing an interval as a range sum of +1 and -1 scores |
| **CodeChef tags** | `Data Structures`, `Arrays`, `Algorithms`, `Constructive`, `Simple Algos`, `Difference Arrays`, `ad-hoc`, `Prefix Sum` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N + C)$ per test case, $C = 10^5$ |
| **Space** | $O(N + C)$ |

## Question

You have $C = 100,000$ cakes, numbered $1$ through $C$. Each cake has an integer height; initially, the height of each cake is $0$.

There are $N$ operations. In each operation, you are given two integers $L$ and $R$, and you should increase by $1$ the height of each of the cakes $L, L+1, \ldots, R$. One of these $N$ operations should be removed and the remaining $N-1$ operations are then performed.

Chef wants to remove one operation in such a way that after the remaining $N-1$ operations are performed, the number of cakes with height exactly $K$ is maximum possible. Since Chef is a bit busy these days, he has asked for your help. You need to find the maximum number of cakes with height exactly $K$ that can be achieved by removing one operation.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- Each of the next $N$ lines contains two space-separated integers $L$ and $R$ describing one operation.

**Output**
For each test case, print a single line containing one integer — the maximum possible number of cakes with height $K$.

**Constraints**
- $1 \le T \le 100$
- $2 \le N \le 10^5$
- $1 \le K \le N$
- $1 \le L \le R \le 10^5$
- the sum of $N$ over all test cases does not exceed $10^6$

## Constraints

- $1 \le T \le 100$
- $2 \le N \le 10^5$
- $1 \le K \le N$
- $1 \le L \le R \le 10^5$
- the sum of $N$ over all test cases does not exceed $10^6$

## Sample

**Sample input**

```
1
3 2
2 6
4 9
1 4
```

**Sample output**

```
3
```

<details><summary>Explanation</summary>

**Example case 1:** Let's look at what happens after an operation is removed.
- Removing operation $1$: The heights of cakes $4$ through $9$ increase by $1$. Then, the heights of cakes $1$ through $4$ increase by $1$. The resulting sequence of heights is $[1, 1, 1, 2, 1, 1, 1, 1, 1]$ (for cakes $1$ through $9$; the other cakes have heights $0$). The number of cakes with height $2$ is $1$.
- Removing operation $2$: The resulting sequence of heights of cakes $1$ through $9$ is $[1, 2, 2, 2, 1, 1, 0, 0, 0]$. The number of cakes with height $2$ is $3$.
- Removing operation $3$: The resulting sequence of heights of cakes $1$ through $9$ is $[0, 1, 1, 2, 2, 2, 1, 1, 1]$. The number of cakes with height $2$ is $3$.

The maximum number of cakes with height $2$ is $3$.

</details>

## Approach

First apply all $N$ operations with a difference array to get every cake's height, and count the cakes of height exactly $K$.

Removing one operation lowers the heights on its interval by 1 and changes nothing else. Inside the interval a cake of height $K + 1$ becomes a cake of height $K$ (gain 1) and a cake of height $K$ stops being one (loss 1). So give every cake the score $+1$ if its height is $K + 1$, $-1$ if it is $K$, and 0 otherwise; the net change for an operation is the sum of scores over $[L, R]$, an $O(1)$ prefix-sum query.

The answer is the base count plus the best net change over the $N$ operations.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        k = next(tokens)
        ranges = [(next(tokens), next(tokens)) for _ in range(n)]
        diff = [0] * 100002
        for l, r in ranges:
            diff[l] += 1
            diff[r + 1] -= 1
        height = base_count = 0
        score = [0] * 100001
        for i in range(1, 100001):
            height += diff[i]
            base_count += height == k
            score[i] = score[i - 1] + (height == k + 1) - (height == k)
        out.append(str(base_count + max((score[r] - score[l - 1] for l, r in ranges))))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- Exactly one operation must be removed, even if every removal makes things worse.
- Several identical intervals are all candidates but give the same result.
- The cake indices go up to 100000 regardless of $N$.
- The best net change can be negative.

## Dry run

`K = 2`, operations `[2,6] [4,9] [1,4]`.

Heights of cakes 1-9: `1 2 2 3 2 2 1 1 1`; four cakes have height 2. Scores: `0 -1 -1 +1 -1 -1 0 0 0`.

- remove `[2,6]`: $-1 - 1 + 1 - 1 - 1 = -3$, leaving 1
- remove `[4,9]`: $+1 - 1 - 1 = -1$, leaving 3
- remove `[1,4]`: $-1 - 1 + 1 = -1$, leaving 3

Answer 3.

---

Same problem grouped by topic: [../docs/prefix-sums/MAXREMOV.md](../docs/prefix-sums/MAXREMOV.md)
