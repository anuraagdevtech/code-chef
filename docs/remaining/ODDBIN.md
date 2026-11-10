# ODDBIN

Over GF(2), (1+x)^(2^b)=1+x^(2^b). Split exponents at their highest bit; lower coefficients use XOR of both groups and upper coefficients use the high group. Memoize identical subproblems and use Lucas for singleton groups.

Complexity: O(60 · 2^M · M) worst-case time and O(60 · 2^M) space, M<=15.
