[&larr; 637. K Increment Palindrome](KPAL.md) &middot; [Index](../../README.md) &middot; [640. No Palindrome &rarr;](NOPALINDROME.md)

# 639. Mountain

> CodeChef problem code [`MOUNTAIN`](https://www.codechef.com/problems/MOUNTAIN) &middot; difficulty **2047** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Shortest block of top rows, then greedy top-up from the heaviest row |
| **Time** | $O(N)$ per query |
| **Space** | $O(N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

You're given an $N\times M$ matrix $A$, where $A_{(i,j)}=i$.

A **mountain** in the matrix is defined as a set of cells and is expressed using $K+2$ integers: $P, K, L_1, L_2, \ldots, L_K$.
This translates to: from the $(P+i-1)^{th}$ row, select the first $L_i$ cells $(1 \leq i \leq K)$ in the row. Refer samples for more clarity.

Your task is to answer $Q$ queries. For the $i^{th}$ query:
- You are given an integer $S_i$ and you need to find a **mountain** with sum $S_i$.

**Input**

- The first line contains three space-separated integers $N$, $M$, and $Q$, the dimensions of the matrix and the number of queries.
- The second line contains $Q$ space-separated integers $S_1,S_2,\ldots,S_Q$, denoting each query.

**Output**

- For each query, if no possible mountain with given sum exists, output $-1$.
- Otherwise, output two lines:
   -  The first line contains two space-separated integers $P$,$K$ $(1 \leq P \leq N,P+K-1 \leq N)$;
   -  The second line contains $K$ space-separated integers $L_1,L_2,\ldots,L_K(1 \leq L_i \leq M)$.

If multiple mountains satisfy the condition, you may print any.

## Constraints

- $2 \leq N,M \leq 3\cdot 10^4$
- $1 \leq Q \leq 10$
- $1 \leq S_i \leq M\cdot N\cdot \frac{(N+1)}{2}$

## Sample

**Sample input**

```
5 4 4
20 36 1 60
```

**Sample output**

```
2 3
2 4 1
1 5
3 1 4 1 3
1 1
1
1 5
4 4 4 4 4
```

<details><summary>Explanation</summary>

**Query $1$:** A possible mountain that satisfies the condition is highlighted below:

<img src="https://s3.amazonaws.com/codechef_shared/download/Images/START79/5atpZQnwFL3BmhW.png" width=200>

Here, $P = 2$ and $K = 3$ and we are selecting $2, 4,$ and $1$ cells from the second, third, and fourth row respectively. The sum of the highlighted cells is $20$.

**Query $2$:** A possible mountain that satisfies the condition is highlighted below:

<img src="https://s3.amazonaws.com/codechef_shared/download/Images/START79/VOiv8mtob2kyraN.png" width=200>

Here, $P = 1$ and $K = 5$ and we are selecting $3, 1, 4, 1,$ and $3$ cells from the first, second, third, fourth and fifth rows respectively. The sum of the highlighted cells is $36$.

</details>

## Approach

A cell in row $i$ is worth $i$, so a mountain on rows $P \dots P+K-1$ with lengths $L_i$ has sum $\sum (P + i - 1) L_i$. Always start at $P = 1$: then row $i$ is worth $i$ per cell and the unit-valued first row makes every remainder payable.

Take the smallest $K$ whose full capacity $M \cdot K(K+1)/2$ reaches $S$; the constraint on $S$ guarantees $K \le N$. Give every row one cell, costing $K(K+1)/2$, which is at most $S$ because $K - 1$ full rows were not enough. The remaining amount has to be paid with "coins" of value $1, 2, \dots, K$, each available $M - 1$ times. Go from the largest row down and take as many extra cells as fit. The greedy never gets stuck: the smaller rows together can cover any remainder up to their full capacity, and by the choice of $K$ the remainder never exceeds it.

So a mountain always exists and $-1$ is never printed.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    n = next(tokens)
    m = next(tokens)
    q = next(tokens)
    for _ in range(q):
        target = next(tokens)
        rows = 1
        while m * rows * (rows + 1) // 2 < target:
            rows += 1
        extra = target - rows * (rows + 1) // 2
        lengths = [1] * rows
        for i in range(rows, 0, -1):
            more = min(m - 1, extra // i)
            lengths[i - 1] += more
            extra -= i * more
        out.append(f'1 {rows}')
        out.append(' '.join(map(str, lengths)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per query
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Each selected row needs at least one cell, which is why the base cost is taken first.
- $S = 1$: a single cell in row 1.
- $S$ equal to the full matrix sum uses all rows completely.
- Several mountains can have the same sum, so the output is validated by a checker.

## Dry run

`N = 5, M = 4, S = 20`.

Capacities: one row 4, two rows 12, three rows 24, so $K = 3$. Base cost $1 + 2 + 3 = 6$, leaving 14.

- row 3: $\min(3, \lfloor 14 / 3 \rfloor) = 3$ extra cells, leaving 5
- row 2: $\min(3, \lfloor 5 / 2 \rfloor) = 2$, leaving 1
- row 1: 1, leaving 0

Lengths `2 3 4`: $1 \cdot 2 + 2 \cdot 3 + 3 \cdot 4 = 20$. Output `1 3` and `2 3 4`.

> CodeChef tags: `Algorithms`

---

Same problem in rating order (#589 of 735): [../../by-rating/589-MOUNTAIN.md](../../by-rating/589-MOUNTAIN.md)
