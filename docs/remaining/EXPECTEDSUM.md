# EXPECTEDSUM

Chef draws ceil(N/2) positions in a uniformly random ordering of the chits. Each position has probability A/N of holding one, so linearity of expectation gives A*ceil(N/2)/N.

Complexity: O(log modulus) time and O(1) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
