---
topic: Dynamic Programming
subtopic: Earliest-prefix dominance and cardinality subset-sum bitsets
time: $O((NC+NQ+CY)Y/w)$ word operations per test case for $C=\min(N,Y)$ and $Q$ an initial valid swap bound
space: $O(NQY/w+NC/w)$ machine words
complexity_note: Auxiliary space excludes the buffered input and output.
---
A winning prefix selects some original cards. If it has length $k$, the required swaps are exactly the number of selected indices at least $k$: exchange those cards with the unselected positions inside the prefix.

First test the original prefixes, then ordinary subset reachability. If no sum in $[X,Y]$ is possible, return minus one. Otherwise reconstruct any winning subset to obtain a valid swap upper bound.

For each selection cardinality and sum, retain its earliest reachable prefix. If that prefix has length $i$ and selects $j$ cards, its exclusion count is $i-j$. Store its sum bit in a table indexed by prefix length and allowed exclusions, then make this table cumulative in both indices.

Sweep suffixes from right to left with exact-cardinality bitsets. A newly reachable suffix sum with $q$ selected cards can improve the answer when the earlier prefix table allows at most $q$ exclusions and some complementary sum in $[X-s,Y-s]$. Test that interval with a bitmask intersection. First occurrences suffice by earliest-prefix dominance; counts no better than the current upper bound are skipped.

See the [CodeChef editorial](https://discuss.codechef.com/t/blkjk-editorial/83432) for the dominance argument.

## Edge cases

- A subset may exist even when the original prefix sums skip the target interval.
- Cards have positive values, so sums above $Y$ can be discarded.
- Maintain exact selection cardinalities during both sweeps.
- One exchange brings in one missing prefix card.

## Dry run

For `[1,2,3]` and interval `[4,5]`, original prefix sums are 1, 3, and 6. Select cards 1 and 3 for sum four; one selected index lies outside a length-two prefix, so one swap suffices.
