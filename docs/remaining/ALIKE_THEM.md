# ALIKE_THEM

Track each final value’s original source under the sequential assignments. Exactly the surviving source positions must share one value; overwritten original positions are independent. Conflicting fixed source values forbid a solution, while every unconstrained independent value contributes a factor M.

Complexity: O(N) time and space.

Validation: repository sample checks and deterministic differential checks where applicable; no online acceptance is claimed.
