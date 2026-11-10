# PTREE

Sort the vertex depths to maximize the polynomial. A perfect tree has nondecreasing level widths and only O(sqrt N) distinct branching depths. Euler intervals and weighted depth lists find subtree width changes. Cache the resulting constant-width depth intervals, sharing the cache between every vertex in a unary chain by using its first branching descendant as an anchor.

Evaluate each interval with an arithmetic-geometric sum. Division-free geometric doubling handles roots of unity, including y^width=1. For queries spanning many intervals, baby-step/giant-step power tables avoid modular exponentiation per interval; y=1 uses depth sums directly.

Complexity: O(N log N + D B log N + Q(sqrt N + D + sum log interval_length + log modulus))) conservative time and O(N+DB) space, where D=O(sqrt N) is the number of branching depths and B is the number of distinct queried branching anchors. Queries with at most 16 intervals use direct exponentiation instead of the power table. The sum of logarithmic interval lengths is O(sqrt N).

Validation includes direct sorted-polynomial comparisons on random perfect trees, y=1 and y=-1. On local PyPy 3.11.15, a 199,396-vertex perfect tree with 631 distinct widths and the maximum 100,000 queries passed three full-output checks: repeated root queries at y=2 (2.89 seconds), queries cycling 631 branching roots (1.73 seconds), and root queries cycling 64 values of y including 1 and -1 (3.07 seconds). Expected answers came from direct polynomials, and queries were encoded with the preceding answer. Timings depend on the runtime and host; no online acceptance is claimed.

Reference: [CodeChef editorial](https://discuss.codechef.com/t/22265). Implementation and validation are original Python code.
