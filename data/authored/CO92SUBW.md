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
