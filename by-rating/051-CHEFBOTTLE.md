# 051. Chef and Water Bottles

> [`CHEFBOTTLE`](https://www.codechef.com/problems/CHEFBOTTLE) &middot; difficulty **662** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Two competing limits |
| **CodeChef tags** | `Basic Programming Concepts`, `Mathematics`, `Basic Math`, `Inbuilt functions`, `Integer Division` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef has $N$ empty bottles where each bottle has a capacity of $X$ litres.
There is a water tank in Chefland having $K$ litres of water. Chef wants to fill the empty bottles using the water in the tank.

Assuming that Chef does not spill any water while filling the bottles, find out the **maximum** number of bottles Chef can fill completely.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, three integers $N, X,$ and $K$.

**Output**

For each test case, output in a single line answer, the **maximum** number of bottles Chef can fill completely.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N, X \leq 10^5$
- $0 \leq K \leq 10^5$

## Sample

**Sample input**

```
3
5 2 8
10 5 4
3 1 4
```

**Sample output**

```
4
0
3
```

<details><summary>Explanation</summary>

**Test Case $1$:** The amount of water in the tank is $8$ litres. The capacity of each bottle is $2$ litres. Hence, $4$ water bottles can be filled completely.

**Test Case $2$:** The amount of water in the tank is $4$ litres. The capacity of each bottle is $5$ litres. Hence, no water bottle can be filled completely.

**Test Case $3$:** The amount of water in the tank is $4$ litres. The capacity of each bottle is $1$ litre. Chef has $3$ bottles available. He can fill all these bottles completely using $3$ litres of water.

</details>

## Approach

Two separate things cap how many bottles Chef can fill, and the answer is whichever binds first.

- **Water:** the tank holds $K$ litres and each full bottle takes $X$, so the water allows $\lfloor K/X \rfloor$ bottles. Partially filled bottles do not count, so this floors.
- **Bottles:** he only owns $N$ of them, however much water is left over.

The answer is therefore

$$\min\left(N,\; \left\lfloor \frac{K}{X} \right\rfloor\right)$$

Taking the minimum of independent caps is the pattern here, and both halves are load-bearing. Sample case 3 is capped by bottles — $4$ litres into $1$-litre bottles could fill four, but Chef has only $3$. Sample case 1 is capped by water: five bottles available, but $8$ litres at $2$ litres each fills only four. Dropping either term fails one of these.

Note that $K$ may be $0$ while $N$ and $X$ are at least $1$, so the answer can legitimately be zero and the division never has a zero divisor. Sample case 2 shows the water running out immediately, with $4$ litres unable to fill even one $5$-litre bottle.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x, k = map(int, data[1 + 3 * i:4 + 3 * i])
        # Limited both by the water available and by the bottles owned.
        out.append(str(min(n, k // x)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/basic-math/CHEFBOTTLE.md](../docs/basic-math/CHEFBOTTLE.md)
