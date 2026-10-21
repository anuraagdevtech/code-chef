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
