# 224. Bella ciao

> CodeChef problem code [`CHFHEIST`](https://www.codechef.com/problems/CHFHEIST) &middot; difficulty **1410** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Summing an arithmetic progression |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Read problem statements in [Vietnamese](https://www.codechef.com/download/translated/JUNE21/vietnamese/CHFHEIST.pdf),

Chef is planning a heist in the reserve bank of Chefland. They are planning to hijack the bank for $D$ days and print the money. The initial rate of printing the currency is $P$ dollars per day and they increase the production by $Q$ dollars after every interval of $d$ days. For example, after $d$ days the rate is $P+Q$ dollars per day, and after $2d$ days the rate is $P+2Q$ dollars per day, and so on. Output the amount of money they will be able to print in the given period.

**Input**
- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, four integers $D, d, P, Q$.

**Output**
For each test case, output in a single line the answer to the problem.

**Constraints**
- $1 \leq T \leq 10^5$
- $1 \leq d \leq D \leq 10^6$
- $1 \leq P, Q \leq 10^6$

**Subtasks**
**Subtask #1 (15 points):** $d \leq D \leq 100$

**Subtask #2 (85 points):** original constraints

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq d \leq D \leq 10^6$
- $1 \leq P, Q \leq 10^6$

## Sample

**Sample input**

```
3
2 1 1 1
3 2 1 1
5 2 1 2
```

**Sample output**

```
3
4
13
```

<details><summary>Explanation</summary>

**Test Case $1$:**
- On the first day, the rate of production is $1$ dollar per day so $1$ dollar is printed on the first day.
- On the second day, the rate of production is $1 + 1 = 2$ dollars per day so $2$ dollars are printed on the second day.
- The total amount of money printed in $2$ days is $1 + 2 = 3$ dollars.

**Test Case $2$:**
- For the first two days, the rate of production is $1$ dollar per day so $1 \cdot 2 = 2$ dollars are printed on the first two days.
- On the third day, the rate of production is $1 + 1 = 2$ dollars per day so $2$ dollars are printed on the third day.
- The total amount of money printed in $3$ days is $2 + 2 = 4$ dollars.

**Test Case $3$:**
- For the first two days, the rate of production is $1$ dollar per day so $1 \cdot 2 = 2$ dollars are printed on the first two days.
- On the next two days, the rate of production is $1 + 2 = 3$ dollars per day so $3 \cdot 2 = 6$ dollars are printed on the next two days.
- On the last day, the rate of production is $3 + 2 = 5$ dollars per day so $5$ dollars are printed on the last day.
- The total amount of money printed in $5$ days is $2 + 6 + 5 = 13$ dollars.

</details>

## Approach

The printing rate steps up every $d$ days: $P$ for the first block, $P + Q$ for the second, $P + 2Q$ for the third, and so on. Over $D$ days there are

$$f = \left\lfloor \frac{D}{d} \right\rfloor \text{ complete blocks, plus } r = D \bmod d \text{ leftover days}$$

Each complete block $k$ (counting from $0$) runs for $d$ days at rate $P + kQ$, and the leftover days run at the next rate $P + fQ$. So

$$\text{total} = d\sum_{k=0}^{f-1}(P + kQ) \;+\; r\,(P + fQ)
= d\left(fP + Q\frac{f(f-1)}{2}\right) + r\,(P + fQ)$$

using the arithmetic-series sum $0 + 1 + \cdots + (f-1) = \frac{f(f-1)}{2}$.

The closed form matters: with $D$ up to $10^6$ and $T$ up to $10^5$, looping day by day would be $10^{11}$ steps. The formula is $O(1)$.

The partial block is the easy thing to drop. Sample case 2 has $D = 3, d = 2$: one full block of two days at rate $1$, then a single leftover day at the **raised** rate $2$, totalling $4$. Ignoring the remainder would give $2$; charging it at the old rate would give $3$.

Sample case 3 is the same shape with a bigger step: two blocks at rates $1$ and $3$ over two days each ($2 + 6 = 8$), plus one day at rate $5$, giving $13$.

The result reaches roughly $10^{15}$, so this **needs 64-bit arithmetic** outside Python — a point the problem's subtask split quietly signals.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        big_d, d, p, q = map(int, data[1 + 4 * i:5 + 4 * i])
        full, rem = divmod(big_d, d)
        # Complete blocks form an arithmetic series; the leftover days run at
        # the next rate up.
        total = d * (full * p + q * full * (full - 1) // 2)
        total += rem * (p + full * q)
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **$D$ not a multiple of $d$** (the second and third rows): the leftover days run at the *next* rate up, $p + \mathrm{full} \cdot q$, which the trailing term supplies — dropping it loses those days entirely.
- **$D$ an exact multiple of $d$** (the first row): the remainder is $0$ and the trailing term vanishes on its own.
- **$d > D$**: there are no complete blocks, so the series term is $0$ and the whole period runs at the base rate $p$, giving $D \cdot p$.
- **$q$ is added per *block*, not per day**, which is why the series is over $\mathrm{full}$ terms and each is multiplied by $d$.
- **The triangular factor must be integer-divided after multiplying**, `full * (full - 1) // 2`, to stay exact.
- **Magnitudes**: with $D \leq 10^6$, $d = 1$, $p, q \leq 10^6$ the total reaches about $5 \cdot 10^{17}$ — past 32-bit and close to the 64-bit ceiling, though native in Python.

## Dry run

Third sample: $D = 5$, $d = 2$, $p = 1$, $q = 2$. Two complete blocks, one day left over.

| days | rate | earned |
|---|---:|---:|
| 1–2 | $p = 1$ | 2 |
| 3–4 | $p + q = 3$ | 6 |
| 5 | $p + 2q = 5$ | 5 |

Total `13`. The formula gives $2(2 \cdot 1 + 2 \cdot 1) + 1 \cdot 5 = 8 + 5$.

> CodeChef tags: `Mathematics`, `Sequences and Progression`

---

Same problem in rating order (#230 of 486): [../../by-rating/230-CHFHEIST.md](../../by-rating/230-CHFHEIST.md)
