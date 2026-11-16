[&larr; 538. India Fights Corona](CORONA.md) &middot; [Index](../../README.md) &middot; [541. FCAR &rarr;](INSQ15_F.md)

# 540. Per Capita Income

> CodeChef problem code [`PERCAPTA`](https://www.codechef.com/problems/PERCAPTA) &middot; difficulty **2132** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | Largest component among maximum-ratio provinces |
| **Time** | $O(N+M)$ per test case |
| **Space** | $O(N+M)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Chefland consists of $N$ provinces (numbered $1$ through $N$) connected by $M$ bidirectional roads (numbered $1$ through $M$). For each valid $i$, the $i$-th road connects provinces $U_i$ and $V_i$. It is possible to travel from each province to any other province using these roads.

For each valid $i$, the annual income of the $i$-th province is $A_i$ and its population is $B_i$. The per-capita income of some provinces is lower than that of some other provinces. For this reason, the king of Chefland wants to choose one or more provinces to keep in his kingdom and abandon the rest, in such a way that the per-capita income of the whole resulting kingdom, i.e. the sum of annual incomes of the chosen provinces divided by the sum of their populations, would be maximum possible. However, it should also be possible to travel from each of the chosen provinces to any other chosen province without visiting any of the abandoned provinces. Among all such ways to form the new kingdom, the king would prefer the number of chosen provinces to be as large as possible.

Can you help the king choose which provinces should form the new kingdom? If there are multiple solutions that maximise the per-capita income, you should choose one with the maximum number of chosen provinces. If there are still multiple solutions, you may choose any one.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $M$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- The third line contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$.
- $M$ lines follow. For each valid $i$, the $i$-th of these lines contains two space-separated integers $U_i$ and $V_i$.

**Output**
Print two lines.
- The first of these lines should contain a single integer $K$ denoting the number of provinces the king should choose.
- The second line should contain $K$ space-separated integers denoting these provinces.

**Constraints**
- $1 \le T \le 5$
- $1 \le N, M \le 2 \cdot 10^5$
- $1 \le U_i, V_i \le N$ for each valid $i$
- $U_i \neq V_i$ for each valid $i$
- there is at most one road between each pair of provinces
- $0 \le A_i \le 10^9$ for each valid $i$
- $1 \le B_i \le 10^9$ for each valid $i$

## Constraints

- $1 \le T \le 5$
- $1 \le N, M \le 2 \cdot 10^5$
- $1 \le U_i, V_i \le N$ for each valid $i$
- $U_i \neq V_i$ for each valid $i$
- there is at most one road between each pair of provinces
- $0 \le A_i \le 10^9$ for each valid $i$
- $1 \le B_i \le 10^9$ for each valid $i$

## Sample

**Sample input**

```
1
3 3
10 1 2
5 1 1 
1 2
2 3
1 3
```

**Sample output**

```
2
1 3
```

<details><summary>Explanation</summary>

If the king chooses provinces $1$ and $3$, then the per-capita income is $\frac{10 + 2}{5 + 1} = 2$. This is the only optimal solution.

</details>

## Approach

The kingdom's income per capita is a population-weighted average of provincial ratios. It cannot exceed the maximum individual ratio, and it equals that maximum exactly when every chosen province has that ratio.

Find the maximum using integer cross products, mark all provinces tying it, and traverse the graph induced by those provinces. The largest connected component maximises the number of retained provinces while preserving the optimal ratio.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m = int(next(tokens)),int(next(tokens))
        a = [int(next(tokens)) for _ in range(n)]
        b = [int(next(tokens)) for _ in range(n)]
        best = 0
        for i in range(1,n):
            if a[i]*b[best] > a[best]*b[i]:
                best = i
        eligible = [a[i]*b[best] == a[best]*b[i] for i in range(n)]
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u,v = int(next(tokens))-1,int(next(tokens))-1
            if eligible[u] and eligible[v]:
                graph[u].append(v)
                graph[v].append(u)
        seen = [False]*n
        answer = []
        for start in range(n):
            if not eligible[start] or seen[start]:
                continue
            component = [start]
            seen[start] = True
            for u in component:
                for v in graph[u]:
                    if not seen[v]:
                        seen[v] = True
                        component.append(v)
            if len(component) > len(answer):
                answer = component
        out.append(str(len(answer)))
        out.append(' '.join(str(i+1) for i in answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N+M)$ per test case
- **Space:** $O(N+M)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Compare ratios without floating-point division.
- Zero incomes are allowed.
- If several largest components tie, any one is valid.
- Abandoned provinces cannot be used as intermediate stops.

## Dry run

The sample ratios are `10/5=2`, `1/1=1`, and `2/1=2`. Provinces 1 and 3 are connected directly, so retain both.

---

Same problem in rating order (#614 of 735): [../../by-rating/614-PERCAPTA.md](../../by-rating/614-PERCAPTA.md)
