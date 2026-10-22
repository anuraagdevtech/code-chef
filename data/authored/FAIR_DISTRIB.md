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

## Edge cases

- **Reparametrising by gaps is what makes this one scan.** Writing $v_i = \sum_{j \leq i} d_j$ with $d_j \geq 0$ turns the difference into $\sum_j d_j \cdot (\text{suffix sum of signs from } j)$, while the maximum value is $\sum_j d_j$.
- **So fairness means every suffix sum of signs lies in $[-1, 1]$.** Concentrating all the value in one gap shows each bound is necessary, and the triangle inequality shows they suffice.
- **The scan runs right to left**, accumulating $+1$ for Alice and $-1$ for Bob, and fails the moment the running total leaves the band.
- **A single toy** (the first row) has suffix sum $\pm 1$ and is always fair.
- **Two toys to the same kid** (the second row, `00`) gives a suffix sum of $-2$ and fails — even though the values are unknown, the adversary can make both toys expensive and equal.
- **Alternating assignments are fair** (the fifth row), since the running total never leaves $\{-1, 0, 1\}$.
- **Trailing imbalance is what the last row catches**: `00001` starts fine but accumulates $-2$ once the three leading zeros are reached.
- **The toys are given in ascending value order**, which is exactly what makes the gaps non-negative and the reparametrisation valid.

## Dry run

Last sample: $S = $ `00001`, scanned from the right.

| position | owner | running suffix sum |
|---:|---|---:|
| 5 | Alice | $+1$ |
| 4 | Bob | $0$ |
| 3 | Bob | $-1$ |
| 2 | Bob | **$-2$** |

The band is breached at position $2$, so `NO`. Concretely, with all five toys worth $1$ Bob holds $4$ against Alice's $1$, a difference of $3$ above the maximum value of $1$.
