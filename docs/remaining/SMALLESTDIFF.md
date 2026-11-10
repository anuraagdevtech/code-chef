# SMALLESTDIFF

A monotone path visits L=N+M-1 distinct entries. Before first reaching a boundary it makes at least min(N,M)-1 choices, requiring alternating strictly smaller and larger rejected neighbors. Thus a sorted length-L window needs at least ceil((min-1)/2) smaller outside values and floor((min-1)/2) larger ones. Choose the narrowest such window, place it down the shorter dimension then along the boundary, and place those outside values at each rejected neighbor. Fill remaining cells arbitrarily. The path follows the chosen window and meets the lower bound.

Complexity: O(NM log(NM)) time and O(NM) space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
