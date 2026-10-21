# 1668 &middot; Chef and Frogs

> CodeChef problem code [`FROGV`](https://www.codechef.com/problems/FROGV) &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Connected components from gaps in sorted order |
| **CodeChef category** | main |
| **Time** | $O(N \log N + P)$ |
| **Space** | $O(N)$ |

Same write-up grouped by topic: [../docs/sorting/FROGV.md](../docs/sorting/FROGV.md)

## Question

Nobody knows, but $N$ frogs live in Chef's garden.

Now they are sitting on the X-axis and want to speak to each other. One frog can send a message to another one if the distance between them is less or equal to $K$.

Chef knows all $P$ pairs of frogs, which want to send messages. Help him to define can they or not!

**Note** : More than $1$ frog can be on the same point on the X-axis.

### Input

-   The first line contains three integers $N$, $K$ and $P$.
-   The second line contains $N$ space-separated integers $A_1$, $A_2$, ..., $A_N$ denoting the x-coordinates of frogs".
-   Each of the next $P$ lines contains two integers $A$ and $B$ denoting the numbers of frogs according to the input.

### Output

For each pair print "Yes" without a brackets if frogs can speak and "No" if they cannot.

### Constraints

-   $1 \le N, P \le 10^5$
-   $0 \le A_i, K \le 10^9$
-   $1 \le A, B \le N$

## Constraints

-   $1 \le N, P \le 10^5$
-   $0 \le A_i, K \le 10^9$
-   $1 \le A, B \le N$

## Sample

**Sample input**

```
5 3 3
0 3 8 5 12
1 2
1 3
2 5
```

**Sample output**

```
Yes
Yes
No
```

<details><summary>Explanation</summary>

- For pair $(1, 2)$ frog $1$ can directly speak to the frog $2$ as the distance between them is $3 - 0 = 3 \le K$ .

- For pair $(1, 3)$ frog $1$ can send a message to frog $2$, frog $2$ can send it to frog $4$ and it can send it to frog $3$.

- For pair $(2, 5)$ frogs can't send a message under current constraints.

</details>

## Approach

The trap is reading "distance $\leq K$" as the whole condition. Messages **relay**: the sample answers `Yes` for frogs at $0$ and $8$ with $K = 3$, which is only possible by hopping $0 \to 3 \to 5 \to 8$. So the question is connectivity in the graph joining every pair within $K$, not a single distance test.

That graph has up to $\binom{N}{2}$ edges, but on a line its components have a simple shape. Sort the positions; two frogs are connected iff **every consecutive gap between them in sorted order is at most $K$**. If some gap exceeds $K$, no edge crosses it at all — any edge spanning it would itself be longer than $K$ — so it is a genuine cut. If all gaps are within $K$, the sorted chain itself is a path connecting them.

So one sweep suffices: sort, then assign component ids, starting a new id whenever the gap to the previous frog exceeds $K$. No DSU or BFS is needed — the components are contiguous blocks of the sorted order.

$$\text{answer} = \text{Yes} \iff \mathrm{comp}[a] = \mathrm{comp}[b]$$

Ties matter: frogs may share a position, giving a gap of $0$, which is always within $K$ — and $K = 0$ is allowed, in which case only co-located frogs can talk.

The sample sorts to $0, 3, 5, 8, 12$ with gaps $3, 2, 3, 4$. The last gap exceeds $K = 3$, so the components are $\{0,3,5,8\}$ and $\{12\}$. Hence frogs 1 and 2 (`Yes`), 1 and 3 (`Yes`, via the relay), and 2 and 5 (`No`, across the cut).

Note a query may name the same frog twice, which is trivially `Yes` — the component test handles it without a special case.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n, k, p = int(data[0]), int(data[1]), int(data[2])
    pos_of = [int(x) for x in data[3:3 + n]]
    order = sorted(range(n), key=pos_of.__getitem__)
    comp = [0] * n
    group = 0
    for rank, idx in enumerate(order):
        # A gap above K cannot be bridged by any edge, so it cuts the line.
        if rank and pos_of[idx] - pos_of[order[rank - 1]] > k:
            group += 1
        comp[idx] = group
    base = 3 + n
    out = []
    for i in range(p):
        a, b = int(data[base + 2 * i]), int(data[base + 2 * i + 1])
        out.append("Yes" if comp[a - 1] == comp[b - 1] else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N + P)$
- **Space:** $O(N)$
