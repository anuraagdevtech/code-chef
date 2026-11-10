# ONEORALL

With odd N every move removes an odd total, fixing the winner by total parity. With even N, induction on total stones shows the losing states are exactly those with even total and even minimum (including zero); each move leaves this set, and every other state has a move into it.

Complexity: O(N) time and O(N) input space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
