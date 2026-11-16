[&larr; 688. GCD Queries](688-GCD_QUERIES.md) &middot; [Index](README.md) &middot; [690. Adjacent Flips &rarr;](690-ADJFLIP.md)

# 689. Two Counters

> [`TWOCOUNTERS`](https://www.codechef.com/problems/TWOCOUNTERS) &middot; difficulty **2425** &middot; time limit **1.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Only the difference of the counters matters, and only within [-2, 2] |
| **CodeChef tags** | `Algorithms`, `Dynamic Programming` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N + M)$ per test case |
| **Space** | $O(M)$ |

## Question

You have $2$ counters $a$ and $b$, both initialised as $0$. You also have a score initialised as $0$.

At the start of every minute from minute $1$ to minute $N$, you **must** increase **either** $a$ or $b$ by $1$.

Additionally, there are $M$ events. The $i^{th}$ event happens at minute $T_i+0.5$ and has type $C_i$ $(C_i \in \{1, 2\})$.

At each event, the counters or the score is updated as:
```
if (type == 1):
    if (a > b):
        score = score + 1;
    else:
        a = 0;
        b = 0;
else:
    if (a < b):
        score = score + 1;
    else:
        a = 0;
        b = 0;
```

Your task is to **maximise** the score after $N$ minutes have passed.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $M$ — the number of minutes and the number of events.
    - The second line of each test case contains $M$ integers $T_1,T_2,\ldots,T_M$ — where the $i^{th}$ event happens at minute $T_i + 0.5$.
    - The third line of each test case contains $M$ integers $C_1,C_2,\ldots,C_M$ — the type of the $i^{th}$ event.

**Output**

For each test case, output on a new line, the maximum score after $N$ minutes have passed.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq M \leq N \leq 10^5$
- $1 \leq T_1 \lt T_2 \lt \ldots \lt T_M \leq N$
- $C_i \in \{1,2\}$
- The sum of $N$ over all test cases will not exceed $10^5$.

## Sample

**Sample input**

```
4
5 3
1 2 5
1 2 1
5 5
1 2 3 4 5
1 1 1 1 1
5 5
1 2 3 4 5
1 2 1 2 1
1 1
1
2
```

**Sample output**

```
2
5
3
1
```

<details><summary>Explanation</summary>

**Test case $1$:** We will demonstrate a way to achieve a score of $2$.

- In the first minute, we will increase $a$ by $1$ so that $a=1$ and $b=0$. Since there is an event with type $1$ and $a\gt b$ our score increases by $1$.
- In the second minute, we will increase $b$ by $1$ so that $a=1$ and $b=1$. Since there is an event with type $2$ and $a$ is not less than $b$, our score remains $1$ and the counters are reset.
- In the third minute, we will increase $a$ by $1$ so that $a=1$ and $b=0$. There are no events in this minute.
- In the fourth minute, we will increase $a$ by $1$ so that $a=2$ and $b=0$. There are no events in this minute.
- In the fifth minute, we will increase $a$ by $1$ so that $a=3$ and $b=0$. Since there is an event with type $1$ and $a\gt b$ our score increases by $1$.

Thus, the total score achieved is $2$.
It can be shown that there is no possible way for our score to be greater than $2$.

**Test case $2$:** We will demonstrate a way to achieve a score of $5$.

- In the first minute, we will increase $a$ by $1$ so that $a=1$ and $b=0$. Since there is an event with type $1$ and $a\gt b$ our score increases by $1$.
- In the second minute, we will increase $a$ by $1$ so that $a=2$ and $b=0$. Since there is an event with type $1$ and $a\gt b$ our score increases by $1$.
- In the third minute, we will increase $a$ by $1$ so that $a=3$ and $b=0$. Since there is an event with type $1$ and $a\gt b$ our score increases by $1$.
- In the fourth minute, we will increase $a$ by $1$ so that $a=4$ and $b=0$. Since there is an event with type $1$ and $a\gt b$ our score increases by $1$.
- In the fifth minute, we will increase $a$ by $1$ so that $a=5$ and $b=0$. Since there is an event with type $1$ and $a\gt b$ our score increases by $1$.

Thus, the total score achieved is $5$.
It can be shown that there is no possible way for our score to be greater than $5$.

</details>

## Approach

Every event only compares $a$ with $b$, and a reset sets both to 0, so the state is the difference $d = a - b$. Each minute $d$ changes by $\pm 1$; a type-1 event scores if $d > 0$ and otherwise resets $d$ to 0; a type-2 event scores if $d < 0$ and otherwise resets.

The difference never needs to leave $[-2, 2]$. An excursion that goes from 2 up to 3 and later comes back can be mirrored to go from 2 down to 1 and back: the sign of $d$ is the same at every moment, so every event has the same outcome, and the walk ends at the same value. The same holds on the negative side.

That leaves a DP with five states: `best[d]` is the maximum score with current difference $d$. Each minute shift the states by $\pm 1$ within the range, then apply the event of that minute, if any: add 1 to the states on the scoring side and merge all other states into $d = 0$ (taking the maximum).

## Solution

```python
import sys


def solve(tokens):
    n, m = (next(tokens), next(tokens))
    times = [next(tokens) for _ in range(m)]
    types = [next(tokens) for _ in range(m)]
    events = dict(zip(times, types))
    NEG = -10 ** 9
    best = [NEG, NEG, 0, NEG, NEG]
    for minute in range(1, n + 1):
        best = [best[1], max(best[0], best[2]), max(best[1], best[3]), max(best[2], best[4]), best[3]]
        kind = events.get(minute)
        if kind == 1:
            best = [NEG, NEG, max(best[:3]), best[3] + 1, best[4] + 1]
        elif kind == 2:
            best = [best[0] + 1, best[1] + 1, max(best[2:]), NEG, NEG]
    return str(max(best))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    minute = int(next(tokens))
    out = [solve(tokens) for _ in range(minute)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- The increment happens at the start of the minute and the event half a minute later, so the move comes first.
- $d = 0$ at an event never scores, whichever type it is.
- Minutes without an event only move the difference.
- Unreachable states use a large negative sentinel.

## Dry run

`N = 5`, events at minutes 1, 2, 5 with types 1, 2, 1.

- Minute 1: go to $d = 1$; type 1 scores: 1 point.
- Minute 2: the type-2 event needs $d < 0$, but from $d = 1$ only 0 or 2 is reachable: reset to 0, still 1 point. (Starting with $d = -1$ instead would score at minute 2 but not at minute 1 - also 1 point.)
- Minutes 3-5: three moves from 0 can end at $d = 1$; type 1 scores: 2 points.

Answer 2.

---

Same problem grouped by topic: [../docs/dynamic-programming/TWOCOUNTERS.md](../docs/dynamic-programming/TWOCOUNTERS.md)
