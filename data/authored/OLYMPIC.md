---
topic: Combinatorics
subtopic: Burnside for reversal, with multinomials updated along a sweep over box sizes
time: $O(S + Q \log Q + E \log N)$, $S$ the total number of chocolates and $E = \sum O(\sqrt{count})$ breakpoints
space: $O(S + Q + E)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
With box size $s$, village $i$ needs $b_i = \lceil count_i / s \rceil$ boxes of its own colour, and the boxes are laid in a row where a row and its mirror image are the same pack. By Burnside's lemma for the two-element group {identity, reversal}

$$\text{answer} = \frac{\text{all arrangements} + \text{palindromic arrangements}}{2}.$$

All arrangements: the multinomial $(\sum b_i)! / \prod b_i!$. A palindrome exists only if at most one $b_i$ is odd; it is determined by its first half, so there are $(\lfloor \sum b_i / 2 \rfloor)! / \prod \lfloor b_i / 2 \rfloor!$ of them.

Recomputing this per query is too slow. Instead sort the distinct query sizes and sweep $s$ upwards: $\lceil c / s \rceil$ takes only $O(\sqrt{c})$ different values, so precompute for each distinct village count the sizes at which its box count drops, and at each such breakpoint patch the running total, the number of odd counts and the two denominators (multiply by old factorial, divide by new). Equal village counts are merged and handled with one modular power.

## Edge cases

- More than one odd box count means no palindromic row at all.
- A box size at least as large as every count gives one box per village: $N!$ arrangements, halved (plus palindromes only when $N \le 1$).
- The same box size may be queried repeatedly; answers are stored per distinct size.
- Division by 2 is multiplication by $(p + 1) / 2$.

## Dry run

Villages `5 3 12`.

- $s = 4$: boxes `2 1 3`. All: $6! / (2! \, 1! \, 3!) = 60$. Two odd counts, so no palindromes. Answer $60 / 2 = 30$.
- $s = 2$: boxes `3 2 6`. All: $11! / (3! \, 2! \, 6!) = 4620$. One odd count; half sizes `1 1 3` give $5! / 3! = 20$ palindromes. Answer $(4620 + 20) / 2 = 2320$.
- $s = 12$: boxes `1 1 1`: $(6 + 0) / 2 = 3$.
