# LCMMANIA

Write N as 2^a times an odd m. For m>1 use (2^a,2^a,2^a*(m-1)/2); special-case multiples of three.

Correctness: The repeated value divides the third, giving total 2^a+2 times the third = N. For impossibility, sort the 2-adic valuations of A,B,C as a<=b<=c. Their pairwise LCM valuations are b,c,c. If b<c, dividing the sum by 2^b leaves an odd integer at least five; if b=c, it leaves an odd integer at least three. Neither can be a power of two.

Complexity: O(1) time and space.

Validation: official samples, semantic construction checks where needed, and deterministic differential regressions in `tools/test_advanced_one.py`. No online judge acceptance is claimed.
