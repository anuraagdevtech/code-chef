[&larr; 614. Per Capita Income](614-PERCAPTA.md) &middot; [Index](README.md) &middot; [616. Interesting Array &rarr;](616-INTARR.md)

# 615. Tourists in Mancunia

> [`TOURISTS`](https://www.codechef.com/problems/TOURISTS) &middot; difficulty **2133** &middot; time limit **2s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Graphs |
| **Technique** | Orient an undirected Euler tour |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N+E)$ overall |
| **Space** | $O(N+E)$ |

## Question

The grand kingdom of Mancunia is famous for its tourist attractions and visitors flock to it throughout the year. King Mancunian is the benevolent ruler of the prosperous country whose main source of revenue is, of course, tourism.

The country can be represented by a network of **unidirectional** roads between the cities. But Mancunian, our benign monarch, has a headache. The road network of the country is not **tourist-friendly** and this is affecting revenue. To increase the GDP of the nation, he wants to redirect some of the roads to make the road network **tourist-friendly** and hence, ensure happiness and prosperity for his loyal subjects.

Now is the time for some formal definitions. :(

A road network is said to be **tourist-friendly** if for every city in the country, if a tourist starts his journey there, there is a path she can take to visit each and every city of the nation and traverse each road **exactly once** before ending up at the city where she started.

Given a description of the road network of Mancunia, can you come up with a scheme to redirect some (possibly none) of the roads to make it **tourist-friendly**?

**Input**

The first line contains two integers **N** and **E** denoting the number of cities and roads in the beautiful country of Mancunia respectively.

Each of the next **E** lines contains two integers **a** and **b** implying that there is a unidirectional road from city **a** to city **b**.

It is guaranteed that there aren't multiple roads in the exact same direction and that there is no road from a city to itself.

**Output**

If there is no solution, print "NO" (without quotes). Else, print "YES" (without quotes), followed by exactly **E** lines.

The **i^th** line of output should represent the **i^th** road in the input. It should have two integers **a** and **b** denoting that the final orientation of that road is from **a** to **b**.

**Constraints**

- **1** ≤ **N** ≤ **100000**

- **1** ≤ **E** ≤ **200000**

- **1** ≤ **a, b** ≤ **N**

**Subtask 1: (20 points)**

- **1** ≤ **N** ≤ **20**

- **1** ≤ **E** ≤ **21**

**Subtask 2: (80 points)**

- **Same as original constraints**

## Constraints

- 1 ≤ N ≤ 100000
- 1 ≤ E ≤ 200000
- 1 ≤ a, b ≤ N

## Sample

**Sample 1 input**

```
3 3
1 2
2 3
3 1
```

**Sample 1 output**

```
YES
1 2
2 3
3 1
```

**Sample 2 input**

```
3 2
1 2
2 3
```

**Sample 2 output**

```
NO
```

**Sample 3 input**

```
5 6
1 2
2 3
3 4
2 4
2 5
1 5
```

**Sample 3 output**

```
YES
1 2
2 3
3 4
4 2
2 5
5 1
```

## Approach

A directed Euler circuit requires equal indegree and outdegree at every vertex. Reorienting preserves undirected degrees, so every degree must be even. The underlying graph must also be connected, including every city.

These conditions suffice. Traverse unused undirected edges using Hierholzer's algorithm and orient each edge in its traversal direction. Every even-degree vertex has equally many arrivals and departures, so the resulting connected directed graph has an Euler circuit from any city. Store directions by edge ID to preserve the input road order; opposite-direction parallel roads remain separate edges.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int,sys.stdin.buffer.read().split()))
    n,m = next(tokens),next(tokens)
    graph = [[] for _ in range(n)]
    for i in range(m):
        u,v = next(tokens)-1,next(tokens)-1
        graph[u].append((v,i))
        graph[v].append((u,i))
    if any(len(adj)%2 for adj in graph):
        print('NO')
        return
    used = bytearray(m)
    visited = bytearray(n)
    orientation = [None]*m
    stack = [0]
    visited[0] = 1
    while stack:
        u = stack[-1]
        while graph[u] and used[graph[u][-1][1]]:
            graph[u].pop()
        if not graph[u]:
            stack.pop()
            continue
        v,e = graph[u].pop()
        used[e] = 1
        orientation[e] = (u+1,v+1)
        visited[v] = 1
        stack.append(v)
    if not all(visited) or not all(used):
        print('NO')
        return
    print('YES')
    sys.stdout.write('\n'.join(f'{u} {v}' for u,v in orientation)+'\n')

if __name__ == '__main__':
    main()
```

## Edge cases

- Any odd degree makes the answer `NO`.
- Isolated cities prevent visiting every city when other roads exist.
- Distinguish edges by ID, not endpoint pair.
- Print roads in the same order as the input.

## Dry run

For triangle `1-2,2-3,3-1`, every degree is two. Orienting the traversal `1->2->3->1` gives the required circuit.

---

Same problem grouped by topic: [../docs/graphs/TOURISTS.md](../docs/graphs/TOURISTS.md)
