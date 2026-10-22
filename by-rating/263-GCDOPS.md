[&larr; 262. Chef and Adventures](262-CHEFADV.md) &middot; [Index](README.md) &middot; [264. Triangle Classification &rarr;](264-TRIANGCL.md)

# 263. GCD operations

> [`GCDOPS`](https://www.codechef.com/problems/GCDOPS) &middot; difficulty **1462** &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Each reduction has a self-fixing pivot |
| **CodeChef tags** | `Mathematics`, `Number Theory`, `Algorithms`, `Constructive`, `Basic Math`, `GCD`, `ad-hoc` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

Consider a sequence $A_1, A_2, \ldots, A_N$, where initially, $A_i = i$ for each valid $i$. You may perform any number of operations on this sequence (including zero). In one operation, you should choose two valid indices $i$ and $j$, compute the greatest common divisor of $A_i$ and $A_j$ (let's denote it by $g$), and change both $A_i$ and $A_j$ to $g$.

You are given a sequence $B_1, B_2, \ldots, B_N$. Is it possible to obtain this sequence, i.e. change $A$ to $B$, using the given operations?

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$.

**Output**
For each test case, print a single line containing the string `"YES"` if it is possible to obtain $A = B$ or `"NO"` if it is impossible.

**Constraints**
- $1 \le N \le 10^4$
- $1 \le B_i \le i$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^5$

**Subtasks**
**Subtask #1 (10 points):** $N \le 4$

**Subtask #2 (20 points):** there is at most one valid index $p$ such that $B_p \neq p$

**Subtask #3 (70 points):** original constraints

## Constraints

- $1 \le N \le 10^4$
- $1 \le B_i \le i$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^5$

## Sample

**Sample input**

```
2
3
1 2 2
4
1 2 3 2
```

**Sample output**

```
NO
YES
```

<details><summary>Explanation</summary>

**Example case 1:** We cannot make the third element of the sequence $(1, 2, 3)$ become $2$.

**Example case 2:** We can perform one operation with $(i, j) = (2, 4)$, which changes the sequence $(1, 2, 3, 4)$ to $(1, 2, 3, 2)$.

</details>

## Approach

The whole problem reduces to one test:

$$B_i \mid i \quad \text{for every } i$$

**Necessity.** Initially $A_i = i$, and an operation replaces a value by a gcd of it with something else, which still divides the old value. So $A_i \mid i$ is an invariant, and $B_i$ must divide $i$. (The given bound $B_i \leq i$ is weaker — sample 1 fails on $B_3 = 2$, which is below $3$ but does not divide it.)

**Sufficiency** is the constructive half, and the trick is choosing the partner well. To reduce index $i$ to $B_i < i$, operate on $i$ and the index $p = B_i$. Since $A_p = p = B_i$ divides $i$,

$$\gcd(A_i, A_p) = \gcd(i, B_i) = B_i$$

so $A_i$ lands on $B_i$ — and $A_p$ is set to $B_i = p$, i.e. **unchanged**. One operation per index, with no collateral damage. The partner is valid because $p = B_i < i$, so $p \neq i$, and $p \leq N$.

The one ordering subtlety: the pivot $p$ must still hold its original value $p$. It loses that only when $p$ itself gets reduced, and $B_p < p$ then. So process indices in **decreasing** order — every pivot is smaller than its target, hence reduced only later. The dependency graph $i \to B_i$ points strictly downward, so there is never a cycle.

Sample 2 is this construction in one step: $B = [1,2,3,2]$ needs only index $4$ lowered to $2$, and operating on indices $4$ and $2$ gives $\gcd(4,2) = 2$, leaving $A_2$ at $2$. Sample 1 fails the divisibility test outright.

Note $B_1 = 1$ is forced by the constraints, which is consistent — $A_1$ can never move.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        vals = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        # A_i | i is invariant, and conversely pairing i with index B_i
        # realises any divisor without disturbing the pivot.
        ok = all(i % int(v) == 0 for i, v in enumerate(vals, 1))
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **$A_i \mid i$ is invariant**, since each operation replaces a value by a gcd involving it and therefore only ever shrinks it to a divisor. So $B_i \nmid i$ is immediately fatal — the first row's $B_3 = 2$ does not divide $3$.
- **The condition is also sufficient, thanks to a self-fixing pivot.** To set $A_i$ to a divisor $d$ of $i$, pair index $i$ with index $d$: at that moment $A_d = d$, so the gcd is $d$ and index $d$ is left exactly as it was. Each target can therefore be realised independently, in order of $i$.
- **The pivot always exists**, because $d \mid i \leq N$ means $d \leq N$ is a valid index.
- **$B_i = i$ needs no operation at all**, so the identity sequence is always reachable.
- **$B_i \leq i$ is given by the constraints**, so the only thing left to test is divisibility, not range.
- **Sum of $N \leq 10^5$**: one modulo per element, with `all` short-circuiting on the first failure.

## Dry run

| $N$ | $B$ | divisibility checks | output |
|---:|---|---|---|
| 3 | $1, 2, 2$ | $1 \mid 1$ ✓, $2 \mid 2$ ✓, $2 \mid 3$ **✗** | `NO` |
| 4 | $1, 2, 3, 2$ | $1 \mid 1$, $2 \mid 2$, $3 \mid 3$, $2 \mid 4$ — all ✓ | `YES` |

For the second row, $A_4$ is set by pairing index $4$ with index $2$: $\gcd(4, 2) = 2$, and index $2$ stays at $2$.

---

Same problem grouped by topic: [../docs/constructive/GCDOPS.md](../docs/constructive/GCDOPS.md)
