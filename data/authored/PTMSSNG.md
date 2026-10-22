---
topic: Bit Manipulation
subtopic: XOR cancels everything that appears twice
time: $O(N)$ per test case
space: $O(1)$
---
An axis-parallel rectangle with corners at $x \in \{x_1, x_2\}$ and $y \in \{y_1, y_2\}$ contributes each of its two $x$-values **exactly twice** among its four vertices, and likewise each $y$-value.

So across all $N$ rectangles, every $x$-coordinate occurs an **even** number of times, and the same holds for $y$. Removing one vertex breaks that parity for exactly one $x$ and one $y$ — the missing ones.

XOR is the perfect detector: $v \oplus v = 0$, so every value occurring an even number of times cancels out entirely, leaving only the odd one out.

$$X = \bigoplus_i x_i, \qquad Y = \bigoplus_i y_i$$

over the $4N-1$ given vertices.

Note the $x$ and $y$ folds are **independent** — the missing point's coordinates need not come from the same input vertex, and the parity argument applies to each axis separately.

The guarantee that all $4N$ vertices are **pairwise distinct** is what makes the rectangles unambiguous, but the XOR argument does not actually depend on it: it only needs each coordinate value to appear an even number of times, which the rectangle structure guarantees regardless.

Coordinates may be **negative**, down to $-10^9$. Python's XOR on negative integers follows two's-complement semantics over arbitrary precision, and $v \oplus v = 0$ still holds, so no offsetting is needed — though a fixed-width language would want care.

In the sample the $x$ values fold to $2$ and the $y$ values to $2$, giving the missing vertex $(2,2)$ — which completes the rectangle with corners $1$ and $2$ on both axes.

## Edge cases

- **Every coordinate appears an even number of times across a rectangle's four vertices** — each $x$ twice and each $y$ twice — so XOR-ing all the given coordinates cancels every complete rectangle and leaves the lone unpaired value.
- **The two axes fold independently**, since the $x$ and $y$ values are separate multisets.
- **XOR is used rather than a sum** because it needs no extra bookkeeping about which rectangle a vertex belongs to — and it works even though the rectangles may intersect.
- **The vertices are given in no particular order**, which is exactly why a pairing-based approach would be awkward and the XOR is not.
- **The $4N$ vertices are pairwise distinct**, so no accidental cancellation occurs between different rectangles' vertices.
- **Negative coordinates work**, since Python's XOR on negative integers is well defined in two's complement and the cancellation argument is unaffected.
- **Exactly $4N - 1$ points are read**, one short of four per rectangle.
- **Sum of $N \leq 2 \cdot 10^5$**: one pass with two accumulators.

## Dry run

Sample: $N = 2$ rectangles with seven given vertices.

| axis | values | XOR |
|---|---|---:|
| $x$ | $1, 1, 4, 2, 9, 9, 4$ | **2** |
| $y$ | $1, 2, 6, 1, 6, 3, 3$ | **2** |

Output `2 2`. The $1$s, $4$s and $9$s cancel in $x$; the $1$s, $6$s and $3$s cancel in $y$.
