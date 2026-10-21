---
topic: Constructive
subtopic: Checkerboard parity, with a third colour only when forced
time: $O(NM)$ per test case
space: $O(M)$
---
A grid is bipartite, so two colours always suffice for a proper colouring: paint by the parity of $r + c$. The only question is whether the two pre-painted cells are compatible with such a colouring.

In any 2-colouring of a grid, cells of the same $r + c$ parity get the same colour. So:

- **Parities differ:** the checkerboard assigning colour $1$ to the parity of $(x_1, y_1)$ and colour $2$ to the other parity respects both fixed cells. Two colours, the minimum possible.
- **Parities match:** both fixed cells would need the same colour, but they are $1$ and $2$. So two colours are impossible and **three** is the answer. Build it as a checkerboard in colours $1$ and $3$ — colour $1$ on the parity of $(x_1, y_1)$ — and then overwrite $(x_2, y_2)$ with $2$. That cell's neighbours all lie on the other parity and carry $3$, so the colouring stays proper.

Three is never exceeded, so the construction is optimal in both branches.

The second sample has $(1,1)$ and $(1,2)$ on opposite parities, so the plain checkerboard works and uses two colours. The first sample has $(1,1)$ and $(2,2)$ both on even parity, forcing three: our grid is $\begin{smallmatrix}1 & 3\\ 3 & 2\end{smallmatrix}$ while the sample prints $\begin{smallmatrix}1 & 4\\ 4 & 2\end{smallmatrix}$ — the third colour's value is free, any of $1 \ldots 10^9$ will do, so both are accepted.

Note $N, M \geq 2$, so the grid always has at least one adjacency and the conflict is real rather than vacuous.
