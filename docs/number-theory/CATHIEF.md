# 288. Catch the Thief

> CodeChef problem code [`CATHIEF`](https://www.codechef.com/problems/CATHIEF) &middot; difficulty **1550** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | An invariant from step size and parity |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

A policeman wants to catch a thief. Both the policeman and the thief can only move on a line on integer coordinates between $0$ and $N$ (inclusive).

Initially, the policeman is at a coordinate $x$ and the thief is at a coordinate $y$. During each second, each of them must move to the left or right (not necessarily both in the same direction) by distance $\textbf{exactly}$ equal to $K$. No one may go to the left of the coordinate $0$ or to the right of $N$. Both the policeman and the thief move simultaneously and they cannot meet while moving, only at the end of each second.

Will the policeman be able to catch the thief if they both move optimally? The thief is caught as soon as the policeman and thief meet at the same position at the same time.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains four space-separated integers $x$, $y$, $K$ and $N$.

**Output**
For each test case, print a single line containing the string `"Yes"` if the thief can be caught or `"No"` if the thief cannot be caught (without quotes).

**Constraints**
- $1 \le T \le 1,000$
- $1 \le N \le 10^9$
- $1 \le K \le N$
- $0 \le x, y \le N$
- $x \neq y$

## Constraints

- $1 \le T \le 1,000$
- $1 \le N \le 10^9$
- $1 \le K \le N$
- $0 \le x, y \le N$
- $x \neq y$

## Sample

**Sample input**

```
5
0 1 1 1
1 4 1 5
4 2 1 7
3 7 2 10
8 2 3 15
```

**Sample output**

```
No
No
Yes
Yes
Yes
```

<details><summary>Explanation</summary>

**Example case 1:** The policeman is at $0$ and the thief is at $1$. After the $1$-st second, the policeman is at $1$ and the thief is at $0$. After the next second, the policeman is again at $0$ and the thief at $1$. They cannot end up at the same coordinate.

</details>

## Approach

Both move **exactly** $K$ every second, so after $t$ seconds the policeman stands at $x + K p$ and the thief at $y + K q$, where $p$ and $q$ are sums of $t$ terms of $\pm 1$ — hence both have the **same parity as $t$**.

Meeting requires $x + Kp = y + Kq$, that is

$$x - y = K\,(q - p)$$

Two conditions fall out. First, $K$ must divide $x - y$. Second, $q - p$ is a difference of two integers of equal parity, so it is **even** — meaning $(x-y)/K$ must be even too.

Together:

$$K \mid (x - y) \quad\text{and}\quad \frac{x - y}{K} \text{ is even}$$

Both are invariants no evasion can break, so when either fails the answer is `No` regardless of play. When both hold, the policeman can close the gap and pin the thief against a wall, so the answer is `Yes`.

The parity half is the easily missed one, and the samples target it. Case 1 has adjacent positions with $K = 1$: the gap is $1$, odd, so they swap places forever and never coincide. Case 2 has a gap of $3$ with $K = 1$ — divisible, but odd — also `No`. Case 3 has a gap of $2$, even, giving `Yes`.

Cases 4 and 5 show the divisibility doing work: gaps of $4$ and $6$ against steps of $2$ and $3$ give quotients $2$ and $2$, both even.

Note the simultaneous-move rule means they can pass *through* each other without meeting, which is exactly what the parity obstruction encodes.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, k, n = map(int, data[1 + 4 * i:5 + 4 * i])
        d = abs(x - y)
        # Both displacements share the parity of t, so their difference is
        # even - hence the gap must be an even multiple of k.
        ok = d % k == 0 and (d // k) % 2 == 0
        out.append("Yes" if ok else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Both displacements share the parity of the elapsed time.** After $t$ seconds each has moved $\pm K$ exactly $t$ times, so each net displacement is $K$ times an integer congruent to $t$ modulo $2$ — making their difference an *even* multiple of $K$.
- **So the gap must be divisible by $K$ and the quotient must be even.** Both halves are needed: the second row has $|x-y| = 3$, divisible by $K = 1$ but with an odd quotient, so `No`.
- **A divisibility failure alone** is enough to answer `No` when $K > 1$ and the gap is not a multiple.
- **An odd gap with $K = 1$ is always hopeless** (the first row), since the quotient is the gap itself.
- **The board bounds do not matter.** $K \leq N$ is guaranteed, so both can always oscillate within $[0, N]$ without being forced into a corner — which is why $N$ is read and never used.
- **They may not meet mid-move**, only at the end of a second, which is exactly what the parity argument captures: positions are only ever compared at integer times.
- **$x \neq y$ is guaranteed**, so the gap is at least $1$ and the trivial "already caught" case does not arise.

## Dry run

| $x$ | $y$ | gap | $K$ | gap $\bmod K$ | quotient | quotient even? | output |
|---:|---:|---:|---:|---:|---:|:---:|---|
| 0 | 1 | 1 | 1 | 0 | 1 | no | `No` |
| 1 | 4 | 3 | 1 | 0 | 3 | no | `No` |
| 4 | 2 | 2 | 1 | 0 | 2 | **yes** | `Yes` |
| 3 | 7 | 4 | 2 | 0 | 2 | **yes** | `Yes` |
| 8 | 2 | 6 | 3 | 0 | 2 | **yes** | `Yes` |

In row 3 both step right then the policeman steps right again while the thief steps left: positions $4 \to 5 \to 4$ and $2 \to 3 \to 4$.

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#325 of 486): [../../by-rating/325-CATHIEF.md](../../by-rating/325-CATHIEF.md)
