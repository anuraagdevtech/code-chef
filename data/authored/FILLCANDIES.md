---
topic: Basic Math
subtopic: Ceiling division by a composite capacity
time: $O(1)$ per test case
space: $O(1)$
---
Work out the capacity of one bag first. It has $K$ pockets and each pocket takes at most $M$ candies, so a bag holds $K \cdot M$. Every candy must be placed and bags cannot be split, so the count rounds up:

$$\left\lceil \frac{N}{K \cdot M} \right\rceil$$

written in integers as `(n + k * m - 1) // (k * m)`.

Composing the capacity before dividing is the key move. Dividing by $K$ and then by $M$ in two steps is *not* equivalent once rounding enters — each step would round separately and inflate the result. With $N = 25, K = 4, M = 2$ the correct answer is $\lceil 25/8 \rceil = 4$, whereas rounding up at each stage gives $\lceil \lceil 25/2 \rceil / 4 \rceil = \lceil 13/4 \rceil = 4$ here but diverges on other inputs. Collapsing to a single division by $KM$ avoids the question entirely.

It is also worth seeing that the pockets impose no extra constraint. Candies are interchangeable and may be spread freely across pockets, so a bag is simply a container of size $KM$; nothing is wasted by an awkward split. Had each pocket needed to be filled completely, or had candies come in indivisible groups, the pocket structure would have mattered.

Sample case 2 is the ragged one: $3$ candies into bags of capacity $2$ needs $2$ bags, the second holding a single candy.
