[&larr; 587. Symmetric Swaps](587-SYMARRSWAP.md) &middot; [Index](README.md) &middot; [589. Mountain &rarr;](589-MOUNTAIN.md)

# 588. Kirito in labyrinth

> [`KIRLAB`](https://www.codechef.com/problems/KIRLAB) &middot; difficulty **2047** &middot; time limit **1.5s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Longest chain DP keyed by prime factor, with a smallest-prime-factor sieve |
| **Complexity class** | Near-linear $O(n \log \log n)$ |
| **Time** | $O(A \log \log A + N \log A)$ over the whole input, $A$ the largest value |
| **Space** | $O(A)$ |

## Question

Kirito faced a dangerous labyrinth, and now he requires your help.

He's in a tunnel which contains **N** different rooms. Each room contains **A_i** monsters inside it. He starts from room **1**. Every time he stays near a room **X**, he may go in and clear it from monsters, or just leave the room locked and move to the room **X+1**. However, if he clears a room with **K** monsters, and the next room he clears consists of **L** monsters, then the greatest common divisor of **K** and **L** must be greater than **1**, otherwise he will die (awful curse). Formally, let us say that the order of rooms he visited is **i_1**,  **i_2**, , ..., **i_t**. Then gcd(**A_ij**, **A_ij + 1**) **> 1** for all **j < t**. Help him cross all the rooms by clearing the maximum number of rooms.

**Input**

The first line of input contains an integer **T** denoting the number of test cases.

The first line of each test case contains one integer **N** denoting the number elements in sequence.

The second line of each test case contains **N** integers where **i-th** integer is number of monsters in room **A_i**.

**Output**

For each test case, output the maximum number of rooms he could clear. (Kirito should survive.)

**Constraints**

- **1** ≤ **T** ≤ **10**

- **1** ≤ **N** ≤ **10^5**

- **1** ≤ **a_i** ≤ **10^7**

**Subtasks**

- **Subtask 1:** **1** ≤ **N** ≤ **10^3** - **30 points**

- **Subtask 2:** **Original constraints** - **70 points**

## Constraints

- 1 ≤ T ≤ 10
- 1 ≤ N ≤ 10^5
- 1 ≤ a_i ≤ 10^7

## Sample

**Sample input**

```
2
7
13 2 8 6 3 1 9
6
1 2 2 3 3 1
```

**Sample output**

```
5
2
```

<details><summary>Explanation</summary>

**Example 1**. Kirito can clear the monsters in the rooms 2, 3, 4, 5, 7 in that order. These rooms consist of 2, 8, 6, 3, and 9 monsters, respectively. You can check that gcd(2, 8), gcd(8, 6), gcd(6, 3) and gcd(3, 9), all are greater than 1.

**Example 2**. Kirito can clear the monsters in the rooms numbered 2, 3. Each of these two rooms contains two monsters. And we know that gcd(2, 2) = 2 > 1.

There is one more possible solution: Kirito can clear the monsters in the rooms numbered 4, 5. These rooms contains 3 monsters each, and he can clear these rooms as gcd(3, 3) = 3 > 1.

</details>

## Approach

We want the longest subsequence in which neighbouring values share a prime factor. Let `best[p]` be the length of the longest valid subsequence seen so far whose last element is divisible by the prime $p$.

For a new value $x$ with distinct prime factors $p_1, \dots, p_k$, the previous chosen element must share one of them, so the longest chain ending at $x$ has length $1 + \max_i \text{best}[p_i]$. Afterwards $x$ itself is a chain end divisible by each $p_i$, so set every `best[p_i]` to that length - it is at least as large as the old value.

Factorisation uses a smallest-prime-factor sieve built once up to the largest value in the input.

## Solution

```python
import sys
from array import array


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    cases = [[next(tokens) for _ in range(next(tokens))] for _ in range(next(tokens))]
    limit = max(map(max, cases), default=1)
    spf = array('I', [0]) * (limit + 1)
    for prime in range(2, int(limit ** 0.5) + 1):
        if not spf[prime]:
            for x in range(prime * prime, limit + 1, prime):
                if not spf[x]:
                    spf[x] = prime
    out = []
    for rooms in cases:
        best_for_prime = {}
        answer = 1
        for x in rooms:
            factors = []
            while x > 1:
                prime = spf[x] or x
                factors.append(prime)
                while x % prime == 0:
                    x //= prime
            length = 1 + max((best_for_prime.get(prime, 0) for prime in factors), default=0)
            for prime in factors:
                best_for_prime[prime] = length
            answer = max(answer, length)
        out.append(str(answer))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- A room with 1 monster has no prime factors; it can only form a chain of length 1 by itself.
- Read all factors' values before updating any of them, otherwise $x$ would chain with itself.
- The sieve only marks composites, so a zero entry means the number is prime.
- Equal values chain with each other because they share all their primes.

## Dry run

`A = [13, 2, 8, 6, 3, 1, 9]`.

| value | primes | length | updates |
|---:|---|---:|---|
| 13 | 13 | 1 | best[13] = 1 |
| 2 | 2 | 1 | best[2] = 1 |
| 8 | 2 | 2 | best[2] = 2 |
| 6 | 2, 3 | 3 | best[2] = best[3] = 3 |
| 3 | 3 | 4 | best[3] = 4 |
| 1 | - | 1 | - |
| 9 | 3 | 5 | best[3] = 5 |

Answer 5 (rooms 2, 8, 6, 3, 9).

---

Same problem grouped by topic: [../docs/number-theory/KIRLAB.md](../docs/number-theory/KIRLAB.md)
