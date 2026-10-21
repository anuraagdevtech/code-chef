# 888 &middot; Secret Recipe

> CodeChef problem code [`CHEFRUN`](https://www.codechef.com/problems/CHEFRUN) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Comparing ratios by cross-multiplication |
| **CodeChef tags** | `Special`, `Physics` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/basic-math/CHEFRUN.md](../docs/basic-math/CHEFRUN.md)

## Question

Chef and his competitor Kefa own two restaurants located at a straight road. The position of Chef's restaurant is $X_1$, the position of Kefa's restaurant is $X_2$.

Chef and Kefa found out at the same time that a bottle with a secret recipe is located on the road between their restaurants. The position of the bottle is $X_3$.

The cooks immediately started to run to the bottle. Chef runs with speed $V_1$, Kefa with speed $V_2$.

Your task is to figure out who reaches the bottle first and gets the secret recipe (of course, it is possible that both cooks reach the bottle at the same time).

### Input
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains five space-separated integers $X_1$, $X_2$, $X_3$, $V_1$ and $V_2$.

### Output
For each test case, print a single line containing the string `"Chef"` if Chef reaches the bottle first, `"Kefa"` if Kefa reaches the bottle first or `"Draw"` if Chef and Kefa reach the bottle at the same time (without quotes).

### Constraints
- $1 \le T \le 10^5$
- $|X_1|, |X_2|, |X_3| \le 10^5$
- $X_1 \lt X_3 \lt X_2$
- $1 \le V_1 \le 10^5$
- $1 \le V_2 \le 10^5$

## Constraints

- $1 \le T \le 10^5$
- $|X_1|, |X_2|, |X_3| \le 10^5$
- $X_1 \lt X_3 \lt X_2$
- $1 \le V_1 \le 10^5$
- $1 \le V_2 \le 10^5$

## Sample

**Sample input**

```
3
1 3 2 1 2
1 5 2 1 2
1 5 3 2 2
```

**Sample output**

```
Kefa
Chef
Draw
```

<details><summary>Explanation</summary>

**Example case 1.** Chef and Kefa are on the same distance from the bottle, but Kefa has speed $2$, while Chef has speed $1$.

</details>

## Approach

The constraint $X_1 < X_3 < X_2$ places the bottle strictly between the two restaurants, so each cook runs directly toward it and the distances are

$$d_{\text{Chef}} = X_3 - X_1, \qquad d_{\text{Kefa}} = X_2 - X_3$$

both automatically positive — no absolute values needed, which is exactly what that ordering constraint buys.

Comparing arrival times $d_1/V_1$ against $d_2/V_2$ and cross-multiplying by the positive quantity $V_1 V_2$ gives the exact integer test

$$d_1 \cdot V_2 \quad\text{versus}\quad d_2 \cdot V_1$$

with Chef first when $d_1 V_2 < d_2 V_1$. Note the cross: Chef's distance pairs with **Kefa's** speed.

Float division would be the risky route precisely because `Draw` is a possible answer — sample case 3 is an exact tie, and a float comparison could miss it. Integers decide equality cleanly.

The magnitudes are worth a glance for a C solution: coordinates reach $10^5$ in absolute value so a distance can reach $2 \times 10^5$, and multiplying by a speed up to $10^5$ gives $2 \times 10^{10}$ — past the 32-bit limit and needing a 64-bit type. Python handles it without comment.

Sample case 2 shows the shorter distance winning despite the slower speed: Chef covers $1$ unit at speed $1$ in one second, while Kefa needs $1.5$ seconds for $3$ units at speed $2$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x1, x2, x3, v1, v2 = map(int, data[1 + 5 * i:6 + 5 * i])
        # x1 < x3 < x2 is guaranteed, so both distances are positive.
        chef, kefa = (x3 - x1) * v2, (x2 - x3) * v1
        out.append("Chef" if chef < kefa else "Kefa" if kefa < chef else "Draw")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
