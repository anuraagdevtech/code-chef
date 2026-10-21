---
topic: Constructive
subtopic: Parity blocks and the number of switches
time: $O(N)$ per test case
space: $O(N)$
---
$P_i + P_{i+1}$ is odd exactly when the two have **different parity**. So reading the permutation as a string of O's and E's, the answer counts the positions where that string changes — and a string with $b$ maximal blocks has exactly $b - 1$ changes.

So the task is to arrange $\lceil N/2 \rceil$ odd numbers and $\lfloor N/2 \rfloor$ even numbers into exactly

$$b = K + 1$$

alternating blocks. Starting with an odd block, that needs $\lceil b/2 \rceil$ odd blocks and $\lfloor b/2 \rfloor$ even blocks — and both fit, since $b \leq N$ gives $\lceil b/2 \rceil \leq \lceil N/2 \rceil$ and likewise for the evens. So starting with odds always works and no case analysis is needed.

The leftovers go into the **first** block of each parity: give every block one number, then dump the surplus odds into the first odd block and the surplus evens into the first even block. Padding a block never creates a new change, since the block's parity is unchanged.

The constraint $K \geq 1$ guarantees $b \geq 2$, so there is at least one even block to receive the evens — with $b = 1$ there would be nowhere to put them.

For $N = 4, K = 2$ this builds three blocks: odds $[1]$, evens $[2,4]$, odds $[3]$, giving `1 2 4 3` with changes at positions $1$ and $3$. The published sample, `4 3 1 2`, has a different block structure with the same count — **any valid permutation is accepted**, so this is judged by a checker.

## Edge cases

- **An adjacent pair sums to an odd number exactly when its parities differ**, so $K$ such indices means $K$ parity switches — which means the permutation splits into $K+1$ maximal blocks of one parity each, alternating.
- **Padding a block adds no switches**, which is what makes the surplus placement free: all the extra odds go into the first odd block and all the extra evens into the first even block.
- **The block counts must match the available numbers.** With $K+1$ blocks, $\lceil (K+1)/2 \rceil$ are odd-parity and $\lfloor (K+1)/2 \rfloor$ even, and each needs at least one number of that parity — which $K \leq N-1$ guarantees.
- **$K = N - 1$ forces full alternation**, with every block a singleton and no surplus to place.
- **$K = 1$** gives two blocks: all the odds then all the evens (or the reverse).
- **Starting with the odd parity is a choice, not a requirement** — this construction always leads with odds, which is why its output differs from the sample's (`1 2` against `2 1`) while having the same switch count. A special judge counts the odd sums.
- **Sum of $N \leq 2 \cdot 10^5$**: the odds and evens are built as ranges and sliced.

## Dry run

$N = 4$, $K = 2$: odds $\{1, 3\}$, evens $\{2, 4\}$, and $K + 1 = 3$ blocks (two odd-parity, one even).

| block | parity | numbers taken |
|---:|---|---|
| 1 | odd | $1$ (one of the two odds) |
| 2 | even | $2, 4$ (both evens, the surplus) |
| 3 | odd | $3$ |

Permutation `1 2 4 3`, with adjacent sums $3$ (odd), $6$ (even), $7$ (odd) — exactly $K = 2$ odd sums.
