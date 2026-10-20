---
topic: Greedy
subtopic: Greedy change-making in a canonical system
time: $O(k)$ per test case, $k = 6$ denominations
space: $O(1)$
---
Minimise the number of notes summing to $N$, using denominations $\{1, 2, 5, 10, 50, 100\}$. Walk the denominations from largest to smallest, taking as many of each as fit:

```
count += n // d
n %= d
```

The greedy works here, but it is worth being precise about *why*, because greedy change-making is **not** correct in general. A currency system is called **canonical** when the greedy algorithm is optimal for every amount, and this one is. The classic counterexample is $\{1, 3, 4\}$: greedily making $6$ takes $4 + 1 + 1$ for three coins, while $3 + 3$ needs only two. For such systems the minimum requires dynamic programming, at $O(N \cdot k)$.

What saves this system is that each denomination divides fairly neatly into the next, so taking a large note never strands the remainder in a position where smaller notes do worse. The same property licensed the greedy in the $\{5, 10\}$ coins problem.

Iterating over a tuple of denominations, rather than writing six divisions by hand, keeps the structure visible and makes the ordering requirement explicit — the list **must** be sorted descending, since processing $1$ first would consume the whole amount in ones.

Sample case 3: $242 \to$ two $100$s, leaving $42 \to$ four $10$s, leaving $2 \to$ one $2$. That is $2 + 4 + 1 = 7$ notes.
