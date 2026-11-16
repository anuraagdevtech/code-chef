[&larr; 707. Ancient Berland Roads](ABROADS.md) &middot; [Index](../../README.md)

# 720. Connect All Cities

> CodeChef problem code [`CNCTCT`](https://www.codechef.com/problems/CNCTCT) &middot; difficulty **2417** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Disjoint Set Union |
| **Technique** | Kruskal over bits - each bit is a clique of equal-weight edges |
| **Time** | $O(30 \cdot N \cdot \alpha(N))$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

The country of Berland initially has $N$ isolated cities, the $i$-th city has a significance of $A_i$. The President of Berland wants to connect all the cities. He can construct a bidirectional road of length $L$ $(L > 0)$ from city $X$ to city $Y$ if $(A_X \& A_Y \& L) = L$, where $\&$ represents the [bitwise AND](https://en.wikipedia.org/wiki/Bitwise_operation#AND) operator.

What is the minimum total length of roads he has to construct, in order to connect all the cities in Berland? Print $-1$ if it is impossible.

Note: City $X$ and City $Y$ are said to be connected if there exists a sequence of cities $C_1, C_2, \ldots, C_K$ $(K \ge 1)$ such that $C_1 = X$, $C_K = Y$, and there exists a road from $C_i$ to $C_{i+1}$, $(1 \le i < K)$. All the cities in Berland are said to be connected when every pair of cities in Berland are connected.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains $N$ — the number of cities.
    - The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$ — the significance of each of the $N$ cities.

**Output**

For each test case, output on a new line the minimum total length of roads to connect all the cities in Berland, or $-1$ if it is impossible.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $0 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $3 \cdot 10^5$.

## Sample

**Sample input**

```
2
4
4 4 4 4
3
2 4 6
```

**Sample output**

```
12
6
```

<details><summary>Explanation</summary>

**Test case 1:** The following roads with minimum total length can be constructed to connect Berland:
- A road with $L=4$ between city $1$ and city $2$, since ($A_1 \& A_2 \& 4) = 4$.
- A road with $L=4$ between city $2$ and city $3$, since ($A_2 \& A_3 \& 4) = 4$.
- A road with $L=4$ between city $3$ and city $4$, since ($A_3 \& A_4 \& 4) = 4$.

**Test case 2:** The following roads with minimum total length can be constructed to connect Berland:
- A road with $L=2$ between city $1$ and city $3$, since ($A_1 \& A_3 \& 2) = 2$.
- A road with $L=4$ between city $2$ and city $3$, since ($A_2 \& A_3 \& 4) = 4$.

</details>

## Approach

A road of length $L$ between $X$ and $Y$ needs $L$ to be a non-empty submask of $A_X \mathbin{\&} A_Y$. The cheapest such road is a single bit, the lowest common set bit, and any other allowed length is at least as large; so only single-bit roads are useful, and a road of length $2^b$ exists between any two cities that both have bit $b$.

For each bit $b$ the cities having it therefore form a clique of edges of weight $2^b$. Run Kruskal's algorithm in increasing order of weight, i.e. bit by bit from the lowest. Within a clique all edges have the same weight, and joining every city of the clique to one representative produces the same components as processing all of its edges, so each bit needs only a linear scan with a disjoint-set union. Every successful union adds $2^b$.

If more than one component remains at the end, the cities cannot be connected.

## Solution (Python)

```python
import sys


def solve(tokens):
    n = next(tokens)
    values = [next(tokens) for _ in range(n)]
    parent = list(range(n))
    size = [1] * n
    components = n
    total = 0

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for bit in range(30):
        first = -1
        for i, x in enumerate(values):
            if x >> bit & 1:
                if first < 0:
                    first = i
                    continue
                u, v = (root(first), root(i))
                if u != v:
                    if size[u] < size[v]:
                        u, v = (v, u)
                    parent[v] = u
                    size[u] += size[v]
                    components -= 1
                    total += 1 << bit
    return str(total if components == 1 else -1)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(30 \cdot N \cdot \alpha(N))$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- A city with significance 0 can never be connected; with $N > 1$ the answer is $-1$.
- $N = 1$ needs no road: answer 0.
- Processing the bits from low to high is exactly the sorted edge order Kruskal requires.
- The total can exceed 32 bits.

## Dry run

`A = [2, 4, 6]`.

- bit 1 (weight 2): cities 1 and 3 have it - union, cost 2.
- bit 2 (weight 4): cities 2 and 3 have it - union, cost 4.

One component remains. Answer 6.

> CodeChef tags: `Data Structures`, `Algorithms`, `Graph Algos`, `Tree Algos`

---

Same problem in rating order (#684 of 735): [../../by-rating/684-CNCTCT.md](../../by-rating/684-CNCTCT.md)
