[&larr; 280. Guddu on a Date](KS2.md) &middot; [Index](../../README.md) &middot; [288. Catch the Thief &rarr;](CATHIEF.md)

# 282. Monsters

> CodeChef problem code [`SPCP5`](https://www.codechef.com/problems/SPCP5) &middot; difficulty **1527** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Sieve plus a short search |
| **Time** | $O(\log H)$ per test case after an $O(V \log\log V)$ sieve |
| **Space** | $O(V)$ with $V = 10^6$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Ben is fighting a monster with a health of $H$. He starts with an attack power of $1$.
Ben has two types of moves:
- He can use a *regular attack*, which damages the monster by his current attack power.
After this, his attack power **doubles**.
- He can use a *special move*: choose a **prime number** $P$ such that $P \leq H$ ($H$ being the current health of the monster), and deal $P$ damage to the monster.
This move can be done **at most once**.
Note that this special move doesn't affect his attack power: it doesn't double, and remains the same.

To kill the monster, Ben must deal **exactly** $H$ damage to it.
Find the minimum number of moves needed for Ben to kill the monster, or print $-1$ if it's impossible to kill it no matter what.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each of the next $T$ lines contains one integer $H$ — the initial health of monster.

**Output**

- For each test case, output on a new line the minimum number of moves Ben will perform to kill the monster (if he's able to do so at all).
If he is unable to kill the monster no matter what, output $-1$ instead.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq H \leq 10^6$

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
3
10
21
1000000
```

**Sample output**

```
3
-1
15
```

<details><summary>Explanation</summary>

**Test case $1$:** Ben can do the following:
- Initially, the monster has $H = 10$ health.
- Use a regular attack, with power $1$. The monster's health drops to $9$, and the regular attack's power increases to $2$.
- Use a special attack with $P = 7$. $H$ becomes $2$.
- Use a regular attack, with power $2$. The monster is defeated.

**Test case $2$:** It can be shown that no matter what sequence of moves is chosen, Ben cannot deal exactly $21$ damage. So, the answer is $-1$.

**Test case $3$:** There exists a sequence of $15$ moves that kills the monster, and it can be shown that achieving this in $14$ or less moves is impossible.

</details>

## Approach

Regular attacks are forced: the first deals $1$, the second $2$, the third $4$, and so on. So $k$ regular attacks deal exactly

$$1 + 2 + 4 + \cdots + 2^{k-1} = 2^k - 1$$

no matter how they are interleaved with the special move, because the special move does not touch the attack power.

That leaves only two decisions: how many regular attacks, and whether to spend the one special move. The damage must total exactly $H$, so for each $k$:

- if $2^k - 1 = H$, the monster dies in $k$ moves with no special;
- otherwise the special must cover the remainder $P = H - (2^k - 1)$, which is legal only if $P$ is **prime** — costing $k+1$ moves.

Since $H \leq 10^6$, $k$ never exceeds about $20$, so scanning $k$ upward and stopping at the first success gives the minimum. Primality is answered in $O(1)$ from a sieve built once.

The constraint $P \leq H$ is automatically satisfied — using the special move **first**, while the monster is at full health, makes it so, and the ordering is free.

Sample $H = 10$: neither $k=0$ ($P=10$, composite) nor $k=1$ ($P=9$) works, but $k=2$ leaves $P = 7$, prime — three moves.

Sample $H = 21$ is the impossible case: $22$ is not a power of two, and every remainder $21, 20, 18, 14, 6$ is composite, so $-1$.

Note $P$ must be at least $2$; a remainder of $1$ is not prime, which is why $k$ values leaving exactly $1$ are rejected.

## Solution (Python)

```python
import sys

LIMIT = 10 ** 6 + 1


def build_sieve():
    is_prime = bytearray([1]) * LIMIT
    is_prime[0] = is_prime[1] = 0
    for p in range(2, int(LIMIT ** 0.5) + 1):
        if is_prime[p]:
            is_prime[p * p::p] = bytearray(len(is_prime[p * p::p]))
    return is_prime


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    is_prime = build_sieve()
    out = []
    for i in range(t):
        h = int(data[1 + i])
        best = -1
        k = 0
        # k regular attacks always deal exactly 2^k - 1.
        while (1 << k) - 1 <= h:
            dealt = (1 << k) - 1
            if dealt == h:
                best = k
                break
            rest = h - dealt
            if rest < LIMIT and is_prime[rest]:
                best = k + 1
                break
            k += 1
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(\log H)$ per test case after an $O(V \log\log V)$ sieve
- **Space:** $O(V)$ with $V = 10^6$

## Edge cases

- **$k$ regular attacks always deal exactly $2^k - 1$**, since the power doubles each time: $1 + 2 + 4 + \dots + 2^{k-1}$. The order of moves is therefore irrelevant and only the count matters.
- **The special move must cover the whole remainder**, so the remainder has to be prime — the single prime is the only flexibility available.
- **An exact power-of-two-minus-one health needs no special move.** If $2^k - 1 = H$ the answer is $k$, which the equality check catches before the primality test.
- **Some health values are unreachable** (the second row, $H = 21$): every remainder $21 - (2^k - 1)$ is composite for all valid $k$, so the answer is $-1$.
- **The loop bound is $2^k - 1 \leq H$**, which keeps $k$ under about $20$ for $H \leq 10^6$ and guarantees termination.
- **The remainder is always within the sieve** because it is at most $H \leq 10^6$, but the explicit bound check keeps the index safe.
- **Fewer regular attacks are always better**, so the first $k$ that works is optimal — the loop breaks immediately on success.

## Dry run

First sample: $H = 10$.

| $k$ | regular damage $2^k - 1$ | remainder | remainder prime? | total moves |
|---:|---:|---:|:---:|---:|
| 0 | 0 | 10 | no ($2 \cdot 5$) | — |
| 1 | 1 | 9 | no ($3^2$) | — |
| 2 | 3 | **7** | **yes** | $2 + 1 = $ `3` |

Two regular attacks deal $1$ and $2$, then the special move deals the prime $7$.

---

Same problem in rating order (#312 of 486): [../../by-rating/312-SPCP5.md](../../by-rating/312-SPCP5.md)
