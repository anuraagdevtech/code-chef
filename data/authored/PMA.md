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

## Edge cases

- **The swap is optional** ("at most once"), so a negative gain must be clamped to $0$ — the first row's best available swap gains nothing and the answer stays $0$.
- **Only magnitudes matter**, since the sum is built from $|A_i|$: the second row's negatives contribute their absolute values, and the signs never enter.
- **Same-parity swaps are pointless.** Swapping two added positions, or two subtracted ones, leaves the sum unchanged, so only a cross-parity exchange is worth considering — which is why one minimum and one maximum suffice.
- **The gain is twice the difference**, because the large magnitude stops being subtracted *and* starts being added.
- **$N = 2$** (the first row): exactly one added and one subtracted position.
- **$N \geq 2$ guarantees a subtracted position exists**, so `max_minus` is never `None` and the gain calculation is always reachable.
- **$A_i$ may be $0$**, and a subtracted $0$ is a legitimate candidate — the clamp then keeps the gain at $0$.

## Dry run

Second sample: $A = -3, -2, -1, 0, 1, 2, 3$, magnitudes $3, 2, 1, 0, 1, 2, 3$.

| position | 1-based parity | magnitude | contributes |
|---:|---|---:|---:|
| 1 | added | 3 | $+3$ |
| 2 | subtracted | 2 | $-2$ |
| 3 | added | 1 | $+1$ |
| 4 | subtracted | 0 | $-0$ |
| 5 | added | 1 | $+1$ |
| 6 | subtracted | 2 | $-2$ |
| 7 | added | 3 | $+3$ |

Base sum $= 4$. Smallest added magnitude is $1$, largest subtracted is $2$, so the swap gains $2(2 - 1) = 2$. Output `6`.
