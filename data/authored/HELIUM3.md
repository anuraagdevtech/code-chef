---
topic: Basic Math
subtopic: Comparing two products
time: $O(1)$ per test case
space: $O(1)$
---
Strip the story away and two quantities remain. What the government *demands* is $A$ units of power every year for $B$ years, so the requirement is $A \cdot B$ units in total. What the group can *supply* is $X$ grams of Helium-3 at $Y$ units per gram, so the supply is $X \cdot Y$ units.

Funding is granted when supply meets demand:

$$X \cdot Y \geq A \cdot B$$

The whole difficulty is in the modelling, not the arithmetic. Note that the yearly structure is a red herring — because the requirement is a flat $A$ units per year with no constraint on *when* the fuel is consumed, the $B$ years collapse into a single total. If the problem had capped annual output, the per-year structure would have mattered.

"At least" again means the comparison is `>=`, so exactly meeting the quota is a `Yes`. Sample case 3 is the tight one: demand $2 \times 18 = 36$, supply $9 \times 4 = 36$, which funds the project.

With all four values bounded by $1000$ the products stay under $10^6$, so they fit comfortably in any integer type — and in Python the question never arises.

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
