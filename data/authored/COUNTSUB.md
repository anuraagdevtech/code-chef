---
topic: Arrays
subtopic: A telescoping sum, then counting equal pairs
time: $O(N)$ per test case
space: $O(N)$
---
The definition of $f$ **telescopes**:

$$f(l, r) = \sum_{i=l}^{r-1} (A_i - A_{i+1}) = A_l - A_r$$

every interior term cancelling against its neighbour. So the instability test $f(l,r) \neq A_r - A_l$ becomes

$$A_l - A_r \neq A_r - A_l \quad\Longleftrightarrow\quad 2(A_l - A_r) \neq 0 \quad\Longleftrightarrow\quad A_l \neq A_r$$

The whole elaborate sum collapses to **comparing the two endpoints**.

So count the pairs $l \leq r$ with $A_l \neq A_r$. Singletons always have $A_l = A_r$ and are stable, so only $l < r$ can contribute:

$$\binom{N}{2} - \sum_{v} \binom{\mathrm{cnt}_v}{2}$$

— all unordered pairs of positions, minus those whose values coincide, tallied with a `Counter`.

Spotting the telescope is what turns an apparently $O(N^2)$ or even $O(N^3)$ definition into one linear pass. Enumerating subarrays at $\sum N = 5 \times 10^5$ would be hopeless.

Sample case 2, $[1,2,1,2]$, has $\binom{4}{2} = 6$ pairs, of which the two matching pairs $(1,1)$ and $(2,2)$ are stable, leaving $4$. Sample case 3 has all values distinct, so every one of the $\binom{5}{2} = 10$ pairs is unstable.

The count reaches about $1.25 \times 10^{10}$ at $N = 10^5$, which **overflows 32 bits**.
