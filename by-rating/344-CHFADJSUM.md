[&larr; 343. Odd Sum](343-ODDSUM.md) &middot; [Index](README.md) &middot; [345. Bouncing Ball &rarr;](345-BOUNCE_BALL.md)

# 344. Chef And Adjacent Sums

> [`CHFADJSUM`](https://www.codechef.com/problems/CHFADJSUM) &middot; difficulty **1604** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Keeping the heaviest elements apart |
| **CodeChef tags** | `Algorithms`, `Observation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

You are given an array $A$ of size $N$.
Consider an array $B$ of size $N$ formed by sorting $A$ in non-decreasing order.
Let $Z = (B_N + B_{(N-1)})$.

Find whether there exists any rearrangement of the array $A$, such that, for all $(1\le i \lt N)$,
$(A_i + A_{(i+1)}) \lt Z$.
If such a rearrangement exists, print `YES`, otherwise print `NO`.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains a integer $N$  — the number of elements in the array.
    - The next line contains $N$ space-separated integers, denoting the elements of the array.

**Output**

For each test case, output `YES`, if a rearrangement exists that satisfies the conditions. Otherwise, output `NO`.

You may print each character in uppercase or lowercase. For example, `NO`, `no`, `No`, and `nO` are all considered the same.

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^5$
- The sum of $N$ over all test cases won't exceed $10^5$.

## Sample

**Sample input**

```
4
3
3 4 4
4
1 2 3 4
2
2 2
2
1 2
```

**Sample output**

```
YES
YES
NO
NO
```

<details><summary>Explanation</summary>

**Test case $1$:** Here $B = [3, 4, 4]$ and $Z = (4 + 4) = 8$.
We can rearrange the array to $[4,3,4]$ such that $(A_1 + A_2) = 7 \lt 8$ and $(A_2 + A_3) = 7 \lt 8$. Thus, the rearrangement is valid.

**Test case $2$:** Here $B = [1, 2, 3, 4]$ and $Z = (4 + 3) = 7$.
We can rearrange the array to $[4,2,3,1]$ such that $(A_1 + A_2) = 6 \lt 7$, $(A_2 + A_3) = 5 \lt 7$, and $(A_3 + A_4) = 4 \lt 7$. Thus, the rearrangement is valid.

**Test case $3$:** The exists no possible rearrangement that satisfies the conditions.

**Test case $4$:** The exists no possible rearrangement that satisfies the conditions.

</details>

## Approach

$Z$ is the largest sum any pair can make, so adjacent sums are automatically $\leq Z$ and the question is purely whether the pairs achieving **exactly** $Z$ can be kept non-adjacent. Writing $b_1 \geq b_2$ for the two largest values, a pair sums to $Z = b_1 + b_2$ only if its values are precisely $b_1$ and $b_2$.

That splits into two cases.

**The maximum is repeated** ($b_1 = b_2 = m$, occurring $p$ times). The bad pairs are two copies of $m$ side by side, so the $p$ copies must be mutually non-adjacent. Separating $p$ items among $N$ positions is possible exactly when

$$p \leq \left\lceil \frac{N}{2} \right\rceil$$

Sample case 1, $[3,4,4]$, has $p = 2$ against $\lceil 3/2 \rceil = 2$ — just enough, via $4\;3\;4$. Sample case 3, $[2,2]$, has $p = 2$ against $\lceil 2/2 \rceil = 1$, so `NO`.

**The maximum is unique.** Then $b_1$ occurs once and the bad pairs are $b_1$ beside any copy of $b_2$. Placing $b_1$ at an **end** leaves it a single neighbour, which only needs to be some element strictly below $b_2$. So the answer is `YES` exactly when such an element exists — that is, when the count $q$ of $b_2$-valued elements satisfies $N \geq q + 2$.

Sample case 4, $[1,2]$, has $q = 1$ and $N = 2 < 3$, so the $2$ is forced beside the $1$ — `NO`. Sample case 2, $[1,2,3,4]$, has $q = 1$ and $N = 4$, so $4\;1\;3\;2$ works.

Note $N = 2$ always fails under either branch, since the only arrangement puts the top two together.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = sorted((int(v) for v in data[pos + 1:pos + 1 + n]), reverse=True)
        pos += 1 + n
        if a[0] == a[1]:
            # Copies of the maximum must be kept mutually non-adjacent.
            p = sum(1 for v in a if v == a[0])
            ok = p <= (n + 1) // 2
        else:
            # The unique maximum sits at an end; its neighbour must be below b2.
            q = sum(1 for v in a if v == a[1])
            ok = n >= q + 2
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Two different cases, and $Z$ means different things in each.** When the two largest elements are equal, $Z = 2M$ and only an $M$-beside-$M$ adjacency is forbidden. When the maximum is unique, $Z = M + S$ with $S < M$, and $M$ must simply avoid sitting next to any copy of $S$.
- **Equal maxima**: $p$ copies of $M$ must be mutually non-adjacent, which needs $p \leq \lceil N/2 \rceil$. The third row has two $2$s in an array of two — impossible.
- **Unique maximum**: $M$ goes at an end, so it needs one neighbour strictly below $S$ — requiring at least $q + 2$ elements where $q$ counts the copies of $S$. The last row has $N = 2$ against $q + 2 = 3$, so `NO`.
- **No other adjacency can fail.** Any two non-maximum values sum to at most $2S < M + S = Z$, and $M$ with anything below $S$ is also under $Z$ — so the analysis really does reduce to these two cases.
- **$N = 2$ is always `NO`**, since the single adjacency is exactly $B_N + B_{N-1} = Z$.
- **Sorting descending makes both counts a prefix scan**, and only the top two distinct values are ever inspected.

## Dry run

| array | sorted descending | $Z$ | case | test | output |
|---|---|---:|---|---|---|
| $3,4,4$ | $4,4,3$ | 8 | equal maxima, $p = 2$ | $2 \leq \lceil 3/2 \rceil = 2$ ✓ | `YES` |
| $1,2,3,4$ | $4,3,2,1$ | 7 | unique max, $q = 1$ | $4 \geq 3$ ✓ | `YES` |
| $2,2$ | $2,2$ | 4 | equal maxima, $p = 2$ | $2 \leq 1$ ✗ | `NO` |
| $1,2$ | $2,1$ | 3 | unique max, $q = 1$ | $2 \geq 3$ ✗ | `NO` |

Row 1 works as $4, 3, 4$: sums $7$ and $7$, both under $8$.

---

Same problem grouped by topic: [../docs/greedy/CHFADJSUM.md](../docs/greedy/CHFADJSUM.md)
