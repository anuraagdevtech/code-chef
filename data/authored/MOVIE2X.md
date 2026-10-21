---
topic: Basic Math
subtopic: Rate and time
time: $O(1)$
space: $O(1)$
---
The movie is $X$ minutes long. Chef watches the first $Y$ minutes of *content* at double speed and the remaining $X - Y$ minutes at normal speed.

Playing $Y$ minutes of footage at twice the speed takes $Y/2$ minutes of real time; the rest takes $X - Y$ minutes unchanged. So the time spent is

$$\frac{Y}{2} + (X - Y) \;=\; X - \frac{Y}{2}$$

The simplified right-hand form says it plainly: double speed saves exactly half of the fast-forwarded stretch.

The guarantee that $Y$ is **even** is what keeps the answer an integer, so `y // 2` is exact and no rounding rule is needed. Without that promise the problem would have to say whether to round up or down.

The distinction between *footage* and *real time* is the thing to keep straight. $Y$ measures content, not viewing time, so the saving is $Y/2$ rather than $Y$. Sample: $X = 100$, $Y = 20$ gives $10 + 80 = 90$.

As with The Three Topics, there is **no $T$ on the first line** — the input is a single line holding $X$ and $Y$, so this is one test case only.

## Edge cases

- **The whole movie at double speed** ($Y = X$): the answer is $X/2$, e.g. $X = Y = 100$ gives $50$.
- **$Y$ is guaranteed even**, so $Y/2$ is exact and there is no rounding decision. Were $Y$ odd the problem would have to state how a half minute is handled.
- **Smallest $Y$** is $2$, not $0$, so there is always some footage watched at $2\times$.
- The formula assumes $Y \leq X$ — you cannot fast-forward more footage than the film contains — which the problem's setup implies.
- **Input shape**: one line with $X$ and $Y$, no leading test-case count.

## Dry run

Sample 1: $X = 100$, $Y = 20$.

| part | footage | real time |
|---|---:|---:|
| at $2\times$ | $20$ min | $10$ min |
| at normal speed | $80$ min | $80$ min |
| **total** | $100$ min | **$90$ min** |

Output `90`. Sample 2 ($X = 50$, $Y = 24$) gives $12 + 26 = 38$.
