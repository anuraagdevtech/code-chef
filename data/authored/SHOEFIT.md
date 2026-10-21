---
topic: Conditionals & Case Work
subtopic: Presence of both values in a small collection
time: $O(1)$ per test case
space: $O(1)$
---
Three shoes, each a left ($0$) or a right ($1$). Going out needs **one of each**, so the question is whether both values appear among $A, B, C$.

The neat way to test this on $0/1$ values is to look at the sum $s = A + B + C$:

- $s = 0$ means all three are left shoes — no right shoe, so no pair.
- $s = 3$ means all three are right shoes — no left shoe, so no pair.
- $s = 1$ or $s = 2$ means a mix, so a pair exists.

Hence the answer is $1$ exactly when $0 < s < 3$.

The pigeonhole reasoning is worth seeing: with three items and two categories, having at least one of each is the same as *not* having all three in one category. Those are the only two bad cases, and both are detected by the sum hitting an extreme.

Equivalently, `len({a, b, c}) == 2` asks the question directly — a set of $0/1$ values has size $2$ precisely when both appear. Either formulation beats enumerating the eight possibilities.

Sample case 1 is all-left and fails; cases 2 and 3 each have a mix and succeed. Note that having *two* right shoes and one left is fine — only one pair is needed, and the spare is simply unused.

## Edge cases

- **All left** (sum $0$) and **all right** (sum $3$) are the only two failures — a wearable pair needs at least one of each.
- **Exactly one of a kind** (sum $1$ or $2$): a pair exists.
- Collapsing to the sum turns all eight patterns into one range test $0 < s < 3$, which is harder to get wrong than enumerating the cases.
- $T \leq 8$ is exactly the number of distinct inputs, so the tests may well be all eight patterns.

## Dry run

| $A$ | $B$ | $C$ | sum | $0 < s < 3$? | output |
|---:|---:|---:|---:|:---:|---|
| 0 | 0 | 0 | 0 | no | `0` |
| 0 | 1 | 1 | 2 | yes | `1` |
| 1 | 0 | 1 | 2 | yes | `1` |

The unseen all-ones case would give sum $3$ and output `0`.
