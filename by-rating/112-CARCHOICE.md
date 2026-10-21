# 112. Car Choice

> [`CARCHOICE`](https://www.codechef.com/problems/CARCHOICE) &middot; difficulty **861** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Comparing ratios by cross-multiplication |
| **CodeChef tags** | `Basic Programming Concepts`, `Mathematics`, `Basic Math`, `Conditional Statements`, `Arithmetic` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef is planning to buy a new car for his birthday. After a long search, he is left with $2$ choices:

- **Car 1**: Runs on diesel with a fuel economy of $x_1$ km/l
- **Car 2**: Runs on petrol with a fuel economy of $x_2$ km/l

Chef also knows that
- the current price of diesel is $y_1$ rupees per litre
- the current price of petrol is $y_2$ rupees per litre

Assuming that both cars cost the same and that the price of fuel remains constant, which car will minimize Chef's expenses?

Print your answer as a single integer in the following format

- If it is better to choose **Car 1**, print $-1$
- If both the cars will result in the same expenses, print $0$
- If it is better to choose **Car 2**, print $1$

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line containing $4$ space-separated integers — $x_1, x_2, y_1, y_2$.

**Output**

For each test case, output in a single line the answer as explained earlier.

## Constraints

- $1 \leq T \leq 10000$
- $1 \leq x_1,x_2,y_1,y_2 \leq 50$

## Sample

**Sample input**

```
3
10 5 3 20
7 2 7 2
1 5 3 2
```

**Sample output**

```
-1
0
1
```

<details><summary>Explanation</summary>

**Test Case $1$**: The cost of driving Car 1 is $\frac{3}{10} = 0.3$ rs/km, and the cost of driving Car 2 is $\frac{20}{5} = 4$ rs/km. Therefore, Car 1 is cheaper to drive, so the output is $-1$.

**Test Case $2$**: The cost of driving Car 1 is $1$ rs/km, and the cost of driving Car 2 is also $1$ rs/km. Both cars offer the same economy, so the output is $0$.

**Test Case $3$**: The cost of driving Car 1 is $3$ rs/km and the cost of driving Car 2 is $0.4$ rs/km. Therefore, Car 2 is cheaper to drive, so the output is $1$.

</details>

## Approach

A car with fuel economy $x$ km/l burning fuel at $y$ rupees per litre costs $y/x$ rupees per kilometre. Since both cars cost the same to buy and the distance driven is the same either way, the cheaper car is simply the one with the lower cost per kilometre:

$$\frac{y_1}{x_1} \quad\text{versus}\quad \frac{y_2}{x_2}$$

Cross-multiplying by the positive quantity $x_1 x_2$ gives an exact integer comparison:

$$y_1 \cdot x_2 \quad\text{versus}\quad y_2 \cdot x_1$$

with Car 1 better when $y_1 x_2 < y_2 x_1$.

Note the direction of the ratio. Fuel economy sits in the **denominator** — higher km/l is better, while higher rupees/litre is worse — so the comparison is not simply "cheaper fuel wins" or "better mileage wins". Sample case 1 makes this vivid: diesel at $3$ rupees against petrol at $20$, with Car 1 also managing twice the mileage, so Car 1 wins on both counts. Sample case 3 inverts it, with Car 2 winning despite being the petrol car.

Sample case 2 is the exact tie at $1$ rupee per km each, which is why integer arithmetic matters — float division could miss the equality and print $-1$ or $1$ instead of $0$.

The output encoding is unusual and worth re-reading: $-1$ for Car 1, $0$ for a tie, $1$ for Car 2.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x1, x2, y1, y2 = map(int, data[1 + 4 * i:5 + 4 * i])
        # Cost per km is y/x; cross-multiply to keep it exact.
        car1, car2 = y1 * x2, y2 * x1
        out.append("-1" if car1 < car2 else "1" if car2 < car1 else "0")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/basic-math/CARCHOICE.md](../docs/basic-math/CARCHOICE.md)
