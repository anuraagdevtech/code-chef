---
topic: Prefix Sums
subtopic: Reparametrising by gaps turns it into suffix sums
time: $O(N)$ per test case
space: $O(1)$
---
Set $c_i = +1$ when $S_i = \texttt{1}$ and $-1$ otherwise, so the quantity to bound is $\bigl|\sum_i c_i v_i\bigr| \leq v_N$ for **every** non-decreasing non-negative $v$.

The quantifier over all $v$ is handled by changing variables to the gaps $d_j = v_j - v_{j-1} \geq 0$ (with $d_1 = v_1$), which range freely over the non-negative reals. Since $v_i = \sum_{j \leq i} d_j$, swapping the order of summation gives

$$\sum_i c_i v_i = \sum_j d_j \underbrace{\sum_{i \geq j} c_i}_{T_j}, \qquad v_N = \sum_j d_j$$

So the condition is $\bigl|\sum_j d_j T_j\bigr| \leq \sum_j d_j$ for all $d \geq 0$. Taking $d$ to be a single unit at position $j$ forces $|T_j| \leq 1$; conversely if every $|T_j| \leq 1$ then the triangle inequality gives the bound. Hence

$$\text{fair} \iff \bigl|T_j\bigr| \leq 1 \text{ for every suffix } j$$

a single right-to-left sweep. Note it is the **suffix** sums, not prefix sums, that matter — the gap at position $j$ raises every $v_i$ with $i \geq j$.

The samples show the mechanism. `1010` has suffix sums $0, -1, 0, -1$, all within range: fair. `1100` has the suffix sum $-2$ at $j = 3$, so making $v_3 = v_4$ large and $v_1 = v_2 = 0$ breaks the bound. `00` likewise has $T_1 = -2$. `00001` has $T_2 = -2$, so even a single toy for Alice at the end cannot rescue it. And `1` is fair because the only suffix sum is $1$.
