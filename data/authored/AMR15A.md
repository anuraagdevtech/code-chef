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
