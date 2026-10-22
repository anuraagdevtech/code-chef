---
topic: Combinatorics
subtopic: Independent cut choices between vowel blocks
time: $O(N)$ per test case
space: $O(N)$
---
Every piece holds exactly $K$ vowels, so with $m$ vowels in total there are exactly $m/K$ pieces and the cuts are **forced in position relative to the vowels**: the $j$-th cut must fall after vowel $jK$ and before vowel $jK+1$, for $j = 1, \ldots, m/K - 1$.

What is *not* forced is where among the consonants in between. If those two vowels sit at indices $v_{jK}$ and $v_{jK+1}$, the cut may go in any of the gaps strictly after the first and up to the second, giving $v_{jK+1} - v_{jK}$ placements. The cuts are independent — each lies in its own stretch — so the count multiplies:

$$\text{answer} = \prod_{j=1}^{m/K - 1} \bigl(v_{jK+1} - v_{jK}\bigr) \pmod{10^9+7}$$

Note there are $m/K - 1$ factors, not $m/K$: the final piece ends at the string's end, which is not a choice. Leading and trailing consonants likewise contribute nothing, since they must attach to the first and last piece.

The guarantee that $K$ divides $m$ is what makes the product well defined; otherwise the answer would be $0$.

For `neo` with $K = 1$ the two vowels are adjacent (indices $1$ and $2$), so the single cut has one placement: the answer is $1$. For `babylonian` with $K = 2$ the cut must separate the second vowel `o` (index $5$) from the third, `i` (index $7$), and the consonant `n` between them gives two placements — `babylon|ian` and `babylo|nian` — so the answer is $2$.

## Edge cases

- **Only the cut positions between consecutive vowel blocks are free.** A piece must hold exactly $K$ vowels, so the cut after the $j$-th block may sit anywhere strictly between the $jK$-th vowel and the $(jK+1)$-th — giving as many choices as the index gap between them.
- **The choices are independent**, so the answer is the product of those gaps.
- **Consonants between two vowels widen the gap**, and consonants at the very ends contribute nothing — they are glued to the first or last piece whatever happens.
- **One block means no cuts**, so the answer is $1$ — the first sample row, where $K = 1$ and the two vowels sit adjacent, also gives a gap of $1$.
- **The vowel count is guaranteed to be a multiple of $K$**, so the blocks divide evenly and no leftover case arises.
- **The loop starts at $j = K$ and steps by $K$**, which visits exactly the block boundaries and skips the final block (there is no cut after the last piece).
- **Sum of $N \leq 10^6$**, so the vowel positions are collected in one pass and the product is taken modulo $10^9+7$.

## Dry run

Second sample: $S = $ `babylonian` with $K = 2$. Vowels sit at indices $1$ (`a`), $5$ (`o`), $7$ (`i`), $8$ (`a`).

| block | vowels | boundary |
|---:|---|---|
| 1 | indices $1, 5$ | cut after vowel 2 |
| 2 | indices $7, 8$ | — (last block) |

The single cut may fall anywhere between index $5$ and index $7$, which is $7 - 5 = 2$ positions. Output `2`.
