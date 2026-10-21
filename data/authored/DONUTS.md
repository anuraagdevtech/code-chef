---
topic: Greedy
subtopic: Trading sacrificed chains against links needed
time: $O(M \log M)$ per test case
space: $O(M)$
---
Each cut doughnut becomes one **link**, and joining $p$ separate pieces into a single chain takes $p - 1$ links. So the cost depends on how many pieces survive, and the only lever is how many chains are consumed entirely for link material.

Suppose the $d$ **smallest** chains are sacrificed, supplying $\mathrm{pre}[d] = A_1 + \cdots + A_d$ cuts (sorted ascending). Then $M - d$ pieces remain and need $M - d - 1$ links. Whichever of the two numbers is larger is the number of cuts:

$$\text{cost}(d) = \max\bigl(\mathrm{pre}[d],\ M - d - 1\bigr)$$

If the sacrifice falls short, the shortfall is taken a doughnut at a time from the end of a surviving chain, which shortens it without splitting it. If the sacrifice overshoots, the surplus cuts are made later, from inside the partly-assembled chain. Sacrificing the smallest chains is optimal because $\mathrm{pre}[d]$ is what we pay and it is minimised by taking the cheapest chains first.

As $d$ grows, $\mathrm{pre}[d]$ rises and $M - d - 1$ falls, so the cost is a V shape and the minimum sits at their crossover; with $M \leq 2 \times 10^4$ a direct scan over $d$ is simplest.

The two samples land on either side of that crossover. For chains $4, 3, 4$ nothing is worth sacrificing: $d = 0$ needs $M - 1 = 2$ links, taken from the end of a chain, while sacrificing the $3$-chain would already cost $3$. For chains $3, 2, 1$ the singleton is nearly free — sacrificing it costs $1$ cut and leaves just two pieces, needing exactly $1$ link, so the answer is $1$ rather than $2$.

Note $N$ reaches $2 \times 10^9$ but never enters the computation; only the chain sizes and their count matter.

## Edge cases

- **$M$ chains need $M-1$ links**, and each cut doughnut supplies exactly one link — so cutting $M-1$ doughnuts from any chains always works. That is the baseline the search starts from.
- **Sacrificing a whole small chain can be cheaper.** Cutting every doughnut of the $d$ smallest chains both supplies links and removes those chains from the count, leaving $M-d$ pieces needing $M-d-1$ links.
- **The cost is the larger of the two numbers**, `max(used, m - d - 1)`: if the sacrificed doughnuts exceed the links needed, the surplus cuts are still cuts; if they fall short, more doughnuts must be cut from surviving chains.
- **A chain of length $1$ is the ideal sacrifice** — one cut turns it into a link and removes a chain, a net gain. The second sample's answer of $1$ rests entirely on this.
- **$d = 0$ (no sacrifice) must stay a candidate**, which the initial `best = m - 1` provides; the first sample never improves on it.
- **$M = 1$** needs no links at all, and `best = 0` falls straight out.
- **Sorting ascending is what makes the prefix sums the cheapest sacrifices** for each $d$.

## Dry run

Second sample: $N = 6$ in chains $3, 2, 1$, sorted to $1, 2, 3$.

| $d$ | chains sacrificed | links gained | chains left | links still needed | cost |
|---:|---|---:|---:|---:|---:|
| 0 | — | 0 | 3 | 2 | 2 |
| 1 | the $1$ | 1 | 2 | 1 | **1** |
| 2 | the $1$ and $2$ | 3 | 1 | 0 | 3 |

Output `1`: cut the lone doughnut and use it to join the chains of $2$ and $3$.
