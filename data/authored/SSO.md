---
topic: Bit Manipulation
subtopic: Count the supply of each bit and propagate carries
time: $O(N \log A)$ per test case
space: $O(\log \sum A)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Bit $i$ appears in the OR if some subset sum has bit $i$ set. Count, for each bit, how many of the given numbers have it; think of these as coins of value $2^i$.

- If at least one coin of value $2^i$ is available - an original one or one formed by a carry - a subset sum with bit $i$ set exists.
- Two coins of value $2^i$ can be added to form one coin of value $2^{i+1}$, so pass $\lfloor \text{count}_i / 2 \rfloor$ on to the next bit.

Going from the lowest bit upwards with this rule marks every bit that can be produced by carries, and a bit with no supply at all cannot be produced. The table is sized for sums well beyond the input range.

## Edge cases

- A single element: the answer is the element itself.
- Equal elements matter - `1 1` produces the sum 2 and hence bit 1.
- Carries can cascade through several bits.
- The empty subsequence has sum 0 and contributes nothing.

## Dry run

`A = [1, 9, 8]`: bit 0 occurs twice (1, 9) and bit 3 twice (9, 8).

- bit 0: count 2 - set; carry 1 to bit 1.
- bit 1: count 1 - set; carry 0.
- bit 2: count 0.
- bit 3: count 2 - set; carry 1 to bit 4.
- bit 4: count 1 - set.

Answer $1 + 2 + 8 + 16 = 27$.
