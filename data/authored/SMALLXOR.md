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
