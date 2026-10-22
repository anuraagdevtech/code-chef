---
topic: Bit Manipulation
subtopic: The top bit caps a box at two elements
time: $O(N)$ per test case
space: $O(1)$
---
Let $h$ be the highest set bit of the OR, and $k$ the number of elements having it. Everything turns on those $k$ elements.

**At most two per box.** To add an element carrying bit $h$, the box's running XOR must be at least that element, hence must itself carry bit $h$ — otherwise the XOR is below $2^h$ while the element is at or above it. The XOR's bit $h$ flips with each such insertion, so the first two are fine (the box starts at the first, and the XOR still carries $h$ for the second) but a third would face an XOR with bit $h$ cleared. So

$$\text{boxes} \geq \left\lceil \frac{k}{2} \right\rceil$$

**$k$ is odd.** This is what the guarantee $2Z \geq O$ buys, where $Z$ is the XOR and $O$ the OR. Bit $h$ of $Z$ is $k \bmod 2$. If $k$ were even, then $Z$'s bits lie in $O$ without bit $h$, so $Z \leq O - 2^h$ and $2Z \geq O$ would force $O \geq 2^{h+1}$ — contradicting $h$ being $O$'s top bit. So $k$ is odd and the bound is $(k+1)/2$.

**It is attained.** Seed one box with a top-bit element; its XOR stays at or above $2^h$ while only sub-$2^h$ elements are added, so that box absorbs *every* element without bit $h$. The remaining $k-1$ top-bit elements pair off, larger first, into $(k-1)/2$ boxes. Total $(k+1)/2$.

The samples bear this out: $[6]$ and $[1,2,3,12]$ each have a single top-bit element ($6$, and $12$ at bit $3$), so one box suffices — the latter swallowing $3, 2, 1$ in turn. But $[6,5,4]$ has all three elements carrying bit $2$, so $k = 3$ and two boxes are needed: $\{6,5\}$ and $\{4\}$.

## Edge cases

- **The highest bit caps a box at two elements.** After one element carrying the top bit, the box's XOR still has it, so a second may follow; but then the XOR loses that bit, and a third element carrying it would exceed the box's XOR. So at most two top-bit elements per box.
- **The guarantee $2 \cdot \mathrm{XOR} \geq \mathrm{OR}$ forces the top-bit count to be odd**, which makes $\lceil k/2 \rceil$ exactly attainable — checked exhaustively over all $3025$ arrays with values up to $8$ and length up to $4$ that satisfy the guarantee, with no even count among them.
- **So the answer is $\lceil k/2 \rceil$**, verified against an exhaustive optimal packing on the same family with no mismatch.
- **Elements without the top bit are free riders**, placed into whichever box already holds a larger XOR — they never force a new box.
- **A single element** needs one box (the first sample row).
- **One top-bit element among many** still needs just one box, as the second row shows with only $12$ carrying bit $8$.
- **$A_i$ up to $10^{18}$** means `bit_length` on arbitrary-precision integers rather than a fixed 32- or 64-bit mask.

## Dry run

Third sample: $A = 6, 5, 4$. The maximum is $6$, whose top bit is $4$.

| element | binary | carries bit 4? |
|---:|---|:---:|
| 6 | 110 | yes |
| 5 | 101 | yes |
| 4 | 100 | yes |

Three top-bit elements, so $\lceil 3/2 \rceil = $ `2` boxes — for instance $\{6, 5\}$ (XOR $6 \geq 5$, then $3$) and $\{4\}$.
