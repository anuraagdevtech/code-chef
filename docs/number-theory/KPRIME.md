# 353. Count K-Primes

> CodeChef problem code [`KPRIME`](https://www.codechef.com/problems/KPRIME) &middot; difficulty **1549** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Sieve of distinct prime factors plus prefix counts |
| **Time** | $O(V \log \log V + 5V)$ precomputation, $O(1)$ per query |
| **Space** | $O(5V)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

Alice and Bob are studying for their class test together. The topic of the test is **Prime Numbers**. The preparation is getting too boring for their liking. To make it interesting, they turn it into a game. The winner will get an ice-cream treat from the other.

The game is called **Count K-Primes**. A number is a $K$-prime if it has exactly $K$ **distinct** prime factors. The game is quite simple. Alice will give three numbers $A$, $B$ & $K$ to Bob. Bob needs to tell Alice the number of $K$-prime numbers between $A$ & $B$ (both inclusive). If Bob gives the correct answer, he gets a point. If not, Alice gets a point. They play this game $T$ times.

Bob hasn't prepared so well. But he really wants to win the game. He wants you to tell him the correct answer.

**Input**
- First line of input contains a single integer $T$, the number of times they play.
- Each game is described in a single line containing the three numbers $A$,$B$ & $K$.

**Output**
For each game, output on a separate line the number of $K$-primes between $A$ & $B$.

**Constraints:**
- $1 \le T \le 10000$
- $2 \le A \le B \le 100000$
- $1 \le K \le 5$

## Constraints

- $1 \le T \le 10000$
- $2 \le A \le B \le 100000$
- $1 \le K \le 5$
**Example:**
**Sample Input**
```
4
2 5 1
4 10 2
14 15 2
2 20 3
```
**Sample Output**
```
4
2
2
0
```

## Sample

**Sample input**

```
4
2 5 1
4 10 2
14 15 2
2 20 3
```

**Sample output**

```
4
2
2
0
```

<details><summary>Explanation</summary>

**Test case $1$:** The range includes $4$ integers $\{2, 3, 4,5 \}$. We need to find the number of integers in this range having only $1$ distinct prime factor.
- For $2$, since it is prime, it has $1$ distinct prime factor.
- For $3$, since it is prime, it has $1$ distinct prime factor.
- For $4$, we can write it as $2\times 2$. Thus, it has $1$ distinct prime factor which is $2$.
- For $5$, since it is prime, it has $1$ distinct prime factor.

Thus, all $4$ integers in the given range are $1$-primes.

**Test case $2$:** The only *K-primes* in the given range are $6$ and $10$. This is because $6 = 2\times 3$ and $10 = 2\times 5$. Thus both these integers have $2$ distinct prime factors.

**Test case $3$:** The only *K-primes* in the given range are $14$ and $15$. This is because $14 = 2\times 7$ and $15 = 3\times 5$. Thus both these integers have $2$ distinct prime factors.

**Test case $4$:** There are no *K-primes* in the given range.

</details>

## Approach

With $T$ up to $10^4$ and ranges up to $10^5$, factorising per query would be wasteful — and entirely avoidable, since the universe of numbers is fixed. Everything is precomputed once.

First, a sieve variant that counts **distinct** prime factors for every $n \leq 10^5$. Walk $p$ upward; if $\omega[p]$ is still $0$ then no smaller prime divides $p$, so $p$ is prime, and we add one to $\omega[m]$ for every multiple $m$ of $p$:

$$\omega[n] = \#\{p \text{ prime} : p \mid n\}$$

Counting multiples rather than factorising means each prime touches $V/p$ entries, for $O(V \log \log V)$ total. Note multiplicity is ignored by construction — $4 = 2^2$ is visited only by $p = 2$, so $\omega[4] = 1$ and $4$ is a $1$-prime.

Second, because $K \leq 5$, build five prefix-count arrays $\mathrm{pre}_k[n] = \#\{x \leq n : \omega[x] = k\}$. Each query is then a subtraction:

$$\mathrm{pre}_K[B] - \mathrm{pre}_K[A-1]$$

The samples exercise the edges. For $K = 1$ on $[2,5]$ all four of $2, 3, 4, 5$ qualify — $4$ included, which is the multiplicity trap. For $K = 2$ on $[4,10]$ only $6$ and $10$ qualify. And $K = 3$ on $[2,20]$ gives $0$, since the smallest number with three distinct primes is $2 \cdot 3 \cdot 5 = 30$. In general the smallest $K$-prime is the product of the first $K$ primes, so $K = 5$ needs $n \geq 2310$.

## Solution (Python)

```python
import sys

LIMIT = 100001
MAXK = 5


def main() -> None:
    omega = [0] * LIMIT
    for p in range(2, LIMIT):
        if omega[p] == 0:                 # untouched, so p is prime
            for m in range(p, LIMIT, p):
                omega[m] += 1             # counts p once, ignoring multiplicity
    pre = [[0] * LIMIT for _ in range(MAXK + 1)]
    for k in range(1, MAXK + 1):
        row = pre[k]
        total = 0
        for n in range(2, LIMIT):
            if omega[n] == k:
                total += 1
            row[n] = total

    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, k = (int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i]))
        row = pre[k]
        out.append(str(row[b] - row[a - 1]))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(V \log \log V + 5V)$ precomputation, $O(1)$ per query
- **Space:** $O(5V)$

## Edge cases

- **Distinct primes, not total factors.** $4 = 2^2$ counts as $1$, and so do $8$ and $16$ — which is why the sieve adds one per *prime* over its multiples, never once per prime power.
- **The answer can be $0$** (the fourth row): the smallest number with three distinct prime factors is $30$, so a range ending at $20$ has none.
- **$A \geq 2$ is guaranteed**, so `row[a - 1]` never reaches a negative index.
- **$0$ and $1$ have no prime factors**, so they sit at $\omega = 0$ and are never counted for $K \geq 1$.
- **A prime is detected by $\omega(p)$ still being $0$** when the outer loop reaches it — the pass doubles as both sieve and counter.
- **$K \leq 5$** means only five prefix rows are needed, so the $5 \times 10^5$ table is affordable where a per-query scan at $T = 10^4$ would not be.
- **Both endpoints are inclusive**, which the prefix difference `row[b] - row[a-1]` handles directly.

## Dry run

| range | $K$ | numbers and their distinct prime counts | matches |
|---|---:|---|---:|
| $2 \dots 5$ | 1 | $2{:}1$, $3{:}1$, $4{:}1$, $5{:}1$ | `4` |
| $4 \dots 10$ | 2 | $6{:}2$, $10{:}2$ (others $1$ or more) | `2` |
| $14 \dots 15$ | 2 | $14 = 2 \cdot 7$, $15 = 3 \cdot 5$ | `2` |
| $2 \dots 20$ | 3 | none reach three distinct primes | `0` |

Note $4$, $8$ and $16$ all have $\omega = 1$, which is what the first row relies on.

---

Same problem in rating order (#324 of 486): [../../by-rating/324-KPRIME.md](../../by-rating/324-KPRIME.md)
