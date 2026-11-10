# SPLITMIN

The larger pile maximum must be at least L=max(min(A_i,B_i)), or some pair has no usable choice. Conversely any two values from distinct pairs with larger value at least L can serve as the two maxima: choose each other pair’s smaller value and put it in the larger pile. Sort all values and find the closest qualifying pair with different owners.

Complexity: O(N log N) time and O(N) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
