---
topic: Greedy
subtopic: Best single swap
time: $O(N)$ per test case
space: $O(1)$
---
Only the **absolute values** enter the sum, so write $b_i = |A_i|$. Odd positions contribute $+b_i$ and even positions $-b_i$.

A swap exchanges the values at two positions. Swapping two positions of the same sign changes nothing — the same two numbers are added and subtracted either way. So the only useful move trades a plus-position value $p$ for a minus-position value $m$, changing the total by

$$(m - p) - (p - m) = 2(m - p)$$

To maximise that, take the **largest** magnitude sitting on a minus position and the **smallest** magnitude sitting on a plus position. The operation is optional, so if that gain is negative it is simply declined — hence the clamp at zero.

Everything is one pass: accumulate the alternating sum while tracking the minimum $b$ over odd positions and the maximum $b$ over even positions.

Sample case 1 is the no-gain case: $[10, -10]$ has magnitudes $10$ and $10$, so the sum is $0$ and swapping changes nothing. Sample case 2 starts at $3 - 2 + 1 - 0 + 1 - 2 + 3 = 4$; the smallest plus magnitude is $1$ and the largest minus magnitude is $2$, so the swap adds $2(2-1) = 2$, giving $6$.

The absolute values are what make the sign of $A_i$ irrelevant — a detail worth checking early, since $A_i$ may be negative and the naive alternating sum of the raw values is a different quantity entirely.
