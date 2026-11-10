# MAKEPAL3

Let the mirrored differences be d. A move changes a contiguous interval of these differences by +1 or -1; an interval crossing the center has the same effect after cancellation. Decompose d into signed horizontal layers. Starting a layer costs one whenever its magnitude increases, or its sign switches; this is necessary at each boundary and achievable by ending and starting intervals there.

Complexity: O(N) time and O(N) input space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
