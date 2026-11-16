[&larr; 655. Travelling in the Graph](TRAVELLING.md) &middot; [Index](../../README.md)

# 717. Minimal Travel Time

> CodeChef problem code [`CLASSES`](https://www.codechef.com/problems/CLASSES) &middot; difficulty **2379** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | BFS distances from the hostel, then the K nearest subjects |
| **Time** | $O(N + M + S \log S)$ per test case |
| **Space** | $O(N + M + S)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

Chef's college is starting next week. There are $S$ subjects in total, and he needs to choose $K$ of them to attend each day, to fulfill the required number of credits to pass the semester. There are $N + 1$ buildings. His hostel is in building number $0$. Subject $i$ is taught in building $A_i$. After each subject, there is a break, during which he goes back to his hostel. There are $M$ bidirectional paths of length $1$ which connects building $u$ to building $v$. Find the minimum possible total distance Chef needs to travel each day if he chooses his subjects wisely.

**Input:**
- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contain $M + 2$ lines of input.
- First line will contain $4$ space separated integers $N$, $M$, $S$, $K$, number of buildings other than hostel building, number of edges, total number of subjects taught, number of subjects required to pass the semester.
- Next $M$ lines have $2$ space separated integers $u$, $v$ representing the path connecting buildings $u$ and $v$.
- Next line has $S$ space separated integers $A_1, A_2, \ldots A_S$ representing the building in which $i^{th}$ subject is taught.

**Output:**
For each testcase, output in a single line answer to the problem.

**Constraints**
- $1 \leq T \leq 3$
- $1 \leq N, S \leq 10^5$
- $1 \leq M \leq 2*10^5$
- $1 \leq K \leq S$
- $1 \leq A_i \leq N$
- $0 \leq u, v \leq N$

Its guaranteed that the graph is connected and has no self loops.

## Constraints

- $1 \leq T \leq 3$
- $1 \leq N, S \leq 10^5$
- $1 \leq M \leq 2*10^5$
- $1 \leq K \leq S$
- $1 \leq A_i \leq N$
- $0 \leq u, v \leq N$
Its guaranteed that the graph is connected and has no self loops.

## Sample

**Sample input**

```
3
2 3 2 2
0 1
1 2
2 0
1 2
2 2 2 2
0 1
1 2
1 2
6 7 5 3
0 1
0 2
0 4
1 3
1 4
2 5
2 6
1 2 3 5 6
```

**Sample output**

```
4
6
8
```

<details><summary>Explanation</summary>

**TestCase 1:** First Chef attends the subject in the building $2$ and he travels $1$ units to go there and $1$ units to come back during the break to the hostel.

Second subject he attends in the building $1$ and he travels $1$ unit to go there and $1$ unit to come back during the break to the hostel.

In total the total minimum distance to be travelled is $2 + 2  = 4$ units.

**TestCase 2:** First Chef attends the subject in the building $2$ and he travels $2$ units to go there and $2$ units to come back during the break to the hostel.

Second subject he attends in the building $1$ and he travels $1$ unit to go there and $1$ unit to come back during the break to the hostel.

In total the total minimum distance to be travelled is $4 + 2  = 6$ units.

**TestCase 3:** First Chef attends the subject in the building $3$ and he travels $2$ units to go there and $2$ units to come back during the break to the hostel.

Second subject he attends in the building $1$ and he travels $1$ unit to go there and $1$ unit to come back during the break to the hostel.

Final subject he attends in the building $2$ and he travels $1$ unit to go there and $1$ unit to come back during the break to the hostel.

In total the total minimum distance to be travelled is $4 + 2 + 2  = 8$ units.

</details>

## Approach

Chef returns to the hostel after every subject, so attending a subject taught in building $b$ costs exactly $2 \cdot \text{dist}(0, b)$, independently of the other subjects he attends and of their order.

All paths have length 1, so one breadth-first search from building 0 gives every distance. Map each subject to the distance of its building, sort, and take the $K$ smallest; the answer is twice their sum.

## Solution (Python)

```python
import sys
from collections import deque


def solve(tokens):
    n, m, subjects, needed = (next(tokens), next(tokens), next(tokens), next(tokens))
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = (next(tokens), next(tokens))
        graph[u].append(v)
        graph[v].append(u)
    dist = [-1] * (n + 1)
    dist[0] = 0
    queue = deque([0])
    while queue:
        u = queue.popleft()
        for v in graph[u]:
            if dist[v] < 0:
                dist[v] = dist[u] + 1
                queue.append(v)
    costs = sorted((dist[next(tokens)] for _ in range(subjects)))
    return str(2 * sum(costs[:needed]))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(N + M + S \log S)$ per test case
- **Space:** $O(N + M + S)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Several subjects may be taught in the same building; each still costs a full round trip.
- A subject taught in the hostel building itself costs 0.
- The graph is connected for the given inputs, so every subject is reachable.
- $K \le S$, so there are always enough subjects to choose from.

## Dry run

Third sample: edges `0-1, 0-2, 0-4, 1-3, 1-4, 2-5, 2-6`; subjects in buildings `1 2 3 5 6`; $K = 3$.

Distances from 0: buildings 1, 2, 4 at distance 1; buildings 3, 5, 6 at distance 2.

Subject distances sorted: `1 1 2 2 2`. The three smallest sum to 4, so the answer is 8.

> CodeChef tags: `Data Structures`, `Algorithms`, `Graph Algos`, `Shortest Paths`, `Traversals`

---

Same problem in rating order (#681 of 735): [../../by-rating/681-CLASSES.md](../../by-rating/681-CLASSES.md)
