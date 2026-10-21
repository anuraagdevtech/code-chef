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
