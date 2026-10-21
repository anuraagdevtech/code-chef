---
topic: Greedy
subtopic: Exchange argument with a max-heap
time: $O((N + D) \log N)$ per test case
space: $O(N + D)$
---
Flip the objective. If nothing were scheduled the sadness would be the fixed total $\sum T_i S_i$, so minimising sadness is the same as **maximising the sadness avoided**, and each lecture granted to trainer $i$ avoids exactly $S_i$. Since there is at most one lecture per day, we are choosing which trainer gets each of the $D$ days.

A trainer arrives on day $D_i$ and stays to the end, so their availability is a **suffix** of days — trainer $i$ can use any day $\geq D_i$, up to $T_i$ of them. Walking days forward, the set of candidates only grows as trainers arrive.

The greedy is: on each day give the lecture to the available trainer with the largest $S_i$ who still wants lectures. The exchange argument is short. Suppose an optimal schedule gives day $d$ to trainer $y$ while trainer $x$ with $S_x > S_y$ is available on $d$ and has an unused quota. If $x$ is idle at some later day, swap — $x$ gains a lecture and $y$ loses one, changing the total by $S_x - S_y > 0$. If $x$ is busy on every later day, swap day $d$ with any one of them, which leaves the multiset of assignments unchanged. Either way the greedy choice is no worse.

Because availability is a suffix, a trainer once available never becomes unavailable, so a **max-heap keyed on $S_i$** is enough: bucket trainers by arrival day, push them as that day comes round, and each day serve the heap's top, decrementing its remaining lectures and popping when it hits zero.

The three samples show the three shapes. In the first, the $300$-trainer takes days 1 and 2 and the $100$-trainer gets only day 3, leaving one missed $100$-lecture. In the second, there is just enough room for everyone, so the answer is $0$. In the third, the $150$-trainer only arrives on day 3, so day 2 goes **unused** even though lectures are still wanted — a greedy that tried to pack days densely without respecting arrival would wrongly report $0$.
