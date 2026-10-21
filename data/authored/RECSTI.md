---
topic: Greedy
subtopic: Pairing by length, then pairing the pairs
time: $O(N + \max L)$ per test case
space: $O(\max L)$
---
A rectangle is two sticks of one length and two of another (equal lengths give a square), so the construction has **two levels**: sticks pair up by equal length, and pairs group up in twos to form rectangles. Both levels are forced, so the minimum additions follow by counting.

At the first level, a length occurring $c$ times gives $\lfloor c/2 \rfloor$ complete pairs and, when $c$ is odd, one orphan. Each orphan needs exactly one new stick of its own length, so

$$\text{additions}_1 = \#\{\text{lengths with odd count}\}, \qquad \text{pairs} = \sum_\ell \left\lceil \frac{c_\ell}{2} \right\rceil$$

At the second level, every rectangle consumes two pairs. If the pair count is odd, one pair is left over and needs a partner — a brand-new pair of two identical sticks, so $+2$. There is no cheaper fix: a single extra stick cannot form a pair on its own once every length already has an even count.

$$\text{answer} = \#\{\text{odd counts}\} + 2 \cdot (\text{pairs} \bmod 2)$$

The samples walk through the cases. A lone stick needs $1$ to make its pair and $2$ more for a second pair, giving $3$ — the worst case for $N = 1$. Two sticks of different lengths need one partner each, and the resulting two pairs already form a rectangle, so $2$. `2 2 3 3` is already a rectangle, so $0$. And `1 3 5 7 1 7 5` has a single odd count (the lone $3$), after which there are four pairs — an even number — so just $1$.

Note it is the number of *pairs* whose parity matters, not the number of sticks: in the last sample $7$ sticks become $8$, and $8/4 = 2$ rectangles fall out without further help.

## Edge cases

- **Two levels of pairing.** Sticks pair up by equal length, and then the *pairs* pair up into rectangles — so both an odd count within a length and an odd total number of pairs cost extra sticks.
- **Each odd length contributes one orphan**, needing one new stick to complete its pair: the last row's lone $3$ costs exactly one.
- **A leftover pair needs a whole new pair**, hence $+2$ rather than $+1$. The first row has a single stick: one added makes one pair, and that pair needs two more sticks to square off — total $3$.
- **Four sticks of one length form a square**, which is a rectangle, so no cross-length matching is required and the pair count is all that matters.
- **Already complete** (the third row, two $2$s and two $3$s) → $0$.
- **The pair count is computed after the orphans are filled**, via $\lceil c/2 \rceil$ — counting $\lfloor c/2 \rfloor$ instead would miss the pairs the new sticks create.
- **Added sticks may be any length**, which is what makes the fix always available.

## Dry run

| sticks | counts | orphans (odd counts) | pairs after filling | pairs odd? | added |
|---|---|---:|---:|:---:|---:|
| $1$ | $1{:}1$ | 1 | 1 | yes → $+2$ | `3` |
| $2, 5$ | $2{:}1$, $5{:}1$ | 2 | 2 | no | `2` |
| $2,2,3,3$ | $2{:}2$, $3{:}2$ | 0 | 2 | no | `0` |
| $1,3,5,7,1,7,5$ | $1{:}2$, $3{:}1$, $5{:}2$, $7{:}2$ | 1 | 4 | no | `1` |

Row 1 ends up with four sticks of two lengths — one rectangle.
