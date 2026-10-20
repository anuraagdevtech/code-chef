---
topic: Basic Math
subtopic: Counting even values in a range
time: $O(1)$ per test case
space: $O(1)$
---
Chef serves at the start of the game, and thereafter whenever he wins a point. So each of Chef's serves happens at a distinct score of his own: $0$ at the opening serve, then $1$ after his first point, then $2$, and so on up to $P$. He serves exactly once at each of the scores $0, 1, \ldots, P$.

Rule 3 says he serves from the **right** when his score is even. So the answer is the number of even integers in $[0, P]$:

$$\left\lfloor \frac{P}{2} \right\rfloor + 1$$

The $+1$ is there because the range starts at the even value $0$ — the opening serve counts, and it is from the right.

The reasoning that each score from $0$ to $P$ is served exactly once is the real content. It holds no matter how the opponent's points are interleaved: Chef may lose the serve repeatedly, but he regains it precisely when he scores, and that is the moment his count ticks up. The opponent's score never enters the formula.

Checking the samples: $P = 9$ gives $4 + 1 = 5$ (scores $0,2,4,6,8$), and $P = 746$ gives $373 + 1 = 374$. The case $P = 0$ is valid too — Chef serves once, from the right, giving $1$.

With $P$ up to $10^9$ a loop is out of the question, but the closed form is immediate.
