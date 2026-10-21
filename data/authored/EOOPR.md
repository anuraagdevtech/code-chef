---
topic: Conditionals & Case Work
subtopic: Reachability of a difference by odd and even steps
time: $O(1)$ per test case
space: $O(1)$
---
With $a$ a fixed positive **odd** step up and $b$ a fixed positive **even** step down, the reachable totals after a few rounds are $a$, $-b$, $2a$, $a - b$, $-2b$, $3a$, $2a - b$, and so on. Only $d = Y - X$ matters, so the answer is a short case analysis on its sign and parity.

- **$d = 0$:** nothing to do, $0$ rounds.
- **$d > 0$ odd:** one round, $a = d$.
- **$d < 0$ even:** one round, $b = -d$.
- **$d < 0$ odd:** one round is impossible ($a > 0$ and $-b$ is even), but two work: $a - b = d$ with $a = 1$ and $b = 1 - d$, which is even and at least $2$.
- **$d > 0$ even:** one round is impossible. Two rounds give $2a$, which is $d$ only when $a = d/2$ is **odd**, i.e. $d \equiv 2 \pmod 4$. So:
  - $d \equiv 2 \pmod 4$: two rounds.
  - $d \equiv 0 \pmod 4$: three rounds, via $2a - b$ — pick any odd $a \geq (d+2)/2$ and set $b = 2a - d$, which is even and positive.

So the answer is never more than $3$, and the only case needing three is a positive difference divisible by $4$ — because two "up" moves always land on $2 \times (\text{odd})$, which is $2$ mod $4$.

The samples: $0 \to 5$ is a positive odd difference, so one round. $4 \to -5$ is $-9$, negative and odd, so two. And $0 \to 10000001$ is again positive and odd, so one — size is irrelevant, since $a$ may be as large as needed.
