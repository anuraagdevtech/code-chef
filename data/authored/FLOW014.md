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
