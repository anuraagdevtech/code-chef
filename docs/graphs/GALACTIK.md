[&larr; 536. Chef and Digit Jumps](DIGJUMP.md) &middot; [Index](../../README.md) &middot; [538. India Fights Corona &rarr;](CORONA.md)

# 537. Galactik Football

> CodeChef problem code [`GALACTIK`](https://www.codechef.com/problems/GALACTIK) &middot; difficulty **1860** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | Connect component minima in a star |
| **Time** | $O(N+M)$ overall |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

It's Galactik Football time! The Galactik Football Assosiation (GFA) has announced a football tournament between all the teams of all the planets in the galaxy.

Each planet of the galaxy has a government. Some governments have a mutual agreement between them. If planet $A$ has mutual agreement with planet $B$, then there is a bidirectional spaceway between $A$ and $B$, using which anybody can go from $A$ to $B$ and vice-versa. People can use these spaceways to travel from one planet to another, if there exists a path between them using some of the spaceways.

Each planet has its own football ground. The GFA has planned the matches in such a way that a team can have a match at any of these grounds. The GFA has come across some problems in the execution of their plan. They have found out that there are many pairs of planets between which there does not exist any path, so the football team of one of those planets can't reach the other planet. They requested the corresponding governments to make a spaceway between them, but they can’t because of the absence of a mutual agreement. So the GFA suggested that they will make teleportation devices between some pairs of planets which will be used only by the football teams to travel.

But there are two types of governments in the galaxy
1. Some of the governments are greedy and they want to make money through the GFA. Each of these government has asked the GFA for a tax value which it has to pay if it wants to make a teleport ending at their planet.
2. Others want to sponsor the event, so they will give money to the GFA if they make a teleport ending at their planet. The GFA would always avoid such governments no matter what the consequences are, because these kind of governments always have some dirty plans up their sleeves.

Now, the GFA wants to make bi-directional teleports between planets such that the football teams of any planet can reach any other planet to play a football match, using spaceways between the planets and/or teleports made by the GFA.

The GFA also has financial problems and want to spend as little money as possible. They have come to you so that you can help them calculate the minimum amount of money needed to fulfil their plan.

**Input**
- The first line of the input consists of two space separated integers - $N$ and $M$. $N$ is the number of planets and $M$ is the number of spaceways. The description of the spaceways follows.
- The next $M$ lines, each contain two space separated integers $A$ and $B$, denoting a mutual agreement and hence a spaceway to travel, between planet $A$ and planet $B$.
- The next $N$ lines each contain a single integer, the integer on the $i^{th}$ line representing $C_i$. If $C_i \geq 0$, then it represents the tax value which the GFA has to pay to the government of planet $i$ (it's a type $1$ government). If $C_i < 0$, then it represents the money that the $i^{th}$ government will pay to the GFA (it's a type $2$ government).

**Output**
Print the minimum amount needed for the GFA to fulfil their plan. If there is no way to do so, print "-1" (without quotes).

**Constraints**
- $1 \leq N \leq 10^5$
- $0 \leq M \leq 10^6$
- $0 \leq |C| \leq 10^4$
- $1 \leq A,B \leq N$
- $A \neq B$

## Constraints

- $1 \leq N \leq 10^5$
- $0 \leq M \leq 10^6$
- $0 \leq |C| \leq 10^4$
- $1 \leq A,B \leq N$
- $A \neq B$

## Sample

**Sample 1 input**

```
6 6
1 2
2 3
1 3
4 5
5 6
4 6
1
3
5
2
4
6
```

**Sample 1 output**

```
3
```

**Sample 2 input**

```
3 1
2 3
1
-1
-1
```

**Sample 2 output**

```
-1
```

## Approach

Existing spaceways form connected components. Within each component, choose its cheapest nonnegative endpoint tax; negative-tax governments are forbidden. If a component has no allowed endpoint and there is more than one component, connecting the galaxy is impossible.

For component minima $c_1,\ldots,c_k$, an added edge costs the sum of its endpoint minima. Every component needs degree at least one in the connecting tree. Giving the remaining $k-2$ degrees to the globally cheapest component minimises the sum. A star attains total $\sum c_i+(k-2)\min c_i$.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int,sys.stdin.buffer.read().split()))
    n,m = next(tokens),next(tokens)
    parent = list(range(n))
    size = [1]*n
    def find(u):
        while parent[u] != u:
            parent[u] = parent[parent[u]]
            u = parent[u]
        return u
    for _ in range(m):
        u,v = find(next(tokens)-1),find(next(tokens)-1)
        if u != v:
            if size[u] < size[v]:
                u,v = v,u
            parent[v] = u
            size[u] += size[v]
    costs = {}
    for i in range(n):
        cost = next(tokens)
        root = find(i)
        costs.setdefault(root,None)
        if cost >= 0 and (costs[root] is None or cost < costs[root]):
            costs[root] = cost
    if len(costs) == 1:
        print(0)
    elif any(v is None for v in costs.values()):
        print(-1)
    else:
        print(sum(costs.values())+(len(costs)-2)*min(costs.values()))

if __name__ == '__main__':
    main()
```

## Complexity

- **Time:** $O(N+M)$ overall
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- An already-connected galaxy costs zero even if every tax is negative.
- A zero tax is an allowed endpoint.
- Reject an unusable component only when a connection is actually required.

## Dry run

The first sample has component minima one and two. One teleport costs `1+2=3`. In the second sample, one disconnected component has only negative taxes, so the result is `-1`.

---

Same problem in rating order (#539 of 735): [../../by-rating/539-GALACTIK.md](../../by-rating/539-GALACTIK.md)
