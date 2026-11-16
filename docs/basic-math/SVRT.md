[&larr; 499. Chef and Polygon Cakes](PCJ18C.md) &middot; [Index](../../README.md) &middot; [547. One more weird game &rarr;](OMWG.md)

# 512. Server Trouble

> CodeChef problem code [`SVRT`](https://www.codechef.com/problems/SVRT) &middot; difficulty **1791** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Balance the circular gaps by quotient and remainder |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You are the Chief Engineer of a fast growing start-up. You wish to place $K$ servers in some distinct locations from among $N$ locations. The locations, numbered $1, 2, \ldots, N$ are arranged in a circular manner. The distance between every adjacent location is 1 unit. $1$ and $N$ are adjacent.

You want to place the servers such that the maximum shortest distance between any two adjacent servers is as less as possible. Find this minimum possible distance that can be achieved, and also the minimum number of pairs of adjacent servers separated by this distance.

**Input:**
- The first line contains a single integer, $T$, denoting the number of test cases.
- Each test case consists of a single line containing two space-separated integers $N$ and $K$, denoting the number of locations, and the number of servers, respectively.

**Output:**
For test case, output two space-separated integers $D$ and $X$, denoting the minimum possible maximum shortest distance that can be achieved between any two adjacent servers, and the minimum number of pairs of servers separated by this distance, respectively, in a separate line.

**Constraints**
- $1 \le T \le 10^5$
- $3 \le K \le N \le 10^9$

## Constraints

- $1 \le T \le 10^5$
- $3 \le K \le N \le 10^9$

## Sample

**Sample input**

```
3
6 3
10 6
10 4
```

**Sample output**

```
2 3
2 4
3 2
```

<details><summary>Explanation</summary>

- **Sample Test $1$:** Let the locations be numbered from $1$ to $6$. We can place the servers at locations $1$, $3$ and $5$. Thus, the distances between locations $1$ and $3$, $3$ and $5$, and $5$ and $1$ are all $=2$, which is the lowest possible maximum distance that can be achieved here. There are $3$ pairs of locations separated by this distance.

- **Sample Test $2$:** Let the locations be numbered from $1$ to $10$. We can place the servers at locations $1,2,4,6,8$ and $10$. Thus, the minimum possible maximum distance between any two adjacent servers is $2$. There shall be at least $4$ pairs of servers separated by this distance. Here, they are $(2,4)$, $(4,6)$, $(6,8)$ and $(8,10)$.

</details>

## Approach

The $K$ consecutive circular gaps are positive integers summing to $N$. Their maximum is at least $D=\lceil N/K\rceil$, and distributing the gaps as evenly as possible attains it.

To minimise how many gaps equal $D$, let all other gaps be at most $D-1$. If there are $x$ maximum gaps, then $N\le K(D-1)+x$, so $x\ge N-K(D-1)$. Choosing exactly that many gaps of size $D$ and all other gaps of size $D-1$ attains the bound. This is the adjacent-gap distance used by the problem's samples.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, k = int(next(tokens)), int(next(tokens))
        d = (n+k-1)//k
        out.append(f'{d} {n-k*(d-1)}')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- If $N$ is divisible by $K$, every gap equals $N/K$, so the count is $K$.
- If $N=K$, every gap has length one.
- Use integer ceiling division.

## Dry run

For `N=10,K=6`, `D=2`, and `X=10-6*(2-1)=4`: four gaps of two and two gaps of one.

> CodeChef tags: `Mathematics`, `Algorithms`, `Constructive`

---

Same problem in rating order (#513 of 735): [../../by-rating/513-SVRT.md](../../by-rating/513-SVRT.md)
