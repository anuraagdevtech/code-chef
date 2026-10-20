---
topic: Geometry
subtopic: Chebyshev distance
time: $O(1)$ per test case
space: $O(1)$
---
The problem hands over the formula directly:

$$D = \max\left(|X_1 - X_2|,\; |Y_1 - Y_2|\right)$$

so the implementation is `max(abs(x1 - x2), abs(y1 - y2))`.

What is worth knowing is *why* this is called the chessboard distance. It counts the moves a **king** needs to travel between two squares. A king may step one square in any of eight directions, so it closes the horizontal and vertical gaps simultaneously whenever both are non-zero; the journey therefore costs only the larger of the two gaps, with the smaller one covered for free along the diagonal.

This metric, also called the Chebyshev or $L_\infty$ distance, sits alongside two neighbours worth contrasting:

- **Manhattan** ($L_1$): $|{\Delta x}| + |{\Delta y}|$ — a rook-like walk with no diagonals, so the gaps add.
- **Euclidean** ($L_2$): $\sqrt{\Delta x^2 + \Delta y^2}$ — straight-line distance.

The absolute values are essential and are the only place to slip. Sample case 3 has $\Delta x = 1 - 3 = -2$; without `abs`, the `max` would pick $\Delta y = 1$ and answer $1$ instead of $2$.

Sample case 2 shows the degenerate axis-aligned case: the points share an $x$, so the answer is purely the vertical gap.
