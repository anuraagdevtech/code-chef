[&larr; 223. Array Halves](ARRHALVES.md) &middot; [Index](../../README.md) &middot; [261. Weird Palindrome Making &rarr;](MAKEPAL.md)

# 229. Fit to Play

> CodeChef problem code [`PLAYFIT`](https://www.codechef.com/problems/PLAYFIT) &middot; difficulty **1419** &middot; time limit **1.64548s**

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Best gain against a running minimum |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Rayne Wooney has been one of the top players for his football club for the last few years. But unfortunately, he got injured during a game a few months back and has been out of play ever since.

He's got proper treatment and is eager to go out and play for his team again. Before doing that, he has to prove to his fitness to the coach and manager of the team. Rayne has been playing practice matches for the past few days. He's played N practice matches in all.

He wants to convince the coach and the manager that he's improved over time and that his injury no longer affects his game. To increase his chances of getting back into the team, he's decided to show them stats of any 2 of his practice games. The coach and manager will look into the goals scored in both the games and see how much he's improved. If the number of goals scored in the 2nd game(the game which took place later) is greater than that in 1st, then he has a chance of getting in. Tell Rayne what is the maximum improvement in terms of goal difference that he can show to maximize his chances of getting into the team. If he hasn't improved over time, he's not fit to play. Scoring equal number of goals in 2 matches will not be considered an improvement. Also, he will be declared unfit if he doesn't have enough matches to show an improvement.

**Note:** Large input data. Use faster I/O methods. Prefer scanf,printf over cin/cout.

**Input**

- The first line of the input contains a single integer $T$, the number of test cases.
- Each test case begins with a single integer $N$, the number of practice matches Rayne has played.
- The next line contains $N$ integers. The $i^{th}$ integer, $g_i$, on this line represents the number of goals Rayne scored in his $i^{th}$ practice match. The matches are given in chronological order i.e. $j > i$ means match number $j$ took place after match number $i$.

**Output**

For each test case output a single line containing the maximum goal difference that Rayne can show to his coach and manager. If he's not fit yet, print "UNFIT".

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 100000$
- $0 \leq g_i \leq 1000000$ (Well, Rayne's a legend! You can expect him to score so many goals!)

## Sample

**Sample input**

```
3
6
3 7 1 4 2 4
5
5 4 3 2 1
5
4 3 2 2 3
```

**Sample output**

```
4
UNFIT
1
```

<details><summary>Explanation</summary>

In the first test case, Rayne can choose the first and second game. Thus he gets a difference of 7-3=4 goals. Any other pair would give him a lower improvement.
In the second test case, Rayne has not been improving in any match. Thus he's declared UNFIT.

</details>

## Approach

This is the classic "best buy/sell" scan. Walk the matches in chronological order holding the **smallest score seen so far**; at each match, the best improvement ending here is the current score minus that running minimum. Keep the largest such value.

$$\text{answer} = \max_{j} \left( g_j - \min_{i < j} g_i \right)$$

One pass, $O(N)$ time and $O(1)$ space. The quadratic version — comparing every pair — is $10^{10}$ operations at $N = 10^5$ and is exactly what the problem's warning about large input is hinting against.

The chronological constraint is what makes the running minimum the right structure: the earlier match must come first, so a low score *after* a high one cannot be used. Sample case 2, a strictly decreasing $[5,4,3,2,1]$, has no valid pair at all and prints `UNFIT`.

That `UNFIT` case needs care. The improvement must be **strictly positive** — equal scores do not count as improvement — so the running best should start at $0$ and the answer printed only if it exceeds $0$. Sample case 3, $[4,3,2,2,3]$, contains the equal pair $(2,2)$ worth $0$ and the genuine pair $(2,3)$ worth $1$, answering $1$.

Updating the running minimum **after** computing the candidate is what keeps $i < j$ strict; updating first would allow a match to be compared against itself, yielding a spurious $0$ — harmless here, but the wrong habit.

Sample case 1 picks up $7 - 3 = 4$ early and never beats it, even though the array dips to $1$ later.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        g = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        best = 0
        lowest = int(g[0])
        for v in g[1:]:
            x = int(v)
            # Compare before updating, so the earlier match is strictly earlier.
            if x - lowest > best:
                best = x - lowest
            if x < lowest:
                lowest = x
        out.append(str(best) if best > 0 else "UNFIT")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The comparison must come before the minimum is updated**, so the earlier match is strictly earlier. Updating first would let a match pair with itself and record a gain of $0$.
- **A gain of exactly $0$ is not fit.** The third row has two consecutive $2$s, and that pairing is rejected; only a strictly positive improvement counts, which the `best = 0` start plus `> best` enforces.
- **Non-increasing goal counts** (the second row) → `UNFIT`.
- **The best pair need not involve the global minimum or maximum.** The first row's answer pairs the opening $3$ with the $7$ right after it, both of which precede the global minimum of $1$ — so tracking only the overall extremes gives the wrong pair.
- **$g_i$ may be $0$**, which is an ordinary value and a legitimate running minimum.
- **$N = 1$**: the loop never runs, so `UNFIT` is printed.

## Dry run

First sample: goals $3, 7, 1, 4, 2, 4$.

| match | goals | running min before | gain | best |
|---:|---:|---:|---:|---:|
| 2 | 7 | 3 | 4 | **4** |
| 3 | 1 | 3 | $-2$ | 4 |
| 4 | 4 | 1 | 3 | 4 |
| 5 | 2 | 1 | 1 | 4 |
| 6 | 4 | 1 | 3 | 4 |

Output `4`, from the first two matches.

> CodeChef tags: `Data Structures`, `Arrays`, `Algorithms`, `Constructive`, `Simple Algos`

---

Same problem in rating order (#238 of 486): [../../by-rating/238-PLAYFIT.md](../../by-rating/238-PLAYFIT.md)
