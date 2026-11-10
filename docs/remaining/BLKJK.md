# BLKJK

Store subset-sum bitsets by cardinality, recording only the first prefix in which each state appears. A cumulative table indexes allowed discarded prefix elements. Scan suffix states when first created and match a compatible prefix-sum range, minimizing selected suffix elements (swaps).

Complexity: O(NY² / word size + Y²) arithmetic/bitset work and O(NY²) bits, Y<=1000; first-appearance states are processed once.

Reference: [CodeChef editorial](https://discuss.codechef.com/t/83432). Implementation and validation are original Python code.
