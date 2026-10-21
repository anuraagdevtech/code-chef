---
topic: Basic Math
subtopic: Two independent supply checks
time: $O(1)$ per test case
space: $O(1)$
---
Chef needs $x_r$ food and $y_r$ water **per day** for $D$ days, so the totals required are $x_r \cdot D$ and $y_r \cdot D$. He survives only if **both** stocks cover their demand:

$$x \geq x_r \cdot D \quad\text{and}\quad y \geq y_r \cdot D$$

The two resources are independent and non-substitutable — surplus food does not offset a water shortfall — so this is an `and`, and each must be checked on its own. That is the same asymmetry as the shoes problem, and the reason a combined test such as $x + y \geq (x_r + y_r)D$ is wrong: it would let an abundance of one supply mask the absence of the other.

Sample case 2 is built exactly on that. Food is fine ($4 \geq 1$) but water fails ($2 < 3$), so the answer is `NO` even though the totals $6$ against $4$ would pass a pooled check.

Sample case 3 fails on food instead, with $4 < 4 \times 2 = 8$, and also shows that $D$ multiplies the daily rate rather than being compared against the stock directly.

The comparisons are inclusive — finishing with exactly zero supplies left still counts as reaching the shore, as sample case 1 nearly illustrates. All values are small, so there is nothing to watch numerically.

## Edge cases

- **Exactly enough of a resource** ($x = x_r \cdot D$): still survivable, so the comparisons are non-strict.
- **One resource short while the other is plentiful** (the second row has ample water but too little food): `NO`. Food and water are **not interchangeable**, so both conditions must hold — an `or`, or a check on the combined total, passes this row wrongly.
- **$D = 1$**: a single day's requirement.
- **Both short** (the third row): `NO`, failing on the first test alone.
- The two checks are independent, which is why they are ANDed rather than summed.

## Dry run

| $x$ | $y$ | $x_r$ | $y_r$ | $D$ | need $x_r D$ | need $y_r D$ | both met? | output |
|---:|---:|---:|---:|---:|---:|---:|:---:|---|
| 4 | 2 | 1 | 1 | 1 | 1 | 1 | yes | `YES` |
| 4 | 2 | 1 | 3 | 1 | 1 | 3 | no (second) | `NO` |
| 4 | 2 | 4 | 2 | 2 | 8 | 4 | no (both) | `NO` |
