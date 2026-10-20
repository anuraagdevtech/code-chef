---
topic: Greedy
subtopic: Budgeting two resources
time: $O(N)$ per test case
space: $O(1)$
---
XOR over a binary subarray is just the **parity of its ones**, so an operation scores $1$ when it removes an odd number of ones, and $0$ otherwise. The goal is to maximise the number of odd-parity removals, each of which must span at least two elements.

So the question becomes: how should the $o$ ones and $z$ zeros be budgeted across operations?

The cheapest scoring operation takes **one 1 plus one 0** — it costs a single one and meets the length requirement using a zero. Doing as many of these as possible gives $\min(o, z)$ operations.

Once the zeros are exhausted, any further operation must be built from ones alone, and it needs an **odd** count of at least two — so three ones. Each such operation scores $1$ for three ones, so the leftovers contribute $\lfloor (o - \min(o,z)) / 3 \rfloor$ more.

Spending zeros first is right because a zero-padded operation costs one 1 while a pure-ones operation costs three.

$$\text{score} = a + \left\lfloor \frac{o - a}{3} \right\rfloor, \qquad a = \min(o, z)$$

Sample case 1, $[1,0,0,0,1]$, has $o = 2$ and $z = 3$: two cheap operations, score $2$. Sample case 2, $[1,1,1]$, has no zeros at all, so the only option is to take all three ones in one go — score $1$, which the $\lfloor 3/3 \rfloor$ term supplies. Sample case 3 has no ones and scores $0$.

A useful edge check is $[1,1]$: no zeros and only two ones, so $\lfloor 2/3 \rfloor = 0$ — the single possible operation removes two ones and XORs to $0$.
