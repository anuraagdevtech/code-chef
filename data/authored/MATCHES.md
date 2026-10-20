---
topic: Basic Math
subtopic: Per-digit lookup table
time: $O(d)$ per test case
space: $O(1)$
---
Compute $A + B$ first, then count the matchsticks its decimal representation needs. Each digit has a fixed cost on a seven-segment display:

| digit | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 |
|---|---|---|---|---|---|---|---|---|---|---|
| matches | 6 | 2 | 5 | 5 | 4 | 5 | 6 | 3 | 7 | 6 |

so the answer is the sum of those costs over the digits of the sum. Holding the table as a tuple indexed by digit turns it into a one-line sum over the string form of $A + B$.

The ordering is what matters: the matches count the **result**, not the operands. Counting the digits of $A$ and $B$ separately would answer a different question entirely — sample case 3 makes this unmissable, where $4 + 4 = 8$ costs $7$ matches, far more than the $4 + 4 = 8$ matches the inputs would suggest.

The table itself is worth memorising, or at least deriving from the seven-segment shapes: $1$ is cheapest at $2$, $7$ next at $3$, and $8$ is the most expensive at $7$ since it lights every segment.

Sample case 2 shows the digit count shrinking: $10101 + 1010 = 11111$, five `1`s at $2$ each for $10$ matches, where the operands have nine digits between them.

Working on the string form of the sum avoids a manual digit-extraction loop and its $0$ edge case — though with $A, B \geq 1$ the sum is at least $2$ and never zero anyway.
