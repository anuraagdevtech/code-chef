# Adi and the Matrix (ADIMAT)

[Problem statement](https://www.codechef.com/problems/ADIMAT) · [Python solution](../../solutions/ADIMAT.py)

## Approach

Apply Burnside's lemma. Enumerate row permutation cycle partitions with cycle-index weight 1/(product(length^count*count!)). A column cycle of length j has 2^(sum count*gcd(length,j)) fixed colorings. Its permutation cycle-index recurrence averages over all column permutations without enumerating their partitions.

## Complexity

- Time: O(p(min(N,M)) times max(N,M) squared).
- Space: O(max(N,M)+min(N,M)).
