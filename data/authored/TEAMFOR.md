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

## Edge cases

- **Four categories, and the pairing order matters.** Specialists pair with each other first — one programmer-only with one English-only — because such a team spends no all-rounder.
- **An all-rounder can carry anyone**, so after the specialist pairs are formed, each leftover specialist and each person who knows neither can be partnered with one all-rounder.
- **Surplus all-rounders pair among themselves, two per team**, which is the halved term — so they are spent last, at the worse rate.
- **Two programmers cannot form a team** (nobody knows English), which is why leftover specialists on one side count as plain spares rather than pairing up.
- **Nobody qualifying** (the third row, where everyone lacks programming) → $0$ teams, even with three people.
- **A single all-rounder plus one specialist** forms a team (the fourth row), since the all-rounder covers both requirements.
- **People who know neither are not useless**, as the first and second rows show — they can fill the second seat beside an all-rounder.

## Dry run

Second sample: $S = $ `1010`, $T = $ `0110`.

| person | programming | English | category |
|---:|:---:|:---:|---|
| 1 | yes | no | programmer only |
| 2 | no | yes | English only |
| 3 | yes | yes | all-rounder |
| 4 | no | no | neither |

| step | teams |
|---|---:|
| pair the specialists ($1$ with $2$) | 1 |
| the all-rounder ($3$) takes the spare ($4$) | 2 |

Output `2`.
