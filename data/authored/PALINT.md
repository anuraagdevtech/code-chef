---
topic: Bit Manipulation
subtopic: XOR pairs values into two-element orbits
time: $O(N)$ per test case
space: $O(N)$
---
XOR with a fixed $X$ is an involution, so each element can only ever hold one of two values, $a$ or $a \oplus X$. The values therefore split into **orbits** $\{a,\, a \oplus X\}$, and elements in different orbits can never be made equal.

So for a target value $v$, every element already equal to $v$ stays put and every element equal to $v \oplus X$ needs exactly one operation:

$$\text{count}(v) = \mathrm{cnt}[v] + \mathrm{cnt}[v \oplus X], \qquad \text{ops}(v) = \mathrm{cnt}[v \oplus X]$$

Both $v$ and $v \oplus X$ give the same count, so per orbit the best is

$$\text{count} = \mathrm{cnt}[a] + \mathrm{cnt}[a \oplus X], \qquad \text{ops} = \min\bigl(\mathrm{cnt}[a],\ \mathrm{cnt}[a \oplus X]\bigr)$$

— flip whichever side is smaller. Scanning the distinct values and taking the largest count, breaking ties by fewest operations, answers both questions at once.

The case $X = 0$ needs care: then $a \oplus X = a$ and the formula would double-count. With $X = 0$ no operation changes anything, so the answer is the largest frequency with $0$ operations.

The samples show each situation. $A = [1,2,3]$ with $X = 2$ has the orbit $\{1,3\}$ containing two elements, so two can be made equal with one flip. $A = [1,\ldots,5]$ with $X = 100$ has every orbit partner outside the array, so nothing can be merged: `1 0`. And $A = [2,2,6,6]$ with $X = 1$ has orbits $\{2,3\}$ and $\{6,7\}$ with the partners absent, so the best is the two existing twos at no cost.
