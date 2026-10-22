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

## Edge cases

- **Chef's code compares each new element against every earlier one**, costing $1 + 2 + \dots + (n-1) = \Theta(n^2)$ comparisons — so the exponent asked for is $2$.
- **A hash set replaces the linear membership scan with an average $O(1)$ lookup**, bringing the whole count to $O(n)$ and fixing the time limit.
- **The elements are stated to be uniformly random**, which is what makes the average-case hashing argument safe rather than merely typical.
- **Two things are printed**: the exponent on one line and the distinct count on the next.
- **The sample shows `*` for the exponent**, a placeholder — a special judge accepts the correct value there rather than matching the literal.
- **Duplicates collapse**, which is the whole point: the sample's $1, 2, 1$ has two distinct values.
- **There is no test-case count**: the input is $n$ followed by the array.
- **The values are compared as raw tokens**, safe because the input has no leading zeros.

## Dry run

Sample: $n = 3$ with the array $1, 2, 1$.

| step | element | already seen? | distinct so far |
|---:|---:|:---:|---:|
| 1 | 1 | no | 1 |
| 2 | 2 | no | 2 |
| 3 | 1 | yes | 2 |

Chef's version would make $0 + 1 + 2 = 3$ comparisons here, and $\Theta(n^2)$ in general — hence the exponent `2`, then the count `2`.
