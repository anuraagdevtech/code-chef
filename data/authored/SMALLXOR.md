---
topic: Heaps
subtopic: Detecting the two-cycle that ends the process
time: $O(N \log N)$ per test case
space: $O(N)$
---
$Y$ reaches $10^9$, so the process cannot be simulated step by step — but it stabilises almost immediately.

Each value only ever alternates between $a$ and $a \oplus X$. These differ at $h$, the highest set bit of $X$, so the one with bit $h$ clear is the smaller; call it the element's **low** form and the other its **high** form.

Now watch the operation. If the global minimum is in low form, flipping it raises it. But if the global minimum is already in **high** form, flipping it gives its low form, which is smaller than the high value that was the minimum — so it is still the minimum, and the next operation flips it straight back. The process has entered a **two-cycle**, and every remaining operation just toggles that one element.

So the simulation only has to run until a popped element turns out to be in high form, which happens within $N+1$ steps because each earlier step promotes a distinct element from low to high and never revisits it. With $r$ operations left at that moment, the element's final value is

$$v \oplus \begin{cases} X & r \text{ odd} \\ 0 & r \text{ even}\end{cases}$$

A min-heap supplies the minimum at each step.

Sample 2 shows both phases: $[1,2,3]$ with $X = 7$ promotes $1 \to 6$, $2 \to 5$, $3 \to 4$, and then $4$ is in high form ($4 \oplus 7 = 3$), so the remaining $41$ operations — an odd count — leave it at $3$, giving `3 5 6`.

Sample 3 shows that elements can start in high form and be ignored entirely: $20$ and $25$ are both above their partners $0$ and $13$, so they are never touched, and the cycle forms on $5 \leftrightarrow 17$ after three promotions.

## Edge cases

- **Two regimes, and spotting the second is the whole problem.** If $v \oplus X > v$ the element grows and leaves the minimum position, so the heap advances. If $v \oplus X < v$ the result is *smaller* than the previous minimum, so it stays the minimum and every remaining operation toggles that same element.
- **So the process becomes a two-cycle**, and the remaining count's parity decides the final value — which is what lets $Y$ up to $10^9$ be handled without simulating it.
- **$v \oplus X = v$ is impossible** since $X \geq 1$, so the two branches are exhaustive.
- **The toggle must use the count still left**, `y - step`, not $Y$ itself — the steps already spent change the parity.
- **The cycle may never be reached**, in which case all $Y$ operations advance the heap normally; the loop simply runs to completion.
- **Ties for the minimum are resolved arbitrarily** by the statement ("pick any one index"), which a heap does naturally.
- **The output is the sorted array**, so the heap's internal order is discarded at the end.
- **Sum of $N \leq 10^5$** with one heap operation per step until the cycle is found.

## Dry run

Third sample: $A = 5, 10, 15, 20, 25$, $X = 20$, $Y = 6$.

| step | minimum $v$ | $v \oplus 20$ | bigger? | action |
|---:|---:|---:|:---:|---|
| 0 | 5 | 17 | yes | promote to 17 |
| 1 | 10 | 30 | yes | promote to 30 |
| 2 | 15 | 27 | yes | promote to 27 |
| 3 | 17 | 5 | **no** | cycle found, $3$ steps left (odd) → take $5$ |

Final array sorted: `5 20 25 27 30`.
