[&larr; 101. Best of N Sets](101-BESTOFTENNIS.md) &middot; [Index](README.md) &middot; [103. Melt Gold &rarr;](103-MELTGOLD.md)

# 102. Mileage matters

> [`MILEAGE`](https://www.codechef.com/problems/MILEAGE) &middot; difficulty **831** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Comparing ratios by cross-multiplication |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef wants to rent a car to travel to his restaurant which is $N$ kilometers away. He can either rent a petrol car or a diesel car.

One litre of petrol costs $X$ rupees and one litre of diesel costs $Y$ rupees. Chef can travel $A$ kilometers with one litre of petrol and $B$ kilometers with one litre of diesel.

Chef can buy petrol and diesel in any amount, not necessarily integer. For example, if $X = 95$, Chef can buy half a litre of petrol by paying $95/2 = 47.5$ rupees.

Which car should the chef rent in order to **minimize** the cost of his travel?

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of each test case contains $5$ space-separated integers, $N, X, Y, A,$ and $B$ - distance that chef needs to travel, the per litre prices of petrol and diesel and the distance chef can travel using one litre of petrol and diesel respectively.

**Output**

For each test case, output on a new line `PETROL` if the cost of travel is less using petrol car, `DIESEL` if the cost of travel is less using diesel car or `ANY` if cost of travel is same in both the cases.

You may print each character of the string in either uppercase or lowercase (for example, the strings `PETrol`, `petrol`, `Petrol`, and `PETROL` will all be treated as identical).

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N,x,y,a,b \leq 100$

## Sample

**Sample input**

```
4
20 10 8 2 4
50 12 12 4 3
40 3 15 8 40
21 9 9 2 9
```

**Sample output**

```
DIESEL
PETROL
ANY
DIESEL
```

<details><summary>Explanation</summary>

**Test case $1$:** The cost of travelling by the petrol car will be $100$ rupees while that of using the diesel car will be $40$ rupees. Hence, diesel car is better.

**Test case $2$:** The cost of travelling by the petrol car will be $150$ rupees while that of using the diesel car will be $200$ rupees. Hence, petrol car is better.

**Test case $3$:** The cost of travel for petrol and diesel car will be $15$ rupees.

**Test case $4$:** The cost of travelling by the petrol car will be $94.5$ rupees while that of using the diesel car will be $21$ rupees. Hence, diesel car is better.

</details>

## Approach

Travelling $N$ kilometres at $A$ km per litre burns $N/A$ litres of petrol at $X$ rupees each, so the two costs are

$$\text{petrol} = \frac{NX}{A}, \qquad \text{diesel} = \frac{NY}{B}$$

The distance $N$ multiplies both sides equally, so it **cancels** — the cheaper fuel is the same whatever the trip length. That leaves

$$\frac{X}{A} \quad\text{versus}\quad \frac{Y}{B}$$

a comparison of cost per kilometre. Multiplying through by the positive quantity $AB$ gives an exact integer test:

$$X \cdot B \quad\text{versus}\quad Y \cdot A$$

with petrol cheaper when $XB < YA$. Note the cross-pairing: petrol's *price* with diesel's *mileage*.

The statement's remark that Chef may buy fractional litres is what licenses this. With fuel sold only in whole litres the costs would involve ceilings, $N$ would stop cancelling, and the clean ratio comparison would break.

Using floats here would be risky precisely because `ANY` is a possible answer — sample case 3 has both sides at $120$, an exact tie that float division might miss. Integer cross-multiplication decides it exactly.

Sample case 4 is a good check on the cross-pairing: $X \cdot B = 81$ against $Y \cdot A = 18$ makes diesel much cheaper, even though the two fuels cost the same per litre, because diesel goes four and a half times further.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x, y, a, b = map(int, data[1 + 5 * i:6 + 5 * i])
        # Cost is n*x/a vs n*y/b; n cancels, then cross-multiply to stay exact.
        petrol, diesel = x * b, y * a
        out.append("PETROL" if petrol < diesel else "DIESEL" if diesel < petrol else "ANY")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **A tie** ($3 \times 40 = 15 \times 8 = 120$): `ANY`, so the equality branch is needed. The sample's third row.
- **$N$ cancels out entirely.** Both costs scale with the distance, so it never affects the comparison — and multiplying it in first would needlessly inflate the operands in a fixed-width language.
- **Equal prices, different mileages** (the second row has $x = y = 12$): the mileage alone decides, so comparing prices without mileage is wrong.
- **Cross-multiplication keeps it exact**: comparing $x/a$ against $y/b$ as floats puts the tie row at risk of a rounding error.
- All values are at most $100$, so the products stay tiny.

## Dry run

| $x$ | $y$ | $a$ | $b$ | petrol $x \cdot b$ | diesel $y \cdot a$ | cheaper | output |
|---:|---:|---:|---:|---:|---:|---|---|
| 10 | 8 | 2 | 4 | 40 | 16 | diesel | `DIESEL` |
| 12 | 12 | 4 | 3 | 36 | 48 | petrol | `PETROL` |
| 3 | 15 | 8 | 40 | 120 | 120 | neither | `ANY` |
| 9 | 9 | 2 | 9 | 81 | 18 | diesel | `DIESEL` |

$N$ appears in none of the columns, because it cancels.

---

Same problem grouped by topic: [../docs/basic-math/MILEAGE.md](../docs/basic-math/MILEAGE.md)
