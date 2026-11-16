---
topic: Combinatorics
subtopic: Inclusion-exclusion over per-digit thresholds with a 4-level sum-over-subsets table
time: $O(D \cdot (N \cdot D + D \cdot 4^D))$ per test case, $D \le 9$ digits
space: $O(4^D)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Fix the length $\ell$ of the lucky result. A subsequence qualifies when no number has more than $\ell$ digits and, in each of the $\ell$ digit positions, the maximum digit is exactly 4 or exactly 7.

"Maximum is exactly 4 or 7" in one position is (max $\le 4$) $-$ (max $\le 3$) $+$ (max $\le 7$) $-$ (max $\le 6$). Expanding this over all positions gives a signed sum over threshold vectors $t \in \{3, 4, 6, 7\}^{\ell}$ of the number of non-empty subsets whose every digit is within its threshold. If $c(t)$ numbers satisfy the thresholds, that number is $2^{c(t)} - 1$.

To get all $c(t)$ at once, classify each digit into four levels ($\le 3$, 4, 5-6, 7), drop numbers containing an 8 or 9, bucket each number by its level vector in base 4, and run a prefix sum along every coordinate. The sign of a threshold vector is negative once for every coordinate at level 0 or 2. Shorter numbers are padded with leading zeros, so a subset made only of shorter numbers has maximum 0 in the leading position and is cancelled out; it is counted under its own length instead.

## Edge cases

- Numbers with a digit 8 or 9 can never be part of a valid subsequence.
- Numbers longer than the current length are excluded for that length.
- The count is exact, not modular, so $2^{c} - 1$ is computed with big integers.
- Duplicated values are different elements and generate different subsequences.

## Dry run

`W = [43, 87, 44]`.

Length 1: no number has a single digit, so nothing is counted. Length 2: 87 is dropped because of the 8. The remaining numbers have level vectors (tens, units) = (4-level, low) for 43 and (4-level, 4-level) for 44.

Tens position: both have digit 4, so every non-empty subset has maximum 4 there. Units position: the maximum is 4 only if 44 is included. Subsets: `{44}` and `{43, 44}`.

Answer 2.
