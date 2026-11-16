---
topic: Dynamic Programming
subtopic: Count prefix partitions using rolling palindrome states
time: $O(|S|^2)$ overall
space: $O(|S|)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Let $ways[r]$ count palindromic partitions of the prefix of length $r$, with $ways[0]=1$. For every palindrome $S[l:r]$, add $ways[l]$ to $ways[r]$; its final part uniquely determines this transition.

For each new right endpoint, maintain whether every substring ending there is a palindrome. The recurrence compares its endpoints and the interior substring from the previous right endpoint. Update left endpoints in ascending order, so the old interior state at `left+1` remains available. This avoids a quadratic palindrome table.

## Edge cases

- A single character always gives a valid final part.
- Partition boundaries, rather than distinct palindrome texts, determine different ways.
- Apply modulus $10^9+7$ to the accumulated count.

## Dry run

For `bob`, prefix partition counts are `1,1,1,2`: the final prefix can use `b|o|b` or `bob`. The full sample `bobseesanna` has 18 partitions.
