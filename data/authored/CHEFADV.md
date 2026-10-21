---
topic: Number Theory
subtopic: Divisibility with an optional one-off offset
time: $O(1)$ per test case
space: $O(1)$
---
Knowledge and power both start at $1$ and are raised independently — knowledge by multiples of $X$, power by multiples of $Y$. The only coupling is ShareChat, which adds $1$ to **both** and may be used at most once.

So there are exactly two scenarios, and the answer is yes if either works.

**Without ShareChat:** knowledge must climb from $1$ to $N$ in steps of $X$, so $X \mid (N-1)$; likewise $Y \mid (M-1)$.

**With ShareChat:** both targets lose an extra $1$, so $X \mid (N-2)$ and $Y \mid (M-2)$ — and both $N$ and $M$ must be at least $2$, since the install alone already carries them past $1$.

Checking both and OR-ing them is the whole solution. Treating ShareChat as optional-per-skill would be wrong: it raises *both* counters or neither, so the two divisibility tests in the second scenario must be applied together.

Sample case 3 shows the coupling biting. With $N = M = 11$, $X = 5$, $Y = 9$: without ShareChat, knowledge works ($10$ is a multiple of $5$) but power does not ($10$ is not a multiple of $9$). With ShareChat, power works ($9$ is a multiple of $9$) but knowledge does not ($9$ is not a multiple of $5$). Neither scenario succeeds in both coordinates, so `Pofik` — even though each coordinate is individually reachable in *some* scenario.

Sample case 5 is the non-negativity guard: $N = 1$ makes $N - 2$ negative, so the ShareChat branch is unavailable and only the first test applies.

## Edge cases

- **ShareChat raises both counters together**, so it is all-or-nothing: the shifted tests on knowledge and power must both hold at once. Checking them independently accepts the third row, where $(11-2)$ is not a multiple of $5$ but $(11-2)$ *is* a multiple of $9$.
- **It can be used at most once**, so exactly two cases exist and no loop is needed.
- **Using it needs both counters at $2$ or more**, since it only adds $1$ to each and the targets must be reached exactly. The fifth row fails here with $N = 1$: there is no room for the extra point.
- **Both counters start at $1$, not $0$**, so the plain test is on $N-1$ and $M-1$ — using $N$ and $M$ directly fails the first row.
- **$X$ or $Y$ may be $1$**, which makes that side's divisibility test vacuous (the first row has $X = 1$).
- **$N, M, X, Y$ up to $10^9$** with constant work per case.

## Dry run

| $N$ | $M$ | $X$ | $Y$ | plain: $(N{-}1) \% X$, $(M{-}1) \% Y$ | with ShareChat: $(N{-}2) \% X$, $(M{-}2) \% Y$ | output |
|---:|---:|---:|---:|---|---|---|
| 2 | 2 | 1 | 2 | $0$, $1$ ✗ | $0$, $0$ ✓ | `Chefirnemo` |
| 11 | 10 | 5 | 9 | $0$, $0$ ✓ | — | `Chefirnemo` |
| 11 | 11 | 5 | 9 | $0$, $1$ ✗ | $4$, $0$ ✗ | `Pofik` |
| 12 | 11 | 5 | 9 | $1$, $1$ ✗ | $0$, $0$ ✓ | `Chefirnemo` |
| 1 | 2 | 1 | 100 | $0$, $1$ ✗ | $N < 2$ ✗ | `Pofik` |

Row 3 passes one shifted test and fails the other, which is why both must be demanded together.
