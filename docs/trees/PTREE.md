[&larr; 614. Chef and Subarray Queries](CSUBQ.md) &middot; [Index](../../README.md) &middot; [649. Full Path Eraser &rarr;](FPE.md)

# 621. Perfect Tree Problem

> CodeChef problem code [`PTREE`](https://www.codechef.com/problems/PTREE) &middot; difficulty **2900** &middot; time limit **2.5s**

| | |
|---|---|
| **Topic** | Trees |
| **Technique** | Level widths of perfect subtrees as constant-width segments with arithmetic-geometric sums |
| **Time** | $O(N \log N + D \cdot B \log N + Q (\sqrt{N} + D))$ with $D = O(\sqrt{N})$ branching depths and $B$ distinct anchors queried |
| **Space** | $O(N + D \cdot B)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

A *perfect tree* is a rooted tree such that all its leaves are at the same distance from the root. The *value* of a perfect tree with $n$ vertices at a time $x$ is
$$W(x) = \mathrm{max}_p \left(\sum_{i=1}^{n} dist(p_i) \cdot x^{i-1}\right) \;,$$
where the vertices of the tree are (arbitrarily) numbered $1$ through $n$, the maximum is taken over all permutations $p$ of integers $1$ through $n$, and $dist(u)$ denotes the distance of vertex $u$ from the root.

Our Chef has a perfect tree with $N$ vertices (numbered $1$ through $N$), which is rooted at vertex $1$. For any vertex $v$ of this tree, the value of the subtree rooted at $v$ (note that it is also a perfect tree) is defined in the same way as above, where the sum and permutations are only taken over vertices of this subtree and $dist()$ denotes the distance from vertex $v$.

You should answer $Q$ queries. In each query, Chef has two parametres $v$ and $y$ and he wants to know the value of the subtree rooted at vertex $v$, at time $y$. The queries are encoded in such a way that they have to be answered online. Since the values may be large, compute them modulo $1000000007$ ($10^9 + 7$).

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $Q$.
- Each of the following $N-1$ lines contains two space-separated integers $u$ and $v$ denoting an edge between vertices $u$ and $v$.
- The following $Q$ lines describe queries. Each of these lines contains two space-separated integers $a$ and $b$. The parametres $v$ and $y$ are computed in the following way: let's denote the answer to the previous query by $ans$ ($ans = 0$ for the first query); then, $v = a \oplus ans$ and $y = b \oplus ans$.

**Output**
For each query, print a single line containing one integer - the value of the given subtree modulo $10^9 + 7$.

**Constraints**
- $1 \le T \le 5$
- $1 \le N \le 200,000$
- $1 \le Q \le 100,000$
- $1 \le u, v \le N$
- $1 \le y \lt 10^9+7$
- the graph described on the input is a perfect tree
- the sum of $N$ over all test cases does not exceed $200,000$
- the sum of $Q$ over all test cases does not exceed $100,000$

**Subtasks**
- Subtask 1 (20 points) :

    $1 \leq $ Sum of $N$ over all test cases $\leq 10000$

    $1 \leq $ Sum of $Q$ over all test cases $\leq 8000$

- Subtask 2 (80 points) :

    Original Constraints

## Constraints

- $1 \le T \le 5$
- $1 \le N \le 200,000$
- $1 \le Q \le 100,000$
- $1 \le u, v \le N$
- $1 \le y \lt 10^9+7$
- the graph described on the input is a perfect tree
- the sum of $N$ over all test cases does not exceed $200,000$
- the sum of $Q$ over all test cases does not exceed $100,000$

## Sample

**Sample input**

```
1
6 3
1 2
1 3
2 4
2 5
3 6
1 1
10 10
5 5
```

**Sample output**

```
8
6
3
```

<details><summary>Explanation</summary>

**Example case 1:** For the first query, the choice of the permutation $p$ is irrelevant, the inner sum (and therefore the value of the tree) is always just the sum of distances of all vertices from vertex $1$. Hence, the answer is $0+1+1+2+2+2 = 8$.

In the second query, $v = 2$ and $y = 2$.

In the third query, $v = 3$ and $y = 3$.

</details>

## Approach

For a non-negative $x$ the maximum over permutations is reached by sorting the distances increasingly, so $W(x) = \sum_i d_i x^{i-1}$ with $d$ sorted. In a perfect subtree the sorted distances are simply the levels in order: level $t$ contributes the distance $t$ to $w_t$ consecutive powers, where $w_t$ is the width of that level.

In a perfect tree every vertex above the leaf level has a child, so widths never decrease, and they change only below vertices with two or more children. Since the widths sum to at most $N$, a subtree has $O(\sqrt{N})$ distinct widths. Group the levels into segments of constant width; inside a segment with width $w$ the contribution is $\sum_t t \cdot y^{\text{offset} + w t} \cdot (y^w - 1)/(y - 1)$, an arithmetic-geometric series with ratio $y^w$ that has a closed form.

To find the segments of a subtree quickly, for every depth keep the branching vertices one level above it sorted by Euler-tour entry time, with prefix sums of (children $-$ 1). The width gain at a depth for the subtree of $v$ is then a range sum over the Euler interval of $v$. A vertex on a chain of single children has the same segments as the first branching vertex below it (its *anchor*), shifted by the chain length, so segment lists are cached per anchor.

The queries are online (xor-ed with the previous answer). $y = 1$ is handled by plain sums of distances; the geometric sum is evaluated by doubling so that $y^w = 1$ needs no division, and when a query spans many segments the powers of $y$ come from baby-step/giant-step tables.

## Solution (Python)

```python
import sys
from bisect import bisect_left
from collections import defaultdict
from math import isqrt


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    MOD = 1000000007
    for _ in range(next(tokens)):
        n, q = (next(tokens), next(tokens))
        graph = [[] for _ in range(n)]
        for _ in range(n - 1):
            u, v = (next(tokens) - 1, next(tokens) - 1)
            graph[u].append(v)
            graph[v].append(u)
        parent = [-1] * n
        depth = [0] * n
        order = [0]
        for v in order:
            for u in graph[v]:
                if u != parent[v]:
                    parent[u] = v
                    depth[u] = depth[v] + 1
                    order.append(u)
        children = [[] for _ in range(n)]
        for v in order[1:]:
            children[parent[v]].append(v)
        tin = [0] * n
        tout = [0] * n
        timer = 0
        stack = [(0, 0)]
        special = defaultdict(list)
        height = max(depth)
        while stack:
            v, exit = stack.pop()
            if exit:
                tout[v] = timer
                continue
            tin[v] = timer
            timer += 1
            stack.append((v, 1))
            if len(children[v]) > 1:
                special[depth[v] + 1].append((tin[v], len(children[v]) - 1))
            for u in reversed(children[v]):
                stack.append((u, 0))
        levels = sorted(special)
        rows = {}
        for d, items in special.items():
            items.sort()
            positions = []
            pref = [0]
            for pos, w in items:
                positions.append(pos)
                pref.append(pref[-1] + w)
            rows[d] = (positions, pref)
        anchor = list(range(n))
        for v in reversed(order):
            if len(children[v]) == 1:
                anchor[v] = anchor[children[v][0]]
        del graph, parent, children, order, special
        cache = {}
        answer = 0

        def geom(r, count):
            result = 0
            power = 1
            block = 1
            while count:
                if count & 1:
                    result = (result + power * block) % MOD
                    power = power * r % MOD
                block = block * (1 + r) % MOD
                r = r * r % MOD
                count //= 2
            return result
        for _ in range(q):
            a, b = (next(tokens), next(tokens))
            v = (a ^ answer) - 1
            y = b ^ answer
            root = anchor[v]
            delta = depth[root] - depth[v]
            if root not in cache:
                segments = []
                last = depth[root]
                width = 1
                for d in levels[bisect_left(levels, depth[root] + 1):]:
                    positions, pref = rows[d]
                    gain = pref[bisect_left(positions, tout[root])] - pref[bisect_left(positions, tin[root])]
                    if gain:
                        segments.append((last - depth[root], d - last, width))
                        last = d
                        width += gain
                segments.append((last - depth[root], height - last + 1, width))
                cache[root] = segments
            segments = cache[root]
            answer = 0
            if delta:
                segments = [(0, segments[0][1] + delta, 1)] + [(start + delta, length, width) for start, length, width in segments[1:]]
            if y == 1:
                answer = sum((width * length * (2 * start + length - 1) // 2 for start, length, width in segments)) % MOD
            else:
                inv = pow(y - 1, MOD - 2, MOD)
                power = 1
                if len(segments) > 16:
                    limit = isqrt(tout[v] - tin[v]) + 1
                    small = [1] * limit
                    for i in range(1, limit):
                        small[i] = small[i - 1] * y % MOD
                    step = small[-1] * y % MOD
                    large = [1] * (limit + 1)
                    for i in range(1, limit + 1):
                        large[i] = large[i - 1] * step % MOD

                    def powerof(exponent):
                        return large[exponent // limit] * small[exponent % limit] % MOD
                else:

                    def powerof(exponent):
                        return pow(y, exponent, MOD)
                for start, length, width in segments:
                    r = powerof(width)
                    if length == 1:
                        endpower = r
                        s = 1
                    else:
                        endpower = powerof(width * length)
                        s = geom(r, length)
                    answer = (answer + power * ((start + length - 1) * endpower - (start - 1) - s)) % MOD
                    power = power * endpower % MOD
                answer = answer * inv % MOD
            out.append(str(answer))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N \log N + D \cdot B \log N + Q (\sqrt{N} + D))$ with $D = O(\sqrt{N})$ branching depths and $B$ distinct anchors queried
- **Space:** $O(N + D \cdot B)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $y = 1$ makes the closed form divide by zero; the answer is the sum of all distances.
- $y^w \equiv 1$ for some width must not be divided by either, hence the division-free geometric sum.
- A query vertex inside a unary chain shifts every distance of its anchor's list by the chain length.
- The decoded vertex and $y$ depend on the previous answer, so queries cannot be reordered.

## Dry run

Tree with edges `1-2, 1-3, 2-4, 2-5, 3-6`, query vertex 1 with $y = 1$.

Level widths are 1, 2, 3 at distances 0, 1, 2, and all three widths differ, so there are three segments of one level each. With $y = 1$ the value is the plain sum of distances: $0 \cdot 1 + 1 \cdot 2 + 2 \cdot 3 = 8$.

The next query is decoded with 8: the pair `10 10` becomes vertex $10 \oplus 8 = 2$ and $y = 2$. Its subtree has distances `0 1 1`, so $W = 0 + 1 \cdot 2 + 1 \cdot 4 = 6$.

---

Same problem in rating order (#712 of 735): [../../by-rating/712-PTREE.md](../../by-rating/712-PTREE.md)
