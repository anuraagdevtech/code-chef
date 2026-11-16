---
topic: Combinatorics
subtopic: Each value contributes a difference of two binomial tails, maintained incrementally
time: $O(N)$ per test case after $O(\max N)$ precomputation
space: $O(\max N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
In the sorted subsequence, the positions holding the value $v$ form a contiguous block, and position $v$ lies in that block exactly when

$$\#\{\text{chosen} < v\} < v \le \#\{\text{chosen} \le v\}.$$

Every value contributes at most one to the goodness, so the total is the sum over $v$ of the number of subsequences satisfying this. Because "at least $v$ chosen below $v$" implies "at least $v$ chosen up to $v$", that number is the difference of two tail counts. With $c_v$ the number of array elements $\le v$,

$$\text{count}(v) = \#\{\text{subsets with} \ge v \text{ of the } c_v\} - \#\{\text{subsets with} \ge v \text{ of the } c_{v-1}\}.$$

Work with probabilities (divide by $2^N$) so the unrelated elements disappear. Let $T(m, t) = \Pr[\text{Bin}(m, \tfrac12) \ge t]$. It can be updated in $O(1)$ in both arguments:

- adding one element: $T(m+1, t) = T(m, t) + \binom{m}{t-1} / 2^{m+1}$;
- raising the threshold: $T(m, t+1) = T(m, t) - \binom{m}{t} / 2^{m}$.

Sweep $v$ upwards: add the elements equal to $v$ one at a time, record the increase of the tail (this is the difference above), then raise the threshold for the next value. Multiply the final sum by $2^N$.

## Edge cases

- Values larger than their own count can never sit at their index and add 0 automatically.
- Duplicates of $v$ are added one by one; each changes the tail.
- The empty subsequence has goodness 0, so including it does not matter.
- Inverse powers of two and factorials are precomputed once for all test cases.

## Dry run

`A = [1, 2]`.

- $v = 1$: tail $T(0, 1) = 0$. Add the element 1: $T(1, 1) = 0 + \binom{0}{0}/2 = 1/2$. Contribution $1/2$. Raise the threshold: $T(1, 2) = 1/2 - \binom{1}{1}/2 = 0$.
- $v = 2$: add the element 2: $T(2, 2) = 0 + \binom{1}{1}/4 = 1/4$. Contribution $1/4$.

Total $3/4$, times $2^2$ gives 3: `[1]` has goodness 1 and `[1, 2]` has goodness 2.
