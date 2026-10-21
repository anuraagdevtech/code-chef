# 274. Chef and Numbers

> [`CHEFFED`](https://www.codechef.com/problems/CHEFFED) &middot; difficulty **1477** &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Brute Force |
| **Technique** | Bounding the search window |
| **CodeChef tags** | `Mathematics`, `Number Theory`, `Basic Math` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ — a fixed-width scan |
| **Space** | $O(1)$ |

## Question

Chef likes problems related to numbers a lot. He is generally quite good at solving these kinds of problems, but today he got stuck at one number theory problem, and so he asks your help to solve it.

Given a positive integer **N**, find out how many positive integers **X** satisfy the equation **X** + S(**X**) + S(S(**X**)) = **N**, where S(**X**) denoting sum of digits of **X** in decimal (base 10) representation.

**Input**

The only line of the input contains one integer number - **N**.

**Output**

Output single integer in a line denoting the count of number of positive integers **X** satisfying the above given equation.

**Constraints**

- **1** ≤ **N** ≤ **10^9**

## Constraints

- 1 ≤ N ≤ 10^9

## Sample

**Sample 1 input**

```
6
```

**Sample 1 output**

```
1
```

<details><summary>Explanation</summary>

**Example 1**. Only one positive integer **X = 2** satisfies the equation **X + S(X) + S(S(X)) = 6**, as **X + S(X) + S(S(X)) = 2 + 2 + 2 = 6**.

</details>

**Sample 2 input**

```
9939
```

**Sample 2 output**

```
4
```

<details><summary>Explanation</summary>

**Example 2**.**X** can be 9898, 9907, 9910 and 9913.

9898 + S(9898) + S(S(9898)) = 9898 + 34 + 7 = 9939

9907 + S(9907) + S(S(9907)) = 9907 + 25 + 7 = 9939

9910 + S(9910) + S(S(9910)) = 9910 + 19 + 10 = 9939

9913 + S(9913) + S(S(9913)) = 9913 + 22 + 4 = 9939

You can verify that there is not other positive value of **X** satisfying the given equation.

</details>

## Approach

Solve $X + S(X) + S(S(X)) = N$ by searching, but only over a **narrow window** below $N$.

The bound comes from how small digit sums are. For $X \leq 10^9$ the digit sum $S(X)$ is at most $9 \times 10 = 90$, and $S(S(X))$ is at most $S(99) = 18$. So the two correction terms together never exceed about $108$, which forces

$$N - 108 \leq X \leq N$$

Scanning a couple of hundred candidates below $N$ and testing each directly is therefore enough — and it is $O(1)$ regardless of how large $N$ is. The window is taken a little wider than the bound for safety, which costs nothing.

Without that bound the search space is $10^9$ and hopeless; recognising that $S$ grows **logarithmically** while $X$ grows linearly is the whole idea, and the same reasoning appears in every "number plus its digit sum" problem.

Candidates must be clamped to stay positive, since $X$ is required to be a positive integer and $N$ may be small — as in the sample, where $N = 6$ and the window would otherwise run below $1$.

Checking that sample: $X = 2$ gives $2 + 2 + 2 = 6$, so the count is $1$. Note $X = 6$ itself gives $6 + 6 + 6 = 18$, far past the target — the solution is well below $N$, which is exactly what the window is for.

Note there is **no $T$**: the input is a single integer $N$.

## Solution

```python
import sys


def digit_sum(x: int) -> int:
    return sum(map(int, str(x)))


def main() -> None:
    # Single value, no test-case count.
    n = int(sys.stdin.buffer.read().split()[0])
    # S(X) <= 90 and S(S(X)) <= 18 for X <= 1e9, so X cannot be far below N.
    count = 0
    for x in range(max(1, n - 200), n + 1):
        if x + digit_sum(x) + digit_sum(digit_sum(x)) == n:
            count += 1
    print(count)


main()
```

---

Same problem grouped by topic: [../docs/brute-force/CHEFFED.md](../docs/brute-force/CHEFFED.md)
