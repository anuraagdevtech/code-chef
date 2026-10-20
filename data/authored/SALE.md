---
topic: Basic Math
subtopic: Total minus the extremum
time: $O(1)$ per test case
space: $O(1)$
---
Three items are bought and the cheapest is free, so Chef pays for the other two:

$$A + B + C - \min(A, B, C)$$

Expressing it as "total minus the minimum" rather than "sum of the two largest" is the move worth internalising. Both are correct, but the subtraction form needs only two passes over the values — one to add, one to find the minimum — and it extends unchanged to $n$ items with the cheapest free, whereas "add the two largest" would need a sort or a running top-two.

Ties are handled correctly without any special case. Sample case 2 has three items priced $3$; exactly one of them is free, so the answer is $6$ rather than $3$ or $9$. `min` returns the value, not every element equal to it, so only one copy is deducted. The same applies to sample case 3, where two items share the lowest price of $4$ and only one is discounted, giving $8 + 4 = 12$.

That subtlety — *one* free item, even when several are tied for cheapest — is where an approach built on filtering out the minimum value would go wrong, since it would remove both $4$s and answer $8$.
