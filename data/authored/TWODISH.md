---
topic: Greedy
subtopic: Bottleneck across shared and exclusive resources
time: $O(1)$ per test case
space: $O(1)$
---
Both dish types consume **one vegetable** each; they differ only in the second ingredient, a fruit or a fish. That asymmetry is the whole problem.

Two limits apply:

- **Vegetables are shared.** Every dish needs one, so at most $B$ dishes can be made however the types are mixed.
- **Fruits and fish are interchangeable in aggregate.** Each dish needs exactly one of them, and Chef may freely choose which type to cook, so together they support at most $A + C$ dishes.

The maximum is therefore

$$\min(B,\ A + C)$$

and Chef succeeds when that reaches $N$.

Recognising that $A$ and $C$ **add** rather than each capping separately is the key step. Chef is not forced into a fixed ratio of the two dish types, so a shortage of fruit is covered by fish. Sample case 3 shows it: $A = 2$ and $C = 3$ give $5$ possible second ingredients, comfortably covering $N = 4$, with vegetables at $6$ not binding.

Sample case 2 is vegetable-bound: $A + C = 4$ would allow four dishes, but only $2$ vegetables exist, so just $2$ are possible against a required $3$.

Sample case 4 is the mirror case, bound by $A + C = 2$ while vegetables are plentiful at $3$. Dropping either term of the `min` fails one of these two.
