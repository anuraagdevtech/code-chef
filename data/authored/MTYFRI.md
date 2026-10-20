---
topic: Greedy
subtopic: Exchange the largest for the smallest
time: $O(N \log N)$ per test case
space: $O(N)$
---
Play proceeds strictly left to right, so Motu takes the even-indexed elements and Tomu the odd ones — the positions are fixed, and only *which values sit in them* can change.

A swap moves one value out of Motu's set and one into it. The useful kind trades one of **Motu's largest** for one of **Tomu's smallest**: if Motu holds $m$ and Tomu holds $u$ with $m > u$, swapping shifts the score gap by $2(m - u)$ in Tomu's favour — he gains $m - u$ and Motu loses the same.

So sort Motu's values descending and Tomu's ascending, then pair them off: the first swap trades Motu's biggest for Tomu's smallest, the second his next biggest for her next smallest, and so on for up to $K$ swaps. Stop early once $m \leq u$, because from there every remaining trade would shrink the gap rather than widen it.

The greedy is optimal because the swaps are independent — each takes one element from each side — and the gains $2(m_i - u_i)$ are sorted descending by construction, so taking the $K$ largest gains is best possible.

Swapping within one player's own set is pointless, since it changes neither total.

Sample case 1 has $K = 0$ and equal totals of $3$; Tomu needs **strictly** greater, so a tie is a loss — `NO`. Sample case 2 trades Motu's $6$ for Tomu's $3$, turning $12$–$7$ into $9$–$10$.
