# CHEFQUE

Store membership of each possible 31-bit element in a packed bitmap. Every generated operation tests and changes one bit; maintain the sum incrementally only on actual membership changes.

Complexity: O(Q) time and 2^28 bytes of bitmap space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
