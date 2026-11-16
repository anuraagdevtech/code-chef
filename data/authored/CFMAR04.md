---
topic: Hashing
subtopic: Use letter-frequency tuples as anagram signatures
time: $O(\sum |S_i|+26N)$ overall
space: $O(26N)$ in the worst case
complexity_note: Auxiliary space excludes the buffered input and output.
---
Two words can be rearranged into each other exactly when all 26 letter frequencies agree. Count words by this frequency tuple and output the largest bucket. This directly models the equivalence classes without constructing pairwise edges or a DSU.

## Edge cases

- There is one test case with a leading word count.
- Repeated identical words belong to the same class.
- Letter order is irrelevant, but multiplicity is essential.

## Dry run

The signatures of `aba` and `aab` are both two `a`s and one `b`; they form the largest sample bucket, of size two.
