# 681 &middot; Blackjack

> CodeChef problem code [`BLACKJACK`](https://www.codechef.com/problems/BLACKJACK) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Solving for the unknown, then range checking |
| **CodeChef tags** | `Mathematics`, `Basic Math` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/basic-math/BLACKJACK.md](../docs/basic-math/BLACKJACK.md)

## Question

Chef is playing a variant of Blackjack, where $3$ numbers are drawn and each number lies between $1$ and $10$ (with both $1$ and $10$ inclusive). Chef wins the game when the sum of these $3$ numbers is exactly $21$.

Given the first two numbers $A$ and $B$, that have been drawn by Chef, what should be $3$-rd number that should be drawn by the Chef in order to win the game?

Note that it is possible that Chef cannot win the game, no matter what is the $3$-rd number. In such cases, report $-1$ as the answer.

**Input**

- The first line will contain an integer $T$ - number of test cases. Then the test cases follow.
- The first and only line of each test case contains two integers $A$ and $B$ - the first and second number drawn by the Chef.

**Output**

For each testcase, output the $3$-rd number that should be drawn by the Chef in order to win the game. Output $-1$ if it is not possible for the Chef to win the game.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq A, B \leq 10$

## Sample

**Sample input**

```
3
1 10
1 5
4 9
```

**Sample output**

```
10
-1
8
```

<details><summary>Explanation</summary>

**Test case $1$**: The first two numbers are $1$ and $10$. If the third number will be $10$, the resulting sum will be $1 + 10 + 10 = 21$. So Chef will win the game if the third number is $10$.

**Test case $2$**: The first two numbers are $1$ and $5$. There is no number between $1$ and $10$, that can make the resulting sum $21$. Hence, the answer will be $-1$ in this test case.

</details>

## Approach

The three drawn numbers must total $21$, so the required third card is forced:

$$C = 21 - A - B$$

There is nothing to search. The only question is whether that value is a card that can actually be drawn, which the problem fixes at $1 \leq C \leq 10$. If it falls outside, no draw can win and the answer is $-1$.

This two-step shape — **solve for the unknown, then validate it against the domain** — is worth naming, because the validation is where the problem actually lives. Computing $C$ is arithmetic; remembering that not every integer is a legal card is the part that is easy to skip.

Both ends of the range can fail in principle. With $A$ and $B$ each at most $10$ the sum is at most $20$, so $C \geq 1$ always holds and only the upper bound bites in practice. Sample case 2 shows it: $A = 1, B = 5$ needs a $15$, which no card can supply, so `-1`.

Sample case 1 sits exactly on the boundary at $C = 10$, which is legal — the check must be `<= 10`, not `< 10`.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        c = 21 - a - b
        # The third card is forced; it just has to be a card that exists.
        out.append(str(c) if 1 <= c <= 10 else "-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
