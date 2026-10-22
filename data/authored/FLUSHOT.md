---
topic: Binary Search
subtopic: Binary search on a real-valued answer
time: $O(N \log \frac{1}{\varepsilon})$ per test case
space: $O(N)$
---
Ask whether a given maximum movement $D$ suffices. Each person $i$ may end up anywhere in $[x_i - D,\ x_i + D]$, clipped below at $0$ since nobody may pass the receptionist, and consecutive people must sit at least $T$ apart.

That feasibility test is a **left-greedy sweep**: push each person as far left as the rules permit.

$$p_1 = \max(0,\ x_1 - D), \qquad p_i = \max(p_{i-1} + T,\ x_i - D)$$

and the arrangement fails the moment some $p_i$ exceeds $x_i + D$. Placing each person as early as possible is optimal because it leaves the most room for everyone after them — any feasible arrangement can be slid left to this one.

Since the people arrive in non-decreasing order, keeping them in that order is also optimal: swapping two would only widen the distance one of them must travel.

Feasibility is monotone in $D$ — more slack never hurts — so a **binary search on the real line** finds the threshold. About $100$ halvings take the interval well below the $10^{-4}$ the output needs.

Sample case 3 is the instructive one. Three people crowd near the receptionist at $0$, $0.5$ and $0.6$ while a fourth sits far off at $2.75$. The cramped trio must spread to $0$, $1$ and $2$, and it is the person at $0.6$ who moves furthest — $1.4$ — not the isolated one, who barely shifts.

The answer is printed to four decimal places, matching the published format.

## Edge cases

- **The objective is the largest single move**, so binary searching that value turns the problem into a feasibility question: can everyone reach a legal spot within distance $d$?
- **Pushing everyone as far left as allowed is optimal**, because the leftmost legal position for person $i$ leaves the most room for everyone after them — a greedy that never needs revisiting.
- **The order is preserved.** People stay in line, so person $i$'s new spot must be at least $T$ past person $i-1$'s, which is what `max(place + T, x - d)` enforces.
- **Nobody may step behind position $0$**, hence the clamp on the first placement.
- **Infeasibility shows up as overshooting the right bound**: if the forced spot exceeds $x + d$, this $d$ is too small.
- **The inputs carry up to three decimals**, so the answer is real-valued and $100$ bisection rounds take the interval far below the required precision.
- **The upper bound must be generous** — $T \cdot N + x_N$ covers the worst spread — and the answer is printed to four decimals.

## Dry run

Third sample: $N = 4$, $T = 1$, positions $0, 0.5, 0.6, 2.75$. Testing $d = 1.4$:

| person | original | earliest legal spot | within $x + d$? |
|---:|---:|---:|:---:|
| 1 | 0 | $\max(0, 0 - 1.4) = 0$ | $0 \leq 1.4$ ✓ |
| 2 | 0.5 | $\max(0 + 1, -0.9) = 1$ | $1 \leq 1.9$ ✓ |
| 3 | 0.6 | $\max(1 + 1, -0.8) = 2$ | $2 \leq 2.0$ ✓ |
| 4 | 2.75 | $\max(2 + 1, 1.35) = 3$ | $3 \leq 4.15$ ✓ |

Feasible, and person $3$ sits exactly on its bound — so $1.4$ is the answer. Output `1.4000`.
