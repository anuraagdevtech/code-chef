# 328. Shortest Route

> CodeChef problem code [`SHROUTE`](https://www.codechef.com/problems/SHROUTE) &middot; difficulty **1756** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Nearest qualifying index from each side |
| **Time** | $O(N + M)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

**Read problem statements in [Vietnamese](https://www.codechef.com/download/translated/JUNE21/vietnamese/SHROUTE.pdf),**
There are $N$ cities in Chefland numbered from $1$ to $N$ and every city has a railway station. Some cities have a train and each city has at most one train originating from it. The trains are represented by an array $A$, where $A_i = 0$ means the $i$-th city doesn't have any train originating from it, $A_i = 1$ means the train originating from the $i$-th city is moving right (to a higher numbered city), and $A_i = 2$ means the train originating from the $i$-th city is moving left (to a lower numbered city).

Each train keeps on going forever in its direction and takes $1$ minute to travel from the current station to the next one. There is a special station at city $1$ which lets travellers instantaneously teleport to any other station that currently has a train. Teleportation and getting on a train once in the city both take $0$ minutes and all trains start at time $0$.

There are $M$ travellers at city $1$, and the $i$-th traveller has destination city $B_i$. They ask Chef to guide them to teleport to a particular station from which they can catch a train to go to their destination in the least time possible. In case it's not possible for a person to reach his destination, print $-1$.

**Note:** The input and output of this problem are large, so prefer using fast input/output methods.

**Input**
- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains three lines of input.
- The first line contains two integers $N$, $M$.
- The second line contains $N$ integers $A_1, A_2, \ldots, A_N$.
- The third line contains $M$ integers $B_1, B_2, \ldots, B_M$.

**Output**
For each test case, output $M$ space-separated integers $C_1, C_2, \ldots, C_M$, where $C_i$ is the minimum time required by the $i$-th traveller to reach his destination and if the $i$-th traveller can't reach his destination, $C_i = -1$.

**Constraints**
- $1 \leq N, M \leq 10^5$
- $0 \leq A_i \leq 2$
- $1 \leq B_i \leq N$
- The sum of $N$ over all test cases is at most $10^6$.
- The sum of $M$ over all test cases is at most $10^6$.

**Subtasks**
**Subtask #1 (100 points):** original constraints

## Constraints

- $1 \leq N, M \leq 10^5$
- $0 \leq A_i \leq 2$
- $1 \leq B_i \leq N$
- The sum of $N$ over all test cases is at most $10^6$.
- The sum of $M$ over all test cases is at most $10^6$.

## Sample

**Sample input**

```
3
5 1
1 0 0 0 0
5
5 1
1 0 0 0 2
4
5 2
2 0 0 0 1
3 1
```

**Sample output**

```
4
1
-1 0
```

<details><summary>Explanation</summary>

**Test Case $1$:** The only person takes the train from station $1$ and hence takes $|5 - 1| = 4$ minutes to reach his destination.

**Test Case $2$:** The only person takes the train from station $5$ and hence takes $|5 - 4| = 1$ minute to reach his destination.

**Test Case $3$:** Since no train passes station $3$, it's impossible for the first person to reach his destination and since the second person is already at station $1$, it takes him $0$ minutes to reach his destination.

</details>

## Approach

Teleporting is free, so the traveller may board **any** train in the country. The only cost is the ride.

A right-moving train from city $i$ visits $i, i+1, i+2, \ldots$, reaching $B$ in $B - i$ minutes — and only if $i \leq B$. A left-moving train from $i$ reaches $B$ in $i - B$ minutes, and only if $i \geq B$.

To minimise the ride, take the **closest** usable train on each side:

- the largest $i \leq B$ with $A_i = 1$, costing $B - i$;
- the smallest $i \geq B$ with $A_i = 2$, costing $i - B$.

Take the better of the two, or $-1$ if neither exists.

Both are answered in $O(1)$ after two linear sweeps: one left-to-right carrying the most recent right-moving train, one right-to-left carrying the next left-moving train. With the sums of $N$ and $M$ reaching $10^6$, that linear preprocessing plus constant-time queries is what the problem's note about fast I/O is pointing at.

Note that a train **at** $B$ itself costs $0$ in either direction, which the formulas give naturally.

The samples cover each branch. Case 1 has only a right-mover at city $1$, so reaching city $5$ takes $4$ minutes. Case 2 adds a left-mover at city $5$, which reaches city $4$ in a single minute — far better than the $3$ the right-mover would need. Case 3 asks for city $3$, where the right-mover sits to its right and the left-mover to its left, so neither can help: $-1$. Its second query, city $1$, boards the left-mover already there for $0$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        a = data[pos + 2:pos + 2 + n]
        pos += 2 + n
        # Nearest right-mover at or before i, and left-mover at or after i.
        prev_right = [-1] * (n + 1)
        last = -1
        for i in range(1, n + 1):
            if a[i - 1] == b"1":
                last = i
            prev_right[i] = last
        next_left = [-1] * (n + 2)
        nxt = -1
        for i in range(n, 0, -1):
            if a[i - 1] == b"2":
                nxt = i
            next_left[i] = nxt
        res = []
        for i in range(m):
            b = int(data[pos + i])
            best = -1
            if prev_right[b] != -1:
                best = b - prev_right[b]
            if next_left[b] != -1:
                cand = next_left[b] - b
                best = cand if best == -1 else min(best, cand)
            res.append(str(best))
        pos += m
        out.append(" ".join(res))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N + M)$ per test case
- **Space:** $O(N)$
