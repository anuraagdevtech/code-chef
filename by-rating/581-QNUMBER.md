[&larr; 580. Little Elephant and Median](580-MEDIAN.md) &middot; [Index](README.md) &middot; [582. Maximum And Or &rarr;](582-MAXANDOR.md)

# 581. Queries About Numbers

> [`QNUMBER`](https://www.codechef.com/problems/QNUMBER) &middot; difficulty **2026** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Factorise N once and answer from prime exponents |
| **CodeChef tags** | `Mathematics`, `Number Theory`, `Integer Factorisation` |
| **Complexity class** | Square root $O(\sqrt{n})$ |
| **Time** | $O(\sqrt{N} + Q \cdot \omega(N) \log K)$ |
| **Space** | $O(\omega(N))$ besides the output |

## Question

Chef loves number theory very much. Now it is time to solve a new kind of problem.

There is given a natural number **N**. Chef has to answer **Q** queries of the form **T K**.

Here **T** is the type of query and **K** is the natural number.

If **T=**1, Chef must find the number of natural numbers which is divisor of both **N** and **K**.

If **T=**2, Chef must find the number of natural numbers which is divisor of **N** and is divisible by **K**.

If **T=**3, Chef must find the number of natural numbers which is divisor of **N** and is not divisible by **K**.

Chef can solve all these queries, but you will be hungry for night if this happens, because Chef will not have free time to cook a meal. Therefore you compromise with him and decided that everyone must do his/her own job. You must program and Chef must cook.

**Input**

There will be 2 numbers in the first line: **N** and **Q**.

**Q** lines follow with 2 numbers each: **T** and **K**

**Output**

For each of the **Q** lines you must output the result for corresponding query in separat line.

**Constraints**

1<=**N**<=10^12
1<=**Q**<=5*10^5
1<=**T**<=3

1<=**K**<=10^12

## Constraints

1<=N<=10^12
1<=Q<=5*10^5
1<=T<=3
1<=K<=10^12

## Sample

**Sample input**

```
12 6
1 6
1 14
2 4
2 3
3 12
3 14
```

**Sample output**

```
4
2
2
3
5
6
```

<details><summary>Explanation</summary>

Numbers for each query:

{1,2,3,6}

{1,2}

{4,12}

{3,6,12}

{1,2,3,4,6}

{1,2,3,4,6,12}

</details>

## Approach

Factorise $N = \prod p_i^{e_i}$ once by trial division. $N$ has at most about a dozen distinct primes, so each query is cheap.

- Type 1, common divisors of $N$ and $K$: these are the divisors of $\gcd(N, K)$. The gcd only contains primes of $N$, so read its exponents $v_i$ by dividing by each $p_i$; the count is $\prod (v_i + 1)$.
- Type 2, divisors of $N$ that are multiples of $K$: there are none unless $K$ divides $N$. If it does, with exponents $v_i$ in $K$, the divisor's exponent of $p_i$ ranges over $v_i \dots e_i$: the count is $\prod (e_i - v_i + 1)$.
- Type 3, divisors of $N$ not divisible by $K$: the total number of divisors minus the type-2 answer.

## Solution

```python
import sys
from math import gcd


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n = next(tokens)
    q = next(tokens)
    rest = n
    factors = []
    prime = 2
    while prime * prime <= rest:
        exponent = 0
        while rest % prime == 0:
            rest //= prime
            exponent += 1
        if exponent:
            factors.append((prime, exponent))
        prime = 3 if prime == 2 else prime + 2
    if rest > 1:
        factors.append((rest, 1))
    total = 1
    for prime, exponent in factors:
        total *= exponent + 1
    out = []
    for _ in range(q):
        kind = next(tokens)
        k = next(tokens)
        if kind == 1:
            k = gcd(n, k)
            answer = 1
            for prime, exponent in factors:
                power = 0
                while k % prime == 0:
                    k //= prime
                    power += 1
                answer *= power + 1
        else:
            answer = 0
            if n % k == 0:
                answer = 1
                for prime, exponent in factors:
                    power = 0
                    while k % prime == 0:
                        k //= prime
                        power += 1
                    answer *= exponent - power + 1
            if kind == 3:
                answer = total - answer
        out.append(str(answer))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- $K$ not dividing $N$: type 2 is 0 and type 3 is the full divisor count.
- $K$ may have primes that $N$ lacks; the gcd in type 1 removes them.
- $N$ up to $10^{12}$ still factorises quickly by trial division.
- $K = 1$: type 2 counts all divisors and type 3 is 0.

## Dry run

`N = 12 = 2^2 * 3`, 6 divisors.

- `1 6`: gcd 6 = $2 \cdot 3$, count $2 \cdot 2 = 4$.
- `1 14`: gcd 2, count 2.
- `2 4`: $4 = 2^2$ divides 12: $(2 - 2 + 1)(1 - 0 + 1) = 2$.
- `2 3`: $(2 + 1)(1 - 1 + 1) = 3$.
- `3 12`: $6 - 1 = 5$.
- `3 14`: 14 does not divide 12, so $6 - 0 = 6$.

---

Same problem grouped by topic: [../docs/number-theory/QNUMBER.md](../docs/number-theory/QNUMBER.md)
