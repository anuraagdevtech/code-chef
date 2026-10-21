---
topic: Arrays
subtopic: Parity counting in a single pass
time: $O(N)$
space: $O(1)$
---
A soldier is "lucky" when the number of weapons they hold is even, and the army is ready when the lucky soldiers *strictly* outnumber the unlucky ones. So the task reduces to counting how many of the $N$ values are even.

Two observations keep this to one pass and constant memory. First, parity is decided by `a % 2` alone — the magnitude of $A_i$ is irrelevant, so nothing needs to be stored. Second, every soldier is either lucky or unlucky, so if $E$ is the number of even values then the odd count is simply $N - E$. There is no need to maintain two counters.

The comparison $E > N - E$ rearranges to

$$2E > N$$

which is the cleanest form: a strict majority of the soldiers must be even. Note that for odd $N$ a tie is impossible, but for even $N$ the split $E = N/2$ is exactly a tie and must answer `NOT READY` — which `2E > N` handles correctly.

Unlike most problems in this set there is no $T$ wrapper: the input is a single test case, one $N$ followed by one array.

## Edge cases

- **Exactly half lucky** ($N = 2$ with one even count): $2 \times 1 > 2$ is false, so `NOT READY` — a **strict** majority is required and `>=` would be wrong.
- **$N = 1$**: the single soldier decides it, and the two sample runs are precisely the two outcomes.
- **All lucky** or **none lucky**: the extremes.
- **"Lucky" means an even weapon count**, so a soldier carrying $1$ weapon is unlucky while $2$ is lucky — the parity, not the amount.
- **Input shape**: $N$ followed by the array, with no test-case count.

## Dry run

Sample 1: $N = 1$, weapons $[1]$.

| step | value |
|---|---|
| even counts | $0$ |
| $2 \times 0 > 1$? | no |
| output | `NOT READY` |

Sample 2: $N = 1$, weapons $[2]$ — one even count, and $2 \times 1 > 1$ holds, so `READY FOR BATTLE`.
