# 739 &middot; Building Race

> CodeChef problem code [`BUILDINGRACE`](https://www.codechef.com/problems/BUILDINGRACE) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Comparing ratios by cross-multiplication |
| **CodeChef tags** | `Mathematics`, `Basic Math` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/basic-math/BUILDINGRACE.md](../docs/basic-math/BUILDINGRACE.md)

## Question

Two friends Chef and Chefina are currently on floors $A$ and $B$ respectively. They hear an announcement that prizes are being distributed on the ground floor and so decide to reach the ground floor as soon as possible.

Chef can climb down $X$ floors per minute while Chefina can climb down $Y$ floors per minute. Determine who will reach the ground floor first (ie. floor number 0). In case both reach the ground floor together, print `Both`.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line of each test case contains four space-separated integers $A$, $B$, $X$, and $Y$ — the current floor of Chef, the current floor of Chefina, speed of Chef and speed of Chefina in floors per minute respectively.

**Output**

For each test case, output on a new line:
- `Chef` if Chef reaches the ground floor first.
- `Chefina` if she reaches the ground floor first.
- `Both` if both reach the ground floor at the same time.

You may print each character of the string in uppercase or lowercase. For example, the strings `CHEF`, `chef`, `Chef`, and `chEF` are all considered the same.

## Constraints

- $1 \leq T \leq 2500$
- $1 \leq A, B \leq 100$
- $1 \leq X, Y \leq 10$

## Sample

**Sample input**

```
4
2 2 2 2
4 2 1 5
3 2 4 1
3 2 2 1
```

**Sample output**

```
Both
Chefina
Chef
Chef
```

<details><summary>Explanation</summary>

**Test case $1$:** Chef is on the second floor and has a speed of $2$ floors per minute. Thus, Chef takes $1$ minute to reach the ground floor. Chefina is on the second floor and and has a speed of $2$ floors per minute. Thus, Chefina takes $1$ minute to reach the ground floor. Both Chef and Chefina reach the ground floor at the same time.

**Test case $2$:** Chef is on the fourth floor and has a speed of $1$ floor per minute. Thus, Chef takes $4$ minute to reach the ground floor. Chefina is on the second floor and and has a speed of $5$ floors per minute. Thus, Chefina takes $0.4$ minutes to reach the ground floor. Chefina reaches the ground floor first.

**Test case $3$:** Chef is on the third floor and has a speed of $4$ floors per minute. Thus, Chef takes $0.75$ minutes to reach the ground floor. Chefina is on the second floor and and has a speed of $1$ floor per minute. Thus, Chefina takes $2$ minutes to reach the ground floor. Chef reaches the ground floor first.

**Test case $4$:** Chef is on the third floor and has a speed of $2$ floors per minute. Thus, Chef takes $1.5$ minutes to reach the ground floor. Chefina is on the second floor and and has a speed of $1$ floor per minute. Thus, Chefina takes $2$ minutes to reach the ground floor. Chef reaches the ground floor first.

</details>

## Approach

Chef descends $A$ floors at $X$ floors per minute and Chefina descends $B$ floors at $Y$, so their times are $A/X$ and $B/Y$ and the **smaller** time wins.

The important modelling decision is that time is **continuous**, not rounded up to whole minutes. Sample case 4 is built to expose this: $A=3, X=2$ gives Chef $1.5$ minutes while $B=2, Y=1$ gives Chefina $2$. Rounding each up to whole minutes would make both $2$ and wrongly print `Both`; the expected answer is `Chef`.

So compare the fractions directly. Both speeds are at least $1$, so multiplying through by the positive quantity $XY$ is safe and gives an exact integer comparison:

$$A \cdot Y \quad\text{versus}\quad B \cdot X$$

Chef is faster when $A \cdot Y < B \cdot X$. Note the cross-pairing — Chef's distance with Chefina's speed — and note too that the inequality points the opposite way from the speed-comparison problems: here a smaller value is better, because this is a time, not a rate.

Floats would mostly work at these bounds but make the tie in sample case 1 a matter of luck; the integer form decides equality exactly.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, x, y = map(int, data[1 + 4 * i:5 + 4 * i])
        # Times a/x and b/y, cross-multiplied. Time is not rounded to minutes.
        chef, chefina = a * y, b * x
        out.append("Chef" if chef < chefina else "Chefina" if chefina < chef else "Both")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
