---
topic: Number Theory
subtopic: Finding the invariant
time: $O(1)$ per test case
space: $O(1)$
---
Both operations move the same $d$ from one number to the other. Whatever one gains, the other loses, so the **sum stays fixed**:

$$A + B = \text{constant}$$

That invariant settles the problem. If Chef can reach $A = B$, then each must equal half the total, so $A + B$ has to be even. Conversely, when $A + B$ is even the target is reachable in a single move: take $d = \frac{B - A}{2}$ and add it to $A$ while subtracting from $B$, landing both on the average. So the condition is exactly

$$A + B \equiv 0 \pmod 2$$

Looking for a quantity the operations cannot change is the standard opening move for "can this state be reached" problems, and it is usually faster than trying to construct a sequence of moves. Here the invariant immediately gives both directions of the proof — impossibility when the sum is odd, and an explicit one-move construction when it is even.

Note that $d$ is unrestricted: it may be negative, zero, or larger than either number, and the problem never requires the values to stay positive. That generality is what makes a single move always sufficient; a constraint keeping both numbers non-negative would make this a harder question.

Since $A$ and $B$ have the same parity exactly when their sum is even, `(a + b) % 2 == 0` and `a % 2 == b % 2` are interchangeable here. Sample case 1 has equal numbers already ($d = 0$ works); sample case 2 has an odd sum and is impossible.
