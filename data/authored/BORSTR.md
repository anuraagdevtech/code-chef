---
topic: Strings
subtopic: Longest repeated run
time: $O(N)$ per test case
space: $O(1)$
---
A boring substring is a run of one repeated character, so for each letter only its **run lengths** matter.

Fix a letter with runs of lengths $r_1 \geq r_2 \geq \cdots$. A boring substring of that letter with length $m$ occurs $\max(0, r - m + 1)$ times inside a run of length $r$, and it must occur at least twice overall. There are exactly two ways to achieve that:

- **Twice inside the longest run**, which needs $r_1 - m + 1 \geq 2$, i.e. $m \leq r_1 - 1$;
- **Once in each of the two longest runs**, which needs $m \leq r_2$.

So the best length for that letter is $\max(r_1 - 1,\ r_2)$, and the answer is the maximum over all $26$ letters.

Both branches are genuinely needed. Sample case 1, `aaa`, has a single run of $3$: sliding a window of length $2$ gives two occurrences, so the answer is $2$ — the first branch. Sample case 4, `caabaa`, has two runs of `a` of length $2$ each: here $r_1 - 1 = 1$ but $r_2 = 2$, so the second branch wins with $2$.

Sample case 3, `bcaca`, has two runs of length $1$ for both `a` and `c`, giving $\max(0, 1) = 1$.

Sample case 2, `abc`, has every run at length $1$ with no repeats, so $\max(0, 0) = 0$ — the explicit "no answer" case.

Tracking only the two largest runs per letter keeps this to one pass and constant space, which matters at $\sum N = 5 \times 10^5$.

## Edge cases

- **One long run already contains two occurrences.** A run of length $L$ holds the substring of length $L-1$ at two different offsets, so a single run of `aaa` yields the answer $2$ — this is the case most easily missed.
- **Two separate runs give the shorter of them**, so the second-longest run of a letter is the other candidate: `bcaca` has two one-character `a` runs and answers $1$.
- **The answer per letter is $\max(L_1 - 1, L_2)$**, and either term can win. `caabaa` has two runs of length $2$, where $L_2 = 2$ beats $L_1 - 1 = 1$.
- **No repeat at all** → $0$ (the second row, `abc`, where every letter appears once).
- **Only the top two runs per letter matter**, so a constant $26 \times 2$ table suffices and no per-letter list is needed.
- **A sentinel byte flushes the final run**, which is why `b"\x00"` is appended — otherwise the last run is never recorded.
- **$N > 1$ is guaranteed**, so a single-character string never arises; sum of $N \leq 5 \cdot 10^5$.

## Dry run

| $S$ | runs | per-letter top two | $\max(L_1 - 1, L_2)$ | output |
|---|---|---|---|---:|
| `aaa` | `aaa` | a: $3, 0$ | $\max(2, 0)$ | `2` |
| `abc` | `a`,`b`,`c` | each $1, 0$ | $\max(0, 0)$ | `0` |
| `bcaca` | `b`,`c`,`a`,`c`,`a` | a: $1,1$; c: $1,1$ | $\max(0, 1)$ | `1` |
| `caabaa` | `c`,`aa`,`b`,`aa` | a: $2, 2$ | $\max(1, 2)$ | `2` |

Row 1 wins from a single run; row 4 from two.
