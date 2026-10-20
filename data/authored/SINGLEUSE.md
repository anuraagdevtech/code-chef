---
topic: Greedy
subtopic: Comparing both strategies explicitly
time: $O(1)$ per test case
space: $O(1)$
---
The special attack may be used **at most once**, so there are exactly two strategies and the answer is the cheaper one.

**Never use it.** Plain attacks deal $X$ each, so the boss falls in $\lceil H/X \rceil$ hits.

**Use it once.** The special removes $Y$ immediately, leaving $\max(0, H - Y)$ health for plain attacks:

$$1 + \left\lceil \frac{\max(0, H - Y)}{X} \right\rceil$$

The clamp matters because $Y$ may finish the boss outright — sample case 4 has $Y = H = 78$, so the special alone wins in a single attack and the remaining health must not go negative.

It is tempting to assume that since $X < Y$ the special is always worth using, making the second branch the answer. That is wrong, and sample case 1 shows why: $H = 100, X = 25, Y = 40$ costs $4$ attacks either way, because the special's extra damage is wasted inside a hit that would have been spent anyway. The special helps only when it removes enough to save a whole plain attack — a *rounding* effect, not a raw-damage one. Sample case 3 is the extreme: with $X = 1$ and $Y = 2$ the special saves exactly one hit out of $46$.

So compute both and take the minimum. With only two options, evaluating both is simpler and safer than deriving the condition under which the special pays off.
