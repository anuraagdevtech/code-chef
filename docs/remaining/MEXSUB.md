# MEXSUB

Every part must have the whole array’s MEX: all smaller values must occur and that MEX is absent globally. For a fixed right endpoint, valid starts are precisely those no later than the minimum last occurrence of a required value. Prefix sums of partition counts sum all such starts; a lazy heap maintains this minimum.

Complexity: O(N log N) time and O(N) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
