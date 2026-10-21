# 563 &middot; Sugarcane Juice Business

> CodeChef problem code [`SUGARCANE`](https://www.codechef.com/problems/SUGARCANE) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Percentages that cancel |
| **CodeChef tags** | `Mathematics`, `Basic Math` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/basic-math/SUGARCANE.md](../docs/basic-math/SUGARCANE.md)

## Question

While Alice was drinking sugarcane juice, she started wondering about the following facts:
- The juicer sells each glass of sugarcane juice for $50$ coins.
- He spends $20\%$ of his total income on buying sugarcane.
- He spends $20\%$ of his total income on buying salt and mint leaves.
- He spends $30\%$ of his total income on shop rent.

Alice wonders, what is the juicer's profit (in coins) when he sells $N$ glasses of sugarcane juice?

**Input**

- The first line of input will contain an integer $T$ — the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains an integer $N$, as described in the problem statement.

**Output**

For each test case, output on a new line the juicer's profit when he sells $N$ glasses of juice.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^6$

## Sample

**Sample input**

```
4
2
4
5
10
```

**Sample output**

```
30
60
75
150
```

<details><summary>Explanation</summary>

**Test case $1$**: The total income is $50\times 2 = 100$ coins. The juicer spends $20$ coins on sugarcane, $20$ coins on  salt and mint leaves and $30$ coins on rent. Thus, the profit is $100-(20+20+30) = 30$ coins.

**Test case $2$**: The total income is $50\times 4 = 200$ coins. The juicer spends $40$ coins on sugarcane, $40$ coins on  salt and mint leaves and $60$ coins on rent. Thus, the profit is $200-(40+40+60) = 60$ coins.

**Test case $3$**: The total income is $50\times 5 = 250$ coins. The juicer spends $50$ coins on sugarcane, $50$ coins on  salt and mint leaves and $75$ coins on rent. Thus, the profit is $250-(50+50+75) = 75$ coins.

**Test case $4$**: The total income is $50\times 10 = 500$ coins. The juicer spends $100$ coins on sugarcane, $100$ coins on  salt and mint leaves and $150$ coins on rent. Thus, the profit is $500-(100+100+150) = 150$ coins.

</details>

## Approach

Selling $N$ glasses at $50$ coins each gives a total income of $50N$. The three costs are all quoted as percentages **of that same income**, which is what makes the problem collapse:

$$20\% + 20\% + 30\% = 70\%$$

So $70\%$ of income is spent and $30\%$ remains as profit:

$$\text{profit} = 0.30 \times 50N = 15N$$

The entire problem is the single expression `15 * n`. The useful habit is to sum the percentage *rates* before touching the money, rather than computing three separate costs and subtracting them one at a time — fewer operations, and no intermediate rounding to worry about.

That rounding point matters here. Because $30\%$ of $50$ is exactly $15$, the profit is always a whole number of coins and integer arithmetic is exact. Had the rate produced a fraction of a coin, the problem would have had to say how to round, and computing `0.3 * 50 * n` in floating point could then drift for large $N$. Sticking to the pre-simplified integer coefficient avoids the issue entirely.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        # Income 50n, costs 20 + 20 + 30 = 70%, so profit is 30% of 50n.
        out.append(str(15 * n))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
