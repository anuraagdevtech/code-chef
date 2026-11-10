# KEEPOUT

Start after every insertion and undo posts in reverse. A doubly linked list of sorted posts finds each removed post’s neighbors in constant time. Removal only merges two gaps, so the maximum gap can only increase.

Complexity: O(N log N) time and O(N) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
