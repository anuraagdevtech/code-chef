[&larr; 170. Maximum Length Even Subarray](MXEVNSUB.md) &middot; [Index](../../README.md) &middot; [204. Chef and Linear Chess &rarr;](LINCHESS.md)

# 180. Hard Cash

> CodeChef problem code [`CASH`](https://www.codechef.com/problems/CASH) &middot; difficulty **1300** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | A conserved total modulo K |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

Chef wants to take Chefina on a date. However, he has to complete one more task before leaving. Since he does not want to be late, he is asking you for help.

There are $N$ bags with coins in a row (numbered $1$ through $N$); for each valid $i$, the $i$-th bag contains $A_i$ coins. Chef should make the number of coins in each bag divisible by a given integer $K$ in the following way:
- choose an integer $c$ between $0$ and $N$ (inclusive)
- take some coins from the first $c$ bags ― formally, for each $i$ ($1 \le i \le c$), he may choose any number of coins between $0$ and $A_i$ inclusive and take them out of the $i$-th bag
- move some of these coins to some of the last $N-c$ bags ― formally, for each $i$ ($c+1 \le i \le N$), he may place a non-negative number of coins in the $i$-th bag

Of course, the number of coins placed in the last $N-c$ bags must not exceed the number of coins taken out from the first $c$ bags, but there may be some coins left over. Let's denote the number of these coins by $R$. You should find the smallest possible value of $R$.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two integers $N$ and $K$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

**Output**
For each test case, print a single line containing one integer ― the smallest value of $R$.

**Constraints**
- $1 \le T \le 10^3$
- $1 \le N \le 10^5$
- $0 \le A_i \le 10^9$ for each valid $i$
- $1 \le K \le 10^9$
- the sum of $N$ over all test cases does not exceed $10^5$

**Subtasks**
**Subtask #1 (10 points):** $K = 2$

**Subtask #2 (20 points):** $N \le 3$

**Subtask #3 (70 points):** original constraints

## Constraints

- $1 \le T \le 10^3$
- $1 \le N \le 10^5$
- $0 \le A_i \le 10^9$ for each valid $i$
- $1 \le K \le 10^9$
- the sum of $N$ over all test cases does not exceed $10^5$

## Sample

**Sample input**

```
2
5 7
1 14 4 41 1
3 9
1 10 19
```

**Sample output**

```
5
3
```

<details><summary>Explanation</summary>

**Example case 1:** One of the possible solutions is to choose $c = 4$, remove $1$, $0$, $4$ and $13$ coins from bags $1$, $2$, $3$ and $4$ respectively, and add $13$ coins to bag $5$.

**Example case 2:** The optimal solution is to choose $c = 3$ and remove one coin from each bag.

</details>

## Approach

The elaborate rules about choosing $c$, taking from a prefix and depositing into a suffix are a smokescreen. Two facts settle the problem.

**Coins are conserved.** Moving coins between bags never creates or destroys any, so the grand total $\sum A_i$ is fixed. The leftover $R$ is whatever the bags do not absorb.

**The final configuration absorbs a multiple of $K$.** Every bag ends divisible by $K$, so the coins in bags sum to a multiple of $K$. Therefore

$$R = \sum A_i - (\text{multiple of } K)$$

and the smallest non-negative such $R$ is

$$R = \left(\sum A_i\right) \bmod K$$

That value is also achievable, so it is the answer — and it does not depend on $c$ at all.

It is worth seeing *why* $c$ drops out. Moving one bag from the suffix to the prefix changes the prefix's required withdrawal by $A_i \bmod K$ and the suffix's required deposit by $(K - A_i \bmod K) \bmod K$. Those two always sum to $0$ or $K$, so the difference between withdrawals and deposits shifts by a multiple of $K$ and its residue is **invariant**. Every choice of $c$ gives the same leftover.

Checking sample 1: $1 + 14 + 4 + 41 + 1 = 61$, and $61 \bmod 7 = 5$. Sample 2: $1 + 10 + 19 = 30$, and $30 \bmod 9 = 3$.

Spotting the conserved quantity turns an apparent optimisation over $N+1$ split points into a single modulo — which also makes the $10^5$ bound on $\sum N$ a non-issue.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        total = sum(int(v) for v in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        # Coins are conserved and the bags end up holding a multiple of k,
        # so the leftover is fixed regardless of where the split is made.
        out.append(str(total % k))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Where the splits are made is irrelevant.** Coins are conserved and every bag ends holding a multiple of $K$, so the leftover is $\left(\sum A_i\right) \bmod K$ whatever the arrangement — no search over distributions is needed.
- **$A_i$ may be $0$**, contributing nothing to the total.
- **A total of $0$** gives $0$ left over.
- **$K$ larger than the total**: no bag can be filled at all, and the modulo already returns the whole sum.
- **$K$ divides the total**: nothing is left over, and the answer is $0$.
- **Sums reach $10^5 \times 10^9 = 10^{14}$**, past 32-bit but native in Python.

## Dry run

| coins | total | $K$ | total $\bmod K$ |
|---|---:|---:|---:|
| $1, 14, 4, 41, 1$ | 61 | 7 | `5` |
| $1, 10, 19$ | 30 | 9 | `3` |

$61 = 8 \cdot 7 + 5$, so eight bags fill and five coins remain.

---

Same problem in rating order (#202 of 486): [../../by-rating/202-CASH.md](../../by-rating/202-CASH.md)
