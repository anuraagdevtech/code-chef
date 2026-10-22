[&larr; 85. Binary Battles](BIN_BAT.md) &middot; [Index](../../README.md) &middot; [91. The Cooler Dilemma 2 &rarr;](WATERCOOLER2.md)

# 86. Best of Two

> CodeChef problem code [`DICEGAME2`](https://www.codechef.com/problems/DICEGAME2) &middot; difficulty **789** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Total minus the extremum, then compare |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Alice and Bob are playing a game. Each player rolls a standard six-sided die three times.
The score of a player is calculated as the sum of the two highest rolls. The player with the higher score wins. If both players have the same score, the game ends in a tie.

Determine the winner of the game or if it is a tie.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case contains six space-separated integers $A_1$,  $A_2$,  $A_3$,  $B_1$, $B_2$ and $B_3$ — the values Alice gets in her $3$ dice rolls, followed by the values which Bob gets in his $3$ dice rolls.

**Output**

For each test case, output on a new line `Alice` if Alice wins, `Bob` if Bob wins and `Tie` in case of a tie.

Note that you may print each character in uppercase or lowercase. For example, the strings `tie`, `TIE`, `Tie`, and `tIe` are considered identical.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq A_1, A_2, A_3, B_1, B_2, B_3 \leq 6$

## Sample

**Sample input**

```
3
3 2 5 6 1 1
4 4 5 6 4 1
6 6 6 6 6 1
```

**Sample output**

```
Alice
Bob
Tie
```

<details><summary>Explanation</summary>

**Test Case $1$:** Alice's score is $8 = (3 + 5)$ which is greater than Bob's score $7 = (6 + 1)$.

**Test Case $2$:** Alice's score is $9 = (5 + 4)$ which is less than Bob's score $10 = (6 + 4)$.

**Test Case $3$:** Alice's score is $12 = (6 + 6)$ which is same as Bob's score $12 = (6 + 6)$.

</details>

## Approach

Each player's score is the sum of their **two highest** of three rolls, which is the same as dropping the lowest:

$$\text{score} = A_1 + A_2 + A_3 - \min(A_1, A_2, A_3)$$

Computing it this way avoids sorting or a top-two scan, and it handles ties for the lowest roll correctly — only one copy is dropped. Sample case 3 relies on that: Alice rolls $6,6,6$ and scores $12$, discarding exactly one six rather than all of them.

With both scores in hand the result is a three-way comparison: `Alice`, `Bob`, or `Tie`. The equality branch is required — sample case 3 ends level at $12$ apiece.

The input packs both players onto one line as six integers, with Alice's three first. Splitting them in the wrong place is the main hazard; sample case 2 would otherwise look winnable for Alice.

Working through case 2: Alice has $4,4,5$ for $13 - 4 = 9$; Bob has $6,4,1$ for $11 - 1 = 10$. Bob wins, even though his rolls include the lowest single die on the table — dropping it is exactly what the scoring rule lets him do.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        v = list(map(int, data[1 + 6 * i:7 + 6 * i]))
        a, b = v[:3], v[3:]
        # Best two of three = total minus the single lowest roll.
        sa, sb = sum(a) - min(a), sum(b) - min(b)
        out.append("Alice" if sa > sb else "Bob" if sb > sa else "Tie")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The totals mislead.** In the sample's second row Alice rolls $4, 4, 5$ for a total of $13$ against Bob's $6, 4, 1$ totalling $11$ — yet **Bob wins**, because dropping each player's lowest roll leaves $9$ against $10$. Comparing raw totals gives the wrong winner here, which is the whole point of the row.
- **A tie** ($12$ each in the third row): needs its own branch.
- **All three rolls equal** ($6, 6, 6$): one of the tied minima is dropped, giving $12$.
- **The lowest roll is discarded, not the highest** — inverting that flips most answers.
- With exactly three dice, "best two" is simply the total minus the single minimum, so no sorting is needed.

## Dry run

| Alice | total | $-\min$ | Bob | total | $-\min$ | output |
|---|---:|---:|---|---:|---:|---|
| $3, 2, 5$ | 10 | 8 | $6, 1, 1$ | 8 | 7 | `Alice` |
| $4, 4, 5$ | 13 | 9 | $6, 4, 1$ | 11 | 10 | `Bob` |
| $6, 6, 6$ | 18 | 12 | $6, 6, 1$ | 13 | 12 | `Tie` |

Row 2 reverses on the discard; row 3 ties despite very different totals.

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#91 of 486): [../../by-rating/091-DICEGAME2.md](../../by-rating/091-DICEGAME2.md)
