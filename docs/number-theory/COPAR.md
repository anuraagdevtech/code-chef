[&larr; 677. Partition It](PARPERM.md) &middot; [Index](../../README.md) &middot; [689. Interesting Representation &rarr;](INTREP.md)

# 683. Cute Chef Gift

> CodeChef problem code [`COPAR`](https://www.codechef.com/problems/COPAR) &middot; difficulty **2235** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Each prime spans an interval - find the first position no interval crosses |
| **Time** | $O(V \log \log V + N \log V)$, $V$ the largest value |
| **Space** | $O(V + N \log V)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

Chef wants to give a gift to Chefina to celebrate their anniversary. Of course, he has a sequence $a_1, a_2, \ldots, a_N$ ready for this occasion. Since the half-heart necklace is kind of cliche, he decided to cut his sequence into two pieces and give her a piece instead. Formally, he wants to choose an integer $l$ ($1 \le l \lt N$) and split the sequence into its prefix with length $l$ and its suffix with length $N-l$.

Chef wants his gift to be *cute*; he thinks that it will be cute if the product of the elements in Chefina's piece is coprime with the product of the elements in his piece. Can you tell him where to cut the sequence? Find the smallest valid $l$ such that Chef's gift would be cute.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains the integer $N$.
- The second line contains $N$ space-separated integers $a_1, a_2, \ldots, a_N$.

**Output**
For each test case, print a single line containing one integer $l$ where Chef should cut the sequence.

It is guaranteed that a solution exists for the given test data.

**Constraints**
- $1 \le T \le 20$
- $2 \le N \le 10^5$
- $2 \le a_i \le 10^5$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $3 \cdot 10^5$

**Subtasks**
**Subtask #1 (25 points):**
- $N \le 200$
- the sum of $N$ over all test cases does not exceed $600$

**Subtask #2 (40 points):**
- $N \le 2,000$
- the sum of $N$ over all test cases does not exceed $6,000$

**Subtask #3 (35 points):** original constraints

## Constraints

- $1 \le T \le 20$
- $2 \le N \le 10^5$
- $2 \le a_i \le 10^5$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $3 \cdot 10^5$

## Sample

**Sample input**

```
1
4
2 3 4 5
```

**Sample output**

```
3
```

## Approach

The two products are coprime exactly when no prime divides an element on both sides of the cut. For each prime $p$ look at the first and the last index where it divides an element: a cut is valid when it does not fall strictly inside any such span.

Factorise every element with a smallest-prime-factor sieve and record the last index of each prime. Then scan from the left keeping `end`, the furthest last-occurrence of any prime seen so far. The prefix ending at $i$ is a valid piece exactly when $i = \text{end}$: no prime that appears in the prefix appears later. The first such $i$ gives the smallest valid $l$, which is what is asked; the statement guarantees that one exists before the end of the array.

## Solution (Python)

```python
import sys


spf = list(range(100001))
for i in range(2, 317):
    if spf[i] == i:
        for j in range(i * i, 100001, i):
            if spf[j] == j:
                spf[j] = i


def solve(tokens):
    n = next(tokens)
    values = [next(tokens) for _ in range(n)]
    last = {}
    factor_lists = []
    for i, value in enumerate(values):
        primes = []
        while value > 1:
            prime = spf[value]
            primes.append(prime)
            while value % prime == 0:
                value //= prime
        factor_lists.append(primes)
        for prime in primes:
            last[prime] = i
    end = 0
    for i, primes in enumerate(factor_lists):
        for prime in primes:
            end = max(end, last[prime])
        if i == end:
            return str(i + 1)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(V \log \log V + N \log V)$, $V$ the largest value
- **Space:** $O(V + N \log V)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Elements equal to 1 have no primes and never extend the span.
- The cut must leave both pieces non-empty; the guaranteed answer satisfies this.
- Repeated prime factors of one element are recorded once.
- Products are never formed - they would be astronomically large.

## Dry run

`A = [2, 3, 4, 5]`. Last occurrences: prime 2 at index 3 (the 4), prime 3 at index 2, prime 5 at index 4.

- $i = 1$ (value 2): `end = 3`.
- $i = 2$ (value 3): `end` stays 3.
- $i = 3$ (value 4): `end = 3 = i` - cut here.

Answer $l = 3$: $2 \cdot 3 \cdot 4 = 24$ and 5 are coprime.

> CodeChef tags: `Data Structures`, `Arrays`, `Mathematics`, `Number Theory`, `Integer Factorisation`, `Divisors`

---

Same problem in rating order (#645 of 735): [../../by-rating/645-COPAR.md](../../by-rating/645-COPAR.md)
