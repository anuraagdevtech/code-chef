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
