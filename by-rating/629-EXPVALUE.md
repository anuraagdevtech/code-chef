[&larr; 628. Increase 2 consecutive characters](628-CCD.md) &middot; [Index](README.md) &middot; [630. Cherry and Bits &rarr;](630-CENS20A.md)

# 629. Expected Value

> [`EXPVALUE`](https://www.codechef.com/problems/EXPVALUE) &middot; difficulty **2177** &middot; time limit **2s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Probability |
| **Technique** | Carry the mean and the second moment through independent increments |
| **CodeChef tags** | `Mathematics`, `Probability`, `Expected Value` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ |
| **Space** | $O(1)$ besides the output |

## Question

Stack has a positive integer $P(P > 1)$.
He starts a game where his initial score is $0$.

In the $i^{th}$ turn, with a probability of $\frac{1}{2}$, Stack adds $\frac{1}{P^{i-1}}$ to his score.

Stack stops after $N$ turns.

Let $S_i$ be his score after $i$ turns and $F(i)$ denote the [expected value](https://en.wikipedia.org/wiki/Expected_value) of $S_i^2$.

For each integer $i(1 \leq i \leq N)$, find the value of $F(i)$ modulo $998244353$.

**Input**

The only line of input contains two space-separated positive integers $N$ and $P$, as mentioned in the statement.

**Output**

Print $N$ space-separated integers. For each integer $i(1 \leq i \leq N)$, output the value of $F(i)$ modulo $998244353$.

Formally, let $M=998244353$. It can be shown that the answer can be expressed as an irreducible fraction $\frac{x}{y}$, where $x$ and $y$ are integers and $y \not \equiv 0 \pmod{M}$.
Output the integer equal to $x \cdot y^{-1} \bmod M $.
In other words, output such an integer $z$ that $0 \leq z < M$ and $z \cdot y \equiv x \pmod{M}$.
.

## Constraints

- $1 \leq N \leq 3 \cdot 10^5$
- $2 \leq P \leq 10^5$

## Sample

**Sample 1 input**

```
2 2
```

**Sample 1 output**

```
499122177 124780545
```

<details><summary>Explanation</summary>

$S_1$ can be $0$ or $1$ with equal probability.
Thus $F(1)=\frac{0 \cdot 0}{2}+\frac{1 \cdot 1}{2} = \frac{1}{2}$.

$F(2)=\frac{7}{8}$.

</details>

**Sample 2 input**

```
10 343
```

**Sample 2 output**

```
499122177 379526990 822885144 761122022 256959043 151932103 340445396 758502677 478338987 125853909
```

## Approach

Turn $i$ adds $w_i = P^{-(i-1)}$ with probability $\tfrac12$, independently of the past. If $S$ is the score so far and $X$ the new increment,

$$E[(S + X)^2] = E[S^2] + 2\,E[S]\,E[X] + E[X^2] = E[S^2] + E[S] \cdot w + \frac{w^2}{2},$$

using independence, $E[X] = w/2$ and $E[X^2] = w^2/2$. Also $E[S + X] = E[S] + w/2$.

So keep two numbers, the mean and the second moment, update them in that order for each turn, and print the second moment after every turn. All values are fractions modulo $998244353$: $1/2$ and $1/P$ are modular inverses, and $w$ is multiplied by $1/P$ each turn.

## Solution

```python
import sys


def main() -> None:
    n, base = map(int, sys.stdin.buffer.read().split())
    MOD = 998244353
    inv = pow(base, -1, MOD)
    half = (MOD + 1) // 2
    mean = second = 0
    weight = 1
    out = []
    for i in range(n):
        second = (second + mean * weight + half * weight * weight) % MOD
        mean = (mean + half * weight) % MOD
        out.append(str(second))
        weight = weight * inv % MOD
    print(' '.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- The second moment must be updated before the mean, since it uses the old mean.
- $F(1)$ is always $1/2$.
- Only one modular inverse of $P$ is needed; powers follow by multiplication.
- The output has $N$ values on one line.

## Dry run

`N = 2, P = 2`.

- Turn 1, $w = 1$: second moment $0 + 0 \cdot 1 + \tfrac12 = \tfrac12$; mean $\tfrac12$.
- Turn 2, $w = \tfrac12$: second moment $\tfrac12 + \tfrac12 \cdot \tfrac12 + \tfrac18 = \tfrac78$.

$1/2$ and $7/8$ modulo $998244353$ are `499122177` and `124780545`.

---

Same problem grouped by topic: [../docs/probability/EXPVALUE.md](../docs/probability/EXPVALUE.md)
