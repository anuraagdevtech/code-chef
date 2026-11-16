---
topic: Constructive
subtopic: Start from the minimum array and raise elements in steps of two
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Half of the elements must be odd and half even. The smallest such array is $N/2$ ones and $N/2$ twos with sum $3N/2$; the largest uses 99999 for the odd half and 100000 for the even half, sum $199999 \cdot N/2$.

Changing an element without changing its parity moves the sum by a multiple of 2, so the parity of $K$ must equal the parity of the minimum sum. Conversely, if $K$ lies between the two bounds and $K - 3N/2$ is even, distribute $(K - 3N/2)/2$ steps of $+2$ greedily: each element can take up to 49999 steps (1 up to 99999, 2 up to 100000). The total capacity is exactly the gap between the bounds, so the greedy always fits.

## Edge cases

- $K$ below $3N/2$ or above $199999 \cdot N/2$: print $-1$.
- Wrong parity of $K - 3N/2$: print $-1$.
- Elements may repeat; only the range and the parity balance are required.
- Any valid array is accepted, so the judge uses a checker.

## Dry run

`N = 4, K = 20`. Minimum array `1 1 2 2` with sum 6; the gap 14 is even, so 7 steps of $+2$ are needed.

The first element takes all 7: $1 + 14 = 15$.

Output `15 1 2 2` - two odd, two even, sum 20.
