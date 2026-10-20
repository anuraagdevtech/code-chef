# 64. Speed Limit Test

> CodeChef problem code [`SPEEDTEST`](https://www.codechef.com/problems/SPEEDTEST) &middot; difficulty **718** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Comparing ratios by cross-multiplication |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Alice is driving from her home to her office which is $A$ kilometers away and will take her $X$ hours to reach.
Bob is driving from his home to his office which is $B$ kilometers away and will take him $Y$ hours to reach.

Determine who is driving faster, else, if they are both driving at the same speed print `EQUAL`.

**Input**

- The first line will contain $T$, the number of test cases. Then the test cases follow.
- Each test case consists of a single line of input, containing four integers $A,X,B,$ and $Y$, the distances and and the times taken by Alice and Bob respectively.

**Output**

For each test case, if Alice is faster, print `ALICE`. Else if Bob is faster, print `BOB`. If both are equal, print `EQUAL`.

You may print each character of the string in uppercase or lowercase (for example, the strings `equal`, `equAL`, `EquAl`, and `EQUAL` will all be treated as identical).

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq A,X,B,Y \leq 1000$

## Sample

**Sample input**

```
3
20 6 20 5
10 3 20 6
9 1 1 1
```

**Sample output**

```
Bob
Equal
Alice
```

<details><summary>Explanation</summary>

**Test case $1$:** Since Bob travels the distance between his office and house in $5$ hours, whereas Alice travels the same distance of $20$ kms in $6$ hours, `BOB` is faster.

**Test case $2$:** Since Alice travels the distance of $10$ km between her office and house in $3$ hours and Bob travels a distance of $20$ km in $6$ hours, they have equal speeds.

**Test case $3$:** Since Alice travels the distance of $9$ km between her office and house in $1$ hour and Bob travels only a distance of $1$ km in the same time, `ALICE` is faster.

</details>

## Approach

Speed is distance over time, so the comparison is

$$\frac{A}{X} \quad\text{versus}\quad \frac{B}{Y}$$

Computing the two quotients as floats would work at these bounds, but it is the fragile route: `10 / 3` and `20 / 6` are mathematically equal yet can differ in the last bit, which would turn sample case 2 from `EQUAL` into a spurious winner. Equality tests on floats are exactly where this bites.

Multiply out instead. Both $X$ and $Y$ are at least $1$, so multiplying both sides by the positive quantity $XY$ preserves the direction and gives

$$A \cdot Y \quad\text{versus}\quad B \cdot X$$

a comparison of two integers, exact by construction. Note the cross: Alice's distance pairs with **Bob's** time. Multiplying $A \cdot X$ against $B \cdot Y$ is the natural typo and compares something meaningless.

Checking sample case 2: $10 \cdot 6 = 60$ and $20 \cdot 3 = 60$, equal, so `EQUAL` — decided exactly, with no tolerance to tune.

Three outcomes need three branches; collapsing the tie into one of the inequalities would silently report a winner for equal speeds.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, x, b, y = map(int, data[1 + 4 * i:5 + 4 * i])
        # a/x vs b/y, cross-multiplied so the comparison stays exact.
        alice, bob = a * y, b * x
        out.append("ALICE" if alice > bob else "BOB" if bob > alice else "EQUAL")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Mathematics`
