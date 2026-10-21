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

## Edge cases

- **$f(l,r)$ telescopes to $A_l - A_r$**, so the instability test $f(l,r) \neq A_r - A_l$ becomes $A_l - A_r \neq A_r - A_l$, i.e. simply $A_l \neq A_r$. Everything between the endpoints is irrelevant.
- **Single-element subarrays are always stable.** $f(i,i)$ is defined as $0$ and $A_i - A_i$ is also $0$, which is why the count runs over $l < r$ and the total is $N(N-1)/2$.
- **Counting the complement is easier**: subtract the pairs of equal-valued positions, $\sum \binom{c_v}{2}$, from the total.
- **All values equal** → $0$ unstable subarrays.
- **All values distinct** (the first and third rows) → every pair counts, giving $N(N-1)/2$.
- **Duplicates are counted per position, not per value.** The second row has two $1$s and two $2$s, removing one pair each from six.
- **Sum of $N \leq 5 \cdot 10^5$**: a `Counter` on raw byte tokens, with totals near $10^{10}$ at $N = 10^5$ — past 32-bit.

## Dry run

Second sample: $A = 1, 2, 1, 2$, so $N(N-1)/2 = 6$ subarrays with $l < r$.

| value | count | equal-endpoint pairs |
|---:|---:|---:|
| 1 | 2 | 1 (positions $1,3$) |
| 2 | 2 | 1 (positions $2,4$) |

Unstable $= 6 - 2 = $ `4`. The two excluded subarrays are $A[1,3]$ and $A[2,4]$.
