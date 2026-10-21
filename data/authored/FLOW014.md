---
topic: Conditionals & Case Work
subtopic: Grading from a set of independent flags
time: $O(1)$ per test case
space: $O(1)$
---
Three independent tests are applied to each sample:

1. hardness $> 50$
2. carbon content $< 0.7$
3. tensile strength $> 5600$

The grade then depends on *which* subset passed, not merely how many — grades $9$, $8$ and $7$ all correspond to two conditions met but distinguish which pair. So evaluate the three booleans once and branch on the combination.

The cleanest reading of the rules: grade $10$ for all three, then a specific grade for each pair, then $6$ for exactly one and $5$ for none. Note the pair-to-grade mapping is not in an obvious order — $(1,2) \to 9$, $(2,3) \to 8$, $(1,3) \to 7$ — so it has to be read off the statement rather than guessed from the count.

Two practical traps.

**Carbon content is not an integer.** It is compared against $0.7$, so the value must be parsed as a float. Reading it as an `int` would fail on the sample's $0.6$ outright.

**The comparisons are strict in all three cases**, and the middle one points the other way: carbon must be *less than* $0.7$ while the other two must *exceed* their thresholds. Sample case 3, with all values zero, passes condition 2 alone — $0 < 0.7$ — giving grade $6$ rather than $5$. That is the case that catches a solution which assumes all-zero means nothing passed.

## Edge cases

- **The carbon content is not an integer** ($0.6$ in the sample), so it must be parsed as a float. Reading it with `int()` raises or truncates, and this is the single most common way to fail this problem.
- **The thresholds differ in direction and strictness**: hardness must be $> 50$, tensile $> 5600$, but carbon $< 0.7$. Values of exactly $50$, $5600$ or $0.7$ all *fail* their own test.
- **Grade $5$ needs all three to fail**, which the samples never show — note that any carbon reading below $0.7$ already satisfies one condition, so a grade of $5$ requires carbon at or above $0.7$ as well.
- **The pair grades are not symmetric**: hardness and carbon give $9$, carbon and tensile give $8$, hardness and tensile give $7$. The order of the `elif` chain encodes that mapping, and reordering the branches silently changes answers.

## Dry run

| hardness | carbon | tensile | $>50$ | $<0.7$ | $>5600$ | grade |
|---:|---:|---:|:---:|:---:|:---:|---:|
| 53 | 0.6 | 5602 | yes | yes | yes | `10` |
| 45 | 0 | 4500 | no | yes | no | `6` |
| 0 | 0 | 0 | no | yes | no | `6` |

Rows 2 and 3 satisfy exactly one condition each, which lands them both on $6$.
