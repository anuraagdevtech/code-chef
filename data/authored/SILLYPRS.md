---
topic: Greedy
subtopic: Matching by parity
time: $O(N)$ per test case
space: $O(1)$
---
The floor is what makes this interesting. Writing it exactly,

$$\left\lfloor \frac{a+b}{2} \right\rfloor = \frac{a+b}{2} - \frac{[\,a+b \text{ odd}\,]}{2}$$

Summed over all $N$ pairs, the first term is $\frac{\sum A + \sum B}{2}$ — **fixed**, since every chef and every chefette is used exactly once regardless of the pairing. So the only thing the matching controls is the number of pairs whose sum is odd, and maximising the total means **minimising** that count.

A sum is odd exactly when the two heights have different parity. So pair odd with odd and even with even as far as possible: with $o_A, o_B$ odd heights and $e_A, e_B$ even ones, the number of parity-matched pairs is $\min(o_A, o_B) + \min(e_A, e_B)$, and everything left over is forced into mismatches:

$$\text{mismatched} = N - \min(o_A, o_B) - \min(e_A, e_B)$$

$$\text{answer} = \frac{\sum A + \sum B - \text{mismatched}}{2}$$

The actual heights never enter the decision — only their parities — which is why no sorting or assignment algorithm is needed. Recognising that the fractional loss, not the sum, is what the matching affects is the whole insight.

Sample case 1 has $A = [4,5,6]$ and $B = [1,2,3]$: one odd in $A$ against two in $B$, and two evens against one, giving two matched pairs and one mismatch. The total is $(21 - 1)/2 = 10$.

Sample case 2 totals $48$ with two forced mismatches, giving $23$.

Heights reach $10^9$ with $N$ up to $10^5$, so the sums reach $10^{14}$ — **64-bit territory** outside Python.

## Edge cases

- **Only parity matters.** Each pair contributes $\lfloor (A_i + B_j)/2 \rfloor$, which loses exactly $\tfrac12$ when the sum is odd — so the total is $(\sum A + \sum B - \#\text{odd-sum pairs})/2$ and the magnitudes never need comparing. No sorting is required.
- **Maximising means minimising mismatched parities**, which is a two-group matching: pair odds with odds and evens with evens as far as the counts allow.
- **The mismatch count is $|{\#\text{odd }A} - {\#\text{odd }B}|$**, and it has the same parity as $\sum A + \sum B$ — which is why the final halving is always exact and the floor division never truncates anything real.
- **Perfectly matching parities** gives the clean $(\sum A + \sum B)/2$ with no loss.
- **All the same parity on one side** forces the leftovers to mismatch, as in the second sample where $A$ has one odd and $B$ has three.
- **$A_i, B_i$ up to $10^9$ with $N$ up to $10^5$** puts the sums near $10^{14}$, past 32-bit.

## Dry run

First sample: $A = 4, 5, 6$ and $B = 1, 2, 3$.

| | odd | even |
|---|---:|---:|
| $A$ | 1 (the $5$) | 2 |
| $B$ | 2 | 1 |

Matched pairs: $\min(1,2) + \min(2,1) = 1 + 1 = 2$, so one pair mismatches.

$\sum A = 15$, $\sum B = 6$, giving $(21 - 1)/2 = $ `10`. For instance $5{+}1$, $4{+}2$ and $6{+}3$ → $3 + 3 + 4$.
