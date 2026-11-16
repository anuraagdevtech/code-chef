---
topic: Bit Manipulation
subtopic: Greedy on answer bits with a partition DP over cluster counts
time: $O(Q \cdot B \cdot P^2)$ with $P \le 50$ topped slices and $B$ bits in the total sweetness
space: $O(P)$ big integers
complexity_note: Auxiliary space excludes the buffered input and output.
---
Only slices with a topping matter - the statement guarantees there are few of them - and a slice with sweetness 0 can be attached to a neighbouring cluster without changing any sum. If $K$ exceeds the number of sweet slices some cluster has sweetness 0 and the AND is 0; if $K = 1$ the answer is the total.

Otherwise build the answer bit by bit from the top. Suppose the bits chosen so far form `ans`; try `mask = ans | bit`. The AND of all clusters contains `mask` exactly when every cluster sum contains `mask`, so the question is whether the positive values can be cut into exactly $K$ contiguous groups whose sums are all supersets of `mask`.

That is a partition DP over prefixes: `dp[r]` is a bitset of the possible numbers of groups for the first $r$ values, and `dp[r] |= dp[l] << 1` for every $l < r$ with `(prefix[r] - prefix[l]) & mask == mask`. Keep the bit if bit $K$ of `dp[m]` is set.

## Edge cases

- Fewer than $K$ sweet slices: answer 0.
- $K = 1$: the single cluster is everything, no bit search needed.
- Clusters must be contiguous in the original row, which the compressed list preserves.
- Sums can be far larger than 32 bits, so the bit loop starts from the bit length of the total rather than a fixed 30.

## Dry run

First sample query: $K = 3$, sweetness values `30 15 26 16 21 13 25 5 27 11`.

Testing bits from the top, bit 5 (32) can be kept: the split `45 | 101 | 43` has all three sums containing 32. Lower bits are then tested against masks containing 32; only bit 0 survives, because 45, 101 and 43 are all odd, while no three-way split keeps 32 together with any of 16, 8, 4 or 2.

$45 \mathbin{\&} 101 \mathbin{\&} 43 = 33$.
