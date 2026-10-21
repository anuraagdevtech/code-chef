---
topic: Greedy
subtopic: Remove the largest item first
time: $O(1)$ per test case
space: $O(1)$
---
The free space on the phone is

$$F = S - X - Y$$

and Chef needs $Z$ megabytes. There are only three possible answers, so the solution is a short ladder — but the order in which the options are tried is the whole point.

- **Delete nothing** if $F \geq Z$.
- **Delete one app** if removing the larger of the two is enough: $F + \max(X, Y) \geq Z$.
- **Delete both** otherwise.

The greedy step is in the second line. If exactly one app is to be deleted, it should be the one that frees the most space — deleting the smaller app can only do worse, and never better. So testing $\max(X, Y)$ alone settles whether *any* single deletion suffices; there is no need to try both. The constraints happen to guarantee $X \leq Y$, making $Y$ the larger, but writing `max(x, y)` keeps the logic correct without leaning on that.

The third branch always succeeds because $Z \leq S$ is guaranteed: with both apps gone the phone is empty and has $S$ megabytes free. So the answer is never "impossible", and no fourth case is needed.

Sample case 3 is the one that forces both deletions — $Z = 15$ equals the entire $15$ MB phone, so nothing else may remain. Sample case 4 is the greedy case: deleting the $30$ MB app frees enough, while deleting the $20$ MB one would not.

## Edge cases

- **Already enough free space** ($S = 10$, apps $1$ and $2$, need $3$): free space is $7$, so zero deletions.
- **Deleting one is enough, but it must be the larger app.** The sample's last row has $50$ free and needs $75$: removing the $30$ app gives $80$ and works, removing the $20$ app gives only $70$ and does not. A solution that deletes either app, or the smaller one, fails here.
- **Neither one alone suffices** ($S = 15$, apps $5$ and $10$, need $15$): both must go, so $2$. Since $Z \leq S$ is guaranteed, deleting both *always* works, which is why the answer never exceeds $2$.
- **An exact fit** (free space equal to $Z$): zero deletions, so the comparison is non-strict.

## Dry run

| $S$ | $X$ | $Y$ | $Z$ | free $S-X-Y$ | free $+\max(X,Y)$ | output |
|---:|---:|---:|---:|---:|---:|---|
| 10 | 1 | 2 | 3 | 7 | — | `0` |
| 9 | 4 | 5 | 1 | 0 | 5 | `1` |
| 15 | 5 | 10 | 15 | 0 | 10 | `2` |
| 100 | 20 | 30 | 75 | 50 | 80 | `1` |

Row 4 is the one that needs the *larger* app removed; row 3 needs both.
