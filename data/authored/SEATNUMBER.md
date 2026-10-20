---
topic: Conditionals & Case Work
subtopic: Decomposing an index into deck and position
time: $O(1)$ per test case
space: $O(1)$
---
The answer has two independent halves — which deck, and single or double — so the clean approach is to compute each separately and join them, rather than enumerating all four combinations.

**Deck.** There are $30$ seats split into two decks of $15$. Seats $1$–$15$ are Lower and $16$–$30$ are Upper, so the test is `n <= 15`.

**Position within the deck.** Reduce the seat to its offset inside its own deck:

$$p = ((N - 1) \bmod 15) + 1$$

The $-1$ and $+1$ convert to and from zero-based indexing, which is what makes the modulo land in the range $1..15$ rather than $0..14$. Seat $16$ maps to $p = 1$, seat $28$ maps to $p = 13$.

**Single or double.** Within each deck the first $10$ seats form five double berths and the last $5$ are singles, so $p \leq 10$ is Double and $p \geq 11$ is Single. This matches every anchor the problem gives: seats $1$ and $2$ are Double, seat $11$ is Single, and the samples confirm $p = 6, 10$ Double against $p = 13$ Single — the latter twice, once as seat $13$ (Lower) and once as seat $28$ (Upper).

Because the two decks are numbered identically, computing $p$ once and reusing it for both decks avoids writing the seat layout twice. Combining two independent binary decisions this way turns four cases into two.
