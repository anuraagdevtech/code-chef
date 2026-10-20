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
