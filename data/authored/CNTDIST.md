---
topic: Sets
subtopic: Replacing a linear scan with a hash set
time: $O(n)$ overall
space: $O(n)$
---
Two things are asked: the complexity of Chef's code, and the actual answer.

**The exponent.** Chef's approach compares each new element against **every element seen so far**. Processing element $i$ costs $O(i)$ comparisons, so the total is

$$1 + 2 + \cdots + (n-1) = \frac{n(n-1)}{2} = \Theta(n^2)$$

giving $a = 2$. That is why it times out at $n = 10^5$ — around $5 \times 10^9$ comparisons.

**The fix.** A hash set makes membership $O(1)$ on average instead of $O(i)$, so the whole pass is $O(n)$. In Python that is simply `len(set(values))`, which both deduplicates and counts in one go.

The trade is the classic one: $O(n)$ extra space buys a factor of $n$ in time. Sorting would be a middle road at $O(n \log n)$ and $O(1)$ extra space, but hashing is strictly better here since the values need no ordering.

The problem's note that the elements are drawn **uniformly at random** from a range of $10^9$ matters for the hashing guarantee: it rules out the adversarial collision patterns that could degrade a hash set toward $O(n)$ per lookup.

The published sample prints `*` on the first line rather than the real exponent — the statement says explicitly that this is a placeholder to show the output format, not the answer. So the sample cannot be compared verbatim, and this repository checks it with a real checker: line one must be $2$, and line two the true distinct count.

Note there is **no $T$**: the input is a single array, with $n$ followed by $n$ values one per line.
