---
topic: Strings
subtopic: Longest repeated run
time: $O(N)$ per test case
space: $O(1)$
---
A boring substring is a run of one repeated character, so for each letter only its **run lengths** matter.

Fix a letter with runs of lengths $r_1 \geq r_2 \geq \cdots$. A boring substring of that letter with length $m$ occurs $\max(0, r - m + 1)$ times inside a run of length $r$, and it must occur at least twice overall. There are exactly two ways to achieve that:

- **Twice inside the longest run**, which needs $r_1 - m + 1 \geq 2$, i.e. $m \leq r_1 - 1$;
- **Once in each of the two longest runs**, which needs $m \leq r_2$.

So the best length for that letter is $\max(r_1 - 1,\ r_2)$, and the answer is the maximum over all $26$ letters.

Both branches are genuinely needed. Sample case 1, `aaa`, has a single run of $3$: sliding a window of length $2$ gives two occurrences, so the answer is $2$ — the first branch. Sample case 4, `caabaa`, has two runs of `a` of length $2$ each: here $r_1 - 1 = 1$ but $r_2 = 2$, so the second branch wins with $2$.

Sample case 3, `bcaca`, has two runs of length $1$ for both `a` and `c`, giving $\max(0, 1) = 1$.

Sample case 2, `abc`, has every run at length $1$ with no repeats, so $\max(0, 0) = 0$ — the explicit "no answer" case.

Tracking only the two largest runs per letter keeps this to one pass and constant space, which matters at $\sum N = 5 \times 10^5$.
