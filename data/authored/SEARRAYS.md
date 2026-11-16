---
topic: Combinatorics
subtopic: Counting tilings with a single zero and a block of K ones
time: $O(N)$ per test case
space: $O(N)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
An operation subtracts 1 from $K$ consecutive positions, and the entries are only 0 or 1, so no position may be covered twice: a good array is exactly a union of disjoint length-$K$ segments of ones. Equivalently every maximal run of ones has a length divisible by $K$, and cutting such a run into consecutive blocks of $K$ is unique.

So good arrays of length $n$ correspond one-to-one to tilings of a strip of length $n$ with tiles `0` (length 1) and `11...1` (length $K$):

$$f(i) = f(i-1) + f(i-K), \qquad f(i) = 1 \text{ for } i < K.$$

## Edge cases

- $K = 1$: both tiles have length 1 and are different, so the count is $2^n$ - the recurrence gives exactly that.
- $K = n$: only all zeros or all ones, answer 2.
- $i < K$: only the all-zero array, answer 1.
- Reduce modulo $10^9 + 7$ at every step.

## Dry run

`n = 5, K = 2`: $f = 1, 1, 2, 3, 5, 8$ for $i = 0 \dots 5$, the Fibonacci numbers. Answer 8.

`n = 3, K = 3`: $f(3) = f(2) + f(0) = 2$ - the arrays `000` and `111`.
