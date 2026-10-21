---
topic: Arrays
subtopic: Maximum over a filtered subset
time: $O(N)$ per test case
space: $O(1)$
---
Chef wants the highest-rated movie that **fits**, so the answer is

$$\max \{\, R_i : S_i \leq X \,\}$$

a single pass keeping a running maximum over the qualifying entries only.

The guarantee that $X \geq S_i$ for at least one $i$ means the filtered set is never empty, so no sentinel or "no answer" case is needed — but it is worth noticing the guarantee rather than assuming it, since a running maximum seeded at $0$ would silently return $0$ on an empty set.

The trap is sorting. It is tempting to sort by rating and scan for the first that fits, or to sort by size — both work, but both are $O(N \log N)$ for no benefit, and with $N$ up to $5 \times 10^4$ the single $O(N)$ pass is simply better. Nothing here needs order.

Equally, this is **not** a knapsack: Chef picks exactly one movie, so sizes do not combine and there is no packing decision. The word "single best" in the statement is what rules that out.

Sample case 3 is the discriminating one. The movies are $(1, 51)$, $(3, 100)$ and $(2, 50)$ with $X = 2$. The best rating overall is $100$, but that movie needs $3$ GB and does not fit; among those that do, the best is $51$. A solution ignoring the size filter would answer $100$.

Note the inclusive comparison: a movie of exactly $X$ GB fits.

## Edge cases

- **A movie needing exactly $X$ GB still fits** (the third row has a $2$ GB movie with $X = 2$): the comparison is non-strict.
- **The highest-rated movie may not fit.** That same row has a rating of $100$ on a $3$ GB movie, which is excluded — taking the global maximum answers $100$ instead of $51$. This is the whole point of the problem.
- **All movies fit** (the second row): the answer is the plain maximum.
- **$X \geq S_i$ for at least one $i$ is guaranteed**, so there is always a candidate and the initial best of $0$ is never printed.
- **$N$ up to $5 \times 10^4$ with ten test cases**, so a single pass per case is wanted rather than sorting.

## Dry run

Third sample: $X = 2$, movies $(S, R) = (1,51), (3,100), (2,50)$.

| size | rating | fits ($S \leq 2$)? | best so far |
|---:|---:|:---:|---:|
| 1 | 51 | yes | 51 |
| 3 | 100 | **no** | 51 |
| 2 | 50 | yes | 51 |

Output `51` — the $100$ is unreachable.
