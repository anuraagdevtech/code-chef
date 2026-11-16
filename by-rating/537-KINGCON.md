[&larr; 536. Yet Another Cute Girl](536-PRETNUM.md) &middot; [Index](README.md) &middot; [538. Maze of Digits &rarr;](538-K3.md)

# 537. Kingdom Unity

> [`KINGCON`](https://www.codechef.com/problems/KINGCON) &middot; difficulty **1851** &middot; time limit **1 - 3s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | Iterative low-link articulation-point search |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N+M)$ per test case |
| **Space** | $O(N+M)$ |

## Question

The Kingdom of Bytelandia has **N** cities, numbered from **0** to **N**−**1**. There are **M** bidirectional roads, each of which connects two different cities. The road network in the kingdom is such that people of any city can reach any other city they desired through the road network. This is called having *unity* in the kingdom. Bytelandia is very famous for its unity. The people are united and familiar with each other. The king of Bytelandia is also very proud of this fact.

But, **some people just want to watch the world burn**. Dr. Bobo is one of such people. He is very wicked. He doesn't like *unity* of Bytelandia. He has a chemical missile to spread diseases. He plans to attack one of the cities of Bytelandia.

The king's secret intelligence service became aware of Dr. Bobo's wicked plan and informed the king about it. The king could not catch Dr. Bobo hence he is a genius. So the king planned the rescue mission with his own defense system. The scientists of Bytelandia have made one kind of shields which can protect an entire city from the attack of Dr. Bobo's missile. The shield will not affect the road network, in the sense that a citizen can still travel on the roads connected to a protected city. But the shields are very very expensive to build.

The king also has a team of brilliant doctors, who have already discovered the cure for the disease which the missile will spread. But they can only handle one city at a time. The king has planned his rescue mission as follows:

If a shielded city is attacked by the missile, then no one is harmed. If a city without a shield is attacked, all the roads connected to that city will be closed to prevent the disease from spreading to the other cities. Then, the doctors will begin to cure each citizen of that city and as a precautionary measure, none of those citizens are allowed to leave the city until each and every of them is cured. It will take a very long time to cure an entire city.

Taking a long time to cure an attacked city will affect the road network of the kingdom. The roads which are closed due to the attack can not be used until the affected city is entirely cured. This would have an adverse affect on the kingdom's *unity*, which the king would never want, especially at the time of crisis because in that case Dr. Bobo would have achieved his evil goal of dividing the people.

The king can make as many shields as he wants but as we know, they are very expensive. So, he would let a city be attacked and then be cured by his doctors rather than pay to plant a shield over a city, as long as it will not affect the unity of the remaining kingdom. That is, city **x** must be protected by the shield if there exists a pair of cities (except city **x**) such that people cannot come and go between these cities when the roads connected city **x** are closed. He doesn't want to make unnecessary shields. He wants you to find the minimum amount of money that is needed to make the shields to prevent Mr. Bobo from succeeding in his evil plan.

**Input**

First line of input contains an integer **T**, denoting the number of test cases. Then **T** test cases follow. First line of each test case contains **3** space-separated integers **N**, **M**, and **K**, denoting number of cities, the number of bidirectional roads, and the cost to make one shield, respectively. Then **M** lines follow each containing **2** space-separated integers **A** and **B**, denoting that there is a road between city **A** and city **B**.

**Output**

For each test case, output the minimum amount of money required to fulfill the king's requirements and protect *unity* of his kingdom.

**Constraints**

- **1** ≤ **T** ≤ **1500**

- **2** ≤ **N** ≤ **3000**

- **N**−**1** ≤ **M** ≤ **N***(**N**−**1**)/**2**)

- **0** ≤ **A**, **B** ≤ **N**−**1**, **A** ≠ **B**

- **1** ≤ **K** ≤ **1000**

- The road network has *unity*

- No two roads connect the same pair of cities

- The sum of **N** in one test file does not exceed **3000**

## Constraints

- 1 ≤ T ≤ 1500
- 2 ≤ N ≤ 3000
- N−1 ≤ M ≤ N*(N−1)/2)
- 0 ≤ A, B ≤ N−1, A ≠ B
- 1 ≤ K ≤ 1000
- The road network has unity
- No two roads connect the same pair of cities
- The sum of N in one test file does not exceed 3000

## Sample

**Sample input**

```
1
7 6 5
0 1
1 2
3 4
2 4
2 6
5 2
```

**Sample output**

```
15
```

<details><summary>Explanation</summary>

In the sample, the cities **1**, **2**, and **4** must be protected by the shields.

</details>

## Approach

A city needs a shield exactly when removing it disconnects the remaining graph: it is an articulation point. Use DFS discovery times and low-link values. A non-root vertex $u$ is an articulation point when some DFS child $v$ cannot reach a proper ancestor of $u$, meaning $low[v]\ge tin[u]$. A DFS root is an articulation point exactly when it has more than one DFS child.

Maintain the next adjacency position in each explicit DFS stack frame, propagating low-link values when frames finish. Count marked vertices and multiply by the shield price.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m,price = (int(next(tokens)) for _ in range(3))
        graph = [[] for _ in range(n)]
        for _ in range(m):
            u,v = int(next(tokens)),int(next(tokens))
            graph[u].append(v)
            graph[v].append(u)
        tin = [-1]*n
        low = [0]*n
        parent = [-1]*n
        children = [0]*n
        cut = [False]*n
        timer = 0
        for start in range(n):
            if tin[start] != -1:
                continue
            tin[start] = low[start] = timer
            timer += 1
            stack = [(start,0)]
            while stack:
                u,index = stack[-1]
                if index == len(graph[u]):
                    stack.pop()
                    p = parent[u]
                    if p == -1:
                        cut[u] = children[u] > 1
                    else:
                        low[p] = min(low[p],low[u])
                        if parent[p] != -1 and low[u] >= tin[p]:
                            cut[p] = True
                    continue
                v = graph[u][index]
                stack[-1] = (u,index+1)
                if v == parent[u]:
                    continue
                if tin[v] != -1:
                    low[u] = min(low[u],tin[v])
                else:
                    parent[v] = u
                    children[u] += 1
                    tin[v] = low[v] = timer
                    timer += 1
                    stack.append((v,0))
        out.append(str(sum(cut)*price))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- Vertices are zero-based.
- Treat DFS roots separately from other vertices.
- Mark a city once even if several child subtrees separate.
- A two-vertex graph has no articulation point.

## Dry run

The sample tree has internal vertices 1, 2, and 4 whose removal separates other cities. Three shields at cost five each give 15.

---

Same problem grouped by topic: [../docs/graphs/KINGCON.md](../docs/graphs/KINGCON.md)
