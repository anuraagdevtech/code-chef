[&larr; 159. Mutated Minions](159-CHN15A.md) &middot; [Index](README.md) &middot; [161. Playing with Matches &rarr;](161-MATCHES.md)

# 160. Joining Date

> [`JOINING`](https://www.codechef.com/problems/JOINING) &middot; difficulty **970** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Counting residues in a range |
| **CodeChef tags** | `Mathematics` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

$N$ candidates (numbered from $1$ to $N$) join Chef's firm. The first $5$ candidates join on the first day, and then, on every subsequent day, the next $5$ candidates join in.
For example, if there are $12$ candidates, candidates numbered $1$ to $5$ will join on day $1$, candidates numbered $6$ to $10$ on day $2$ and the remaining $2$ candidates will join on day $3$.

Candidate numbered $K$ decided to turn down his offer and thus, Chef adjusts the position by shifting up all the higher numbered candidates. This leads to a change in the joining day of some of the candidates.

Help Chef determine the number of candidates who will join on a different day than expected.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two space-separated integers $N$ and $K$ denoting the number of candidates and the candidate who turned down the offer.

**Output**

For each test case, output a single integer denoting the number of candidates whose joining day will be changed.

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 1000$
- $1 \leq K \leq N$

## Sample

**Sample input**

```
4
7 3
6 6
2 1
14 2
```

**Sample output**

```
1
0
0
2
```

<details><summary>Explanation</summary>

**Test case $1$:** The original joining day of each candidate is given as $[1, 1, 1, 1, 1, 2, 2]$ but as candidate $3$ turns down his offer, the new joining days are now $[1, 1, NA, 1, 1, 1, 2]$. Candidate numbered $6$ is the only one to have his joining day changed.

**Test case $2$:** The original joining day of each candidate is given as $[1, 1, 1, 1, 1, 2]$ but as candidate $6$ turns down his offer, the new joining days are now $[1, 1, 1, 1, 1, NA]$. No candidate got his joining day changed.

**Test case $3$:** The original joining day of each candidate is given as $[1, 1]$ but as candidate $1$ turns down his offer, the new joining days are now $[NA, 1]$. No candidate got his joining day changed.

**Test case $4$:** The original joining day of each candidate is given as $[1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3]$ but as candidate $2$ turns down his offer, the new joining days are now $[1, NA, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3]$. Candidate numbered $6$ and $11$ are the only ones to have their joining days changed.

</details>

## Approach

Candidate $i$ joins on day $\lceil i/5 \rceil$. When candidate $K$ withdraws, everyone numbered above $K$ shifts down one place, so a candidate originally at position $j > K$ now sits at $j - 1$ and joins on day $\lceil (j-1)/5 \rceil$.

Their day changes only when that shift crosses a day boundary — that is, when

$$\left\lceil \frac{j}{5} \right\rceil \neq \left\lceil \frac{j-1}{5} \right\rceil$$

which happens precisely when $j$ is the **first** candidate of a block of five, i.e. $j \equiv 1 \pmod 5$.

So the answer counts the integers $j$ in $(K, N]$ with $j \equiv 1 \pmod 5$, computed as a difference of two prefix counts.

The insight is that shifting everyone down by one does **not** change most people's day — only those standing exactly at a block boundary move. The naive reading, that everyone after $K$ is affected, would give $N - K$ and fail every sample.

Sample case 4 ($N = 14$, $K = 2$) is the clearest: candidates $6$ and $11$ are the block leaders above $K$, so two people shift to an earlier day, giving $2$. Sample case 1 has only candidate $6$ qualifying. Sample cases 2 and 3 answer $0$ — in case 2 the withdrawal is the last candidate, so nobody shifts at all.

Note that candidates below $K$ are never affected, which is why the count starts strictly above $K$.

## Solution

```python
import sys


def leaders_upto(n: int) -> int:
    """Count of j in [1, n] with j = 1 (mod 5) - the block leaders."""
    return (n + 4) // 5 if n >= 1 else 0


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Shifting down only moves someone who starts a block of five.
        out.append(str(leaders_upto(n) - leaders_upto(k)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **$K = N$** (the second row): nobody moves, so $0$.
- **The count of block leaders is $\lceil n/5 \rceil = (n+4)//5$, not $(n+3)//5$.** This is a real off-by-one that the sample catches: leaders are the positions $1, 6, 11, \ldots$, so for $n = 6$ there are two of them, while a $+3$ variant reports one. It was exactly this that a sample run flagged while this solution was being written.
- **Adjacent positions** ($N = 2$, $K = 1$): no leader lies strictly above $K$, so $0$.
- The subtraction counts leaders in the half-open range $(K, N]$, which is why both ends use the same helper rather than an adjusted bound.

## Dry run

Block leaders are the positions $\equiv 1 \pmod 5$: $1, 6, 11, \ldots$

| $N$ | $K$ | leaders $\leq N$ | leaders $\leq K$ | difference | output |
|---:|---:|---:|---:|---:|---|
| 7 | 3 | 2 ($1, 6$) | 1 ($1$) | 1 | `1` |
| 6 | 6 | 2 | 2 | 0 | `0` |
| 2 | 1 | 1 | 1 | 0 | `0` |
| 14 | 2 | 3 ($1,6,11$) | 1 | 2 | `2` |

Row 2 is where $(n+3)//5$ would wrongly give $1$ instead of $2$.

---

Same problem grouped by topic: [../docs/number-theory/JOINING.md](../docs/number-theory/JOINING.md)
