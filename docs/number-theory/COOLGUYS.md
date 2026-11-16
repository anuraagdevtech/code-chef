[&larr; 567. Levy Conjecture](LEVY.md) &middot; [Index](../../README.md) &middot; [569. Churu and Balls &rarr;](CBALLS.md)

# 568. Cool Guys

> CodeChef problem code [`COOLGUYS`](https://www.codechef.com/problems/COOLGUYS) &middot; difficulty **1758** &middot; time limit **3s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Dirichlet hyperbola count of divisible ordered pairs |
| **Time** | $O(\sqrt N+\log N)$ per test case |
| **Space** | $O(1)$ auxiliary |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Given an integer **N**. Integers **A** and **B** are chosen randomly in the range **[1..N]**. Calculate the probability that the Greatest Common Divisor(GCD) of **A** and **B** equals to **B**.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows. Each test case consists of a single integer **N** on a separate line.

**Output**

For each test case, output a single line containing probability as an irreducible fraction.

**Constraints**

1<=**T**<=10^3

1<=**N**<=10^9

## Constraints

1<=T<=10^3
1<=N<=10^9

## Sample

**Sample input**

```
3
1
2
3
```

**Sample output**

```
1/1
3/4
5/9
```

## Approach

The condition $gcd(A,B)=B$ is equivalent to $B$ dividing $A$. For fixed $B$, there are $\lfloor N/B\rfloor$ choices of $A$, so favourable ordered pairs total $S=\sum_{b=1}^N\lfloor N/b\rfloor$.

Count lattice points $ab\le N$ by symmetry around $a=b$. With $r=\lfloor\sqrt N\rfloor$, the count is $S=2\sum_{i=1}^r\lfloor N/i\rfloor-r^2$. The subtraction removes the square counted twice. Reduce $S/N^2$ by its GCD.

## Solution (Python)

```python
import sys
from math import gcd,isqrt


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        r = isqrt(n)
        numerator = 2*sum(n//i for i in range(1,r+1))-r*r
        denominator = n*n
        g = gcd(numerator,denominator)
        out.append(f'{numerator//g}/{denominator//g}')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(\sqrt N+\log N)$ per test case
- **Space:** $O(1)$ auxiliary
- Auxiliary space excludes the buffered input and output.

## Edge cases

- The two choices are independent and ordered, giving denominator $N^2$.
- Include pairs with equal entries.
- Use an exact integer square root.

## Dry run

For `N=3`, favourable pairs number `3+1+1=5`, out of nine ordered pairs. The irreducible probability is `5/9`.

---

Same problem in rating order (#484 of 735): [../../by-rating/484-COOLGUYS.md](../../by-rating/484-COOLGUYS.md)
