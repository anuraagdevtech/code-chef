# 275. Chef Drinks Coke

> CodeChef problem code [`COKE`](https://www.codechef.com/problems/COKE) &middot; difficulty **1511** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Closed form for a drift-to-target process |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Chef went to the store in order to buy one can of coke. In the store, they offer $N$ cans of coke (numbered $1$ through $N$). For each valid $i$, the current temperature of the $i$-th can is $C_i$ and its price is $P_i$.

After buying a can of coke, Chef wants to immediately start walking home; when he arrives, he wants to immediately drink the whole can. It takes Chef $M$ minutes to get home from the store.

The ambient temperature outside is $K$. When a can of coke is outside, its temperature approaches the ambient temperature. Specifically, if its temperature is $t$ at some point in time:
- if $t \gt K+1$, then one minute later, its temperature will be $t-1$
- if $t \lt K-1$, then one minute later, its temperature will be $t+1$
- if $K-1 \le t \le K+1$, then one minute later, its temperature will be $K$

When Chef drinks coke from a can, he wants its temperature to be between $L$ and $R$ (inclusive). Find the cheapest can for which this condition is satisfied or determine that there is no such can.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains five space-separated integers $N$, $M$, $K$, $L$ and $R$.
- $N$ lines follow. For each $i$ ($1 \le i \le N$), the $i$-th of these lines contains two space-separated integers $C_i$ and $P_i$.

**Output**
For each test case, print a single line containing one integer — the price of the can Chef should buy, or $-1$ if it is impossible to buy a can such that Chef's condition is satisfied.

**Constraints**
- $1 \le T \le 1,000$
- $1 \le N \le 100$
- $1 \le M \le 100$
- $|C_i| \le 50$ for each valid $i$
- $|K| \le 50$
- $-50 \le L \le R \le 50$
- $1 \le P_i \le 10^6$ for each valid $i$

## Constraints

- $1 \le T \le 1,000$
- $1 \le N \le 100$
- $1 \le M \le 100$
- $|C_i| \le 50$ for each valid $i$
- $|K| \le 50$
- $-50 \le L \le R \le 50$
- $1 \le P_i \le 10^6$ for each valid $i$

## Sample

**Sample input**

```
2
3 2 5 4 6
1 6
2 8
8 10
3 5 10 20 30
21 20
22 22
23 23
```

**Sample output**

```
8
-1
```

<details><summary>Explanation</summary>

**Example case 1:** Chef should buy the second can (with price $8$), even though the first can is cheaper. If Chef bought the first can, its temperature would be $3$ when he got home, and that is outside the range $[4, 6]$.

**Example case 2:** No matter which can Chef buys, when he gets home, its temperature will be less than $20$, so there is no suitable can available in the store.

</details>

## Approach

Each can drifts one degree per minute toward the ambient temperature $K$, and snaps exactly onto $K$ once it is within one degree. So from a starting gap $d = |C - K|$, the can reaches $K$ after exactly $d$ minutes — $d-1$ minutes of drifting down to a gap of $1$, then one more to snap.

That gives a closed form after $M$ minutes, with no simulation:

$$\text{final} = \begin{cases} K & M \geq d \\ C - M & C > K \\ C + M & C < K \end{cases}$$

Then keep the cheapest can whose final temperature lands in $[L, R]$, or report $-1$.

The snapping rule is what makes this exact rather than asymptotic — without it, a can would approach $K$ but the last step would need care. With it, once the gap is at most $1$ the next minute closes it entirely.

Sample case 1 has ambient $5$ and $M = 2$. The can at $1$ reaches $3$ (gap $4$, only two minutes of drift) — outside $[4,6]$. The can at $2$ reaches $4$, and the can at $8$ reaches $6$; both qualify, so the cheaper one at price $8$ wins. Note the **cheapest valid** can is wanted, not the coldest or the closest.

Sample case 2 has all cans far above a cold ambient with only five minutes to cool, so none reaches the required range.

Temperatures may be negative — the constraints allow $|C_i|, |K| \leq 50$ and $L$ down to $-50$ — so no positivity may be assumed anywhere.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m, k, l, r = (int(v) for v in data[pos:pos + 5])
        pos += 5
        best = None
        for i in range(n):
            c, p = int(data[pos + 2 * i]), int(data[pos + 2 * i + 1])
            gap = abs(c - k)
            # It snaps onto k once within one degree, so k is reached at m = gap.
            if m >= gap:
                final = k
            elif c > k:
                final = c - m
            else:
                final = c + m
            if l <= final <= r and (best is None or p < best):
                best = p
        pos += 2 * n
        out.append(str(best if best is not None else -1))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The snap is what makes the timing exact.** Once the temperature is within one degree of $K$, the next minute lands it precisely on $K$ — so a can starting $g$ degrees away reaches ambient after exactly $g$ minutes, never $g-1$ or $g+1$.
- **A can already at ambient stays there** for any walk length, which the $m \geq g$ branch covers with $g = 0$.
- **Cheapest, not coldest.** The first sample has two qualifying cans; the one at price $8$ wins over the one at price $10$ even though both land inside $[L, R]$.
- **No qualifying can** → $-1$ (the second sample, where every can cools to $16$–$18$ against a window of $[20, 30]$).
- **Temperatures and the window may be negative** ($|C_i|, |K| \leq 50$ and $-50 \leq L$), so the drift direction must be chosen by comparison rather than assumed.
- **Both endpoints are inclusive**, and the first sample's winner lands exactly on $L = 4$.
- **$M \geq 1$** by the constraints, so the zero-walk case never arises in practice though the formula handles it.

## Dry run

First sample: $M = 2$ minutes, ambient $K = 5$, window $[4, 6]$.

| can | start $C$ | gap $|C - K|$ | $M \geq$ gap? | temperature on arrival | in $[4,6]$? | price |
|---:|---:|---:|:---:|---:|:---:|---:|
| 1 | 1 | 4 | no | $1 + 2 = 3$ | no | — |
| 2 | 2 | 3 | no | $2 + 2 = 4$ | yes | **8** |
| 3 | 8 | 3 | no | $8 - 2 = 6$ | yes | 10 |

Output `8`.

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#303 of 486): [../../by-rating/303-COKE.md](../../by-rating/303-COKE.md)
