[&larr; 513. Server Trouble](513-SVRT.md) &middot; [Index](README.md) &middot; [515. String Reverse &rarr;](515-STR_REVERSE.md)

# 514. Prime Game

> [`PRIGAME`](https://www.codechef.com/problems/PRIGAME) &middot; difficulty **1792** &middot; time limit **1s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Game Theory |
| **Technique** | Prime-count threshold via the smallest forbidden prime product |
| **Complexity class** | Near-linear $O(n \log \log n)$ |
| **Time** | $O(V\log\log V+T)$ overall for $V=\max X$ |
| **Space** | $O(V+T)$ |

## Question

Chef and Divyam are playing a game with the following rules:
- First, an integer $X!$ is written on a board.
- Chef and Divyam alternate turns; Chef plays first.
- In each move, the current player should choose a positive integer $D$ which is divisible by up to $Y$ distinct primes and does not exceed the integer currently written on the board. Note that $1$ is not a prime.
- $D$ is then subtracted from the integer on the board, i.e. if the integer written on the board before this move was $A$, it is erased and replaced by $A-D$.
- When one player writes $0$ on the board, the game ends and this player wins.

Given $X$ and $Y$, determine the winner of the game.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $X$ and $Y$.

**Output**
For each test case, print a single line containing the string `"Chef"` if Chef wins the game or `"Divyam"` if Divyam wins (without quotes).

**Constraints**
- $1 \leq T \leq 10^6$
- $1 \leq X,Y \leq 10^6$

**Subtasks**
**Subtask #1 (5 points):** $Y=1$

**Subtask #2 (10 points):**
- $1 \leq T \leq 10^2$
- $1 \leq X \leq 6$

**Subtask #3 (85 points):** original constraints

## Constraints

- $1 \leq T \leq 10^6$
- $1 \leq X,Y \leq 10^6$

## Sample

**Sample input**

```
3
1 2
3 1
2021 42
```

**Sample output**

```
Chef
Divyam 
Divyam
```

<details><summary>Explanation</summary>

**Example case 1:** Since $D = 1$ is divisible by $0$ primes, Chef will write $0$ and win the game in the first move.

**Example case 2:** Chef must choose $D$ between $1$ and $5$ inclusive, since $D = 6$ is divisible by more than one prime. Then, Divyam can always choose $6-D$, write $0$ on the board and win the game.

</details>

## Approach

Let $P$ be the product of the first $Y+1$ primes. Every positive number below $P$ has at most $Y$ distinct prime factors and is a legal subtraction. Every multiple of $P$ is illegal to subtract. Thus multiples of $P$ are losing positions: a legal move leaves a nonmultiple, and from a nonmultiple subtracting its residue modulo $P$ returns to a multiple.

The starting $X!$ is divisible by $P$ exactly when at least $Y+1$ primes are at most $X$. Otherwise $X!$ itself has at most $Y$ prime factors, so Chef wins immediately. Sieve prime prefix counts; print `Divyam` if the prime count through $X$ exceeds $Y$,  else `Chef`.

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
    values = list(map(int,sys.stdin.buffer.read().split()))
    queries = list(zip(values[1::2],values[2::2]))
    limit = max(x for x,_ in queries)
    prime = sieve(limit)
    prefix = [0]*(limit+1)
    for x in range(1,limit+1):
        prefix[x] = prefix[x-1]+prime[x]
    sys.stdout.write('\n'.join('Chef' if prefix[x] <= y else 'Divyam' for x,y in queries)+'\n')

if __name__ == '__main__':
    main()
```

## Edge cases

- One is a legal subtraction with zero prime factors.
- Equality between the prime count and $Y$ is a Chef win.
- Never construct the factorial or the forbidden prime product.

## Dry run

For `X=3,Y=1`, the factorial has distinct primes two and three, exceeding the threshold. It is a losing position, so Divyam wins.

---

Same problem grouped by topic: [../docs/game-theory/PRIGAME.md](../docs/game-theory/PRIGAME.md)
