# LONGESTARRAY

Both parts must have the whole array’s OR. Thus the window needs at least one occurrence of every active bit and must leave at least one outside. Slide the longest window respecting the latter upper bounds; it is a valid answer exactly when every bit also appears inside.

Complexity: O(30N) time and O(30N) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
