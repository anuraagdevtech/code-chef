# RDF

For each step E_k(n) is the average of E_(k-1)(0..n-1), evaluated by prefix sums. For K>=70, E is at most N/2^K < 10^-6, so output zero.

Complexity: O(70 max N + T) time and O(max N + T) space.
