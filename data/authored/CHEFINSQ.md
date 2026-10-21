---
topic: Combinatorics
subtopic: Choosing among the tied boundary value
time: $O(N \log N)$ per test case
space: $O(N)$
---
The minimum sum is obtained by taking the $K$ smallest elements, so sort and look at where the cut falls. Let $v = A_{(K)}$ be the $K$-th smallest value. Everything strictly below $v$ is **forced** into the subsequence, and everything strictly above is forced out — swapping either way would change the sum.

The only freedom is among the copies of $v$ itself. If $v$ occurs $c$ times in the whole array and $u$ of them lie in the first $K$ sorted positions, then any $u$ of the $c$ copies may be chosen, and the sum is the same:

$$\text{answer} = \binom{c}{u}$$

Subsequences are indexed by position, so two choices of copies are different subsequences even though they produce the same multiset of values — which is exactly what the problem counts.

The sample has $A = [1,2,3,4]$ with $K = 2$. The cut value is $2$, which occurs once and is used once, giving $\binom{1}{1} = 1$: the subsequence $\{1,2\}$ is the unique minimiser.

The count only becomes interesting with ties. For $A = [1,2,2,2]$ with $K = 2$ the cut value $2$ occurs three times and one is used, giving $\binom{3}{1} = 3$. And for $A = [5,5,5]$ with $K = 2$ it is $\binom{3}{2} = 3$.

With $N \leq 50$ the binomial fits easily in Python's unbounded integers; $\binom{50}{25} \approx 1.3 \times 10^{14}$ needs 64-bit arithmetic in C++.
