---
topic: Arrays
subtopic: Fitting a window into the gaps between maxima
time: $O(N)$ per test case
space: $O(N)$
---
A right shift by $k$ moves the chocolate originally at index $i$ to position $i + k$, so the half Chef eats — positions $1 \ldots N/2$ — is the **cyclic block of $N/2$ original chocolates** starting at index $(N-k) \bmod N$. As $k$ runs over $0 \ldots N-1$ that start runs over every index exactly once, so the question becomes:

> how many cyclic windows of length $N/2$ contain no chocolate of maximum sweetness?

The maxima cut the circle into gaps of consecutive non-maximal chocolates. A window avoiding every maximum must sit inside one gap, and a gap of length $g$ holds

$$\max\bigl(0,\ g - N/2 + 1\bigr)$$

such windows. Summing over the gaps gives the answer, in one pass after locating the maxima.

Thinking in terms of gaps rather than shifts is what removes the $O(N^2)$ "check each shift" loop, and it makes the structure obvious: with two or more maxima well spread around the circle, no gap can reach half the length and the answer is $0$.

The samples are exactly that contrast. $[1,1,2,1,1,1]$ has a single maximum, leaving one gap of length $5$, so $5 - 3 + 1 = 3$ shifts work. $[1,1,2,1,1,2]$ has two maxima three apart, splitting the circle into gaps of length $2$ and $2$, both shorter than the required $3$ — so Chef cannot avoid the sweetest chocolate however he shifts.

Note that if every chocolate ties for the maximum there are no gaps at all, and the answer is $0$.
