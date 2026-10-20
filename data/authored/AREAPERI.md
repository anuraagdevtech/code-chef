---
topic: Geometry
subtopic: Comparing area against perimeter
time: $O(1)$
space: $O(1)$
---
For a rectangle with sides $L$ and $B$:

$$\text{area} = L \cdot B, \qquad \text{perimeter} = 2(L + B)$$

Compare them, print the label on the first line and the larger value on the second.

Comparing an area against a perimeter is dimensionally meaningless in physical terms — one is square units, the other linear — but as a numeric exercise it is well defined, and the problem simply wants the two numbers compared.

The output format is the part to get right: **two lines**, the word then the number. Print `Area`, `Peri`, or `Eq`, then the corresponding value. On a tie either value may be printed, and since they are equal it does not matter which expression is evaluated.

There is **no $T$** and the two inputs arrive on **separate lines** — $L$ first, then $B$. Reading them as one line of two tokens happens to work when parsing the whole stream as whitespace-separated tokens, which is what the solution below does, so the line structure is handled for free.

The sample is a thin rectangle where the perimeter wins: $L=1, B=2$ gives area $2$ against perimeter $6$. For most small rectangles the perimeter dominates; area overtakes it only once both sides grow past about $4$, with equality on cases such as $4 \times 4$ and $3 \times 6$.
