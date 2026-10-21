# 130. Chef and Battery 

> [`FIFTYPE`](https://www.codechef.com/problems/FIFTYPE) &middot; difficulty **901** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Brute Force |
| **Technique** | Searching one variable of a linear Diophantine equation |
| **CodeChef tags** | `Basic Programming Concepts`, `Loops` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case — the search is bounded by a small constant |
| **Space** | $O(1)$ |

## Question

Chef's phone has a battery level of $N$ percent.
Each minute:
- If the phone is on charging, the battery level **increases** by $2\%$.
- Otherwise, the battery level **decreases** by $3\%$.

Find the **minimum** time in which Chef can make the battery level reach **exactly** $50\%$.
Note that the battery level should always lie in the range $0$ to $100$ (both included).

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of single lines of input $N$ - the current battery level of Chef's phone.

**Output**

For each test case, output on a new line the **minimum** time in which Chef can make the battery level reach **exactly** $50\%$.

## Constraints

- $1 \leq T \leq 1000$
- $0 \leq N \leq 100$

## Sample

**Sample input**

```
4
51
50
23
0
```

**Sample output**

```
2
0
16
25
```

<details><summary>Explanation</summary>

**Test case $1$:** Chef can use his phone for $1$ minute. Thus, the battery drops to $48\%$.
Then, he can charge it for $1$ minute. Thus, the battery reaches exactly $50\%$.

**Test case $2$:** The battery level is already at $50\%$.

**Test case $3$:** Chef can charge the battery for $15$ minutes and use it for $1$ minute.
Thus, after $16$ minutes, the battery will be $50\%$ .

**Test case $4$:** Chef can charge the battery for $25$ minutes to reach the battery level of $50\%$.

</details>

## Approach

Charging adds $2$ and discharging subtracts $3$, so with $a$ charging minutes and $b$ discharging minutes the battery changes by $2a - 3b$. Reaching exactly $50\%$ from $N$ requires

$$2a - 3b = 50 - N$$

with $a, b \geq 0$, minimising $a + b$. This is a linear Diophantine equation in two unknowns.

Fixing $b$ determines $a$, so the search runs over $b$ alone: for each candidate, $a = \frac{(50 - N) + 3b}{2}$ is valid when the numerator is non-negative and even. Since $N \leq 100$, the gap never exceeds $50$ and a small bound on $b$ suffices — the loop below runs to $200$, far past any optimum, and still costs nothing.

Working out the structure by hand is instructive. Let $d = 50 - N$.

- $d$ **even and positive**: pure charging, $d/2$ minutes. Sample case 4 ($N = 0$) gives $25$.
- $d$ **odd**: parity blocks pure charging, since $2a$ is always even. One discharge flips the parity, costing $1 + \frac{d+3}{2}$ minutes in total. Sample case 3 ($N = 23$, $d = 27$) gives $1 + 15 = 16$.
- $d$ **negative**: the battery must come down, which only discharging does, but $-3$ steps may overshoot and need charging to correct. Sample case 1 ($N = 51$, $d = -1$) needs one of each: $51 \to 48 \to 50$, two minutes.

That last case is the one that defeats a naive "just divide the gap" solution. Searching over $b$ handles all three shapes uniformly without case analysis, which is why it is preferred here over deriving each branch.

The requirement that the level stay within $[0, 100]$ never forces extra moves at these bounds, since the charging and discharging minutes can be interleaved to keep the battery inside the range.

## Solution

```python
import sys


def minutes(n: int) -> int:
    d = 50 - n
    best = None
    # Fixing the number of discharges determines the number of charges.
    for b in range(0, 201):
        num = d + 3 * b
        if num < 0 or num % 2:
            continue
        a = num // 2
        total = a + b
        if best is None or total < best:
            best = total
    return best


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = [str(minutes(int(data[1 + i]))) for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Already at the target** ($N = 50$): zero minutes, with no charging or discharging.
- **Above the target** ($N = 51$): the shortfall is negative, so some discharging is forced before the arithmetic works out — the `num < 0` guard is what skips the impossible choices.
- **Parity forces the pairing.** The charge step moves the level by $2$ and the discharge by $3$, so for a given shortfall the number of discharges must match its parity; $N = 23$ has an odd shortfall of $27$ and needs an odd count of discharges, landing on $1$ discharge and $15$ charges.
- **Empty battery** ($N = 0$): $25$ minutes of pure charging.
- The search bound of $201$ is generous — the shortfall is at most $50$, so the optimum always uses a small number of discharges and the loop never runs out.

## Dry run

| $N$ | shortfall $50 - N$ | discharges $b$ | $\text{shortfall} + 3b$ | charges $a$ | total | output |
|---:|---:|---:|---:|---:|---:|---|
| 51 | $-1$ | 1 | 2 | 1 | 2 | `2` |
| 50 | 0 | 0 | 0 | 0 | 0 | `0` |
| 23 | 27 | 1 | 30 | 15 | 16 | `16` |
| 0 | 50 | 0 | 50 | 25 | 25 | `25` |

For $N = 23$, $b = 0$ leaves the odd value $27$, which cannot be halved — hence $b = 1$.

---

Same problem grouped by topic: [../docs/brute-force/FIFTYPE.md](../docs/brute-force/FIFTYPE.md)
