# DIANE

A block of k copies of a followed by a+1 contributes k(a-1): only subarrays containing the final entry and at least one preceding entry contribute. Separate independent blocks with 1, making every crossing contribution zero. Divide D by 99998 and encode quotient and remainder in two blocks.

Complexity: O(D/99998 + 1) time and output space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
