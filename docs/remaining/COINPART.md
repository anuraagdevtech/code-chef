# COINPART

Reserve the largest coin for Chefu, then partition the other coins with minimum sum difference. Assign Chefu the smaller part plus the reserved coin and simulate the required allocation order, using that coin when his smaller part runs out. This achieves (total+largest-minimum difference)/2.

Complexity: O(N S / word size) time and O(N S) bits for reconstruction.
