# End Of The World (CHEFHACK)

[Problem statement](https://www.codechef.com/problems/CHEFHACK) · [Python solution](../../solutions/CHEFHACK.py)

## Approach

Sieve primality up to V=10000000. Prime cells cost their zero-based prime rank. Every nonprime same-parity component is hacked when first encountered in row-major order; charge its first cell and flood-fill the component. Even cost is x/2, while odd cost is floor(x/2)+2.

## Complexity

- Time: O(V log log V+N squared log V).
- Space: O(V+N squared).
