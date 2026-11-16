---
topic: Constructive
subtopic: Only the bipartition sizes matter; realise them with a double star
time: $O(\sqrt{x + y})$ per test case
space: $O(\sqrt{x + y})$ for the output
complexity_note: Auxiliary space excludes the buffered input and output.
---
A tree is bipartite, and the distance between two vertices is even exactly when they are on the same side. If the sides have $a$ and $b$ vertices, the ordered pairs (a vertex may be paired with itself) give

$$x = a^2 + b^2, \qquad y = 2ab .$$

Hence $x + y = (a + b)^2$ and $x - y = (a - b)^2$: both must be perfect squares, $n = \sqrt{x + y}$ is the number of vertices, and $|a - b| = \sqrt{x - y}$ must have the same parity as $n$ so that $a = (n + |a - b|)/2$ is an integer. Since $y \ge 1$, both sides are non-empty.

Any sizes $a, b \ge 1$ are realised by a double star: vertices $1 \dots a$ form one side and $a + 1 \dots n$ the other; join vertex 1 to every vertex of the second side, and join vertex $a + 1$ to the remaining vertices of the first side. That is $b + (a - 1) = n - 1$ edges, connected, and every edge crosses between the sides.

## Edge cases

- $x < y$ is impossible because $a^2 + b^2 \ge 2ab$.
- Either $x + y$ or $x - y$ not being a perfect square gives NO.
- A parity mismatch between $n$ and $|a - b|$ gives NO.
- Many trees have the right bipartition, so the output is validated by a checker.

## Dry run

`x = 29, y = 20`: $x + y = 49 = 7^2$ and $x - y = 9 = 3^2$, so $n = 7$, $a = 5$, $b = 2$ ($25 + 4 = 29$, $2 \cdot 10 = 20$).

Sides `{1, 2, 3, 4, 5}` and `{6, 7}`. Edges: `1-6`, `1-7`, then `6-2`, `6-3`, `6-4`, `6-5`.

`x = 3, y = 12`: $x < y$, so NO.
