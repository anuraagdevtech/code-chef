---
topic: Probability
subtopic: Linearity of expectation over the positions Chef draws
time: $O(\log p)$ per test case
space: $O(1)$
complexity_note: Auxiliary space excludes the buffered input and output.
---
Drawing chits uniformly at random without replacement produces a uniformly random ordering of the $N = A + B$ chits. Chef takes the 1st, 3rd, 5th, ... chits of that ordering, $\lceil N / 2 \rceil$ positions in total.

Any fixed position of a uniformly random ordering holds a `1` with probability $A / N$. By linearity of expectation - no independence is needed -

$$E[\text{Chef's score}] = \Bigl\lceil \frac{N}{2} \Bigr\rceil \cdot \frac{A}{N}.$$

The fraction is printed modulo $998244353$ using the modular inverse of $N$.

## Edge cases

- $A = 0$: the answer is 0.
- $N$ odd gives Chef one more draw than Chefina.
- $N < 998244353$ always, so the inverse exists.
- The product before reduction is about $10^{27}$, fine for Python integers.

## Dry run

- `A = 1, B = 1`: Chef draws 1 of 2 chits: $1 \cdot 1/2 = 1/2$, printed as `499122177`.
- `A = 3, B = 4`: Chef draws 4 of 7 chits: $4 \cdot 3/7 = 12/7$, printed as `285212674`.
