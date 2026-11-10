# CHEFFFUNC

For a k-bit x, f(x)=k-popcount(x), while g(x)=3*2^(k-1)-1-x. Inside each fixed bit length, minimizing x+popcount(x) maximizes the objective. For any x>L, take its highest differing bit from L: setting every lower bit to zero only improves the objective while remaining in the interval. Thus an optimum is L or L rounded upward to a multiple of some power of two. Evaluate all O(log R) such candidates, including bit-length boundaries.

Complexity: O(log R) time and O(1) space.

Validation: samples and deterministic interval enumeration; no online acceptance is claimed.
