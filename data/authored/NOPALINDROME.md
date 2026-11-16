---
topic: Constructive
subtopic: The greedy smallest number is periodic - count the digits in one period
time: $O(1)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Build the smallest number greedily from the left. It must start with 1. Then zeros are best, but $K + 1$ zeros in a row would be a palindrome longer than $K$, so exactly $K$ zeros follow. The next digit cannot be 0, and it cannot be 1 either, because `1 0...0 1` is a palindrome of length $K + 2$; so it is 2.

After the 2, zeros are again preferred, but a palindrome centred on the 2 grows by two with every zero, mirroring the zeros before it: `0..0 2 0..0` with $z$ zeros on each side has length $2z + 1$, which must stay at most $K$, so $z \le \lfloor (K-1)/2 \rfloor$. Then a 1 is allowed, and from there the situation is the same as at the start.

So the answer is the prefix of length $N$ of the periodic word

$$1 \; \underbrace{0 \dots 0}_{K} \; 2 \; \underbrace{0 \dots 0}_{\lfloor (K-1)/2 \rfloor}$$

with period $K + 2 + \lfloor (K-1)/2 \rfloor$ and digit sum 3 per period. A partial period contributes 1 if it is non-empty and 3 once it is long enough to include the 2, i.e. longer than $K + 1$.

## Edge cases

- $N$ is up to $10^9$, so only counting is possible.
- A partial period of length exactly $K + 1$ ends just before the 2 and contributes only 1.
- $K = 1$: the period is `102`.
- Substrings may have leading zeros and still count as palindromes, which is what limits the zero runs.

## Dry run

`N = 5, K = 1`: period `1 0 2` of length 3.

$5 = 1 \cdot 3 + 2$: one full period (sum 3) and a tail `1 0` of length 2, which is not longer than $K + 1 = 2$, so it adds 1.

The number is `10210` and the answer is 4.
