---
topic: Arrays
subtopic: Running minimum over a prefix
time: $O(N)$ per test case
space: $O(1)$
---
Overtaking is impossible, so a car's actual speed is capped by every car ahead of it. Car $i$ therefore travels at

$$\min(A_1, A_2, \ldots, A_i)$$

and it moves at its **own** maximum speed exactly when $A_i$ is no greater than everything before it — that is, when $A_i \leq \min(A_1, \ldots, A_{i-1})$.

So the solution is one pass maintaining a running minimum, counting how often the current car is at or below it. The first car is always free, and the running minimum updates to $A_i$ whenever that happens.

The key realisation is that only the **prefix minimum** matters, not the immediately preceding car. A slow car far ahead throttles everything behind it, even cars whose immediate predecessor is fast. Sample case 3, $[4,5,1,2,3]$, shows this: cars $4$ and $5$ have faster cars directly in front of them, yet both are stuck behind the $1$, so the answer is $2$, not $4$.

Sample case 2, $[8,3,6]$, gives $2$: the $8$ runs free, the $3$ is slower than everything ahead so it also runs free, and the $6$ is throttled to $3$.

Since all speeds are distinct, the comparison could be strict without changing the result — but `<=` is the safer habit.

The statement warns that input files reach 4 MB, so bulk reading via `sys.stdin.buffer.read()` rather than per-line `input()` is genuinely necessary here, not just tidy.

## Edge cases

- **The cap comes from every car ahead, not just the one immediately in front.** Take $3, 5, 4$: car $2$ is held to speed $3$, so car $3$ at max speed $4$ is held too, and the answer is $1$. Comparing each car only with its predecessor's *maximum* speed accepts car $3$ (since $4 < 5$) and answers $2$. The running minimum is what encodes the speed a car actually travels at.
- **The first car is always free**, which the initial infinite minimum handles without a special case.
- **All speeds are distinct**, so `<=` and `<` behave identically here; the non-strict form is the one that stays correct if duplicates ever appear.
- **A monotonically decreasing input** means every car runs free, giving $N$.
- **Input files up to 4 MB** with an explicit warning in the statement: a single buffered read and token split is required, and per-line reading will time out.

## Dry run

Third sample: maximum speeds $4, 5, 1, 2, 3$.

| car | max speed | running min before | $\leq$ min? | actual speed | free so far |
|---:|---:|---:|:---:|---:|---:|
| 1 | 4 | $\infty$ | yes | 4 | 1 |
| 2 | 5 | 4 | no | 4 | 1 |
| 3 | 1 | 4 | yes | 1 | 2 |
| 4 | 2 | 1 | no | 1 | 2 |
| 5 | 3 | 1 | no | 1 | 2 |

Output `2`.
