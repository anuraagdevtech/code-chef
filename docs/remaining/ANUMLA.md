# ANUMLA

Sort the subset sums, remove the empty subset, then repeatedly take the smallest unused sum as the next positive element and remove all sums formed by adding it to known subsets. Every remaining subset must use an undiscovered element, so its smallest sum is exactly the smallest undiscovered element.

Complexity: O(N 2^N) time and O(2^N) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
