---
topic: Trees
subtopic: Rerooting - subtree gcds below, complement gcds above
time: $O(N \log A)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Destroying vertex $u$ leaves one component per child of $u$ - that child's whole subtree - and, unless $u$ is the root, one component containing everything outside the subtree of $u$. The damage is the sum of the gcds of these components.

Subtree gcds come from a bottom-up pass. For the outside part define `outside[v]` as the gcd of all vertices not in the subtree of $v$. For a child $v$ of $u$ it is the gcd of `outside[u]`, the value of $u$, and the subtree gcds of all *other* children of $u$. Computing "all but one" for every child with prefix and suffix gcds over the child list keeps this linear even at vertices of high degree.

The answer is the maximum over $u$ of `outside[u]` plus the sum of its children's subtree gcds; for the root the outside part is empty and counts 0.

## Edge cases

- Destroying a leaf leaves a single component.
- The root has no outside component.
- A star's centre has many children; the prefix/suffix trick avoids a quadratic scan there.
- In this problem the edges come before the values in the input.

## Dry run

Edges `1-2, 1-3, 3-4, 3-5`, values `4 6 8 12 15`.

Subtree gcds (root 1): $g_2 = 6$, $g_4 = 12$, $g_5 = 15$, $g_3 = \gcd(8, 12, 15) = 1$.

- Destroy 1: $g_2 + g_3 = 7$.
- Destroy 3: outside is $\gcd(4, 6) = 2$; children give $12 + 15$; total 29.
- Destroying 2, 4 or 5 leaves one component with gcd 1.

Answer 29.
