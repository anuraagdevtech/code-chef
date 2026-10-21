---
topic: Sorting
subtopic: Pairing extremes to lift the median
time: $O(N \log N)$ per test case
space: $O(N)$
---
$B$ has $N$ entries with $N$ odd, so its median is both the $k$-th smallest and the $k$-th largest for $k = \frac{N+1}{2}$. The median is therefore at least $X$ exactly when **$k$ of the pairs have maximum at least $X$**, and each such pair needs its own element $\geq X$. So the median can never exceed the $k$-th largest element of $A$:

$$\text{answer} = a_{2N - k + 1} = a_{N + \frac{N+1}{2}} \quad (\text{1-indexed, } a \text{ sorted ascending})$$

That bound is attained by **pairing the extremes**: match the $k$ largest elements with the $k$ smallest, one each, and let the middle $2(N-k)$ elements pair up among themselves. The $k$ chosen pairs then each have maximum at least $a_{2N-k+1}$, so the $k$-th largest entry of $B$ is at least that — and by the bound, exactly that.

Pairing large with small is what makes the construction work: spending two large elements on one pair would waste one of them, since a pair contributes only its maximum. Each large element must carry its own pair.

The sample shows the answer is a value *of $A$*, not an average: $N = 3$ with $A = [1,\ldots,6]$ gives $k = 2$ and the $2$nd largest, $5$. Our pairing prints `1 5 2 6 3 4`, whose $B = [5,6,4]$ has median $5$; the sample's `1 3 2 5 4 6` gives $B = [3,5,6]$, also median $5$ — any optimal arrangement is accepted.

The third sample has repeats, $A = [1,3,3,3,2,2]$, and the $2$nd largest is $3$; here the input order already happens to be optimal, which is why the expected output echoes it unchanged.

## Edge cases

- **$N$ is odd**, so the median of $B$ is its $\lceil N/2 \rceil$-th largest element — call that count $k$. Maximising the median means making the $k$ largest entries of $B$ as large as possible.
- **Each of the $k$ largest values should carry its own pair**, partnered with one of the $k$ smallest so that it is the pair's maximum. Then the $k$-th largest entry of $B$ is the $k$-th largest value overall, $A_{2N-k}$ in sorted order — and no arrangement can do better, since $B$ has only $N$ entries drawn from pairs.
- **The leftover middle values pair among themselves**, and their maxima all fall below the median, so their arrangement is irrelevant.
- **$N = 1$** (the first row) makes $k = 1$: the single pair's maximum is the larger of the two values.
- **Duplicates are handled by position, not value.** The third row has three $3$s, and the answer is $3$ — the construction never needs distinct values.
- **Two things must be printed**: the median on one line and a witnessing permutation on the next.
- **This permutation differs from the sample's** (`1 5 2 6 3 4` against `1 3 2 5 4 6` for the second case), and both achieve a median of $5$, so a special judge verifies the pairing.

## Dry run

Second sample: $N = 3$ and $A = 1,2,3,4,5,6$ (already sorted), so $k = 2$.

| pair | values | max |
|---:|---|---:|
| 1 | $1, 5$ | 5 |
| 2 | $2, 6$ | 6 |
| 3 | $3, 4$ | 4 |

$B = 5, 6, 4$, whose median is `5` $= A_{2N-k} = A_4$. The two largest values each head their own pair.
