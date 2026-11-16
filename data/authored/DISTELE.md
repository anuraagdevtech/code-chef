---
topic: Combinatorics
subtopic: Independent choice from each frequency class
time: $O(N)$ per test case
space: $O(U)$ for $U$ distinct values
complexity_note: Auxiliary space excludes the buffered input and output.
---
For a value occurring $f$ times, a good subsequence either skips it or selects exactly one of its $f$ positions. That gives $f+1$ choices. Choices for different values are independent, and their selected indices define exactly one subsequence in original order.

Multiply all $f+1$ values modulo $10^9+7$, then subtract the empty subsequence.

## Edge cases

- Repeated values represent distinct index choices.
- An all-equal array has exactly $N$ good nonempty subsequences.
- Subtract one modulo the modulus.

## Dry run

For `[1,1]`, the frequency is two, giving `(2+1)-1=2`. For `[1,2]`, `(1+1)(1+1)-1=3`.
