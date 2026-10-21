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
