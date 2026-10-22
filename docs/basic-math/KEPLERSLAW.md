[&larr; 145.  Am I Lucky!](SPCP4.md) &middot; [Index](../../README.md) &middot; [157. Richie Rich &rarr;](CHFRICH.md)

# 154. Keplers Law

> CodeChef problem code [`KEPLERSLAW`](https://www.codechef.com/problems/KEPLERSLAW) &middot; difficulty **992** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Testing proportionality by cross-multiplication |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Kepler’s Law states that the planets move around the sun in elliptical orbits with the sun at one focus. Kepler's 3rd law is The Law of Periods, according to which:

- The **square of the time period** of the planet is directly proportional to the **cube of the semimajor axis** of its orbit.

You are given the Time periods ($T_1, T_2$) and Semimajor Axes ($R_1, R_2$) of two planets orbiting the same star.

Please determine if the Law of Periods is satisfied or not, i.e, if the [constant of proportionality](https://en.wikipedia.org/wiki/Proportionality_(mathematics)) of both planets is the same.

Print `"Yes"` (without quotes) if the law is satisfied, else print `"No"`.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists a single line of input, containing four space-separated integers $T_1, T_2, R_1, R_2$.

**Output**

For each test case, output a single line containing one string — `"Yes"` or `"No"` (without quotes); the answer to the problem.

You may print each character of the answer in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq T_1,T_2 \leq 10$
- $1 \leq R_1,R_2 \leq 10$

**Subtasks**

**Subtask 1(100 points):** Original constraints

## Sample

**Sample input**

```
3
1 1 1 1
1 2 3 4
1 8 2 8
```

**Sample output**

```
Yes
No
Yes
```

<details><summary>Explanation</summary>

- **Test Case $1$**: $1^2/1^3 = 1^2/1^3$
- **Test Case $2$**: $1^2/3^3 \neq 2^2/4^3$
- **Test Case $3$**: $1^2/2^3 =  8^2/8^3$

</details>

## Approach

Kepler's third law says $T^2 \propto R^3$, so the constant $T^2/R^3$ must match for both planets:

$$\frac{T_1^2}{R_1^3} = \frac{T_2^2}{R_2^3}$$

Cross-multiplying by the positive quantity $R_1^3 R_2^3$ turns this into an exact integer identity:

$$T_1^2 \cdot R_2^3 = T_2^2 \cdot R_1^3$$

This is the right way to test any proportionality. Computing the two ratios as floats and comparing with `==` is unreliable — the quotients are rarely representable exactly, and sample case 3 ($1, 8, 2, 8$) would hinge on whether $1/8$ and $64/512$ happen to round identically. The integer form decides it exactly: $1 \cdot 512 = 512$ and $64 \cdot 8 = 512$.

Note the **cross** again: planet 1's period pairs with planet 2's axis. Writing $T_1^2 R_1^3 = T_2^2 R_2^3$ tests a different and meaningless relation.

The exponents must also be the right way round — period **squared** against axis **cubed**. Swapping them would pass sample case 1, where every value is $1$, but fail the others.

With all inputs at most $10$, the products stay below $10^5$, so there is no magnitude concern even in a fixed-width language.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        t1, t2, r1, r2 = map(int, data[1 + 4 * i:5 + 4 * i])
        # T^2 / R^3 equal for both, cross-multiplied to stay in integers.
        out.append("Yes" if t1 * t1 * r2 ** 3 == t2 * t2 * r1 ** 3 else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Identical pairs** ($1\,1\,1\,1$): trivially `Yes`.
- **The exponents must be the right way round** — $T$ squared against $R$ cubed. Swapping them changes the third row's answer from `Yes` to `No`, since $1 \cdot 8^2 = 64$ against $8^3 \cdot 2^2 = 2048$.
- **Cross-multiplication keeps the exact case exact.** Comparing $T^2/R^3$ as floats risks a false negative precisely on the third row, where the equality holds exactly ($512 = 512$).
- **No overflow**: the cubes reach $1000$ and the squares $100$, so the products stay around $10^5$.

## Dry run

| $T_1$ | $T_2$ | $R_1$ | $R_2$ | $T_1^2 R_2^3$ | $T_2^2 R_1^3$ | output |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 1 | 1 | 1 | 1 | 1 | `Yes` |
| 1 | 2 | 3 | 4 | 64 | 108 | `No` |
| 1 | 8 | 2 | 8 | 512 | 512 | `Yes` |

Row 3 is the exact equality that floating point would endanger.

---

Same problem in rating order (#162 of 486): [../../by-rating/162-KEPLERSLAW.md](../../by-rating/162-KEPLERSLAW.md)
