---
topic: Conditionals & Case Work
subtopic: Intersecting interval constraints
time: $O(1)$ per test case
space: $O(1)$
---
Each person constrains the temperature $t$ from one side: Alice needs $t \geq A$, Charlie needs $t \geq C$, and Bob needs $t \leq B$. Together they describe an interval, and the question is whether that interval is non-empty.

The two lower bounds combine into the tighter of the pair — satisfying both $t \geq A$ and $t \geq C$ is the same as satisfying $t \geq \max(A, C)$. There is a single upper bound. So a valid temperature exists exactly when

$$\max(A, C) \leq B$$

Collapsing several same-direction bounds into one extremum is the general move here: many lower bounds become their maximum, many upper bounds become their minimum, and a solution exists when the resulting low point does not pass the high point.

Equality is allowed, so a single feasible temperature is enough. Sample case 3 ($A=30, B=35, C=35$) leaves exactly one option, $35$ degrees, and answers `Yes`.

Note also that sample case 4 fails for a different reason than case 2: there $B = 25$ sits below even Alice's $A = 30$, so Bob alone conflicts with Alice. The single `max` comparison covers both failure modes without separate cases.
