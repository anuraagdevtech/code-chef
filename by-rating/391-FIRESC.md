# 391. Fire Escape Routes

> [`FIRESC`](https://www.codechef.com/problems/FIRESC) &middot; difficulty **1671** &middot; time limit **3s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | Connected components by DSU, then a product of sizes |
| **CodeChef tags** | `Advanced Data Structures`, `Mathematics`, `Disjoint Set Union`, `Combinatorics` |
| **Complexity class** | Near-linear $O(n \log \log n)$ |
| **Time** | $O((N + M)\,\alpha(N))$ per test case |
| **Space** | $O(N)$ |

## Question

There are $N$ people working in a building, and each one works in a separate cabin. Chef’s employees are numbered by integers from $1$ to $N$, inclusive. Chef wants to ensure the safety of his employees. He wants to have fire escapes in the building and wants to train the employees to use these by conducting mock drills.

Chef knows that the number of people working in his office can be very large. In order to avoid crowding of a common fire escape route during emergency, Chef has decided to build multiple fire escapes. For the safety of every employee, each cabin has a fire exit which is connected to one of the fire escape routes.

A lot of employees are friends with each other. The friendship is mutual. This means that if employee $i$ is a friend of employee $j$ then employee $j$ is a friend of employee $i$ as well. But friendship is NOT necessarily transitive. This means that if employee $i$ is a friend of employee $j$ AND employee $j$ is a friend of employee $k$, then employee $i$ and employee $k$ need not necessarily be friends.

If two employees are friends, they do not want to escape through different routes.
This complicates the task for the Chef. As already mentioned, he wants to have the maximum number of fire escape routes to ensure maximum safety. Also, for every escape route, one of the employees using that route needs to be appointed as the fire drill captain. The captain will be responsible for conducting the mock drills and train all the employees using that route. Your task is simple. Given the number of employees and the friendship list, you need to tell the Chef the maximum number of fire escape routes that he can have in the building and the number of ways of selecting the captains for every route. Since the number of ways can be really large, output this value modulo $10^{9} + 7$.

**Input**
- The first line of the input contains a single integer $T$, denoting the number of test cases. The description of T test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $M$, denoting the number of employees and the number of friendship relations, respectively.
- Each of the following $M$ lines contains two space-separated integers $i$ and $j$, denoting that employee $i$ and employee $j$ are friends.

**Output**
For each test case, output a single line containing two space separated integers, denoting the maximum number of distinct fire escape routes that can be constructed and the number of ways of selecting the captains modulo $10^{9} + 7$.

**Constraints**
- $1 \leq T \leq 5$
- $1 \leq N \leq 10^{5}$
- $0 \leq M \leq 10^{5}$
- $1 \leq i, j \leq N$
- $ i \neq j$
- For any pair of employees $i$ and $j$ such that $1 \leq i, j \leq N$, at most one pair among $(i, j)$ and $(j, i)$ will appear in the input

## Constraints

- $1 \leq T \leq 5$
- $1 \leq N \leq 10^{5}$
- $0 \leq M \leq 10^{5}$
- $1 \leq i, j \leq N$
- $ i \neq j$
- For any pair of employees $i$ and $j$ such that $1 \leq i, j \leq N$, at most one pair among $(i, j)$ and $(j, i)$ will appear in the input

## Sample

**Sample input**

```
3
4 2
1 2
2 3
5 3
1 2
2 3
1 3
6 3
1 2
3 4
5 6
```

**Sample output**

```
2 3
3 3
3 8
```

<details><summary>Explanation</summary>

**Example case 1:** Here employees $1$ and $2$ are friends and should share the same fire escape. Also employees $2$ and $3$ share the same fire escape. This means employees $1$, $2$, and $3$ will have a common route. But to maximize number of routes Chef could assign another route to employee $4$ since it is not a friend of other employee. So we have two escape routes with the following distribution of employees by routes: $\{1, 2, 3\}$, $\{4\}$. Therefore, there are $3$ ways to chose drill captains: $(1, 4)$, $(2, 4)$, $(3, 4)$, where first element in the pair denotes the captain for the first route and second element denotes the captain for the second route.

**Example case 2:** Here the optimal distribution of employees by routes is $\{1, 2, 3\}$, $\{4\}$, $\{5\}$. Therefore, there are $3$ ways to chose drill captains: $(1, 4, 5)$, $(2, 4, 5)$, $(3, 4, 5)$.

**Example case 3:** Here the optimal distribution of employees by routes is $\{1, 2\}$, $\{3, 4\}$, $\{5, 6\}$. Therefore, there are 8 ways to chose drill captains: $(1, 3, 5)$, $(1, 3, 6)$, $(1, 4, 5)$, $(1, 4, 6)$, $(2, 3, 5)$, $(2, 3, 6)$, $(2, 4, 5)$, $(2, 4, 6)$.

</details>

## Approach

Friends must share a route, and friendship is *not* transitive — but "must share" is, so the constraint propagates along chains. Two employees therefore end up on the same route exactly when they are in the same **connected component** of the friendship graph. Maximising routes means giving each component its own:

$$\text{routes} = \#\text{components}$$

That is the most possible, since merging two components would only reduce the count, and it is legal, since no constraint spans components.

Each route then needs one captain chosen from its own members, and the choices are independent, so

$$\text{ways} = \prod_{\text{components } c} |c| \pmod{10^9 + 7}$$

The product can be astronomically large — $2^{50000}$ for a graph of $10^5$ people paired off — which is why the modulus is there. Note the count of *routes* is not reduced modulo anything; only the second number is.

A disjoint-set-union structure with union by size and path compression computes both numbers in one pass, and the component sizes come for free from the DSU's own size array. A BFS or DFS over adjacency lists would also work; DSU avoids building the lists.

Isolated employees are components of size $1$ and contribute a factor of $1$ — they add a route without adding choices. The samples show that directly: $4$ people with the chain $1$–$2$–$3$ give $2$ routes and $3 \cdot 1 = 3$ ways, while the triangle on $\{1,2,3\}$ plus two isolated people gives $3$ routes and again $3$ ways. The third sample's three disjoint pairs give $3$ routes and $2^3 = 8$ ways.

## Solution

```python
import sys

MOD = 1_000_000_007


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        pos += 2
        parent = list(range(n + 1))
        size = [1] * (n + 1)

        def find(x):
            while parent[x] != x:
                parent[x] = parent[parent[x]]
                x = parent[x]
            return x

        for _ in range(m):
            a, b = find(int(data[pos])), find(int(data[pos + 1]))
            pos += 2
            if a != b:
                if size[a] < size[b]:
                    a, b = b, a
                parent[b] = a
                size[a] += size[b]
        routes = 0
        ways = 1
        for v in range(1, n + 1):
            if find(v) == v:
                routes += 1
                # One captain per route, chosen independently.
                ways = ways * size[v] % MOD
        out.append(f"{routes} {ways}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Friends must share a route, so each connected component becomes one route** — and maximising the route count means using exactly one per component, since merging two would waste a route.
- **Friendship is not transitive but connectivity is**, which is the whole point: the components, not the individual friendships, decide the grouping.
- **An isolated employee is their own route** (the first sample's employee $4$), so singletons count.
- **$M$ may be $0$**, leaving $N$ routes and exactly one captain choice per route, for $1$ way in total.
- **The captain count is a product over components**, since each route picks its own captain independently — $3 \cdot 1 = 3$ in the first sample, $2^3 = 8$ in the third.
- **Extra edges inside a component change nothing** (the second sample's triangle has three edges and still forms one component of size $3$).
- **The product needs the modulus**: $5 \times 10^4$ components of size $2$ give $2^{50000}$, far past any fixed integer width.
- **Union by size with path halving** keeps the DSU near-linear at $N, M \leq 10^5$.

## Dry run

Third sample: $N = 6$ with edges $(1,2)$, $(3,4)$, $(5,6)$.

| component | members | size |
|---:|---|---:|
| 1 | $\{1, 2\}$ | 2 |
| 2 | $\{3, 4\}$ | 2 |
| 3 | $\{5, 6\}$ | 2 |

Three routes, and $2 \times 2 \times 2 = 8$ ways to pick the captains. Output `3 8`.

---

Same problem grouped by topic: [../docs/graphs/FIRESC.md](../docs/graphs/FIRESC.md)
