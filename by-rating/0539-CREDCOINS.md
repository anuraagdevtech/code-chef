# 539 &middot; CRED Coins

> CodeChef problem code [`CREDCOINS`](https://www.codechef.com/problems/CREDCOINS) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Floor division |
| **CodeChef tags** | `Mathematics`, `Basic Math`, `Integer Division`, `Arithmetic` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/basic-math/CREDCOINS.md](../docs/basic-math/CREDCOINS.md)

## Question

For each bill you pay using CRED, you earn $X$ CRED coins.
At CodeChef store, each bag is worth $100$ CRED coins.

Chef pays $Y$ number of bills using CRED. Find the **maximum** number of bags he can get from the CodeChef store.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers $X$ and $Y$.

**Output**

For each test case, output in a single line - the **maximum** number of bags Chef can get from the CodeChef store.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X,Y \leq 1000$

**Subtasks**

- **Subtask 1 (100 points):** Original constraints.

## Sample

**Sample input**

```
3
10 10
20 4
70 7
```

**Sample output**

```
1
0
4
```

<details><summary>Explanation</summary>

**Test Case $1$:** For each bill payment, one receives $10$ CRED coins. Chef pays $10$ bills using CRED. Thus, he receives $100$ CRED coins. Chef can get $1$ bag from the CodeChef store using these coins.

**Test Case $2$:**  For each bill payment, one receives $20$ CRED coins. Chef pays $4$ bills using CRED. Thus, he receives $80$ CRED coins. Chef cannot get any bag from the CodeChef store using these coins.

**Test Case $3$:** For each bill payment, one receives $70$ CRED coins. Chef pays $7$ bills using CRED. Thus, he receives $490$ CRED coins. Chef can get at most $4$ bags from the CodeChef store using these coins.

</details>

## Approach

Chef earns $X$ coins per bill and pays $Y$ bills, so he ends up with $X \cdot Y$ coins. Each bag costs $100$ coins, and coins cannot be split across a partial purchase, so the number of bags is the floor:

$$\left\lfloor \frac{X \cdot Y}{100} \right\rfloor$$

This is the mirror image of a ceiling-division problem: here the leftover coins are simply wasted rather than forcing an extra unit, so we round **down**. Recognising which way a remainder should push is the whole skill being drilled — "how many whole things can I afford" floors, "how many containers do I need" ceils.

Python's `//` is exactly floor division on non-negative integers, so `x * y // 100` is the entire computation. Avoid `int(x * y / 100)`, which routes through a float and would start misbehaving on larger inputs.

Sample case 2 shows the rounding clearly: $20 \times 4 = 80$ coins, which is not enough for even one bag, so the answer is $0$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Total coins earned, floored against the 100-coin bag price.
        out.append(str(x * y // 100))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
