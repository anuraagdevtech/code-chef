---
topic: Number Theory
subtopic: Product expansion for parity, then base-5 indexing
time: $O(\log K)$ per test case
space: $O(1)$
---
The sum over all non-empty subsequences has a closed form. Expanding the product $\prod_i (1 + d_i)$ generates exactly one term per subset of digits — the product of the chosen digits — so subtracting the empty term gives

$$\sum_{s \in S} \mathrm{prod}(s) = \prod_{i=1}^{m} (1 + d_i) \;-\; 1$$

That sum is even iff the product is odd iff **every factor $1 + d_i$ is odd** iff every digit $d_i$ is even. So the magical numbers are precisely those written with digits from $\{0, 2, 4, 6, 8\}$ — the whole subsequence machinery collapses to a digit test.

Checking the statement's examples: $246$ gives $3 \cdot 5 \cdot 7 - 1 = 104$, even; $55$ gives $6 \cdot 6 - 1 = 35$, odd; and $204$ gives $3 \cdot 1 \cdot 5 - 1 = 14$, even.

Listing them in order — $0, 2, 4, 6, 8, 20, 22, \ldots$ — reveals a **base-5 numbering**: the $K$-th magical number is $K-1$ written in base $5$ with each digit doubled. This works because the even digits are an ordered alphabet of size $5$, and the ordering of magical numbers by value matches the lexicographic ordering of their base-5 codes, including leading zeros.

So the answer is a base conversion: write $K - 1$ in base $5$, then map each digit $c \mapsto 2c$. With $K \leq 10^{12}$ that is about $18$ digits, so each query is a short loop and $T = 10^5$ is comfortable.

The samples confirm the indexing starts at $0$: $K = 2$ gives $K-1 = 1$, i.e. `1` in base $5$, so $2$; and $K = 5$ gives $4$, so $8$. $K = 6$ would give `10`, i.e. $20$.

## Edge cases

- **The subsequence sum collapses to a product.** Summing $\mathrm{prod}(s)$ over all non-empty digit subsequences gives $\prod (1 + d_i) - 1$, so "magical" means that product is odd — which happens exactly when every digit is even.
- **So magical numbers are the all-even-digit numbers**, listed increasingly as $0, 2, 4, 6, 8, 20, 22, \dots$ — and the $K$-th one is $K-1$ written in base $5$ with each digit doubled.
- **The list is 0-indexed from $0$**, so $K$ must be decremented first: $K = 1$ gives the magical number $0$.
- **The do-while shape matters.** A plain `while k:` loop would emit nothing for $k = 0$ and print an empty string instead of `0`.
- **No leading zeros appear**, because the base-5 representation of a positive $k$ never starts with $0$, and doubling preserves that.
- **$K$ up to $10^{12}$** gives about $18$ base-5 digits, so the answer is built as text rather than as an integer.
- **The digit $0$ is even and allowed inside the number**, which is why base $5$ (not base $4$) is the right radix.

## Dry run

| $K$ | $K - 1$ | base 5 | digits doubled | magical number |
|---:|---:|---|---|---|
| 1 | 0 | $0$ | $0$ | `0` |
| 2 | 1 | $1$ | $2$ | `2` |
| 5 | 4 | $4$ | $8$ | `8` |
| 6 | 5 | $10$ | $2, 0$ | `20` |

Check $246$: $\prod(1+d) = 3 \cdot 5 \cdot 7 = 105$, odd, so $105 - 1 = 104$ is even and $246$ is magical — consistent with all its digits being even.
