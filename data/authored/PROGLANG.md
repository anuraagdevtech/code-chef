---
topic: Sets
subtopic: Subset containment
time: $O(1)$ per test case
space: $O(1)$
---
Chef needs a language providing **both** features $A$ and $B$. Each candidate language offers exactly two features, so the test is whether the required pair is contained in the offered pair:

$$\{A, B\} \subseteq \{A_1, B_1\} \quad\text{or}\quad \{A, B\} \subseteq \{A_2, B_2\}$$

Since both sides have exactly two distinct elements, containment here is the same as set equality — but writing it as `<=` (subset) states the requirement directly and would still be right if a language offered more features.

Using sets removes the ordering question entirely, which is the main trap. The features may be listed in either order, so a positional comparison of $A$ against $A_1$ and $B$ against $B_1$ fails. Sample case 1 is built on that: the required $\{1, 2\}$ is offered as $A_1 = 2, B_1 = 1$ — the same pair, reversed — and the answer is $1$.

The first language is checked first, which matters only if both qualified; the constraint that $A_1, B_1, A_2, B_2$ are **pairwise distinct** means the two languages share no feature at all, so at most one can ever match and the order is immaterial.

Sample case 3 is the zero case: $\{1,2\}$ is split across the two languages, each holding one required feature, so neither suffices and the answer is $0$. That pairwise-distinct guarantee is precisely what makes such a split possible.

## Edge cases

- **Features may be listed in either order**: the first row offers $\{2, 1\}$ against a need of $\{1, 2\}$, so the comparison must be on sets rather than positions.
- **Neither language works** (the third row): the answer is $0$.
- **The two languages share no feature.** Since $A_1, B_1, A_2, B_2$ are pairwise distinct, their feature sets are disjoint, so at most one language can supply both needs — which is why checking the first and then the second with an `elif` cannot mask a valid answer.
- **$A \neq B$ is guaranteed**, so the requirement always has exactly two distinct features.

## Dry run

| needed | language 1 | language 2 | subset of 1? | subset of 2? | output |
|---|---|---|:---:|:---:|---|
| $\{1,2\}$ | $\{2,1\}$ | $\{3,4\}$ | yes | — | `1` |
| $\{3,4\}$ | $\{2,1\}$ | $\{4,3\}$ | no | yes | `2` |
| $\{1,2\}$ | $\{1,3\}$ | $\{2,4\}$ | no | no | `0` |

Row 3 has each needed feature available, but split across the two languages.
