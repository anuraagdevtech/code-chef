[&larr; 423. Fencing](423-FENCE.md) &middot; [Index](README.md) &middot; [425. 3-Blast Palindrome &rarr;](425-BLAST3.md)

# 424. Churu and Balls

> [`CBALLS`](https://www.codechef.com/problems/CBALLS) &middot; difficulty **1697** &middot; time limit **1s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Try prime common divisors with bucketed rounding costs |
| **Complexity class** | Near-linear $O(n \log \log n)$ |
| **Time** | $O(V\log\log V+N+V\sum_{p\le V+1}1/p+\pi(V+1))$ per test case |
| **Space** | $O(N+V)$ |

## Question

Little Churu is a naughty child, who likes to play with balls. He has **N** buckets. Each bucket contains one or more balls. He has numbered his buckets **1** to **N** (both inclusive). He has an infinite supply of extra balls, apart from the ones already in the buckets. He wants to add zero or more number of balls to each of the buckets in such a way, that number of balls in the buckets are in a non-decreasing order, and their [GCD](https://en.wikipedia.org/wiki/Greatest_common_divisor) is strictly greater than 1.

He wants to do it using the minimum number of extra balls. As he is too young to solve the problem, please help him with the solution.

**Input**

- First line of input contains an integer **T** denoting the number of test cases.

- For each test case, first line contains an integer **N** denoting the number of buckets.

- Second line of each test case contains **N** space separated integers, where the **i^th** denotes the number of balls in the **i^th** bucket.

**Output**

For each test case, output a line containing a single integer — the answer for that test case.

**Constraints**

**Subtask #1: 20 points**

	- **1 ≤ T  ≤ 10, 1 ≤ N  ≤ 1000, 1 ≤ number of balls in a bucket  ≤ 1000**

**Subtask #2: 80 points**

	- **1 ≤ T  ≤ 10, 1 ≤ N  ≤ 10000, 1 ≤ number of balls in a bucket  ≤ 10000**

## Constraints

- 1 <= T <= 10.
- 1 <= N <= 10000.
- 1 <= A_i <= 10000.
- Only additions are allowed; final values must be nondecreasing with GCD greater than one.

## Sample

**Sample input**

```
1
3
11 13 15
```

**Sample output**

```
3
```

<details><summary>Explanation</summary>

Add one ball to each of the buckets.

</details>

## Approach

Fix a prime divisor $p$ for the final common GCD. The least feasible final value at position $i$ is the smallest multiple of $p$ at least the running maximum of the original values up to $i$. Rounding a nondecreasing running maximum preserves order and gives the minimal cost for this $p$.

Every GCD greater than one has a prime divisor, so trying primes suffices. Let $V$ be the maximum original value. Prime two gives every final value at most $V+1$, so primes larger than $V+1$ cannot improve the cost. Build a frequency prefix table of the running maxima. For a prime $p$, values in $((k-1)p,kp]$ round to $kp$; prefix counts sum each bucket in constant time. This avoids rescanning all $N$ entries for every prime.

## Solution

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
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        a = [int(next(tokens)) for _ in range(n)]
        limit = max(a)
        frequency = [0]*(limit+1)
        running = 0
        for value in a:
            running = max(running,value)
            frequency[running] += 1
        for value in range(1,limit+1):
            frequency[value] += frequency[value-1]
        original_sum = sum(a)
        answer = 10**30
        prime = sieve(limit+1)
        for p in range(2,limit+2):
            if not prime[p]:
                continue
            rounded_sum = 0
            for upper in range(p,limit+p,p):
                count = frequency[min(upper,limit)]-frequency[upper-p]
                rounded_sum += upper*count
            answer = min(answer,rounded_sum-original_sum)
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- Original order must be preserved.
- An already nondecreasing array may still need increments to give GCD greater than one.
- For an all-one array, changing every value to two is optimal.

## Dry run

For `[11,13,15]`, prime two rounds to `[12,14,16]`, requiring three additional balls. No candidate prime gives a smaller total.

---

Same problem grouped by topic: [../docs/number-theory/CBALLS.md](../docs/number-theory/CBALLS.md)
