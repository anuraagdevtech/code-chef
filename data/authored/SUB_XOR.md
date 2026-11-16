---
topic: Bit Manipulation
subtopic: Parity of contributions to each output bit
time: $O(N)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Fix an output bit $b$. A one at zero-based index $i$ contributes to it when the substring ends at $i+b$. There are $i+1$ possible starting positions, so only even $i$ survive XOR cancellation. The bit is therefore the parity of ones at even indices up to $N-1-b$.

Scan these prefix parities from left to right. At index $i$, the parity is exactly output bit $N-1-i$. Folding with `answer = 2 * answer + parity` reconstructs the integer modulo $998244353$ without constructing enormous integers.

## Edge cases

- Leading zeros still occupy positions.
- Only even zero-based indices contribute.
- Apply the modulus during the fold, after deciding each bit.

## Dry run

For `101`, the prefix parities at even indices are `1, 1, 0`. These form binary `110`, so the answer is `6`.
