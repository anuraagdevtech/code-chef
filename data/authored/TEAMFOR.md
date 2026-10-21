---
topic: Greedy
subtopic: Pair the specialists first, then spend the all-rounders
time: $O(N)$ per test case
space: $O(1)$
---
Split the students into four groups: $b$ who know both, $p$ who know only programming, $e$ who know only English, and $n$ who know neither. A team of two is valid exactly when it contains an all-rounder, or one of each specialist:

- $(\text{both},\ \text{anyone})$ — valid, since that one person covers both skills;
- $(p,\ e)$ — valid;
- $(p, p)$, $(e, e)$, $(p, n)$, $(e, n)$, $(n, n)$ — invalid.

So the all-rounders are the scarce resource and should not be wasted on anything a specialist pair can do. **First** form $\min(p, e)$ specialist teams, consuming two non-all-rounders each. That is optimal by exchange: replacing such a team with an all-rounder-based one spends a $b$ to free a $p$ and an $e$ that can no longer pair with each other.

After that, the leftovers are $r = |p - e| + n$ people who cannot pair with one another, plus $b$ all-rounders. Each team now needs at least one all-rounder, so

$$\text{extra} = \begin{cases} b & r \geq b \\ r + \left\lfloor \frac{b-r}{2} \right\rfloor & r < b \end{cases}$$

— pair every all-rounder with a leftover while they last, then marry the surplus all-rounders to each other.

The samples cover the shapes. $(p,e,b,n) = (1,0,1,1)$ gives no specialist team and one all-rounder team, so $1$. $(1,1,1,1)$ gives one of each, so $2$. $(0,2,0,1)$ has no all-rounder and no programmer at all, so $0$ — the two English speakers cannot help each other. And $(0,1,1,0)$ gives one all-rounder team.
