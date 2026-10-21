---
topic: Basic Math
subtopic: Parity of consecutive prefix sums
time: $O(1)$ per test case
space: $O(1)$
---
Consecutive prefix sums differ by one element, so $A_i = S_i - S_{i-1}$ for $i \geq 2$. Both are odd, and odd minus odd is even, which fixes the parity pattern completely:

$$A_1 \text{ is odd}, \qquad A_2, \ldots, A_N \text{ are all even}$$

Conversely any such array has all prefix sums odd, so this is the only constraint besides distinctness and non-negativity. The two halves can therefore be minimised independently.

The smallest non-negative odd number is $1$, so $A_1 = 1$. The remaining $N-1$ entries are distinct non-negative evens, and the smallest such set is $\{0, 2, 4, \ldots, 2(N-2)\}$ — note $0$ is allowed, since the elements are only required to be non-negative. Its sum is $2 \cdot \frac{(N-2)(N-1)}{2}$, giving

$$\text{answer} = 1 + (N-2)(N-1)$$

No distinctness clash arises between the halves, because $1$ is odd and every other entry is even.

For $N = 3$ the array is $[1, 0, 2]$ with prefix sums $1, 1, 3$ — all odd — and sum $3$, matching the sample. Note the prefix sums need not be *increasing*, which is what lets $0$ appear.

The formula also covers the small cases without special-casing: $N = 1$ gives $1 + (-1)(0) = 1$ and $N = 2$ gives $1 + 0 = 1$, the array $[1, 0]$.

With $T$ up to $10^6$ the arithmetic is irrelevant and the I/O is the whole problem — read the stream in one go and join the output.

## Edge cases

- **Only the first element may be odd.** All prefix sums are odd, so consecutive sums differ by an even amount — meaning $A_2, \dots, A_N$ are all even, and $A_1$ is odd.
- **The minimum is then forced**: $A_1 = 1$, the smallest odd non-negative value, and the rest are the smallest distinct non-negative evens $0, 2, 4, \dots, 2(N-2)$, summing to $(N-2)(N-1)$.
- **Zero is allowed and is used**, since the elements need only be non-negative and distinct — excluding it would cost two extra.
- **$N = 1$** gives $1 + (-1)(0) = 1$, the single array $[1]$; the formula handles the negative factor correctly.
- **$N = 2$** gives $1$, from $[1, 0]$ — both prefix sums are $1$.
- **Distinctness is what forces the evens apart**, so the sum grows quadratically rather than staying linear.
- **$T$ up to $10^6$** with the note to use fast I/O, so the whole input is read and the output joined once.

## Dry run

| $N$ | optimal array | prefix sums | total |
|---:|---|---|---:|
| 1 | $[1]$ | $1$ | `1` |
| 2 | $[1, 0]$ | $1, 1$ | `1` |
| 3 | $[1, 0, 2]$ | $1, 1, 3$ | `3` |
| 4 | $[1, 0, 2, 4]$ | $1, 1, 3, 7$ | 7 |

Every prefix sum is odd, and the formula $1 + (N-2)(N-1)$ matches each row.
