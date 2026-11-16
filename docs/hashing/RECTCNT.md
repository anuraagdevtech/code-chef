[Index](../../README.md) &middot; [519. IS IT DSU HARD!! &rarr;](CFMAR04.md)

# 494. Rectangles Counting

> CodeChef problem code [`RECTCNT`](https://www.codechef.com/problems/RECTCNT) &middot; difficulty **1770** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Hashing |
| **Technique** | Group vertical sides by their two heights |
| **Time** | $O(N)$ expected per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Given N separate integer points on the Cartesian plane satisfying: there is no any three of them sharing a same X-coordinate. Your task is to count the number of rectangles (whose edges parrallel to the axes) created from any four of given points.

**Input**

There are several test cases (ten at most), each formed as follows:

- The first line contains a positive integer N (N ≤ 10^5).

- N lines follow, each containing a pair of integers (each having an absolute value of 10^9 at most) describing coordinates of a given point.

The input is ended with N = 0.

**Output**

For each test case, output on a line an integer which is the respective number of rectangles found.

## Constraints

- At most 10 cases, terminated by N = 0.
- 1 <= N <= 10^5.
- At most two points share an x-coordinate.
- Absolute coordinates are at most 10^9.

## Sample

**Sample input**

```
6
7 1
3 5
3 1
1 5
1 1
7 5
0
```

**Sample output**

```
3
```

## Approach

No three points share an $x$ coordinate, so each vertical line has at most one possible vertical side. Record the ordered pair of its two $y$ coordinates. Two vertical sides form an axis-aligned rectangle exactly when these height pairs agree.

When a pair has already appeared $f$ times, its next occurrence contributes $f$ new rectangles. Sum these contributions without enumerating rectangles.

## Solution (Python)

```python
import sys
from collections import Counter


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    while True:
        n = int(next(tokens))
        if n == 0:
            break
        columns = {}
        pairs = Counter()
        answer = 0
        for _ in range(n):
            x, y = int(next(tokens)), int(next(tokens))
            if x in columns:
                key = tuple(sorted((columns[x], y)))
                answer += pairs[key]
                pairs[key] += 1
            else:
                columns[x] = y
        out.append(str(answer))
    sys.stdout.write('\n'.join(out)+'\n')

if __name__ == '__main__':
    main()
```

## Complexity

- **Time:** $O(N)$ expected per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Input ends with `0`; there is no leading test-case count.
- A vertical line with one point contributes no side.
- Normalise the two heights so input order does not matter.

## Dry run

The sample has vertical sides at `x=1,3,7`, all with heights `(1,5)`. Their contributions are `0+1+2=3`.

> CodeChef tags: `Data Structures`, `Basic Programming Concepts`, `Mathematics`, `Algorithms`, `Constructive`

---

Same problem in rating order (#493 of 735): [../../by-rating/493-RECTCNT.md](../../by-rating/493-RECTCNT.md)
