# 297. Andrew and the Meatballs again

> CodeChef problem code [`AMMEAT2`](https://www.codechef.com/problems/AMMEAT2) &middot; difficulty **1597** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | A shared prime factor guarantees non-coprimality |
| **Time** | $O(K)$ per test case |
| **Space** | $O(K)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Andrew likes meatballs very much as you know.

He has **N** plates of meatballs, here the **i**^th plate contains exactly **i** meatballs. Andrew wants to take exactly **K** plates to his trip to Las Vegas.

On this occasion, he wants to choose the **K** plates by a strange way: if both **i**^th and **j**^th plates are chosen, then **i** and **j** must not be [relative prime](http://en.wikipedia.org/wiki/Coprime_integers), for all **1 ≤ i < j ≤ N**.

Please help him to choose **K** plates. Output one of the possible choices.

**Input**

The first line of the input contains an integer **T**, denoting the number of test cases. The description of **T** test cases follows. The first line and only line of each test case contains two space-separated integers **N** and **K**.

**Output**

For each test case, output **K** distinct integers, denoting the number of selected plates, where the plates are numbered from **1** to **N**. If there are multiple solutions, any one will do. If it is impossible to choose **K** plates, print only one integer **-1**.

**Constraints**

- **1** ≤ **T** ≤ **7**

- **1** ≤ **K** ≤ **N** ≤ **777**

## Constraints

- 1 ≤ T ≤ 7
- 1 ≤ K ≤ N ≤ 777

## Sample

**Sample input**

```
2
100 3
100 100
```

**Sample output**

```
45 63 35
-1
```

<details><summary>Explanation</summary>

**Example case 1**: One of the possible choices is that he takes **45**^th plate, **63**^rd plate, and **35**^th plate. Because
**GCD(45, 63) = 9**,
**GCD(45, 35) = 5**,
**GCD(63, 35) = 7**.

**Example case 2**: He must choose all **N = K** plates in this case. But, for example, the pair of **3**^rd plate and **5**^th plate does not satisfy his desire. So it is impossible to choose **K** plates.

</details>

## Approach

The requirement is that **every pair** of chosen plates share a common factor above $1$. The simplest way to guarantee that is to give them all the same prime factor — and $2$ is the best choice, because the multiples of $2$ are the most numerous in $1 \ldots N$.

So take $2, 4, 6, \ldots, 2K$, which works whenever $2K \leq N$, i.e.

$$K \leq \left\lfloor \frac{N}{2} \right\rfloor$$

That bound is also the limit. The even numbers form a **maximal** set: no odd number can join, since it would have to share a factor with every even number present, including the largest power of two — and only an even number does that. And no larger pairwise-non-coprime set exists in $1 \ldots N$.

$K = 1$ is a genuine exception and needs its own branch. With a single plate there are no pairs at all, so the condition holds vacuously and any plate works — even when $\lfloor N/2 \rfloor = 0$, as happens for $N = 1$. Falling through to the general rule would wrongly print $-1$ there.

Sample case 2 asks for all $100$ plates from $1 \ldots 100$, far beyond the $50$ evens, so $-1$. Sample case 1 asks for $3$ and publishes `45 63 35` — an odd triple whose pairwise gcds are $9$, $5$ and $7$, with **no common factor at all**. That is a perfectly valid alternative, which is why this is judged by a checker rather than by text comparison; the construction here simply prints `2 4 6`.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        if k == 1:
            # No pairs to check, so any single plate is fine.
            out.append("1")
        elif 2 * k <= n:
            # All even, so every pair shares the factor 2.
            out.append(" ".join(str(2 * j) for j in range(1, k + 1)))
        else:
            out.append("-1")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(K)$ per test case
- **Space:** $O(K)$

> CodeChef tags: `Mathematics`, `Number Theory`, `Set Theory`
