---
topic: Combinatorics
subtopic: Leaves forced by depth, choosing which slots of each level are leaves
time: $O(N + \log \sum a_i)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Every internal vertex splits its weight into two equal halves, so a vertex at depth $d$ carries exactly $S / 2^d$, where $S$ is the total weight. In particular a leaf of weight $w$ can only sit at the depth where $S / 2^d = w$: the multiset of weights fixes how many leaves each level has.

Walk down level by level. Start with one slot (the root) carrying weight $S$. If the current level has `slots` positions and `leaves` of the given weights are equal to the current weight, choose which positions become leaves in $\binom{\text{slots}}{\text{leaves}}$ ways; the left and right child are distinguishable, so different choices give different mobiles. The remaining positions are internal and produce $2 (\text{slots} - \text{leaves})$ slots of half the weight.

The count is the product of these binomials. It is 0 if there are more leaves than slots at some level, if a weight that still has to be split is odd, if slots remain when the weights are used up, or if weights remain when no slot is left. Since every open slot needs at least one leaf below it, having more slots than remaining weights is also an immediate 0, which bounds the loop.

## Edge cases

- A single weight is one leaf: answer 1.
- Weights that are not $S / 2^d$ for any $d$ can never be placed and leave unused leaves: answer 0.
- An odd weight cannot be halved while internal slots remain.
- Equal weights are interchangeable; only positions are chosen, which is exactly what the binomial counts.

## Dry run

Weights `5 5 10 20`, total 40.

| depth | weight | slots | leaves | ways | next slots |
|---:|---:|---:|---:|---:|---:|
| 0 | 40 | 1 | 0 | 1 | 2 |
| 1 | 20 | 2 | 1 | 2 | 2 |
| 2 | 10 | 2 | 1 | 2 | 2 |
| 3 | 5 | 2 | 2 | 1 | 0 |

Answer $1 \cdot 2 \cdot 2 \cdot 1 = 4$.
