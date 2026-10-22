---
topic: Greedy
subtopic: Hall's condition on value-capped positions
time: $O(N)$ per test case
space: $O(N)$
---
An element of value $v$ can occupy positions $1, 2, \ldots, v$ of a positive array, and no further — position $i$ demands a value of at least $i$. With $k$ arrays there are exactly $k$ slots at each position index.

So the question is whether the elements can be matched into slots, and **Hall's condition** answers it. The elements with value at most $t$ are confined to positions $1 \ldots t$, which offer only $kt$ slots. So feasibility with $k$ arrays requires, for every $t$,

$$\#\{i : A_i \leq t\} \;\leq\; k\,t$$

and that condition is also sufficient, since the constraint sets are nested intervals. Rearranging gives the answer directly:

$$k = \max_{t} \left\lceil \frac{c_t}{t} \right\rceil, \qquad c_t = \#\{i : A_i \leq t\}$$

Because $A_i \leq N$, the counts $c_t$ come from one counting pass and a prefix sum, so the whole thing is $O(N)$ with no sorting or binary search.

The small values are what force extra arrays — each array can hold only one element of value $1$, since only position $1$ accepts it. Sample case 3, $[1,1,1]$, needs three arrays for exactly that reason, even though the array is tiny.

Sample case 5, $[3,2,1,2,2,1]$, is decided at $t = 2$: five elements are at most $2$, but each array offers only two such slots, so $\lceil 5/2 \rceil = 3$ arrays are needed — more than the $t=1$ bound of $2$ or the $t=3$ bound of $2$. Checking only one threshold would under-count.

## Edge cases

- **An element of value $v$ can only sit at positions $1 \dots v$**, so across $k$ arrays the values at most $t$ have only $k \cdot t$ slots available — giving the bound $k \geq \lceil c_t / t \rceil$ where $c_t$ counts the elements with value $\leq t$.
- **Every threshold must be tested, not just one.** The binding $t$ varies: the fourth row is limited at $t = 2$ (three elements for two slots per array) while the second is limited at $t = 1$.
- **All ones is the worst case** (the third row): each needs position $1$, so $N$ arrays are required.
- **The bound is achievable**, which is Hall's condition in this setting — so the maximum over thresholds is exactly the answer and no construction is needed.
- **The answer is at least $1$**, which the initialiser provides for arrays where every bound comes out as $0$ or less.
- **$A_i \leq N$ is guaranteed**, so the frequency table is $O(N)$ and the threshold loop runs to $N$.
- **A single array suffices when the values are large enough** (the first row), since $\lceil c_t/t \rceil$ never exceeds $1$.

## Dry run

Fourth sample: $A = 1, 2, 2, 4, 5$.

| threshold $t$ | elements with value $\leq t$ | $\lceil c_t / t \rceil$ |
|---:|---:|---:|
| 1 | 1 | 1 |
| 2 | 3 | **2** |
| 3 | 3 | 1 |
| 4 | 4 | 1 |
| 5 | 5 | 1 |

Output `2`: the three values at most $2$ cannot all fit in the two low positions of a single array. A valid pair of arrays is $[1, 2]$ and $[2, 4, 5]$ — checking the first, $1 \geq 1$ and $2 \geq 2$; and the second, $2 \geq 1$, $4 \geq 2$, $5 \geq 3$.
