# Yet Another Problem About Sequences (EARTSEQ)

[Problem statement](https://www.codechef.com/problems/EARTSEQ) · [Python solution](../../solutions/EARTSEQ.py)

## Approach

Choose cyclic edge primes from {2,3,5,7,11} so no two within distance two agree. Give vertex i the product of its two incident edge primes and a unique prime greater than eleven. Adjacent values share an edge prime; no three consecutive values share any prime. The unique large factors ensure distinctness and all products stay below 10^9.

## Complexity

- Time: O(V log log V+N).
- Space: O(V+N).
