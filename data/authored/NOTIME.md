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

## Edge cases

- **Exactly enough** (sample 1: $x = 3$ plus a zone of $2$ reaches $H = 5$): `YES`, so the comparison is non-strict. The two sample runs differ only in $H$ by one, which is precisely the test of that boundary.
- **$x < H$ is guaranteed**, so Chef always needs at least one zone — he can never already be done.
- **Only existence matters**, so there is no need to find the best zone; taking the maximum would also work but is unnecessary.
- **Input shape**: the first line is $N$, $H$, $x$ — *not* a test-case count, which is the usual trap in these single-case problems.

## Dry run

Sample 1: $N = 2$, $H = 5$, $x = 3$, zones $1, 2$.

| zone $t$ | $x + t$ | $\geq H$? |
|---:|---:|:---:|
| 1 | 4 | no |
| 2 | 5 | **yes** |

One zone suffices, so `YES`. Sample 2 raises $H$ to $6$: now $4$ and $5$ both fall short, so `NO`.
