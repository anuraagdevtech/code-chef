[Index](../../README.md)

# 555. Gravel

> CodeChef problem code [`SPREAD`](https://www.codechef.com/problems/SPREAD) &middot; difficulty **1822** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Fenwick Tree |
| **Technique** | Range additions become two difference-array point updates |
| **Time** | $O((N+M)\log N)$ overall |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Bob has n heap(s) of gravel (initially there are exactly c piece(s) in each). He wants to do m operation(s) with that heaps, each maybe:

- adding pieces of gravel onto the heaps from u to v, exactly k pieces for each,

- or querying "how many pieces of gravel are there in the heap p now?".

**Request**

Help Bob do operations of the second type.

**Input**

- The first line contains the integers n,m,c, respectively.

- m following lines, each forms:
- **S u v k** to describe an operation of the first type.

- **Q p** to describe an operation of the second type.

***(Each integer on a same line, or between the characters S, Q and the integers is separated by at least one space character)***

**Output**

For each operation of the second type, output (on a single line) an integer answering to the respective query (follows the respective Input order).

**Limitations**

- 0 < n <= 10 ^6

- 0 < m <= 250000

- 0 < u <= v <=n

- 0 <= c, k <= 10 ^9

- 0 < p <= n

## Constraints

- 1 <= N <= 10^6.
- 1 <= M <= 250000.
- 1 <= U <= V <= N, and 1 <= P <= N.
- 0 <= C, K <= 10^9.

## Sample

**Sample input**

```
7 5 0
Q 7
S 1 7 1
Q 3
S 1 3 1
Q 3
```

**Sample output**

```
0
1
2
```

## Approach

Use a Fenwick tree for differences from the common initial amount $C$. Adding $K$ to inclusive range $[u,v]$ changes only two differences: add $K$ at $u$ and subtract $K$ at $v+1$. A prefix sum at position $p$ is its total added amount, so the query answer is that prefix sum plus $C$.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    n,m,initial = (int(next(tokens)) for _ in range(3))
    tree = [0]*(n+1)
    def add(index,value):
        while index <= n:
            tree[index] += value
            index += index&-index
    out = []
    for _ in range(m):
        kind = next(tokens)
        if kind == b'S':
            u,v,k = (int(next(tokens)) for _ in range(3))
            add(u,k)
            add(v+1,-k)
        else:
            index = int(next(tokens))
            total = initial
            while index:
                total += tree[index]
                index -= index&-index
            out.append(str(total))
    sys.stdout.write('\n'.join(out)+'\n')

if __name__ == '__main__':
    main()
```

## Complexity

- **Time:** $O((N+M)\log N)$ overall
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Skip the second difference update when $v=N$.
- Amounts can exceed 32-bit integers after many updates.
- There is one input case, without a test-count prefix.

## Dry run

The sample starts at zero. Adding one to `[1,7]` makes position 3 equal one; another addition to `[1,3]` makes it two.

---

Same problem in rating order (#527 of 735): [../../by-rating/527-SPREAD.md](../../by-rating/527-SPREAD.md)
