[&larr; 601. Bytelandian Robots](F2.md) &middot; [Index](../../README.md) &middot; [642. Tetris &rarr;](SPCP6.md)

# 628. Rock Paper Scissors

> CodeChef problem code [`ROPASCI`](https://www.codechef.com/problems/ROPASCI) &middot; difficulty **2013** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Suffix as a function on the three moves, composed right to left |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ for the output, $O(1)$ state |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

There are $N$ players standing in a line, indexed $1$ to $N$ from left to right. They all play a game of Rock, Paper, Scissors. Each player has already decided which move they want to play. You are given this information as a string $S$ of length $N$, i.e,

- $S_i$ is equal to $\verb+R+$ if player $i$ will play Rock.
- $S_i$ is equal to $\verb+P+$ if player $i$ will play Paper.
- $S_i$ is equal to $\verb+S+$ if player $i$ will play Scissors.

Let $W(i, j)$ denote the move played by the winner if players $i, i+1, \ldots, j$ compete in order from left to right. That is,
- First, players $i$ and $i+1$ play a game
- The winner of this game plays against player $i+2$
- The winner of the second game plays against player $i+3$

$\vdots$

- The winner of the first $j-i-1$ games plays against player $j$, and the move played by the winner of this game is declared to be $W(i, j)$.

If $i = j$, then player $i$ is considered to be the winner and $W(i, i) = S_i$.

Your task is to find the value of $W(i,N)$ for all $i$ from $1$ to $N$.

**Note** :
If a person with index $i$ and index $j$ ($i \lt j$) play against each other, then:
- If $S_i \neq S_j$, the winner is decided by classical rules, i.e, rock beats scissors, scissors beats paper, and paper beats rock.
- If $S_i = S_j$, the player with lower index (in this case, $i$) wins.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$, the number of players.
- The second line of each test case contains the string $S$ of length $N$, denoting the moves chosen by the players.

**Output**

For each test case, print a single line containing a string of length $N$, whose $i$-th character is $W(i, N)$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 5\cdot 10^5$
- $S_i$ is either $\verb+R+$, $\verb+P+$ or $\verb+S+$
- Sum of $N$ over all test cases doesn't exceed $5 \cdot 10^5$

**Subtasks**

**Subtask 1 (10 points):**
- $1 \leq T \leq 1000$
- $1 \leq N \leq 5000$
- Sum of $N$ over all test cases doesn't exceed $5000$

**Subtask 2 (90 points):**
- Original constraints

## Sample

**Sample input**

```
2
1
S
4
SSPR
```

**Sample output**

```
S
RRPR
```

<details><summary>Explanation</summary>

**Test Case 1.** $W(1,1) = \verb+S+$ as there is only one player.

**Test Case 2.**

For $W(1,4)$ the game is played as follows  :
- Player $1$ and $2$ compete, player $1$ wins.
- Player $1$ and $3$ compete, player $1$ wins.
- Player $1$ and $4$ compete, player $4$ wins.

Hence, we print $W(1,4) = S_4 = \verb+R+$

For $W(3,4)$ the game is played as follows  :
- Player $3$ and $4$ compete, player $3$ wins.

Hence, we print $W(3,4) = S_3 = \verb+P+$

</details>

## Approach

Think of the players $i+1, \dots, N$ as a machine: a current winner enters holding some move $x$ and after all the duels some move comes out. Call this function $f_{i+1}$; it has only three inputs. Then $W(i, N) = f_{i+1}(S_i)$.

Going one step to the left prepends one duel: an incoming move $x$ first meets $S_i$ and the survivor continues, so

$$f_i(x) = f_{i+1}(\text{winner}(x, S_i)),$$

where the winner is $S_i$ if it beats $x$ and $x$ otherwise. Scanning from right to left and updating the three values gives every $f_i$ in constant time. Because a move does not lose to itself, $f_i(S_i) = f_{i+1}(S_i)$, so the answer for position $i$ can be read off right after the update.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    beat = {'R': 'P', 'P': 'S', 'S': 'R'}
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        moves = next(tokens).decode()
        outcome = {c: c for c in 'RPS'}
        winners = []
        for c in reversed(moves):
            old = outcome.copy()
            for x in 'RPS':
                outcome[x] = old[c if beat[x] == c else x]
            winners.append(outcome[c])
        out.append(''.join(reversed(winners)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$ for the output, $O(1)$ state
- Auxiliary space excludes the buffered input and output.

## Edge cases

- A single player wins with their own move.
- Equal moves never change the current winner's move, which is all that matters.
- The update must use the old table for all three entries - hence the copy.
- The total length over the test cases is bounded, so the constant work per character is enough.

## Dry run

`S = SSPR`, scanning from the right. The table is written as (R, P, S) -> outcomes.

| player | move | table after update | $W$ |
|---:|---|---|---|
| 4 | R | R, P, R | R |
| 3 | P | P, P, R | P |
| 2 | S | P, R, R | R |
| 1 | S | P, R, R | R |

Answer `RRPR`.

> CodeChef tags: `Data Structures`, `Algorithms`, `Dynamic Programming`, `DP Approach`

---

Same problem in rating order (#575 of 735): [../../by-rating/575-ROPASCI.md](../../by-rating/575-ROPASCI.md)
