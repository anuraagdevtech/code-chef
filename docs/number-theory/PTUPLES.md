[&larr; 509. Strange Function](ABX01.md) &middot; [Index](../../README.md) &middot; [564. Odd Divisors &rarr;](ODDDIV.md)

# 563. Prime Tuples

> CodeChef problem code [`PTUPLES`](https://www.codechef.com/problems/PTUPLES) &middot; difficulty **1809** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Every prime-sum triple starts with two |
| **Time** | $O(V\log\log V+T)$ overall for $V=\max N$ |
| **Space** | $O(V+T)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

A tuple $(a, b, c)$ is considered good if it consists of three **prime numbers** $a$, $b$ and $c$ such that $a \lt b \lt c \leq N$ and $a + b = c$.

Two tuples are considered different if they differ in at least one position. Given $N$, find the number of good tuples that can be formed by integers from $1$ to $N$.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The following $T$ lines contain a single integer $N$.

**Output**
For each test case, print a single line containing one integer — the number of good tuples which can be formed using integers from $1$ to $N$.

**Constraints**
- $1 \le T \le 10^5$
- $1 \le N \le 10^6$

## Constraints

- $1 \le T \le 10^5$
- $1 \le N \le 10^6$

## Sample

**Sample input**

```
2
3
6
```

**Sample output**

```
0
1
```

<details><summary>Explanation</summary>

**Example case 1:** There are no good tuples. $(1, 2, 3)$ is not a good tuple since $1$ is not prime.

**Example case 2:** $(2, 3, 5)$ is a good tuple since $2$, $3$ and $5$ are prime and $2 + 3 = 5$.

</details>

## Approach

Two odd primes have an even sum larger than two, which is not prime. Thus the smaller prime must be two, and every good triple is $(2,p,p+2)$ with both $p$ and $p+2$ prime and $p\ge3$.

Sieve all values up to the largest query and build a prefix count of upper twin-prime endpoints. A query is answered by its prefix entry.

## Solution (Python)

```python
import sys
from math import isqrt

def sieve(limit):
    prime = bytearray(b'\x01')*(limit+1)
    prime[0:2] = b'\x00\x00'
    for p in range(2,isqrt(limit)+1):
        if prime[p]:
            start = p*p
            prime[start:limit+1:p] = b'\x00'*((limit-start)//p+1)
    return prime


def main() -> None:
    values = list(map(int,sys.stdin.buffer.read().split()))
    limit = max(values[1:])
    prime = sieve(limit)
    prefix = [0]*(limit+1)
    for c in range(1,limit+1):
        prefix[c] = prefix[c-1]+int(c >= 5 and prime[c] and prime[c-2])
    sys.stdout.write('\n'.join(str(prefix[n]) for n in values[1:])+'\n')

if __name__ == '__main__':
    main()
```

## Complexity

- **Time:** $O(V\log\log V+T)$ overall for $V=\max N$
- **Space:** $O(V+T)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- One is not prime.
- The primes in a triple must be strictly increasing.
- An endpoint exactly equal to $N$ is allowed.

## Dry run

For `N=6`, the only pair of odd primes differing by two is `(3,5)`, yielding triple `(2,3,5)` and answer one.

---

Same problem in rating order (#523 of 735): [../../by-rating/523-PTUPLES.md](../../by-rating/523-PTUPLES.md)
