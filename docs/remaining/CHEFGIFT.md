# Birthday Gift (CHEFGIFT)

[Problem statement](https://www.codechef.com/problems/CHEFGIFT) · [Python solution](../../solutions/CHEFGIFT.py)

## Approach

First compute all-pairs minimum road-switch costs, since multiple switches can occur between toll booths. Dynamic programming over booth positions then chooses the cheapest preceding road plus its switch cost. Subtract the minimum total toll from the budget.

## Complexity

- Time: O(M cubed+N M squared).
- Space: O(M squared+NM).
