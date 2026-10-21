# 1016 &middot; Chef in Vaccination Queue

> CodeChef problem code [`VACCINQ`](https://www.codechef.com/problems/VACCINQ) &middot; time limit **1s** &middot; Level up from 1* to 2* (Level 2)

## Topics used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Prefix sum with a per-element lookup |
| **CodeChef category** | main |
| **Time** | $O(P)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/arrays/VACCINQ.md](../docs/arrays/VACCINQ.md)

## Question

There are $N$ people in the vaccination queue, Chef is standing on the $P^{th}$ position from the front of the queue. It takes $X$ minutes to vaccinate a child and $Y$ minutes to vaccinate an elderly person. Assume Chef is an elderly person.

You are given a binary array $A_1, A_2, \dots, A_N$ of length $N$, where $A_i = 1$ denotes there is an elderly person standing on the $i^{th}$ position of the queue, $A_i = 0$ denotes there is a child standing on the $i^{th}$ position of the queue. You are also given the three integers $P, X, Y$. Find the number of minutes after which Chef's vaccination will be completed.

**Input**

- First line will contain $T$, number of testcases. Then the testcases follow.
- The first line of each test case contains four space-separated integers $N, P, X, Y$.
- The second line of each test case contains $N$ space-separated integer $A_1, A_2,\dots, A_N$.

**Output**

For each testcase, output in a single line the number of minutes after which Chef's vaccination will be completed.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $1 \leq P \leq N$
- $1 \leq X, Y \leq 10$
- $0 \leq A_i \leq 1$
- $A_P = 1$

## Sample

**Sample input**

```
3
4 2 3 2
0 1 0 1
3 1 2 3
1 0 1
3 3 2 2
1 1 1
```

**Sample output**

```
5
3
6
```

<details><summary>Explanation</summary>

**Test case $1$**: The person standing at the front of the queue is a child and the next person is Chef. So it takes a total of $3 + 2 = 5$ minutes to complete Chef's vaccination.

**Test case $2$**: Chef is standing at the front of the queue. So his vaccination is completed after $3$ minutes.

**Test case $3$**: Chef is standing at the rear of the queue. So it takes a total of $2 + 2 + 2 = 6$ minutes to complete Chef's vaccination.

</details>

## Approach

Chef is $P$-th in the queue and nobody is served out of order, so his vaccination finishes once everyone from position $1$ to position $P$ — **including himself** — has been done. Each person costs $Y$ minutes if elderly ($A_i = 1$) or $X$ if a child ($A_i = 0$):

$$\sum_{i=1}^{P} \begin{cases} Y & A_i = 1 \\ X & A_i = 0 \end{cases}$$

Two off-by-one risks sit here. The sum must run **through** $P$, not stop before it — the question asks when Chef's own vaccination completes, not when it starts. And the array is one-indexed in the statement but zero-indexed in code, so the slice is `a[:p]`.

The guarantee $A_P = 1$ confirms Chef is elderly, as the statement says, so his own cost is $Y$. It is a consistency check rather than something the code must enforce.

The people **behind** Chef are irrelevant — the array may be longer than $P$, and everything past position $P$ is ignored. Sample case 1 has a fourth person who never enters the calculation.

Working through case 1: positions $1$ and $2$ hold a child and an elder, costing $X + Y = 3 + 2 = 5$. Case 3 has three elders at $2$ minutes each for $6$.

Since only the first $P$ entries matter, the scan is $O(P)$ rather than $O(N)$ — immaterial at these bounds, but the right shape.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, p, x, y = map(int, data[pos:pos + 4])
        a = data[pos + 4:pos + 4 + n]
        pos += 4 + n
        # Everyone up to and including Chef at position p must be served.
        total = sum(y if v == b"1" else x for v in a[:p])
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(P)$ per test case
- **Space:** $O(1)$
