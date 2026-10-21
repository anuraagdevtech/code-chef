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

## Edge cases

- **The special attack finishes the job alone** ($H = 78$, $Y = 78$): one attack. The `max(0, H - Y)` clamp is what allows this — without it the remaining health goes negative and the ceiling division gives a nonsense extra attack.
- **The special saves nothing** ($H = 100$, $X = 25$, $Y = 40$): both routes cost $4$, so using it is optional. A solution that *always* fires the special happens to get this row right, but the comparison is what makes it right in general.
- **$X < Y$ is guaranteed**, so the special always hits harder — and yet it may still not reduce the attack count, because what matters is whether it saves a whole plain attack rather than how much damage it does.
- **The weakest possible plain attack** ($X = 1$, $H = 46$): $45$ attacks with the special, $46$ without.
- Both strategies are evaluated and the smaller taken, since "hits harder" does not imply "finishes sooner".

## Dry run

| $H$ | $X$ | $Y$ | plain only $\lceil H/X \rceil$ | with special $1 + \lceil (H-Y)^+/X \rceil$ | output |
|---:|---:|---:|---:|---:|---|
| 100 | 25 | 40 | 4 | $1 + \lceil 60/25 \rceil = 4$ | `4` |
| 100 | 29 | 45 | 4 | $1 + \lceil 55/29 \rceil = 3$ | `3` |
| 46 | 1 | 2 | 46 | $1 + 44 = 45$ | `45` |
| 78 | 15 | 78 | 6 | $1 + 0 = 1$ | `1` |

Row 1 is the tie, row 4 the one-shot kill.
