# TSHIRTS

Process shirts one at a time, using a person bitmask to record who has received a shirt. Skip the shirt or give it to one eligible unassigned person. Descending mask updates prevent reusing the same shirt, and each assignment is counted once.

Complexity: O(100 N 2^N) time and O(2^N) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
