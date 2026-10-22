[&larr; 12. Expert Setter](EXPERT.md) &middot; [Index](../../README.md) &middot; [14. Sugarcane Juice Business &rarr;](SUGARCANE.md)

# 13. Chef and NextGen

> CodeChef problem code [`HELIUM3`](https://www.codechef.com/problems/HELIUM3) &middot; difficulty **562** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Comparing two products |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Chef is currently working for a secret research group called NEXTGEN.
While the rest of the world is still in search of a way to utilize Helium-3 as a fuel, NEXTGEN scientists have been able to achieve 2 major milestones:
1. Finding a way to make a nuclear reactor that will be able to utilize Helium-3 as a fuel
2. Obtaining every bit of Helium-3 from the moon's surface

Moving forward, the project requires some government funding for completion, which comes under one condition:
to prove its worth, the project should power Chefland by generating at least $A$ units of power each year for the next $B$ years.

Help Chef determine whether the group will get funded assuming that the moon has $X$ grams of Helium-3 and $1$ gram of Helium-3 can provide $Y$ units of power.

**Input**

- The first line of input contains an integer $T$, the number of testcases. The description of $T$ test cases follows.
- Each test case consists of a single line of input, containing four space-separated integers $A, B, X, Y$ respectively.

**Output**

For each test case print on a single line the answer — `Yes` if NEXTGEN satisfies the government's minimum requirements for funding and `No` otherwise.

You may print each character of the answer string in either uppercase or lowercase (for example, the strings `"yEs"`, `"yes"`, `"Yes"` and `"YES"` will all be treated as identical).

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq A, B, X, Y, \leq 1000$

**Subtasks**

**Subtask #1 (100 points):** Original constraints

## Sample

**Sample input**

```
4
1 2 3 4
4 3 2 1
2 18 9 4
1 100 2 49
```

**Sample output**

```
Yes
No
Yes
No
```

<details><summary>Explanation</summary>

**Test case $1$:** Chefland requires $A = 1$ units of power for the next $B = 2$ years. In total, the moon must be capable of providing $A \cdot B = 2$ units of power. There are in total $X = 3$ grams of Helium-3 on the moon which is capable of providing $X \cdot Y = 12$ units of power. $12 \gt 2$, so the project satisfies the minimum requirements for funding. Thus, the answer is `Yes`.

**Test case $2$:** The total amount of power needed by Chefland is $A \cdot B = 12$, whereas the total that can be provided by the Helium-3 present on the moon is $X \cdot Y = 2$, which is insufficient to receive funding, so the answer is `No`.

**Test case $3$:** The total amount of power needed by Chefland is $A \cdot B = 2 \cdot 18 = 36$, and the total that can be provided by the Helium-3 present on the moon is $X \cdot Y = 9 \cdot 4 = 36$, which is sufficient to receive funding, so the answer is `Yes`.

**Test case $4$:** The total amount of power needed by Chefland is $A \cdot B = 1 \cdot 100 = 100$, and the total that can be provided by the Helium-3 present on the moon is $X \cdot Y = 2 \cdot 49 = 98$, which is insufficient to receive funding, so the answer is `No`.

</details>

## Approach

Strip the story away and two quantities remain. What the government *demands* is $A$ units of power every year for $B$ years, so the requirement is $A \cdot B$ units in total. What the group can *supply* is $X$ grams of Helium-3 at $Y$ units per gram, so the supply is $X \cdot Y$ units.

Funding is granted when supply meets demand:

$$X \cdot Y \geq A \cdot B$$

The whole difficulty is in the modelling, not the arithmetic. Note that the yearly structure is a red herring — because the requirement is a flat $A$ units per year with no constraint on *when* the fuel is consumed, the $B$ years collapse into a single total. If the problem had capped annual output, the per-year structure would have mattered.

"At least" again means the comparison is `>=`, so exactly meeting the quota is a `Yes`. Sample case 3 is the tight one: demand $2 \times 18 = 36$, supply $9 \times 4 = 36$, which funds the project.

With all four values bounded by $1000$ the products stay under $10^6$, so they fit comfortably in any integer type — and in Python the question never arises.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, x, y = map(int, data[1 + 4 * i:5 + 4 * i])
        # Total demand a * b against total supply x * y.
        out.append("Yes" if x * y >= a * b else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Supply exactly meets demand** ($A{=}2, B{=}18$ against $X{=}9, Y{=}4$: both sides $36$): the requirement is "at least", so `Yes`. The comparison is non-strict and the sample checks it.
- **Supply just short** ($1 \times 100 = 100$ needed against $2 \times 49 = 98$): `No` by two units.
- **Only the products matter**, not the shapes: $2 \times 18$ and $9 \times 4$ are quite different pairs with the same total, which is why comparing $A$ to $X$ and $B$ to $Y$ separately is wrong.
- **Largest inputs** ($1000 \times 1000$ on each side): $10^6$, comfortably inside fixed-width range, so no overflow care is needed here.

## Dry run

| $A$ | $B$ | $X$ | $Y$ | demand $AB$ | supply $XY$ | supply $\geq$ demand | output |
|---:|---:|---:|---:|---:|---:|:---:|---|
| 1 | 2 | 3 | 4 | 2 | 12 | yes | `Yes` |
| 4 | 3 | 2 | 1 | 12 | 2 | no | `No` |
| 2 | 18 | 9 | 4 | 36 | 36 | yes (equality) | `Yes` |
| 1 | 100 | 2 | 49 | 100 | 98 | no | `No` |

Row 3 is the exact tie, row 4 the near miss.

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#20 of 486): [../../by-rating/020-HELIUM3.md](../../by-rating/020-HELIUM3.md)
