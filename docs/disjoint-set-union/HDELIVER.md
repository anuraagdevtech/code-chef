[&larr; 523. Queries with Bags](DSUBAGS.md) &middot; [Index](../../README.md) &middot; [699. Spooky Sequences &rarr;](SPOOKYSEQ.md)

# 543. Home Delivery

> CodeChef problem code [`HDELIVER`](https://www.codechef.com/problems/HDELIVER) &middot; difficulty **1621** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Disjoint Set Union |
| **Technique** | Fast-road connected components |
| **Time** | $O((N+M+Q)\alpha(N))$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Chef has decided to start home delivery from his restaurant. He hopes that he will get a lot of orders for delivery, however there is a concern. He doesn't have enough work forces for all the deliveries.  For this he has came up with an idea - he will group together all those orders which have to be delivered in nearby areas.
In particular, he has identified certain bidirectional roads which he calls as fast roads. They are short and usually traffic free, so the fast travel is possible along these roads. His plan is that he will send orders to locations **A** and **B** together if and only if it is possible to travel between **A** and **B** using only fast roads. Your task is, given the configuration of fast roads, identify which orders are to be sent together.

**Input**

First line of input contains an integer **T**, the number of test cases. Then **T** test cases follow. First line of each test case contains two space separated integers **N** and **M**, denoting number of locations and the number of fast roads. Then **M** lines follow each containing two space separated integers **A** and **B**, denoting that there is a fast road between locations **A** and **B**. Assume that locations are indexed by numbers from 0 to **N-1**.

Next line contains an integer **Q** denoting the number of queries. Each of the next **Q** lines contain two integers **X** and **Y**. For each query you have to find out if orders meant for locations **X** and **Y** are to be sent together or not.

Note that there might be multiple fast roads between same pair of locations, also there might be a fast road that links a location to itself.

**Output**

For each test case print **Q** lines - one for each query. Output "YO" if the orders are to be
delivered together and "NO" otherwise (quotes for clarity).

**Constraints**

```
1 ≤ **T** ≤ 100
1 ≤ **N** ≤ 100
1 ≤ **M** ≤ 1000
0 ≤ **A, B, X, Y** ≤ **N-1**
1 ≤ **Q** ≤ 3000
```

**Warning!**

**There are large input and output files in this problem. Make sure you use fast enough I/O methods.**

## Constraints

1 ≤ T ≤ 100
1 ≤ N ≤ 100
1 ≤ M ≤ 1000
0 ≤ A, B, X, Y ≤ N-1
1 ≤ Q ≤ 3000

## Sample

**Sample input**

```
1
4 2
0 1
1 2
3
0 2
0 3
2 1
```

**Sample output**

```
YO
NO
YO
```

## Approach

Union the endpoints of every fast road. Connectivity through a chain of fast roads is transitive, so two delivery locations belong together exactly when their DSU representatives agree. Path compression and union by size make all operations nearly constant time.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n,m = int(next(tokens)),int(next(tokens))
        parent = list(range(n))
        size = [1]*n
        def find(u):
            while parent[u] != u:
                parent[u] = parent[parent[u]]
                u = parent[u]
            return u
        for _ in range(m):
            u,v = find(int(next(tokens))),find(int(next(tokens)))
            if u != v:
                if size[u] < size[v]:
                    u,v = v,u
                parent[v] = u
                size[u] += size[v]
        for _ in range(int(next(tokens))):
            u,v = find(int(next(tokens))),find(int(next(tokens)))
            out.append('YO' if u == v else 'NO')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O((N+M+Q)\alpha(N))$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Locations are zero-based.
- Self-loops and repeated roads do not change components.
- The affirmative output is `YO`, not `YES`.

## Dry run

Edges `0-1` and `1-2` put locations 0, 1, and 2 together. Queries `0 2`, `0 3`, and `2 1` return `YO`, `NO`, `YO`.

---

Same problem in rating order (#371 of 735): [../../by-rating/371-HDELIVER.md](../../by-rating/371-HDELIVER.md)
