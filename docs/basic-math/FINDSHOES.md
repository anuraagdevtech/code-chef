# 39. Finding Shoes

> CodeChef problem code [`FINDSHOES`](https://www.codechef.com/problems/FINDSHOES) &middot; difficulty **646** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Clamping one side of a two-part requirement |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Chef has $N$ friends. Chef promised that he would gift a pair of shoes (consisting of one left shoe and one right shoe) to each of his $N$ friends. Chef was about to go to the marketplace to buy shoes, but he suddenly remembers that he already had $M$ left shoes.

What is the minimum number of extra shoes that Chef will have to buy to ensure that he is able to gift a pair of shoes to each of his $N$ friends?

For example, if $N = 2$, $M = 4$, then Chef already has $4$ left shoes, so he must buy $2$ extra right shoes to form $2$ pairs of shoes.

Therefore Chef must buy at least $2$ extra shoes to **ensure** that he is able to get $N = 2$ pairs of shoes.

**Input**

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $N$ and $M$ - the number of Chef's friends and the number of left shoes Chef has.

**Output**

For each test case, output the minimum number of extra shoes that Chef will have to buy to ensure that he is able to get $N$ pairs of shoes.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$
- $0 \leq M \leq 100$

## Sample

**Sample input**

```
3
2 4
6 0
4 3
```

**Sample output**

```
2
12
5
```

<details><summary>Explanation</summary>

**Test Case 1:** Discussed in the problem statement

**Test Case 2:** Chef initially has no left shoes. He must buy $6$ more left shoes and $6$ more right shoes to form $6$ pairs of shoes.

**Test Case 3:** Chef initially has $3$ left shoes. He must buy $1$ more left shoe and $4$ more right shoes to form $4$ pairs of shoes.

</details>

## Approach

Each of the $N$ friends needs a *pair*, so Chef must end up with $N$ left shoes and $N$ right shoes. He already holds $M$ left shoes and no right shoes at all.

The two sides are accounted for separately:

- **Right shoes:** he has none, so he must buy all $N$.
- **Left shoes:** he must buy the shortfall $N - M$, but only if it is positive — surplus left shoes are useless and cannot be converted.

So the answer is

$$N + \max(0,\; N - M)$$

The clamp is the whole difficulty. Sample case 1 has $N = 2$ and $M = 4$: two spare left shoes that help with nothing, so the answer is $2 + 0 = 2$, not $2 + (2 - 4) = 0$. Without `max(0, ...)` the surplus would subtract from the right-shoe count, which is nonsense — a left shoe is not a right shoe.

That asymmetry is the lesson. When a requirement has several components and a surplus in one cannot offset a deficit in another, each component must be clamped at zero **before** summing. The same clamp appeared in the candy-packets problem, and here it matters even more because the unclamped version silently produces a plausible-looking number.

Case 2 ($N = 6$, $M = 0$) is the no-stock extreme: $6 + 6 = 12$ shoes, a full pair for everyone.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, m = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # All n right shoes, plus the left shortfall; spare lefts don't help.
        out.append(str(n + max(0, n - m)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **More spares than needed** ($N = 2$, $M = 4$): the two surplus shoes are useless, so the clamp is essential — without `max(0, ...)` the shortfall is $-2$ and the answer comes out as $0$ instead of $2$. The sample's first row is this case.
- **No spares at all** ($M = 0$): every shoe must be bought, so $2N$. The sample's second row.
- **Exactly enough spares** ($M = N$): only the other $N$ shoes are needed.
- **The two sides are asymmetric**: all $N$ of one kind must be bought no matter what, and only the other kind benefits from existing stock, which is why the expression is $N + \max(0, N - M)$ rather than symmetric in $M$.

## Dry run

| $N$ | $M$ (spares) | shortfall $N - M$ | clamped | total $N + {\cdot}$ | output |
|---:|---:|---:|---:|---:|---|
| 2 | 4 | $-2$ | 0 | 2 | `2` |
| 6 | 0 | 6 | 6 | 12 | `12` |
| 4 | 3 | 1 | 1 | 5 | `5` |

Row 1 is the one the clamp exists for.

> CodeChef tags: `Basic Programming Concepts`, `Mathematics`, `Basic Math`

---

Same problem in rating order (#46 of 486): [../../by-rating/046-FINDSHOES.md](../../by-rating/046-FINDSHOES.md)
