---
topic: Basic Math
subtopic: Reachable range over repeated choices
time: $O(1)$ per test case
space: $O(1)$
---
Over $M$ months Chef gains between $x_1$ and $x_2$ kilograms each month, and the monthly gains need not be equal. So the **total** gain can be anything from $M \cdot x_1$ to $M \cdot x_2$ — and, since the per-month values vary freely, every value in that range is attainable.

The scale is consistent with the science exactly when the observed gain lands inside:

$$M \cdot x_1 \leq w_2 - w_1 \leq M \cdot x_2$$

The step worth justifying is that the range has no gaps. With each month free to take any value in $[x_1, x_2]$, the achievable totals form a continuous interval rather than a scattered set — so a single two-sided comparison suffices and there is nothing to search over.

Both bounds are needed, and the samples prove it. Case 1 fails the **lower** bound: a gain of $1$ kg over two months is less than the minimum $2$, so the scale is reading too low. Case 5 fails the **upper** bound with a gain of $99$ against a maximum of $4$. Dropping either comparison passes one of these wrongly.

Cases 2 through 4 land on and inside the range — case 2 exactly on the minimum and case 3 exactly on the maximum — confirming both ends are inclusive.

Note that $x_1$ may be $0$, so a gain of zero can be legitimate; but $w_1 < w_2$ is guaranteed, so the observed gain is always at least $1$.
