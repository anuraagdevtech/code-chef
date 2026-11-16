---
topic: Dynamic Programming
subtopic: Suffix as a function on the three moves, composed right to left
time: $O(N)$ per test case
space: $O(N)$ for the output, $O(1)$ state
complexity_note: Auxiliary space excludes the buffered input and output.
---
Think of the players $i+1, \dots, N$ as a machine: a current winner enters holding some move $x$ and after all the duels some move comes out. Call this function $f_{i+1}$; it has only three inputs. Then $W(i, N) = f_{i+1}(S_i)$.

Going one step to the left prepends one duel: an incoming move $x$ first meets $S_i$ and the survivor continues, so

$$f_i(x) = f_{i+1}(\text{winner}(x, S_i)),$$

where the winner is $S_i$ if it beats $x$ and $x$ otherwise. Scanning from right to left and updating the three values gives every $f_i$ in constant time. Because a move does not lose to itself, $f_i(S_i) = f_{i+1}(S_i)$, so the answer for position $i$ can be read off right after the update.

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
