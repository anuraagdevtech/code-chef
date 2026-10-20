---
topic: Arrays
subtopic: Existence check over a list
time: $O(N)$
space: $O(1)$
---
Chef has $x$ hours left and needs $H$. Travelling back $T_i$ hours buys him $T_i$ extra hours, so in time zone $i$ he effectively has $x + T_i$. He succeeds if **some** zone gives him enough:

$$\exists i : \; x + T_i \geq H$$

In Python that is `any(x + t >= h for t in zones)`, which short-circuits on the first success and needs no extra storage.

Since only existence matters, there is nothing to optimise — no need to find the largest $T_i$ or to sort. Comparing against $\max(T)$ would also be correct and is equivalent, but `any` states the question directly.

The comparison is inclusive: arriving with exactly enough time counts. The sample is built on that boundary — $x = 3$, $H = 5$, and the best zone offers $T = 2$, giving precisely $5$ hours, so the answer is `YES`. A strict `>` would fail it.

The constraint $x < H$ guarantees Chef genuinely cannot finish without travelling, so the answer is never trivially yes.

Note the input shape: there is **no $T$ test-case count**. The first line holds three values $N, H, x$ — in that order, with the hours needed before the hours remaining — and the second line holds the $N$ time zones. Reading the first number as a test-case count is the likely misstep here.
