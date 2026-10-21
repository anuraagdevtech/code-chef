---
topic: Sorting
subtopic: Connected components from gaps in sorted order
time: $O(N \log N + P)$
space: $O(N)$
---
The trap is reading "distance $\leq K$" as the whole condition. Messages **relay**: the sample answers `Yes` for frogs at $0$ and $8$ with $K = 3$, which is only possible by hopping $0 \to 3 \to 5 \to 8$. So the question is connectivity in the graph joining every pair within $K$, not a single distance test.

That graph has up to $\binom{N}{2}$ edges, but on a line its components have a simple shape. Sort the positions; two frogs are connected iff **every consecutive gap between them in sorted order is at most $K$**. If some gap exceeds $K$, no edge crosses it at all — any edge spanning it would itself be longer than $K$ — so it is a genuine cut. If all gaps are within $K$, the sorted chain itself is a path connecting them.

So one sweep suffices: sort, then assign component ids, starting a new id whenever the gap to the previous frog exceeds $K$. No DSU or BFS is needed — the components are contiguous blocks of the sorted order.

$$\text{answer} = \text{Yes} \iff \mathrm{comp}[a] = \mathrm{comp}[b]$$

Ties matter: frogs may share a position, giving a gap of $0$, which is always within $K$ — and $K = 0$ is allowed, in which case only co-located frogs can talk.

The sample sorts to $0, 3, 5, 8, 12$ with gaps $3, 2, 3, 4$. The last gap exceeds $K = 3$, so the components are $\{0,3,5,8\}$ and $\{12\}$. Hence frogs 1 and 2 (`Yes`), 1 and 3 (`Yes`, via the relay), and 2 and 5 (`No`, across the cut).

Note a query may name the same frog twice, which is trivially `Yes` — the component test handles it without a special case.
