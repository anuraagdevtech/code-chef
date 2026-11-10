# MAXCYCSHIFT

Prefix XORs of a rotated array are one length-N window of doubled-array prefix XORs, each XORed with a common constant. That bijection preserves distinct counts. Slide a frequency window over all rotations.

Complexity: O(N) expected time and O(N) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
