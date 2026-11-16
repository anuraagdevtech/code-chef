[&larr; 544. Shortest Path in Binary Trees](BINTREE.md) &middot; [Index](../../README.md) &middot; [551. Brush Fire &rarr;](FIRE.md)

# 550. Rendezvous

> CodeChef problem code [`TR1`](https://www.codechef.com/problems/TR1) &middot; difficulty **1638** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Trees |
| **Technique** | Count ordered pairs by their lowest common ancestor |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

There are N cities in Byteland numbered 1 to N with city 1 as the capital. The road network of Byteland has a tree structure. All the roads are bi-directional. Alice and Bob are secret agents working for the Bytelandian Security Agency (BSA). Each secret agent is assigned a random city each month, where he/she must be stationed for the complete month. At the end of each month, they come to the capital to submit their reports to the head of BSA. They always take the shortest path from their city to the capital. If Alice is assigned city A and Bob is assigned city B then they meet at a city C which is common to both their routes to the capital and then travel together from C to the capital.

Alice and Bob wish to spend maximum time together in any trip. So for any pair of assigned cities (A,B) they meet at a city C such that C is the farthest city from the capital and appears in the shortest path from capital to A and capital to B. Since this happens each month they compute this for each pair of assigned cities (A,B) and store it in a matrix M, where M[A][B] = C, the city where they meet.

The importance of a city C(according to Alice and Bob), Im(C) is defined as the number of times C appears in their matrix M. Alice and Bob are interested in finding the importance of each city. Since this output can be large, output the sum S defined as S = (sum i=1 to N) i*Im(i) modulo 1000000007.

**Input**

First line of input contains an integer t (t<=25), the number of test cases. Each test case starts with an integer N (1<=N<=10000), the number of cities

The next N-1 lines contain two space separated integers u v (1<=u,v<=N) denoting a road from u to v.

**Output**

For each test case output the required sum S

## Constraints

- 1 <= T <= 25.
- 1 <= N <= 10000.
- The N-1 undirected edges form a tree on vertices 1 through N.

## Sample

**Sample input**

```
3
5
1 2
1 3
2 4
2 5
3
1 2
1 3
1
```

**Sample output**

```
41
12
1
```

<details><summary>Explanation</summary>

For the first test case, the matrix M is:
1 1 1 1 1
1 2 1 2 2
1 1 3 1 1
1 2 1 4 2
1 2 1 2 5

and the corresponding importance array is: 15 7 1 1 1
so the required sum is 1*15 + 2*7 + 3*1 + 4*1 + 5*1 = 41
For the second test case, the matrix M is:
1 1 1
1 2 1
1 1 3
and so the Importance array is: 7 1 1
So the required sum is 1*7 + 2*1 + 3*1 = 12

For the third test case, there is only one city, so the Matrix M just has one entry 1, so S = 1

</details>

## Approach

The city where two agents first meet is the lowest common ancestor of their assigned cities. There are $size[u]^2$ ordered pairs entirely inside $u$'s subtree. Pairs lying entirely in a single child's subtree have their LCA below $u$ and must be subtracted.

Thus $Im(u)=size[u]^2-\sum size[v]^2$ over children. Compute subtree sizes in reverse traversal order, multiply each importance by its one-based city label, and sum modulo $10^9+7$.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        graph = [[] for _ in range(n)]
        for _ in range(n-1):
            u,v = int(next(tokens))-1,int(next(tokens))-1
            graph[u].append(v)
            graph[v].append(u)
        parent = [-1]*n
        order = [0]
        for u in order:
            for v in graph[u]:
                if v != parent[u]:
                    parent[v] = u
                    order.append(v)
        size = [1]*n
        child_squares = [0]*n
        answer = 0
        for u in reversed(order):
            answer += (u+1)*(size[u]*size[u]-child_squares[u])
            if parent[u] != -1:
                size[parent[u]] += size[u]
                child_squares[parent[u]] += size[u]*size[u]
        out.append(str(answer%1000000007))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Pairs are ordered, so `(A,B)` and `(B,A)` both count.
- Include diagonal pairs `(u,u)`.
- A one-city tree returns one.

## Dry run

In the five-city sample tree, subtree sizes are `[5,3,1,1,1]`. Importance at city 1 is `25-9-1=15`; at city 2 it is `9-1-1=7`; leaves contribute one each. The weighted sum is 41.

---

Same problem in rating order (#388 of 735): [../../by-rating/388-TR1.md](../../by-rating/388-TR1.md)
