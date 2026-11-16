[&larr; 702. Chef and Pepperoni Pizza Again](702-PEPPERA.md) &middot; [Index](README.md) &middot; [704. Hussain Set &rarr;](704-COOK82C.md)

# 703. India Fights Corona

> [`CORONA`](https://www.codechef.com/problems/CORONA) &middot; difficulty **2560** &middot; time limit **1.5s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | Multi-source Dijkstra seeded with hospital prices |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O((N+M)\log N)$ per test case |
| **Space** | $O(N+M)$ |

## Question

There are $N$ cities (numbered from $1$ to $N$) and $M$ bidirectional roads. The $i^{th}$ of these roads connects the cities $A_i$ and $B_i$ and has a length of $D_i$ Km.

There are only $K$ cities that have a hospital for corona testing. The cost of corona testing may be different in different cities. For each city, we want to know the minimum cost that needs to be spent to test a corona sample. If city you are in contains a hospital and you choose to test in that hospital itself, then the cost incurred is the cost of corona test in that hospital. Otherwise, if you choose to test in a hospital in another city, then an additional transportation cost is also incurred (Assuming Rs.1 per Km).

So from a city $i$, if you choose to send a sample to city $j$, then the total cost incurred will be $C_j + D(i,j)$. Here $C_j$ denotes the cost of corona testing in a hospital situated in city $j$ and $D(i,j)$ denotes the minimum distance between city $i$ and $j$ via some road network.

Output the *minimum* money that should be spent by a person in each of the $N$ cities for testing a corona sample.

It is guaranteed that there is a path from every city to every other city. Also, there is at most one road between any pair of cities (i.e. no multiple edges). There are no roads from one city to itself (i.e. no self-loops).

**Note:** Since the inputs and outputs are large, prefer using fast input-output methods.

**Input**

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- Each testcase contains $K + M + 1$ lines of input.
- The first line of each test case contains three space-separated integers $N, M, K$.
- $K$  lines follow. For each valid $i$, the $i^{th}$ of these lines contains two space-separated integers $x_i, C_i$ which denotes that there is a hospital in the $x_i^{th}$ city and the cost of corona testing in that hospital is $C_i$. There is at most one hospital in a city i.e. all $x_i$-s are distinct.
- Next $M$ lines follow. For each valid $i$, the $i^{th}$ of these lines contains three space-separated integers $A_i, B_i, D_i$, which denotes that there is a bidirectional road between City $A_i$ and City $B_i$ of length $D_i$ Km.

**Output**

For each test case, print a single line containing $N$ space-separated integers, where the $i^{th}$ integer denotes the minimum cost of corona testing if you are in the $i^{th}$ city.

## Constraints

- $1 \leq T \leq 4000$
- $2 \leq N \leq 2 \cdot 10^5$
- $1 \leq M \leq 4 \cdot 10^5$
- $1 \leq K \leq N$
- $1 \leq x_i, A_i, B_i \leq N$ for each valid $i$
- $1 \leq C_i \leq 10^9$ for each valid $i$
- $1 \leq D_i \leq 10^9$ for each valid $i$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$
- Sum of $M$ over all test cases does not exceed $4 \cdot 10^5$
- All $x_i$-s in a testcase are distinct.
- It is guaranteed that there is a path from every city to every other city.
- It is guaranteed that there are no self loops and multiple edges.

## Sample

**Sample input**

```
2
3 2 2
1 5
2 10
1 2 6
2 3 9
3 2 2
1 5
2 10
1 2 1
2 3 9
```

**Sample output**

```
5 10 19 
5 6 15
```

<details><summary>Explanation</summary>

**Test case $1$:** The hospitals are situated at cities $1$ and $2$ with their costs being $5$ and 10 respectively. For city $1$ it is optimal to test the sample in its own hospital bearing a total cost of $5$. For city $2$ it is again optimal to test the sample in its own hospital bearing a total cost of $10$. For city $3$ it is optimal to test the sample in the hospital at city $2$ which incurs the traveling cost of $9$ and hospital cost of $10$, so the total cost is $10+9=19$.

**Test case $2$:** For city $2$, it is optimal to test the sample in hospital at city $1$ which incurs a traveling cost of $1$ and hospital cost of $5$, so the total cost is $1+5=6$.

</details>

## Approach

Imagine a new source connected to each hospital by an edge equal to that hospital's test price. A shortest route from this source to any city pays exactly one hospital price plus the road distance from it.

There is no need to materialise the new vertex: initialise every hospital's distance to its price and put all hospitals in the heap. Run Dijkstra on the bidirectional roads. Hospital cities can improve through a cheaper hospital elsewhere.

## Solution

```python
import sys
from heapq import heappush,heappop


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m,k = (int(next(tokens)) for _ in range(3))
        distance = [10**30]*n
        heap = []
        for _ in range(k):
            city,price = int(next(tokens))-1,int(next(tokens))
            distance[city] = price
            heappush(heap,(price,city))
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u,v,w = int(next(tokens))-1,int(next(tokens))-1,int(next(tokens))
            graph[u].append((v,w))
            graph[v].append((u,w))
        while heap:
            d,u = heappop(heap)
            if d != distance[u]:
                continue
            for v,w in graph[u]:
                candidate = d+w
                if candidate < distance[v]:
                    distance[v] = candidate
                    heappush(heap,(candidate,v))
        out.append(' '.join(map(str,distance)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- A hospital city need not use its own hospital.
- Prices and road distances can produce totals beyond 32 bits.
- Discard stale heap entries after shorter routes are found.

## Dry run

In sample two, city 2 can use city 1 at cost `5+1=6`, improving on its own price 10. City 3 then uses the same hospital for `6+9=15`.

---

Same problem grouped by topic: [../docs/graphs/CORONA.md](../docs/graphs/CORONA.md)
