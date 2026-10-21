---
topic: Combinatorics
subtopic: Complete layered DAG minus the forbidden pairs
time: $O(1)$ per test case
space: $O(1)$
---
A DAG's edges all point forward in some topological order, so the ceiling is the complete forward graph with $\binom{N}{2}$ edges. The source and sink requirements only remove edges from it.

Lay the vertices out as **sources, then middles, then sinks**. Every forward edge is allowed except two families:

- an edge between two sources would give the later one an incoming edge, so all $\binom{K}{2}$ source-source pairs are forbidden;
- symmetrically all $\binom{L}{2}$ sink-sink pairs are forbidden.

Everything else is fine, and this layout simultaneously satisfies the middles (each gets an edge from a source and one to a sink, so it is neither a source nor a sink).

When $K + L > N$ the groups cannot be disjoint, and a vertex that is both a source and a sink is **isolated** — no edges at all. Since isolated vertices only waste capacity, take as few as the counts force:

$$b = \max(0,\ K + L - N)$$

and apply the layout to the other $N - b$ vertices, which then have $K - b$ pure sources and $L - b$ pure sinks:

$$\text{answer} = \binom{N-b}{2} - \binom{K-b}{2} - \binom{L-b}{2}$$

The samples show both regimes. $N = 3, K = L = 1$ has $b = 0$ and no forbidden pairs, so the full $\binom{3}{2} = 3$ edges. $N = 5, K = L = 3$ forces $b = 1$: one vertex is isolated, and the remaining four split into two sources and two sinks with no middles, giving $6 - 1 - 1 = 4$ — only the four source-to-sink edges survive.

With $N$ up to $10^9$ the count reaches about $5 \times 10^{17}$, which needs 64-bit arithmetic in C++; Python's integers are unbounded.

## Edge cases

- **Sources cannot point at each other, and neither can sinks.** An edge between two sources would give one of them an incoming edge, so the $K$ sources form an independent set — and likewise the $L$ sinks. That removes $\binom{K}{2} + \binom{L}{2}$ from the complete DAG's $\binom{N}{2}$.
- **When $K + L > N$ some vertices must be both**, and such a vertex has no edges at all — so $K + L - N$ vertices drop out entirely and the formula is applied to what remains.
- **That subtraction must come first.** The second sample has $K = L = 3$ with $N = 5$; treating it directly gives $10 - 3 - 3 = 4$ by luck, but the reduced form $n' = 4$, $k' = l' = 2$ is what generalises.
- **$K + L \leq N$ needs no adjustment**, which the `max(0, …)` clamp handles (the first row).
- **A source may point at a sink**, so those cross edges are kept — only the within-group pairs are lost.
- **$K, L < N$ is guaranteed**, so at least one vertex is neither purely a source nor purely a sink after reduction.
- **$N$ up to $10^9$** makes the triangular numbers reach $5 \times 10^{17}$ — past 32-bit, and native in Python.

## Dry run

Second sample: $N = 5$, $K = 3$ sources, $L = 3$ sinks.

| step | value |
|---|---:|
| vertices forced to be both | $3 + 3 - 5 = 1$ |
| remaining vertices $n'$ | 4 |
| pure sources $k'$ | 2 |
| pure sinks $l'$ | 2 |
| complete DAG $\binom{4}{2}$ | 6 |
| minus $\binom{2}{2}$… $\binom{k'}{2} = 1$ | 5 |
| minus $\binom{l'}{2} = 1$ | **4** |

Output `4`; the isolated vertex counts as both a source and a sink while carrying no edges.
