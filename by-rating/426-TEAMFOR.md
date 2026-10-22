# 426. Team Formation

> [`TEAMFOR`](https://www.codechef.com/problems/TEAMFOR) &middot; difficulty **1715** &middot; time limit **0.5s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Pair the specialists first, then spend the all-rounders |
| **CodeChef tags** | `Basic Programming Concepts`, `Mathematics`, `Algorithms`, `Constructive`, `Conditional Statements`, `Basic Math`, `Greedy`, `ad-hoc`, `Observation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

A programming competition will be held in Chef's city which only accepts teams of size $2$. At least one person in a team should know a programming language and at least one person should know about the English language. It is possible that one person in a team knows both programming and the English language. Then the qualification of the other teammate is not important i.e. he may or may not know programming and English. Now Chef has $N$ students and wants to send *maximum* number of teams to the competition.

You are given an integer $N$ and two binary strings $S$ and $T$ of length $N$. $S_i = $ `'1'` denotes that the $i^{th}$ student knows a programming language, and $S_i = $ `'0'` denotes otherwise; similarly, $T_i =$ `'1'` denotes that the $i^{th}$ student knows English language, and $T_i = $ `'0'` denotes otherwise. Determine the maximum number of teams Chef can form.

**Input**

- The first line of input contains a single integer $Q$ denoting the number of test cases. The description of $Q$ test cases follows.
- Each test case contains $3$ lines of input.
- The first line of each test case contains an integer $N$.
- The second line of each test case contains a string $S$.
- The last line of each test case contains a string $T$.

**Output**

For each test case, print a single line containing one integer - the maximum number of teams that Chef can form.

## Constraints

- $1 \leq Q \leq 1000$
- $1 \leq N \leq 100$
- $S$ and $T$ contains only characters `'0'` and `'1'`

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
4
3
101
001
4
1010
0110
3
000
110
2
10
11
```

**Sample output**

```
1
2
0
1
```

<details><summary>Explanation</summary>

**Test case $1$:** The third student can team up with any other students as he knows both programming and English.

**Test case $2$:** The first two students make a team and the last two students make another team.

**Test case $3$:** No student knows how to program, hence there is no way to make a team.

</details>

## Approach

Split the students into four groups: $b$ who know both, $p$ who know only programming, $e$ who know only English, and $n$ who know neither. A team of two is valid exactly when it contains an all-rounder, or one of each specialist:

- $(\text{both},\ \text{anyone})$ — valid, since that one person covers both skills;
- $(p,\ e)$ — valid;
- $(p, p)$, $(e, e)$, $(p, n)$, $(e, n)$, $(n, n)$ — invalid.

So the all-rounders are the scarce resource and should not be wasted on anything a specialist pair can do. **First** form $\min(p, e)$ specialist teams, consuming two non-all-rounders each. That is optimal by exchange: replacing such a team with an all-rounder-based one spends a $b$ to free a $p$ and an $e$ that can no longer pair with each other.

After that, the leftovers are $r = |p - e| + n$ people who cannot pair with one another, plus $b$ all-rounders. Each team now needs at least one all-rounder, so

$$\text{extra} = \begin{cases} b & r \geq b \\ r + \left\lfloor \frac{b-r}{2} \right\rfloor & r < b \end{cases}$$

— pair every all-rounder with a leftover while they last, then marry the surplus all-rounders to each other.

The samples cover the shapes. $(p,e,b,n) = (1,0,1,1)$ gives no specialist team and one all-rounder team, so $1$. $(1,1,1,1)$ gives one of each, so $2$. $(0,2,0,1)$ has no all-rounder and no programmer at all, so $0$ — the two English speakers cannot help each other. And $(0,1,1,0)$ gives one all-rounder team.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        prog, eng = data[2 + 3 * i], data[3 + 3 * i]
        both = only_p = only_e = none = 0
        for a, c in zip(prog, eng):
            if a == 0x31 and c == 0x31:
                both += 1
            elif a == 0x31:
                only_p += 1
            elif c == 0x31:
                only_e += 1
            else:
                none += 1
        # Specialist pairs first; they spend no all-rounder.
        teams = min(only_p, only_e)
        spare = abs(only_p - only_e) + none
        teams += both if spare >= both else spare + (both - spare) // 2
        out.append(str(teams))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

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

---

Same problem grouped by topic: [../docs/greedy/TEAMFOR.md](../docs/greedy/TEAMFOR.md)
