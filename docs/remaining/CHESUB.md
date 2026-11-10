# CHESUB

Maintain the best score using j finished or ongoing subarrays, and the best score with subarray j ending at the current element. Either extend that subarray or start it after an optimal j-1 solution. Update j downward to keep starts disjoint and nonempty.

Complexity: O(NK) time and O(K) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
