---
topic: Greedy
subtopic: Largest two pairs by frequency
time: $O(N \log N)$ per test case
space: $O(N)$
---
A rectangle needs two sticks of one length and two of another (a square being the case where both lengths coincide). So the question is which lengths are available **in pairs**, and the answer takes the two largest of those.

Count occurrences of each length. A length appearing $c$ times contributes $\lfloor c/2 \rfloor$ pairs — importantly, a length appearing four or more times supplies **both** sides on its own, forming a square. Collect all available pairs as a list of lengths, sort descending, and if at least two exist the answer is the product of the top two; otherwise $-1$.

The count-four case is the one most easily missed. With sticks $[5,5,5,5]$ the answer is $25$, not $-1$: one length yields two pairs. Treating each distinct length as contributing at most one pair would wrongly reject it.

Maximising the **area** rather than the perimeter is why the two largest pairs are taken: for a fixed choice of two available lengths $a \geq b$, the area is $ab$, and swapping in any larger available length only increases it. So the greedy is immediate — no comparison of candidate rectangles is needed.

Sample case 1, $[1,2,3,1,2]$, has pairs at lengths $1$ and $2$, giving $2 \times 1 = 2$. Sample case 2, $[1,2,2,3]$, has only a single pair and answers $-1$.

With $A_i \leq 10^3$ a frequency array would also work and would be marginally faster than a dictionary, but the sum of $N$ is only $10^3$ so either is comfortable.

## Edge cases

- **Four sticks of one length form a square** without a special case: `c // 2` emits that length twice, and the two largest pair lengths then happen to be equal.
- **Exactly one pair available** (the second row, where only the $2$s pair up): $-1$, since a rectangle needs two pairs.
- **No pair at all** (every length appearing once): $-1$.
- **Odd leftovers are discarded** — a count of $3$ yields one pair and one unused stick, and a count of $5$ yields two pairs.
- **The two largest pairs give the largest area**, because the area is a product of two independently chosen positive lengths, so maximising each factor maximises the product.
- Sorting the pair lengths descending and taking the first two also handles the equal-pair case naturally, since both copies are adjacent.

## Dry run

First sample: $1, 2, 3, 1, 2$.

| length | count | pairs contributed |
|---:|---:|---|
| 1 | 2 | one pair of $1$ |
| 2 | 2 | one pair of $2$ |
| 3 | 1 | none |

Pair lengths sorted descending: $2, 1$ → area $2 \times 1 = $ `2`.

The second sample has counts $\{1{:}1, 2{:}2, 3{:}1\}$, so only one pair exists and the output is `-1`.
