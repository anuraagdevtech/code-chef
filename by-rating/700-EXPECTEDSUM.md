[&larr; 699. Mex Subsequence](699-MEXSUB.md) &middot; [Index](README.md) &middot; [701. College Admissions &rarr;](701-ADMIT.md)

# 700. Expected Sum

> [`EXPECTEDSUM`](https://www.codechef.com/problems/EXPECTEDSUM) &middot; difficulty **2495** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Probability |
| **Technique** | Linearity of expectation over the positions Chef draws |
| **CodeChef tags** | `Mathematics`, `Probability`, `Combinatorics`, `Expected Value` |
| **Complexity class** | Logarithmic $O(\log n)$ |
| **Time** | $O(\log p)$ per test case |
| **Space** | $O(1)$ |

## Question

There are $N$ chits, out of which, $A$ chits have $1$ written on them and $B$ $(A+B = N)$ chits have $0$ written on them.

Chef and Chefina are taking alternate turns. They both have a personal score which is initially set to $0$. Chef starts first. On their turn, a player will:
- Pick a random chit among the available chits;
- Add the number written on the chit to their personal score;
- Remove the chit that was picked.

Determine the [expected](https://en.wikipedia.org/wiki/Expected_value) score of Chef after all chits have been picked.

The expected score can be written in the form of $\frac{P}{Q}$ such that $Q$ is not divisible by $998244353$ and its guaranteed that for testcases that $Q$ is not a multiple of $998244353$. Output the value of $P \cdot Q^{-1}$ mod $998244353$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two integers $A$ and $B$, the number of chits having $1$ and $0$ respectively.

**Output**

For each test case, output the expected score of Chef.
The expected score can be written in the form of $\frac{P}{Q}$. Output the value of $P \cdot Q^{-1}$ mod $998244353$.

## Constraints

- $1 \leq T \leq 1000$
- $0 \leq A, B \leq 10^9$
- $1 \leq A+B \leq 10^9$

## Sample

**Sample input**

```
3
1 1
0 5
3 4
```

**Sample output**

```
499122177
0
285212674
```

<details><summary>Explanation</summary>

**Test case $1$:** There is one chit with $1$ written on it and $1$ chit with $0$ written on it. Consider all possible cases as follows:
- Chef picks the chit with $1$ on his turn. Thus, Chefina picks the chit with $0$. The final score of Chef is $1$.
- Chef picks the chit with $0$ on his turn. Thus, Chefina picks the chit with $1$. The final score of Chef is $0$.

The expected score of Chef is $\frac {1}{2} \cdot 1 + \frac {1}{2} \cdot 0 = \frac {1}{2}$. This is equivalent to $1\cdot 2^{-1} = 499122177$.

**Test case $2$:** All chits have $0$ written on them. Thus, in any case, the final score would be $0$. Thus, the expected score of Chef is also $0$.

</details>

## Approach

Drawing chits uniformly at random without replacement produces a uniformly random ordering of the $N = A + B$ chits. Chef takes the 1st, 3rd, 5th, ... chits of that ordering, $\lceil N / 2 \rceil$ positions in total.

Any fixed position of a uniformly random ordering holds a `1` with probability $A / N$. By linearity of expectation - no independence is needed -

$$E[\text{Chef's score}] = \Bigl\lceil \frac{N}{2} \Bigr\rceil \cdot \frac{A}{N}.$$

The fraction is printed modulo $998244353$ using the modular inverse of $N$.

## Solution

```python
import sys


def solve(tokens):
    a, b = (next(tokens), next(tokens))
    n = a + b
    MOD = 998244353
    return str(a * ((n + 1) // 2) * pow(n, MOD - 2, MOD) % MOD)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- $A = 0$: the answer is 0.
- $N$ odd gives Chef one more draw than Chefina.
- $N < 998244353$ always, so the inverse exists.
- The product before reduction is about $10^{27}$, fine for Python integers.

## Dry run

- `A = 1, B = 1`: Chef draws 1 of 2 chits: $1 \cdot 1/2 = 1/2$, printed as `499122177`.
- `A = 3, B = 4`: Chef draws 4 of 7 chits: $4 \cdot 3/7 = 12/7$, printed as `285212674`.

---

Same problem grouped by topic: [../docs/probability/EXPECTEDSUM.md](../docs/probability/EXPECTEDSUM.md)
