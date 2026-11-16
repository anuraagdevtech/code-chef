---
topic: Constructive
subtopic: A star with the minority-friendly colour in the centre
time: $O(B + W)$ per test case
space: $O(B + W)$ for the output
complexity_note: Auxiliary space excludes the buffered input and output.
---
- One vertex: the diameter is that single vertex, trivially alternating. Print its colour and no edges.
- Only one colour and at least two vertices: any diameter has two adjacent vertices of the same colour, so the answer is $-1$.
- Two vertices of different colours: the single edge.
- Three or more vertices with both colours: a tree on at least three vertices has diameter at least 2, and a star achieves 2. Its diameters are the paths leaf - centre - leaf, so we need two leaves of one colour and a centre of the other. Some colour has at least two vertices; put a vertex of the *other* colour in the centre and everything else on the leaves.

In the output vertex 1 is the centre and every other vertex is joined to it.

## Edge cases

- $B + W = 1$ prints only the colour string.
- $B = 0$ or $W = 0$ with more than one vertex is impossible.
- When white has at least two vertices the centre is black; otherwise white is the centre and black supplies the two leaves.
- Several trees are optimal, so the output is validated by a checker.

## Dry run

`B = 1, W = 2`: white has two vertices, so the centre is black. Colours `BWW`, edges `1 2` and `1 3`. The diameter `2 - 1 - 3` reads W, B, W.

`B = 3, W = 1`: white cannot supply two leaves, so the white vertex is the centre: colours `WBBB`, edges `1 2`, `1 3`, `1 4`; the diameter B, W, B alternates.
