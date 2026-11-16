---
topic: Prefix Sums
subtopic: Factor a triplet sum into two prefix sums
time: $O(P\log P+Q\log Q+R\log R)$ per test case
space: $O(P+Q+R)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
For fixed $Y$, eligible values satisfy $X\le Y$ and $Z\le Y$. The double sum factors into $(\sum X+Y\cdot\#X)(\sum Z+Y\cdot\#Z)$.

Sort all three arrays. Sweep $B$ in ascending order while adding eligible elements of $A$ and $C$ to running counts and sums. Each array element enters at most once, so after sorting the sweep is linear.

## Edge cases

- Use non-strict comparisons, including values equal to $Y$.
- If either eligible prefix is empty, the contribution is zero.
- Repeated elements count separately.

## Dry run

For the sample `Y=5`, eligible `A=[1,2,3]` and `C=[4,5]`. Their factors are `6+3*5=21` and `9+2*5=19`; product `399`.
