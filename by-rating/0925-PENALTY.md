# 925 &middot; Penalty Shots

> CodeChef problem code [`PENALTY`](https://www.codechef.com/problems/PENALTY) &middot; time limit **0.5s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Summing alternate positions |
| **CodeChef tags** | `Basic Programming Concepts`, `Algorithms`, `Conditional Statements`, `Brute Force`, `Implementation` |
| **CodeChef category** | school |
| **Time** | $O(1)$ per test case — ten fixed entries |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/arrays/PENALTY.md](../docs/arrays/PENALTY.md)

## Question

It's the soccer match finals in Chefland and as always it has reached the penalty shootouts.
Each team is given $5$ shots to make and the team scoring a goal on the maximum number of shots wins the game. If both the teams' scores are equal, then the game is considered a draw and we would have $2$ champions.

Given ten integers $A_1, A_2, \ldots, A_{10}$, where the odd indexed integers($A_1, A_3,$ $A_5,$ $A_7, A_9$) represent the outcome of the shots made by team $1$ and even indexed integers($A_2, A_4, A_6, A_8, A_{10}$) represent the outcome of the shots made by team $2$ (here $A_i = 1$ indicates that it's a goal and $A_i = 0$ indicates a miss), determine the winner or find if the game ends in a draw.

**Input**

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains ten space-separated integers $A_1, A_2, \ldots, A_{10}$.

**Output**

For each test case, print a single line containing one integer - $0$ if the game ends in a draw or $1$ if the first team wins or $2$ if the second team wins.

## Constraints

- $1 \leq T \leq 1024$
- $0 \leq A_i \leq 1$

## Sample

**Sample input**

```
4
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 1
1 0 1 0 0 0 0 0 0 0 
1 1 1 1 1 1 1 1 1 0
```

**Sample output**

```
0
2
1
1
```

<details><summary>Explanation</summary>

**Test case $1$:** No team scores any goal, so the game ends in a draw.

**Test case $2$:** The second team is able to score in their final shot, while the first team has scored 0 goals and hence the second team wins.

**Test case $3$:** The first team is successfully able to make their first $2$ shots count and whereas the second team has not scored any goals. Therefore the first team wins.

**Test case $4$:** Team $2$ misses their final shot and hence team $1$ wins the game with the final score of $5 - 4$.

</details>

## Approach

The ten outcomes interleave the two teams: positions $1, 3, 5, 7, 9$ belong to team 1 and positions $2, 4, 6, 8, 10$ to team 2. Since a goal is encoded as $1$ and a miss as $0$, each team's score is simply the sum of its own positions.

Python's slice stride does the deinterleaving in one step. With the list read zero-based, `a[0::2]` picks the odd-numbered shots (team 1) and `a[1::2]` the even-numbered ones (team 2).

The indexing base is the thing to be careful about. The statement numbers shots from $1$, so team 1 owns the **odd** labels — which land on the **even** zero-based indices. Getting this backwards swaps the teams, and sample case 2 would catch it: a lone goal in the final position belongs to team 2, so the answer is $2$.

Then a three-way comparison yields $1$, $2$, or $0$ for a draw. Note the unusual output encoding: $0$ means draw rather than "team 0", and sample case 1 — ten misses — is a $0$–$0$ draw.

Summing booleans directly works because the values are already $0$ and $1$; no conversion to goals is needed.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a = list(map(int, data[1 + 10 * i:11 + 10 * i]))
        # Shots are numbered from 1, so team 1 holds the even zero-based slots.
        t1, t2 = sum(a[0::2]), sum(a[1::2])
        out.append("1" if t1 > t2 else "2" if t2 > t1 else "0")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case — ten fixed entries
- **Space:** $O(1)$
