---
topic: Probability
subtopic: Sum the carry probabilities as a geometric series
time: $O(1)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Pad both uniformly chosen numbers to $N$ digits with leading zeros. Without an incoming carry, 45 of the 100 digit pairs generate a carry; with one, 55 do. Hence $p_i=0.45+0.1p_{i-1}$ with $p_0=0$, so $p_i=(1-10^{-i})/2$.

Linearity of expectation gives $\sum_{i=1}^N p_i=N/2-(1-10^{-N})/18$. Evaluate this closed form. Once $N$ is large, the correction $10^{-N}$ is below floating-point relevance.

## Edge cases

- Leading zeros are allowed when representing numbers with at most $N$ digits.
- Include the carry from the most significant input digit.
- Print enough decimal places for the error tolerance.

## Dry run

For `N=2`, carry probabilities are `0.45` and `0.495`; their sum is `0.945`.
