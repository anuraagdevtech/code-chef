[&larr; 545. Path-etic Sums](PATHSUMS.md) &middot; [Index](../../README.md) &middot; [630. K Distinct Array &rarr;](DISTK.md)

# 571. Yet Another Problem About Sequences

> CodeChef problem code [`EARTSEQ`](https://www.codechef.com/problems/EARTSEQ) &middot; difficulty **2011** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Distinct large primes interleaved with a small cyclic colouring |
| **Time** | $O(V\log\log V+\sum N)$ overall for fixed sieve bound $V=400000$ |
| **Space** | $O(V+\max N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

For a set of positive integers $S$, let's define $\mathrm{gcd}(S)$ as the greatest integer which divides each element of $S$. If $\mathrm{gcd}(S) = 1$, the set $S$ is called *coprime*. For example, the set $\{7, 12, 15\}$ is coprime, but $\{6, 12, 15\}$ is not coprime, since every element of this set is divisible by $3$.

Your task is to find an integer sequence $A_0, A_1, \ldots, A_{N-1}$ such that:
- for each valid $i$, $1 \le A_i \le 10^9$
- $A_0, A_1, \ldots, A_{N-1}$ are pairwise distinct
- for each valid $i$, the set $\{A_i, A_{(i+1)\%N}\}$ is not coprime ($\%$ denotes the modulo operator)
- for each valid $i$, the set $\{A_i, A_{(i+1)\%N}, A_{(i+2)\%N}\}$ is coprime

It is possible that there is no solution. If there are multiple solutions, you may find any one.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$.

**Output**
For each test case:
- If there is no solution, print a single line containing the integer $-1$.
- Otherwise, print a single line containing $N$ space-separated integers $A_0, A_1, \ldots, A_{N-1}$.

**Constraints**
- $1 \le T \le 1,000$
- $3 \le N \le 50,000$
- the sum of $N$ over all test cases does not exceed $10^6$

**Subtasks**
**Subtask #1 (19 points):** $3 \le N \le 3,333$

**Subtask #2 (81 points):** original constraints

## Constraints

- $1 \le T \le 1,000$
- $3 \le N \le 50,000$
- the sum of $N$ over all test cases does not exceed $10^6$

## Sample

**Sample input**

```
2
3
4
```

**Sample output**

```
6 10 15
374 595 1365 858
```

<details><summary>Explanation</summary>

**Example case 1:** Let's check the answer: $\mathrm{gcd}(6, 10) = 2$, $\mathrm{gcd}(10, 15) = 5$, $\mathrm{gcd}(15, 6) = 3$, $\mathrm{gcd}(6, 10, 15) = 1$. Every two cyclically consecutive numbers are not coprime, but every three cyclically consecutive numbers are coprime.

**Example case 2:**
- $\mathrm{gcd}(374, 595) = 17$, $\mathrm{gcd}(595, 1365) = 35$, $\mathrm{gcd}(1365, 868) = 39$, $\mathrm{gcd}(858, 374) = 22$
- $\mathrm{gcd}(374, 595, 1365) = 1$, $\mathrm{gcd}(595, 1365, 858) = 1$, $\mathrm{gcd}(1365, 858, 374) = 1$, $\mathrm{gcd}(858, 374, 595) = 1$

</details>

## Approach

Choose a circular sequence of edge primes $p_i$ such that every three consecutive edge primes are distinct, and assign vertex value $A_i=p_i p_{i+1}$. Neighbouring values share one edge prime. Three consecutive values have GCD one because no edge prime can appear in all three when the edge-prime sequence has no repeats within distance two.

For even lengths, alternate small primes with pairwise distinct large primes. Colour the circular small-prime positions alternately with two and three, using five at the final position when needed to avoid a repeated colour at the wraparound. Every large prime occurs once and has two different small neighbours, so all products are distinct.

For odd lengths at least five, first construct the even sequence of length $N-1$, then insert a small prime between the first large prime and its following small prime. Choose the inserted prime different from the small primes on either side of that large prime. This preserves distance-two distinctness. Length three uses edge primes two, three, and five directly. The largest large prime needed is below 400000, and every product is below two million.

## Solution (Python)

```python
import sys

from math import isqrt

LIMIT = 400000
prime = bytearray(b'\x01')*(LIMIT+1)
prime[0:2] = b'\x00\x00'
for p in range(2,isqrt(LIMIT)+1):
    if prime[p]:
        prime[p*p:LIMIT+1:p] = b'\x00'*((LIMIT-p*p)//p+1)
LARGE_PRIMES = [p for p in range(7,LIMIT+1) if prime[p]]


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        if n == 3:
            edge_primes = [2,3,5]
        else:
            even = n if n%2 == 0 else n-1
            count = even//2
            small = [2 if i%2 == 0 else 3 for i in range(count)]
            if small[-1] == small[0]:
                small[-1] = 5
            edge_primes = []
            for i in range(count):
                edge_primes.extend((small[i],LARGE_PRIMES[i]))
            if n%2:
                inserted = next(p for p in (2,3,5) if p != edge_primes[0] and p != edge_primes[2])
                edge_primes.insert(2,inserted)
        answer = [edge_primes[i]*edge_primes[(i+1)%n] for i in range(n)]
        out.append(' '.join(map(str,answer)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(V\log\log V+\sum N)$ overall for fixed sieve bound $V=400000$
- **Space:** $O(V+\max N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Check the pair and triple conditions cyclically, including wraparound.
- Distinctness is required for all output values.
- The smallest case $N=3$ uses a separate construction.
- Every value remains below $10^9$.

## Dry run

For `N=5`, edge primes `[2,7,5,3,11]` yield values `[14,35,15,33,22]`. Adjacent GCDs are respectively `7,5,3,11,2`, while every cyclic triple has GCD one.

---

Same problem in rating order (#573 of 735): [../../by-rating/573-EARTSEQ.md](../../by-rating/573-EARTSEQ.md)
