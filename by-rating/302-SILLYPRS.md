# 302. Magda and Silly Pairs

> [`SILLYPRS`](https://www.codechef.com/problems/SILLYPRS) &middot; difficulty **1507** &middot; time limit **1.5s** &middot; 1400 to 1600 difficulty problems (Level 2)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Matching by parity |
| **CodeChef tags** | `Mathematics`, `Algorithms`, `Constructive`, `Basic Math`, `ad-hoc` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef and his friend Magda have $2N$ mutual friends: $N$ of these friends are chefs and the other $N$ are chefettes. The chefs are numbered $1$ through $N$ and the chefettes are (independently) also numbered $1$ through $N$. Since Magda wants their friends to be as happy as possible and to preserve traditional family values, she wants to pair them up in such a way that each chef is paired with exactly one chefette and each chefette with exactly one chef.

The chefs have heights $A_1, A_2, \ldots, A_N$ and the chefettes have heights $B_1, B_2, \ldots, B_N$. For each valid $i, j$, if the $i$-th chef and the $j$-th chefette are paired, they will have exactly one child with height $\left\lfloor\frac{A_i+B_j}{2}\right\rfloor$. Magda wants to pair up the chefs and chefettes in such a way that the sum of heights of all their children ($N$ children in total) is maximum possible. Please help her do that.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.
- The third line contains $N$ space-separated integers $B_1, B_2, \ldots, B_N$.

**Output**
Print a single line containing one integer ― the maximum sum of heights of the children.

**Constraints**
- $1 \le T \le 10$
- $1 \le N \le 10^5$
- $1 \le A_i \le 10^9$ for each valid $i$
- $1 \le B_i \le 10^9$ for each valid $i$

**Subtasks**
**Subtask #1 (40 points):** $1 \le N \le 100$

**Subtask #2 (60 points):** original constraints

## Constraints

- $1 \le T \le 10$
- $1 \le N \le 10^5$
- $1 \le A_i \le 10^9$ for each valid $i$
- $1 \le B_i \le 10^9$ for each valid $i$

## Sample

**Sample input**

```
2
3
4 5 6
1 2 3
5
4 8 6 4 1
2 5 7 4 7
```

**Sample output**

```
10
23
```

<details><summary>Explanation</summary>

**Example case 1:** One possible solution is to pair the first chef with the second chefette, the second chef with the first chefette and the third chef with the third chefette. Their children will have heights $3$, $3$ and $4$, respectively.

</details>

## Approach

The floor is what makes this interesting. Writing it exactly,

$$\left\lfloor \frac{a+b}{2} \right\rfloor = \frac{a+b}{2} - \frac{[\,a+b \text{ odd}\,]}{2}$$

Summed over all $N$ pairs, the first term is $\frac{\sum A + \sum B}{2}$ — **fixed**, since every chef and every chefette is used exactly once regardless of the pairing. So the only thing the matching controls is the number of pairs whose sum is odd, and maximising the total means **minimising** that count.

A sum is odd exactly when the two heights have different parity. So pair odd with odd and even with even as far as possible: with $o_A, o_B$ odd heights and $e_A, e_B$ even ones, the number of parity-matched pairs is $\min(o_A, o_B) + \min(e_A, e_B)$, and everything left over is forced into mismatches:

$$\text{mismatched} = N - \min(o_A, o_B) - \min(e_A, e_B)$$

$$\text{answer} = \frac{\sum A + \sum B - \text{mismatched}}{2}$$

The actual heights never enter the decision — only their parities — which is why no sorting or assignment algorithm is needed. Recognising that the fractional loss, not the sum, is what the matching affects is the whole insight.

Sample case 1 has $A = [4,5,6]$ and $B = [1,2,3]$: one odd in $A$ against two in $B$, and two evens against one, giving two matched pairs and one mismatch. The total is $(21 - 1)/2 = 10$.

Sample case 2 totals $48$ with two forced mismatches, giving $23$.

Heights reach $10^9$ with $N$ up to $10^5$, so the sums reach $10^{14}$ — **64-bit territory** outside Python.

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
        a = [int(v) for v in data[pos + 1:pos + 1 + n]]
        b = [int(v) for v in data[pos + 1 + n:pos + 1 + 2 * n]]
        pos += 1 + 2 * n
        odd_a = sum(1 for v in a if v % 2)
        odd_b = sum(1 for v in b if v % 2)
        # Only parity matters: each mismatched pair costs half a unit.
        matched = min(odd_a, odd_b) + min(n - odd_a, n - odd_b)
        out.append(str((sum(a) + sum(b) - (n - matched)) // 2))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/greedy/SILLYPRS.md](../docs/greedy/SILLYPRS.md)
