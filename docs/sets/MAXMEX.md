# 451. Max Mex

> CodeChef problem code [`MAXMEX`](https://www.codechef.com/problems/MAXMEX) &middot; difficulty **1714** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Sets |
| **Technique** | Keep everything except the forbidden value |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Chef has a sequence of positive integers $A_1, A_2, \ldots, A_N$. He wants to choose some elements of this sequence (possibly none or all of them) and compute their MEX, i.e. the smallest positive integer which does not occur among the chosen elements. For example, the MEX of $[1, 2, 4]$ is $3$.

Help Chef find the largest number of elements of the sequence $A$ which he can choose such that their MEX is equal to $M$, or determine that it is impossible.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $M$.
- The second line contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

**Output**
For each test case, print a single line containing one integer ― the maximum number of elements Chef can choose, or $-1$ if he cannot choose elements in such a way that their MEX is $M$.

**Constraints**
- $1 \le T \le 100$
- $2 \le M \le N \le 10^5$
- $1 \le A_i \le 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^6$

## Constraints

- $1 \le T \le 100$
- $2 \le M \le N \le 10^5$
- $1 \le A_i \le 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^6$

## Sample

**Sample input**

```
1
3 3
1 2 4
```

**Sample output**

```
3
```

<details><summary>Explanation</summary>

**Example case 1:** The MEX of whole array is 3. Hence, we can choose all the elements.

</details>

## Approach

MEX here is the smallest **positive** integer missing, so MEX $= M$ says two things: every value in $1, \ldots, M-1$ must appear among the chosen elements, and $M$ must not.

The second condition is the only reason to discard anything. Every element other than $M$ is harmless — values above $M$ and repeats of values below $M$ cannot change the MEX, since the MEX is determined solely by which of $1, 2, \ldots$ are present. So the maximum selection is "everything except the copies of $M$":

$$\text{answer} = N - \mathrm{cnt}(M)$$

and that selection automatically satisfies the first condition, provided each of $1, \ldots, M-1$ occurs in $A$ at all. If any of them is missing, no selection can work and the answer is $-1$.

Note the problem's MEX starts from $1$, not $0$ — so $0$ never matters, and the constraint $A_i \geq 1$ means every element is a candidate value.

The sample has $A = [1,2,4]$ and $M = 3$. Both $1$ and $2$ are present and no element equals $3$, so all three elements are kept and the MEX of $\{1,2,4\}$ is indeed $3$. Had the array been $[1,2,3,4]$, the $3$ would have to go, leaving $3$ elements again — but from a longer array.

A set is enough for the presence test and a single counter for $\mathrm{cnt}(M)$, so one pass suffices. Checking $1 \ldots M-1$ costs $O(M) \leq O(N)$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        vals = data[pos + 2:pos + 2 + n]
        pos += 2 + n
        present = set(vals)
        # Only copies of M have to go; everything else is harmless.
        if all(str(v).encode() in present for v in range(1, m)):
            out.append(str(n - vals.count(str(m).encode())))
        else:
            out.append("-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$

> CodeChef tags: `Algorithms`, `Constructive`
