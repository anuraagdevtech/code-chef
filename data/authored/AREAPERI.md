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

## Edge cases

- **Area equals perimeter**: then neither label applies and the answer is `Eq`. This happens for $L = B = 4$ (both $16$) and for $L = 3, B = 6$ (both $18$), so the third branch is genuinely reachable and must be there.
- **Smallest input** ($L = B = 1$): area $1$ against perimeter $4$, so `Peri` and $4$.
- **Largest input** ($L = B = 1000$): area $10^6$ against perimeter $4000$, so `Area`.
- **Output is two lines** — the label, then the winning value — and on `Eq` the value printed is the shared one.
- **Input shape**: two integers with no test-case count.

## Dry run

Input is $L = 1$, $B = 2$.

| step | value |
|---|---|
| area $L \times B$ | $2$ |
| perimeter $2(L + B)$ | $6$ |
| comparison | perimeter is larger |
| output | `Peri` then `6` |
