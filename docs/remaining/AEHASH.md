# AEHASH

Memoize hash distributions by substring length and A-count. For each allocation between the fixed halves, cumulative distributions count pairs whose maximum hash equals each value; add the parent A-count.

Complexity: Polynomial in N and A; O(N A² H) conservative time and O(N A H) space, H<=A(ceil(log2 N)+1).
