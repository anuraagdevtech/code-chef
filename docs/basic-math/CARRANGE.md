[&larr; 137. Chef and Pairing Slippers](CHEFSLP.md) &middot; [Index](../../README.md) &middot; [145.  Am I Lucky! &rarr;](SPCP4.md)

# 144. Car Range

> CodeChef problem code [`CARRANGE`](https://www.codechef.com/problems/CARRANGE) &middot; difficulty **938** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Reading an off-by-one from the statement |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

The *fuel economy* of a car is the distance which it can travel on one litre of fuel.

The base fuel economy (i.e, its fuel economy when there is only one person - the driver - in the car) of a certain car is $M$ kilometres per litre. It was also observed that every extra passenger in the car *decreases* the fuel economy by $1$ kilometre per litre.

$P$ people want to take this car for a journey. They know that the car currently has $V$ litres of fuel in its tank.

What is the **maximum** distance this car can travel under the given conditions, assuming that all $P$ people always stay in the car and no refuelling can be done?

**Note** that among the $P$ people is also a driver, i.e, there are exactly $P$ people in the car.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line of input, containing three space-separated integers $P, M$, and $V$ - the number of people, base fuel economy, and amount of fuel present in the car, respectively.

**Output**

For each test case, output a single line containing one integer - the maximum distance that the car can travel.

## Constraints

- $1 \leq T \leq 3 \cdot 10^4$
- $1 \leq P \leq 5$
- $6 \leq M \leq 56$
- $1 \leq V \leq 100$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
3
5 10 20
1 6 10
4 6 1
```

**Sample output**

```
120
60
3
```

<details><summary>Explanation</summary>

**Test Case $1$:**
There are $5$ people in the car, and its base fuel economy is $10$. Thus, its effective fuel economy is $10 - 4 = 6$, since there are $4$ people present other than the driver.
There are $20$ litres of fuel in the car, so the maximum distance that can be travelled is $6\cdot 20 = 120$.

**Test Case $2$:**
The effective fuel economy is $6$, and the maximum distance that can be travelled is $6\cdot 10 = 60$.

**Test Case $3$:**
The effective fuel economy is $3$, and the maximum distance that can be travelled is $3\cdot 1 = 3$.

</details>

## Approach

The base economy $M$ already accounts for the driver, so only the **extra** passengers reduce it. With $P$ people in the car there are $P - 1$ extras, each costing $1$ km/l:

$$\text{economy} = M - (P - 1) = M - P + 1$$

and the distance is that economy multiplied by the fuel available:

$$V \cdot (M - P + 1)$$

The whole problem is the $-1$. Reading the penalty as $P$ rather than $P - 1$ gives a plausible-looking formula that fails every sample, and the statement goes out of its way to warn about it — both by defining the base case as "only the driver" and by the closing note that the $P$ people *include* the driver.

Sample case 2 is the one that isolates it: a single occupant means no extras at all, so the economy is the full $M = 6$ and the answer is $60$. A formula using $M - P$ would give $50$.

Sample case 1 shows the penalty biting hardest: five people drop a $10$ km/l car to $6$ km/l, giving $120$ km from $20$ litres.

The constraints keep the economy positive — $M \geq 6$ while $P \leq 5$, so $M - P + 1 \geq 2$ — meaning no clamping is needed and the distance is never zero or negative.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        p, m, v = map(int, data[1 + 3 * i:4 + 3 * i])
        # The driver is already priced into m, so only p - 1 extras cost.
        out.append(str(v * (m - p + 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **$P = 1$** (just the driver): the answer is $V \cdot M$, the full mileage. The $+1$ in $M - P + 1$ is what makes this come out right — without it the row gives $50$ instead of $60$.
- **The driver is already priced into $M$**, so only the $P - 1$ extra passengers reduce the range. That off-by-one is the entire problem, and it is read from the statement rather than derived.
- **$P \leq 5$ while $M \geq 6$**, so $M - P + 1 \geq 2$ and the answer is always positive — there is no clamp to worry about.
- **Largest input** ($V = 100$, $M = 56$, $P = 1$): $5600$.

## Dry run

| $P$ | $M$ | $V$ | effective mileage $M - P + 1$ | range $V \cdot {\cdot}$ | output |
|---:|---:|---:|---:|---:|---|
| 5 | 10 | 20 | 6 | 120 | `120` |
| 1 | 6 | 10 | 6 | 60 | `60` |
| 4 | 6 | 1 | 3 | 3 | `3` |

Row 2 is the driver-only case that pins the $+1$.

> CodeChef tags: `Mathematics`, `Algorithms`, `Constructive`

---

Same problem in rating order (#148 of 486): [../../by-rating/148-CARRANGE.md](../../by-rating/148-CARRANGE.md)
