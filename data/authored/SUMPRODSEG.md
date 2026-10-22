---
topic: Number Theory
subtopic: Every family shares a pivot, so the pair must be mixed
time: $O(\sqrt{Y})$ per test case
space: $O(1)$
---
Two structural facts collapse the search.

**All sum-segments overlap.** A segment $[L, X-L]$ with $L \leq X-L$ straddles $X/2$, so every one of them contains both $\lfloor X/2 \rfloor$ and $\lceil X/2 \rceil$.

**All product-segments overlap.** A segment $[L, Y/L]$ with $L \leq Y/L$ straddles $\sqrt{Y}$, so every one contains $\lfloor \sqrt{Y} \rfloor$.

So a disjoint pair must take **one from each family**, and within each family we should take the segment best placed to get out of the other's way — which in both cases is the most balanced one. Let the sum-segment be $[\lfloor X/2 \rfloor, \lceil X/2 \rceil]$, the shortest one available, and consider the balanced factor pair $[\ell, Y/\ell]$ where $\ell$ is the **largest divisor of $Y$ at most $\sqrt{Y}$**. Two ways to separate them:

- product-segment entirely to the right: $\ell > \lceil X/2 \rceil$;
- product-segment entirely to the left: $Y/\ell < \lfloor X/2 \rfloor$.

If neither holds, no pair exists and the answer is $-1$: pushing the product-segment further right only shrinks $\ell$, and further left only grows $Y/\ell$, while widening the sum-segment only makes matters worse.

Enumerating divisors to $\sqrt{Y} = 10^6$ handles $Y \leq 10^{12}$.

The samples: $X{=}4, Y{=}24$ gives the sum-segment $[2,2]$ and the balanced pair $[4,6]$, which clears it on the right — the sample's `1 3` plus `4 6` is an equally valid answer. $X{=}3, Y{=}30$ gives $[1,2]$ and $[5,6]$. And $X{=}Y{=}1$ has only $[0,1]$ and $[1,1]$, which share the point $1$, so $-1$.

## Edge cases

- **Within each family every segment contains the most balanced one.** All sum segments $[L, X-L]$ nest around $[\lfloor X/2 \rfloor, \lceil X/2 \rceil]$, and all product segments $[d, Y/d]$ nest around the divisor pair closest to $\sqrt{Y}$ — so two segments from the same family always intersect.
- **Hence the answer must pair one sum segment with one product segment**, and the tightest member of each family is the best candidate: if those two intersect, every other pair does too.
- **Both orderings must be checked**, since the product segment may lie entirely to the right of the sum segment or entirely to the left.
- **$X = Y = 1$ is the smallest failure** (the second row): the sum segment is $[0,1]$ and the only product segment is $[1,1]$, which overlaps it.
- **$L$ may be $0$**, since the segments range over non-negative integers — and $\lfloor X/2 \rfloor$ is $0$ when $X = 1$.
- **The largest divisor at most $\sqrt{Y}$ is found by trial division**, which is $10^6$ steps at $Y = 10^{12}$ — affordable at $T \leq 10$.
- **A perfect square $Y$** gives a single-point product segment, with the two divisors equal.

## Dry run

First sample: $X = 4$, $Y = 24$.

| family | tightest segment | reasoning |
|---|---|---|
| sum | $[2, 2]$ | the balanced split of $4$ |
| product | $[4, 6]$ | $4$ is the largest divisor of $24$ at most $\sqrt{24} \approx 4.9$ |

Since $4 > 2$ the product segment lies entirely to the right. Output `2 2` then `4 6` — disjoint, with $2+2 = 4$ and $4 \cdot 6 = 24$.
