[&larr; 158. Vaccine Dates ](VDATES.md) &middot; [Index](../../README.md) &middot; [373. Say No To Drugs &rarr;](NODRUGS.md)

# 163. Problem Category

> CodeChef problem code [`PROBCAT`](https://www.codechef.com/problems/PROBCAT) &middot; difficulty **860** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Ordered threshold ladder |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

Chef prepared a problem. The admin has rated this problem for $x$ points.

A problem is called :

1) Easy if $1 \leq x \lt 100$

2) Medium if $100 \leq x \lt 200$

3) Hard if $200 \leq x \leq 300$

Find the category to which Chef’s problem belongs.

**Input**

- The first line contains $T$ denoting the number of test cases. Then the test cases follow.
- The first and only line of each test case contains a single integer $x$.

**Output**

For each test case, output in a single line the category of Chef's problem, i.e whether it is an `Easy`, `Medium` or `Hard` problem. **The output is case sensitive.**

## Constraints

- $1 \leq T \leq 50$
- $1 \leq x \leq 300$

**Subtasks**

- **Subtask 1 (100 points):** Original constraints

## Sample

**Sample input**

```
3
50
172
201
```

**Sample output**

```
Easy
Medium
Hard
```

<details><summary>Explanation</summary>

**Test case $1$**: The problem with rating $x = 50$ is an easy problem as $1 \leq 50 \lt 100$.

**Test case $2$**: The problem with rating $x = 172$ is a medium problem as $100 \leq 172 \lt 200$.

**Test case $3$**: The problem with rating $x = 201$ is a hard problem as $200 \leq 201 \leq 300$.

</details>

## Approach

Three bands, read straight from the statement:

- `Easy` for $1 \leq x < 100$
- `Medium` for $100 \leq x < 200$
- `Hard` for $200 \leq x \leq 300$

Testing from the bottom up lets each branch assume the earlier ones failed, so only the upper bound of each band needs stating.

The boundaries are **exclusive at the top** of the first two bands and inclusive at the bottom — so $x = 100$ is `Medium`, not `Easy`, and $x = 200$ is `Hard`. Sample case 3 checks the upper boundary with $x = 201$, but $100$ and $200$ themselves are not in the samples, so they are worth testing by hand before submitting.

The statement says explicitly that **the output is case sensitive**, which is unusual in this set — most neighbouring problems accept any casing. So `Easy` must be written with exactly that capitalisation, not `EASY` or `easy`.

The constraint $1 \leq x \leq 300$ means every input falls into one of the three bands, so the final `else` is genuinely exhaustive and no fallback is needed.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x = int(data[1 + i])
        # Output is case sensitive, so the capitalisation here matters.
        out.append("Easy" if x < 100 else "Medium" if x < 200 else "Hard")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **$x = 100$ exactly**: `Medium`, not `Easy`, because the first test is the strict $x < 100$. An off-by-one here misplaces the whole boundary.
- **$x = 199$ then $x = 200$**: `Medium` then `Hard`, the second boundary.
- **Extremes** ($x = 1$ and $x = 300$): `Easy` and `Hard`.
- **Output is case sensitive**: `Easy`, not `EASY` or `easy`.
- **Band order matters.** The tests run ascending with the first match winning, so each band's lower edge is implied by the branch above it; independent `if`s would let a value match more than one.

## Dry run

| $x$ | first matching test | output |
|---:|---|---|
| 50 | $x < 100$ | `Easy` |
| 172 | $x < 200$ | `Medium` |
| 201 | neither | `Hard` |

The untested boundaries behave as $100 \to$ `Medium` and $200 \to$ `Hard`.

---

Same problem in rating order (#111 of 486): [../../by-rating/111-PROBCAT.md](../../by-rating/111-PROBCAT.md)
