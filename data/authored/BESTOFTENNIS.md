---
topic: Basic Math
subtopic: Inverting a stopping condition
time: $O(1)$ per test case
space: $O(1)$
---
In a best-of-$N$ match with $N$ odd, the winner needs $\frac{N+1}{2}$ sets — a strict majority. The players stop the instant the outcome is decided, which is exactly the moment the winner reaches that number. So at the final score, the winner has **precisely** $\frac{N+1}{2}$ sets, never more.

Inverting that gives $N$ directly from the larger of the two scores:

$$W = \max(X, Y) \quad\Longrightarrow\quad N = 2W - 1$$

The loser's score plays no part at all. That is the counter-intuitive bit, and it is worth seeing why: the match ends when the winner clinches, so the winner's tally pins down the required majority and hence $N$, whatever the loser happened to accumulate along the way. Sample cases 1 and 4 share nothing except $\max = 5$ and $\max = 8$ respectively, and the answers $9$ and $15$ follow from those alone.

Sample case 3 is the extreme: $(99, 1)$ gives $N = 197$, a best-of-197 match that was stopped as soon as Sonu reached $99$ — long before $197$ sets could be played.

The result is automatically odd, since $2W - 1$ is odd for any integer $W$, which satisfies the problem's requirement without a check. The guarantee $X \neq Y$ means there is always a unique winner and no ambiguity about which score to take.

## Edge cases

- **The loser's score is irrelevant.** They stop the instant the winner clinches, so the winner holds exactly the majority $\frac{N+1}{2}$ and $N = 2\max(X,Y) - 1$ regardless of the other score — the sample's $(2,5)$ and $(4,8)$ both depend on only the larger number.
- **A one-set match** ($\max = 1$): $N = 1$.
- **$X \neq Y$ is guaranteed**, so there is always a clear winner and the maximum is unambiguous.
- **Largest input** ($\max = 100$): $N = 199$.
- The answer is always odd, which is what "best of $N$" requires — an even $N$ could end level.

## Dry run

| $X$ | $Y$ | winner's sets | $N = 2\max - 1$ | output |
|---:|---:|---:|---:|---|
| 2 | 5 | 5 | 9 | `9` |
| 8 | 10 | 10 | 19 | `19` |
| 99 | 1 | 99 | 197 | `197` |
| 4 | 8 | 8 | 15 | `15` |

In row 1, winning $5$ of a best-of-$9$ clinches it, which is why the loser's $2$ never enters.
