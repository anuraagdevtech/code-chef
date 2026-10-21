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
