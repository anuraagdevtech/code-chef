[&larr; 524. Family Tree](FAMTREE.md) &middot; [Index](../../README.md) &middot; [531. Treeversion &rarr;](TREEVERS.md)

# 527. Cosmic Temple

> CodeChef problem code [`COSTEMP`](https://www.codechef.com/problems/COSTEMP) &middot; difficulty **unrated** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Trees |
| **Technique** | Reroot distance sums using subtree sizes |
| **Time** | $O(N)$ overall |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Nearly $10^{9} + 7$ trillion kilometers far away from the Milkyway, there exists a parallel Universe of Light called the Cosmos of Solon where each planet is called a Temple. There are total $N$ temples. Unlike humans, the Solomons (Giant aliens of the Light World) can travel from one temple to another through Cosmic Bridges and the distance observed by them between any two temples is $0$ units (Interesting? Well, they travel with more than the speed of light)

But the year $2020$, proved to be a curse for Solomons. This year, a Mega Star Urus struck their Universe and damaged many Cosmic Bridges. However the God of Light ensured that for any two distinct temples $u$ and $v$ there exists exactly one unique path through Cosmic Bridge(s), but the distance between two directly connected temples through a Bridge has now increased to $1$ units.

To prevail the existence of this Universe, the God of Light carved himself into exactly $N$ Solomons which now rule the $N$ temples and are independent of each other. One by one, the $i^{th}$ Solomon ($0 \leq i \leq N-1$) transmits Light pulses through the network of Cosmic Bridges and determines the sum of distances to the remaining $N-1$ Solomons.

Can you help them find these quantities so they can reunite into God of Light again?

**Input Format:**
- The first line of the input contains $N$, the total no. of temples.
- Each of the next $N-1$ lines contain two space-separated integers $u$ and $v$ ($u \neq v$) denoting the bidirectional Cosmic Bridge between temples $u$ and $v$.

**Output Format:**
Print $N$ space separated integers in a single line where the $i^{th}$ integer denotes the sum of distances from the $i^{th}$ ($0 \leq i \leq N-1$) Solomon to the rest of $N-1$ Solomons.

**Constraints:**
- $1 \leq N \leq 10^{6}$
- $0 \leq u, v \leq N-1$

**Sample Input:**
     5
     0 2
     0 3
     1 3
     3 4

**Sample Output:**
     6 8 9 5 8

**Explanation:**
- For temple $0$ : distance($1$) + distance($2$) + distance($3$) + distance($4$) = $2+1+1+2=6$
- For temple $1$ : distance($0$) + distance($2$) + distance($3$) + distance($4$) = $2+3+1+2=8$
- For temple $2$ : distance($0$) + distance($1$) + distance($3$) + distance($4$) = $1+3+2+3=9$
- For temple $3$ : distance($0$) + distance($1$) + distance($2$) + distance($4$) = $1+1+2+1=5$
- For temple $4$ : distance($0$) + distance($1$) + distance($2$) + distance($3$) = $2+2+3+1=8$

## Constraints

- $1 \leq N \leq 10^{6}$
- $0 \leq u, v \leq N-1$
**Sample Input:**
     5
     0 2
     0 3
     1 3
     3 4
**Sample Output:**
     6 8 9 5 8
**Explanation:**
- For temple $0$ : distance($1$) + distance($2$) + distance($3$) + distance($4$) = $2+1+1+2=6$
- For temple $1$ : distance($0$) + distance($2$) + distance($3$) + distance($4$) = $2+3+1+2=8$
- For temple $2$ : distance($0$) + distance($1$) + distance($3$) + distance($4$) = $1+3+2+3=9$
- For temple $3$ : distance($0$) + distance($1$) + distance($2$) + distance($4$) = $1+1+2+1=5$
- For temple $4$ : distance($0$) + distance($1$) + distance($2$) + distance($3$) = $2+2+3+1=8$

## Approach

Root the tree at vertex zero. One traversal computes depths and a parent-first order. The sum of depths is the distance sum for root zero; a reverse traversal gives subtree sizes.

When moving the root across edge $u-v$ to child $v$, distances to the $size[v]$ vertices inside that subtree decrease by one, while all others increase by one. Therefore $answer[v]=answer[u]+N-2size[v]$. Evaluate this in parent-first order.

The adjacency representation uses compact integer arrays because the bound reaches one million vertices. Iterative traversal avoids recursion depth limits.

## Solution (Python)

```python
import sys
from array import array


def main() -> None:
    values = map(int,sys.stdin.buffer.read().split())
    n = next(values)
    head = array('i',[-1])*n
    to = array('i')
    link = array('i')
    def edge(u,v):
        to.append(v)
        link.append(head[u])
        head[u] = len(to)-1
    for _ in range(n-1):
        u,v = next(values),next(values)
        edge(u,v)
        edge(v,u)
    del values
    parent = array('i',[-1])*n
    depth = array('i',[0])*n
    order = array('i',[0])
    for u in order:
        e = head[u]
        while e != -1:
            v = to[e]
            if v != parent[u]:
                parent[v] = u
                depth[v] = depth[u]+1
                order.append(v)
            e = link[e]
    size = array('i',[1])*n
    for u in reversed(order[1:]):
        size[parent[u]] += size[u]
    answer = [0]*n
    answer[0] = sum(depth)
    for u in order[1:]:
        answer[u] = answer[parent[u]]+n-2*size[u]
    print(' '.join(map(str,answer)))

if __name__ == '__main__':
    main()
```

## Complexity

- **Time:** $O(N)$ overall
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Vertices are zero-based in this problem.
- One vertex has distance sum zero.
- Large chains require integer sums beyond 32 bits.
- The published sample is embedded in the statement rather than the API sample list.

## Dry run

For sample edges `0-2,0-3,1-3,3-4`, root-zero depths sum to 6. Subtree 3 has size 3, so its answer is `6+5-6=5`. Its leaf children have answer `5+5-2=8`.

---

Same problem in rating order (#723 of 735): [../../by-rating/723-COSTEMP.md](../../by-rating/723-COSTEMP.md)
