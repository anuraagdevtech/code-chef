---
topic: Greedy
subtopic: Largest denomination first
time: $O(1)$ per test case
space: $O(1)$
---
Only $5$- and $10$-rupee coins exist, so every payable amount is a multiple of $5$. If $X \bmod 5 \neq 0$ the amount is impossible and the answer is $-1$ — sample case 3 covers this with $X = 8$.

Once divisibility holds, minimising the coin count means preferring the larger denomination: a $10$ replaces two $5$s, halving the count. So take $\lfloor X/10 \rfloor$ tens and then, if $5$ rupees remain, a single five:

$$\left\lfloor \frac{X}{10} \right\rfloor + \begin{cases} 1 & X \bmod 10 = 5 \\ 0 & \text{otherwise} \end{cases}$$

The greedy is safe here because the denominations are **nested** — $10$ is an exact multiple of $5$ — so taking a large coin never strands the remainder in a worse state. That property is what licenses the greedy, and it is not universal: with denominations $\{1, 3, 4\}$, greedily paying $6$ takes $4+1+1$ (three coins) when $3+3$ (two) is better. The general case needs dynamic programming; this one does not.

After removing all the tens the remainder is either $0$ or $5$, never anything else, precisely because divisibility by $5$ was already established. That is why a single conditional suffices rather than a second division.

Sample case 2: $X = 15$ gives one ten and one five, so $2$ coins — fewer than the three fives that also sum correctly.

## Edge cases

- **Not a multiple of $5$** ($X = 8$): the only coins are $5$ and $10$, so no combination reaches it and the answer is $-1$. The sample's third row.
- **An odd multiple of $5$** ($X = 15$): one $10$ and one $5$, so two coins.
- **A multiple of $10$** ($X = 50$): all tens, five coins, no fives needed.
- **Smallest payable amount** ($X = 5$): a single coin.
- **Greedy is safe here because $5$ divides $10$.** With nested denominations, taking as many tens as possible never strands an unpayable remainder — the leftover is either $0$ or exactly $5$. That would not hold for a set like $\{1, 3, 4\}$.

## Dry run

| $X$ | $X \bmod 5$ | tens $X // 10$ | a five left? | output |
|---:|---:|---:|:---:|---|
| 50 | 0 | 5 | no | `5` |
| 15 | 0 | 1 | yes | `2` |
| 8 | 3 | — | — | `-1` |
