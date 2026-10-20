# 87. The Lead Game

> CodeChef problem code [`TLG`](https://www.codechef.com/problems/TLG) &middot; difficulty **1190** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Running totals with a tracked maximum |
| **Time** | $O(N)$ |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

The game of billiards involves two players knocking 3 balls around
on a green baize table. Well, there is more to it, but for our
purposes this is sufficient.

 The game consists of several rounds and in each round both players
obtain a score, based on how well they played. Once all the rounds
have been played, the total score of each player is determined by
adding up the scores in all the rounds and the player with the higher
total score is declared the winner.

 The Siruseri Sports Club organises an annual billiards game where
the top two players of Siruseri play against each other. The Manager
of Siruseri Sports Club decided to add his own twist to the game by
changing the rules for determining the winner. In his version, at the
end of each round, the **cumulative score** for each player is calculated, and the leader and her current lead are found. Once
all the rounds are over the player who had the maximum lead at the
end of any round in the game is declared the winner.

Consider the following score sheet for a game with 5 rounds:

  <th>Round</th>
    <th>Player 1</th>
    <th>Player 2</th>
  1
    140
    82
  2
    89
    134
  3
    90
    110
  4
    112
    106
  5
    88
    90

The total scores of both players, the leader and the lead after
each round for this game is given below:

  <th>Round</th>
    <th>Player 1</th>
    <th>Player 2</th>
    <th>Leader</th>
    <th>Lead</th>
  1
    140
    82
    Player 1
    58
  2
    229
    216
    Player 1
    13
  3
    319
    326
    Player 2
    7
  4
    431
    432
    Player 2
    1
  5
    519
    522
    Player 2
    3
  Note that the above table contains the cumulative scores.

 The winner of this game is Player 1 as he had the maximum lead (58
at the end of round 1) during the game.

 Your task is to help the Manager find the winner and the winning
lead. You may assume that the scores will be such that there will
always be a single winner.  That is, there are no ties.

Input

 The first line of the input will contain a single integer N (N
≤ 10000) indicating the number of rounds in the game.  Lines
2,3,...,N+1 describe the scores of the two players in the N rounds.
Line i+1 contains two integer Si and Ti, the scores of the Player 1
and 2 respectively, in round i.  You may assume that 1 ≤ Si ≤
1000 and 1 ≤ Ti ≤ 1000.

Output

 Your output must consist of a single line containing two integers
W and L, where W is 1 or 2 and indicates the winner and L is the
maximum lead attained by the winner.

## Constraints

- $1 \leq N \leq 10^4$
- $1 \leq S_i, T_i \leq 1000$

## Sample

**Sample input**

```
5
140 82
89 134
90 110
112 106
88 90
```

**Sample output**

```
1 58
```

## Approach

The winner is not the player with the higher final score — it is whoever held the **largest lead at the end of any single round**. Sample case aside, those are genuinely different questions: in the worked example Player 2 finishes ahead on total score, yet Player 1 wins because of a $58$-point lead after round 1.

The solution is one pass maintaining two running totals. After adding each round's scores, the current lead is $|s_1 - s_2|$ and the leader is whoever is ahead. Track the largest lead seen so far along with its owner, and report that pair at the end.

Only the running sums and the best-so-far need storing, so this is $O(N)$ time and $O(1)$ space — the per-round table in the statement is an explanation, not a data structure to build.

Two details decide correctness. The lead must be computed from **cumulative** scores, not the round's own scores; using per-round values would make round 1 and round 5 look similar when their cumulative pictures are nothing alike. And the comparison for a new best should be strict (`>`), so that the *earliest* round achieving a given maximum is kept — though with the winner determined by the lead's magnitude, ties in lead value between the same leader change nothing either way.

The input is a single test case: $N$, then $N$ pairs. Output is the winning player's number and that maximum lead, space-separated.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    n = int(data[0])
    s1 = s2 = 0
    best_lead, best_player = 0, 1
    for i in range(n):
        s1 += int(data[1 + 2 * i])
        s2 += int(data[2 + 2 * i])
        # The lead is measured on cumulative totals, not the round's scores.
        lead = abs(s1 - s2)
        if lead > best_lead:
            best_lead = lead
            best_player = 1 if s1 > s2 else 2
    print(best_player, best_lead)


main()
```

## Complexity

- **Time:** $O(N)$
- **Space:** $O(1)$

> CodeChef tags: `Data Structures`, `Arrays`, `Basic Programming Concepts`, `Algorithms`
