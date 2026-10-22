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

## Edge cases

- **XOR with a fixed $X$ pairs values into two-element orbits** $\{a, a \oplus X\}$ — nothing can move between orbits, so the best achievable count is the largest orbit total.
- **Either side of an orbit can be the target**, and flipping the smaller side costs fewer operations — hence the secondary minimisation over $\min(c, c')$.
- **$X = 0$ makes the operation a no-op**, so the answer is the plain modal count with zero operations. Without that branch, $a \oplus 0 = a$ would double-count the same bucket.
- **An orbit with no partner present** contributes just its own count, with zero operations — the second sample row, where no value pairs up.
- **Equal orbit halves** make either choice cost the same, which the tuple comparison resolves deterministically.
- **The tuple trick `(total, -flips)`** maximises the count first and minimises the operations second in a single comparison.
- **Sum of $N \leq 5 \cdot 10^5$**, so each orbit is examined twice (once from each side) and that is affordable.

## Dry run

First sample: $A = 1, 2, 3$ with $X = 2$.

| value | partner $a \oplus 2$ | counts | orbit total | flips needed |
|---:|---:|---|---:|---:|
| 1 | 3 | $1 + 1$ | 2 | 1 |
| 2 | 0 (absent) | $1 + 0$ | 1 | 0 |
| 3 | 1 | $1 + 1$ | 2 | 1 |

Best total is $2$ at a cost of $1$, so the output is `2 1` — turn the $1$ into a $3$ (or the other way round).
