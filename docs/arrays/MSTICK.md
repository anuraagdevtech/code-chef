[&larr; 433. Subarrays with length](SUBARRAYLEN.md) &middot; [Index](../../README.md) &middot; [460. Box of Chocolates &rarr;](CHCBOX.md)

# 453. Matchsticks

> CodeChef problem code [`MSTICK`](https://www.codechef.com/problems/MSTICK) &middot; difficulty **1714** &middot; time limit **3s**

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Sparse-table range min and max with end aggregates |
| **Time** | $O(N \log N + Q)$ |
| **Space** | $O(N \log N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Chef Ceil has some matchsticks in his kitchen.

**Detail of matchsticks:**

There are $N$ matchsticks in total. They are numbered from to $0$ to $N-1$ inclusive. The $i^{th}$ matchstick takes $b_{i}$ time to burn when lighted at one end, and it burns at a uniform rate.

If lighted at both ends simultaneously, the matchstick will take only half of the original time to burn down.

**Arrangement:**

He ties rear end of the all the matchsticks together at one point and the front end is kept free. The matchstick numbered $i$ is adjacent to matchstick numbered $i+1$ for all $0 \leq i \leq N-2$.

*Bodies of matchsticks do not touch each other, except at the rear end.*

**Task:**

There are $Q$ queries, in each query we ask:
If he lights the free end of all matchsticks numbered between $L$ and $R$ inclusive, what will be the time needed for all matchsticks to get completely burnt?

**Input**
- First line of input contains a single integer $N$.
- The next line contains $N$ space separated integers, the $i^{th}$ of which is $b_i$
- The next line contains a single integer $Q$
- The next $Q$ lines each contain two space separated integers - $L$ and $R$. The $i^{th}$ line represents the $i^{th}$ query.

**Output**
For each query, print the answer on a new line.

**Constraints:**
- $1 \leq N \leq 10^{5}$
- $1 \leq b_{i} \leq 10^{8}$
- $1 \leq Q \leq 10^{5}$
- $0 \leq L \leq R \leq N-1$

## Constraints

- $1 \leq N \leq 10^{5}$
- $1 \leq b_{i} \leq 10^{8}$
- $1 \leq Q \leq 10^{5}$
- $0 \leq L \leq R \leq N-1$
**Example Input 1**
```
1
5
1
0 0
```
**Example Output 1**
```
5.0
```
**Example Input 2**
```
2
3 5
1
0 1
```
**Example Output 2**
```
4.0
```
**Example Input 3**
```
18
3 4 2 1 5 7 9 7 10 5 12 3 1 1 2 1 3 2
1
4 10
```
**Example Output 3**
```
9.0
```
**Explanation**
**Test Case 3:** , in the figure above, yellow colored matches are lighted by a lighter simultaneously.
The numbers indicate the time required to burn that matchstick (if lighted at one end).
Now the first lighted matchstick will completely burn in $5$ seconds. Then it will light up all the rest matches from the rear end.
Some matches will have fire at both ends and thus after $5$ seconds, they will start burning with twice the original rate.
Thus time taken for matches to burn completely will be :
(from left to right):  $8.0$, $9.0$, $7.0$, $6.0$, $5.0$, $6.0$, $7.0$, $6.0$, $7.5$, $5.0$, $8.5$, $8.0$, $6.0$, $6.0$, $7.0$, $6.0$, $8.0$, $7.0$.
So, the answer will be $9.0$ (the maximum among these).

## Sample

**Sample 1 input**

```
1
5
1
0 0
```

**Sample 1 output**

```
5.0
```

**Sample 2 input**

```
2
3 5
1
0 1
```

**Sample 2 output**

```
4.0
```

**Sample 3 input**

```
18
3 4 2 1 5 7 9 7 10 5 12 3 1 1 2 1 3 2
1
4 10
```

**Sample 3 output**

```
9.0
```

<details><summary>Explanation</summary>

**Test Case 3:** , in the figure above, yellow colored matches are lighted by a lighter simultaneously.

The numbers indicate the time required to burn that matchstick (if lighted at one end).

Now the first lighted matchstick will completely burn in $5$ seconds. Then it will light up all the rest matches from the rear end.

Some matches will have fire at both ends and thus after $5$ seconds, they will start burning with twice the original rate.

Thus time taken for matches to burn completely will be :
(from left to right):  $8.0$, $9.0$, $7.0$, $6.0$, $5.0$, $6.0$, $7.0$, $6.0$, $7.5$, $5.0$, $8.5$, $8.0$, $6.0$, $6.0$, $7.0$, $6.0$, $8.0$, $7.0$.
So, the answer will be $9.0$ (the maximum among these).

</details>

## Approach

Lighting the free ends of $L \ldots R$ sets up two phases. The first stick to reach the shared rear is the fastest one, so the junction ignites at

$$m = \min(b_L, \ldots, b_R)$$

and from that instant **every** stick is burning from the rear.

- A **lit** stick $i$ has already consumed $m$ of its length from the front, so $b_i - m$ remains; now burning from both ends it finishes in half that, giving $m + \frac{b_i - m}{2} = \frac{b_i + m}{2}$.
- An **unlit** stick $j$ only starts at time $m$, from one end, finishing at $m + b_j$.

So the answer is the larger of the two worst cases:

$$\max\!\left(\frac{\max_{i \in [L,R]} b_i + m}{2},\ m + \max_{j \notin [L,R]} b_j\right)$$

with the second term dropped when the query covers the whole row. Note the unlit sticks can easily dominate, since they get no head start at all — in the worked example a modest unlit stick of $4$ outlasts the lit stick of $12$.

Each query needs a range minimum and maximum, so build sparse tables for both; the outside maximum is a prefix/suffix maximum, which is $O(1)$ per query. Every value is an integer or a half-integer, since $b_i + m$ is divided by $2$, so one decimal place prints the answer exactly.

The input has **no leading $T$**: it is $N$, the burn times, $Q$, then the queries. Lighting a single stick of $5$ takes $5$ seconds; lighting both of $3$ and $5$ gives $\frac{5+3}{2} = 4$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    b = [int(x) for x in data[1:1 + n]]
    levels = max(1, n.bit_length())
    lo, hi = [b[:]], [b[:]]
    step = 1
    while step * 2 <= n:
        prev_lo, prev_hi = lo[-1], hi[-1]
        lo.append([min(prev_lo[i], prev_lo[i + step])
                   for i in range(n - 2 * step + 1)])
        hi.append([max(prev_hi[i], prev_hi[i + step])
                   for i in range(n - 2 * step + 1)])
        step *= 2
    pre = [0] * (n + 1)              # max over b[0..i-1]
    for i in range(n):
        pre[i + 1] = max(pre[i], b[i])
    suf = [0] * (n + 2)              # max over b[i..n-1]
    for i in range(n - 1, -1, -1):
        suf[i] = max(suf[i + 1], b[i])

    pos = 1 + n
    q = int(data[pos])
    pos += 1
    out = []
    for _ in range(q):
        l, r = int(data[pos]), int(data[pos + 1])
        pos += 2
        k = (r - l + 1).bit_length() - 1
        shift = r - l + 1 - (1 << k)
        first = min(lo[k][l], lo[k][l + shift])
        worst_in = max(hi[k][l], hi[k][l + shift])
        best = (worst_in + first) / 2
        outside = max(pre[l], suf[r + 1])
        if outside:                  # unlit sticks only start at time `first`
            best = max(best, first + outside)
        out.append(f"{best:.1f}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N + Q)$
- **Space:** $O(N \log N)$

## Edge cases

- **The rear junction catches fire the instant the first lit stick burns through**, at time $\mathrm{first} = \min$ over the lit range — and from then on every other stick burns from both ends.
- **A lit stick finishes at $(b + \mathrm{first})/2$.** It has already burned $\mathrm{first}$ from the free end, leaving $b - \mathrm{first}$, which then halves.
- **An unlit stick finishes at $\mathrm{first} + b$**, since it only starts at the junction and burns its full length from one end — so the sticks *outside* the query range often dominate the answer.
- **The third example turns on exactly that**: the lit range alone gives $8.5$, but an unlit stick of length $4$ pushes the answer to $9.0$.
- **No sticks outside means no second term**, which the guard handles — and since $b_i \geq 1$, a maximum of $0$ really does mean the range covers everything.
- **The answer is a half-integer**, hence the single decimal place in the output.
- **There is no test-case count**: the input is $N$, the burn times, then $Q$ and the queries.
- **Sparse tables give both the range minimum and maximum in $O(1)$**, which keeps $10^5$ queries affordable alongside the prefix and suffix maxima for the outside.

## Dry run

Third example: burn times $3,4,2,1,5,7,9,7,10,5,12,3,1,1,2,1,3,2$ with the query $L = 4$, $R = 10$ (0-based).

| quantity | value |
|---|---:|
| minimum inside the range | 5 |
| maximum inside the range | 12 |
| lit sticks finish by $(12+5)/2$ | 8.5 |
| maximum outside the range | 4 |
| unlit sticks finish by $5 + 4$ | **9.0** |

Output `9.0`.

---

Same problem in rating order (#423 of 486): [../../by-rating/423-MSTICK.md](../../by-rating/423-MSTICK.md)
