# ANTSCHEF

Unfold equal-speed collisions by exchanging ant identities. A distance shared by multiple ants causes one central collision; those trajectories reflect instead of crossing. For an ant of smallest remaining distance on its line, count larger-distance ants on the same side if it reflects at the center, or on the opposite side if it crosses. This counts each off-center collision once.

Complexity: O(S log S) time and O(S) space, where S is the number of ants.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
