[&larr; 407. Remove One Element](407-REMONE.md) &middot; [Index](README.md) &middot; [409. Average Gift &rarr;](409-AVGGIFT.md)

# 408. Chef and Football Match

> [`WATCHFB`](https://www.codechef.com/problems/WATCHFB) &middot; difficulty **1700** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Simulation |
| **Technique** | Tracking the at-most-two consistent states |
| **CodeChef tags** | `Special`, `Algorithms`, `Constructive`, `Case work`, `ad-hoc` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef and his son Chefu want to watch a match of their favourite football team playing against another team, which will take place today.

Unfortunately, Chef is busy in the kitchen preparing lunch, so he cannot watch the match. Therefore, every now and then, Chef asks Chefu about the current scores of the teams and Chefu tells him the score. However, Chefu sometimes does not specify the teams along with the score — for example, he could say "the score is 3 to 6", and there is no way to know just from this statement if it was their favourite team or the other team that scored 6 goals; in different statements, the order of teams may also be different. Other times, Chefu specifies which team scored how many goals.

Chef asks for the score and receives a reply $N$ times. There are two types of replies:
- `1 A B`: their favourite team scored $A$ goals and the other team scored $B$ goals
- `2 A B`: one team scored $A$ goals and the other scored $B$ goals

Chef is asking you to help him determine the score of his favourite team after each of Chefu's replies. After each reply, based on the current reply and all previous information (but without any following replies), tell him whether it is possible to certainly determine the number of goals scored by his favourite team.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The following $N$ lines describe Chefu's replies in the format described above.

**Output**
For each of Chefu's replies, print a single line containing the string `"YES"` if it is possible to determine the score of Chef's favourite team after this reply or `"NO"` if it is impossible.

**Constraints**
- $1 \le T \le 100$
- $1 \le N \le 10^4$
- $0 \le A, B \le 10^9$
- the sum of $N$ over all test cases does not exceed $10^5$
- there is at least one valid sequence of scored goals consistent with all replies

**Subtasks**
**Subtask #1 (100 points):** original constraints

## Constraints

- $1 \le T \le 100$
- $1 \le N \le 10^4$
- $0 \le A, B \le 10^9$
- the sum of $N$ over all test cases does not exceed $10^5$
- there is at least one valid sequence of scored goals consistent with all replies

## Sample

**Sample input**

```
1
6
2 0 1
1 3 1
2 2 4
2 5 6
2 8 8
2 9 10
```

**Sample output**

```
NO
YES
YES
NO
YES
NO
```

<details><summary>Explanation</summary>

**Example case 1:**
- Reply 1: Chef cannot know who scored the first goal.
- Reply 2: Chefu told Chef that their favourite team has scored $3$ goals so far.
- Reply 3: Chef can conclude that his favourite team has scored $4$ goals, since it already scored $3$ goals earlier.
- Reply 4: the favourite team could have scored $5$ or $6$ goals, but there is no way to know which option is correct.
- Reply 5: since there is a tie, Chef knows that his favourite team has scored $8$ goals.
- Reply 6: again, Chef cannot know if his favourite team has scored $9$ or $10$ goals.

</details>

## Approach

After each reply there are at most **two** candidate scores: $(A, B)$ and $(B, A)$ for an ambiguous reply, or just $(A, B)$ for a labelled one. So the state space never grows, and the whole problem is filtering those candidates against history.

The filter is **monotonicity**: goals accumulate, so the new score must dominate some previously possible score componentwise. Starting from the single state $(0,0)$, each reply becomes

$$\text{new} = \{\,c \in \text{candidates} : \exists\, p \in \text{states},\ c \geq p \text{ in both coordinates}\,\}$$

and the answer is `YES` precisely when every surviving state agrees on the favourite team's goals. That happens either because the reply was labelled, because $A = B$, or because monotonicity eliminated one of the two orderings.

Keeping the whole set of survivors matters: a later reply may be disambiguated by an earlier ambiguous one, and discarding information too early would wrongly report `NO`.

The sample shows each mechanism. The first reply, `2 0 1`, admits both $(0,1)$ and $(1,0)$ — `NO`. The second is labelled, so `YES` and the state collapses to $(3,1)$. The third, `2 2 4`, is ambiguous but $(2,4)$ cannot follow $(3,1)$ — the favourite's score would have dropped — so only $(4,2)$ survives: `YES`. The fourth, `2 5 6`, has both orderings dominating $(4,2)$, so `NO`. The fifth, `2 8 8`, is ambiguous in form but the two orderings coincide: `YES`. And the last, `2 9 10`, is ambiguous again.

Note the ambiguity can return after being resolved, as the last two replies show.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        states = [(0, 0)]
        for _ in range(n):
            kind = data[pos]
            a, b = int(data[pos + 1]), int(data[pos + 2])
            pos += 3
            cand = [(a, b)] if kind == b"1" or a == b else [(a, b), (b, a)]
            # Goals only accumulate, so a candidate must dominate some past state.
            states = [c for c in cand
                      if any(c[0] >= p[0] and c[1] >= p[1] for p in states)]
            out.append("YES" if len({c[0] for c in states}) == 1 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **At most two states survive each reply**, since an ambiguous score admits only the two orderings — so the whole history collapses to a tiny candidate set rather than needing a search.
- **Goals only accumulate**, so a candidate is viable only if it dominates some state consistent with the previous replies — that monotone filter is what prunes the ambiguity.
- **Equal scores are unambiguous even when the teams are unnamed**, which is why `a == b` collapses to a single candidate (the fifth reply, $8$ to $8$).
- **A type-1 reply names the teams**, so it always leaves one state — and it can retroactively resolve nothing, but it does narrow the future.
- **The answer is `YES` when all surviving states agree on the favourite team's score**, which is the deducible case — the second reply becomes deducible even though the first was not.
- **The first reply with distinct scores is always ambiguous**, since both orderings dominate the initial $0$–$0$.
- **At least one consistent sequence is guaranteed**, so the surviving set is never empty.

## Dry run

The sample's six replies, tracking the viable states as (favourite, other):

| reply | candidates | viable after filtering | deducible? |
|---|---|---|---|
| `2 0 1` | $(0,1)$, $(1,0)$ | both | `NO` |
| `1 3 1` | $(3,1)$ | $(3,1)$ | `YES` |
| `2 2 4` | $(2,4)$, $(4,2)$ | $(4,2)$ only — $(2,4)$ cannot follow $(3,1)$ | `YES` |
| `2 5 6` | $(5,6)$, $(6,5)$ | both | `NO` |
| `2 8 8` | $(8,8)$ | $(8,8)$ | `YES` |
| `2 9 10` | $(9,10)$, $(10,9)$ | both | `NO` |

The third reply is resolved by the second: a favourite-team score of $2$ would mean goals were lost.

---

Same problem grouped by topic: [../docs/simulation/WATCHFB.md](../docs/simulation/WATCHFB.md)
