---
topic: Basic Math
subtopic: Triangular numbers and a local search
time: $O(1)$ per test case
space: $O(1)$
---
Station $k$ sits at the triangular number $T_k = \frac{k(k+1)}{2}$, since the gaps are $1, 2, 3, \ldots$

Reaching station $k$ is cheap: walk one unit to station $1$ (one minute), then ride $k-1$ hops (one minute each), for **$k$ minutes total** regardless of how far away it is. From there, walk the remaining $|X - T_k|$ units. So the cost of using station $k$ is

$$k + |X - T_k|$$

and pure walking costs $X$. The answer is the minimum.

Scanning every $k$ would cost about $\sqrt{2X} \approx 45{,}000$ steps, which is affordable but unnecessary. The function is **unimodal**: while $T_k < X$ the cost is $k + X - T_k$, and each step adds $1$ to $k$ while subtracting $k+1 \geq 2$ from the walk, so it strictly decreases; once $T_k > X$ it strictly increases. So only the two stations bracketing $X$ matter, found by inverting the triangular formula with $\texttt{isqrt}$.

Sample $X = 9$ shows the key behaviour: station $4$ sits at $10$, **past** the cinema, yet riding there (4 minutes) and walking back one unit beats stopping at station $3$ at point $6$ and walking three units. Overshooting is often optimal, because riding is flat-rate while walking is not.

Sample $X = 2$ ties at $2$ — walk the whole way, or ride to station $1$ and walk one more.

Using `math.isqrt` rather than a float square root keeps the station index exact at $X = 10^9$.

## Edge cases

- **Walking the whole way is a candidate**, which is what `best = x` represents — it is the $k = 0$ case, and for $X = 1$ and $X = 2$ it ties or wins.
- **The cost is unimodal in $k$**, since riding further adds one minute per station while the walk shrinks by an ever-growing amount and then grows again — so only the stations bracketing $X$ matter, not a full scan.
- **Overshooting can beat undershooting.** At $X = 9$ the nearest station below is $6$ (cost $3 + 3 = 6$) but station $4$ at $10$ costs $4 + 1 = 5$ — so the window must include stations past $X$, which is why the loop runs to $k_0 + 2$.
- **`isqrt` must be exact.** Inverting $k(k+1)/2 \leq X$ gives $k_0 = \lfloor (\sqrt{8X+1} - 1)/2 \rfloor$, and a float `sqrt` at $X = 10^9$ can land one off and shift the window.
- **The window is widened by one on each side** rather than trusted exactly, which costs nothing and absorbs any off-by-one in the inversion.
- **$X$ up to $10^9$** puts $k_0$ near $44{,}720$, so the closed-form inversion is essential — scanning stations would be $10^4$ per case but computing them all would not scale.

## Dry run

$X = 9$. Stations sit at $1, 3, 6, 10, 15, \dots$

| $k$ | station at $k(k+1)/2$ | ride cost | walk $|9 - T_k|$ | total |
|---:|---:|---:|---:|---:|
| 0 | 0 (home) | 0 | 9 | 9 |
| 2 | 3 | 2 | 6 | 8 |
| 3 | 6 | 3 | 3 | 6 |
| 4 | 10 | 4 | 1 | **5** |
| 5 | 15 | 5 | 6 | 11 |

Output `5`: ride four stations past the target, then walk back one unit.
