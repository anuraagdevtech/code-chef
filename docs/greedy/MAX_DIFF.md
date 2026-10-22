# 160. The Two Dishes

> CodeChef problem code [`MAX_DIFF`](https://www.codechef.com/problems/MAX_DIFF) &middot; difficulty **1254** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Pushing one variable to its bound |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

Chef prepared two dishes yesterday. Chef had assigned the $\textbf{tastiness}$ $T_1$ and $T_2$ to the first and to the second dish respectively. The tastiness of the dishes can be any $\textbf{integer}$ between $0$ and $N$ (both inclusive).

Unfortunately, Chef has forgotten the values of $T_1$ and $T_2$ that he had assigned to the dishes. However, he remembers the sum of the tastiness of both the dishes - denoted by $S$.

Chef wonders, what can be the maximum possible absolute difference between the tastiness of the two dishes. Can you help the Chef in finding the maximum absolute difference?

It is guaranteed that at least one pair $\{T_1, T_2\}$ exist such that $T_1 + T_2 = S, 0 \leq T_1, T_2 \leq N$.

**Input**

- The first line of input contains a single integer $T$, denoting the number of testcases. The description of the $T$ testcases follows.
- The first and only line of each test case contains two space-separated integers $N$, $S$, denoting the maximum tastiness and the sum of tastiness of the two dishes, respectively.

**Output**

For each testcase, output a single line containing the maximum absolute difference between the tastiness of the two dishes.

## Constraints

- $1 \leq T \leq 10^3$
- $1 \leq N \leq 10^5$
- $1 \leq S \leq 2 \cdot 10^5$

## Sample

**Sample input**

```
3
3 1
4 4
2 3
```

**Sample output**

```
1
4
1
```

<details><summary>Explanation</summary>

**Test Case $1$:** The possible pairs of $\{T_1, T_2\}$ are $\{0, 1\}$ and $\{1, 0\}$. Difference in both the cases is $1$, hence the maximum possible absolute difference is $1$.

**Test Case $2$:** The possible pairs of $\{T_1, T_2\}$ are $\{0, 4\}$, $\{1, 3\}$, $\{2, 2\}$, $\{3, 1\}$ and $\{4, 0\}$. The maximum possible absolute difference is $4$.

**Test Case $3$:** The possible pairs of $\{T_1, T_2\}$ are $\{1, 2\}$ and $\{2, 1\}$. Difference in both the cases is $1$, and hence the maximum possible absolute difference is $1$.

</details>

## Approach

With $T_1 + T_2 = S$ fixed, the difference is

$$|T_1 - T_2| = |2T_1 - S|$$

so maximising it means pushing $T_1$ as far from $S/2$ as possible. Both variables are capped at $N$ and floored at $0$, so the extreme choice is

$$T_1 = \min(N, S)$$

— take everything, unless the cap or the sum itself stops you. The partner is then $T_2 = S - T_1$, and the difference is

$$2\min(N, S) - S$$

Both terms of the `min` are needed. When $S \leq N$ the sum is the binding limit: one dish takes all $S$ and the other takes $0$, giving a difference of $S$. Sample case 2 ($N=4, S=4$) is this, answering $4$. When $S > N$ the cap binds: one dish maxes at $N$ and the other absorbs $S - N$. Sample case 3 ($N=2, S=3$) gives $2 \cdot 2 - 3 = 1$.

The guarantee that some valid pair exists means $S \leq 2N$, so $T_2 = S - \min(N,S)$ never exceeds $N$ and the construction is always legal — no feasibility check is needed.

The answer also carries a parity fact worth noticing: $2\min(N,S) - S$ has the same parity as $S$, which is forced, since $T_1 - T_2$ and $T_1 + T_2$ always share a parity. Sample case 1, with odd $S = 1$, correctly gives the odd answer $1$ rather than $0$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, s = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # Push one dish as high as the cap and the sum allow.
        hi = min(n, s)
        out.append(str(2 * hi - s))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **$S$ larger than $N$** (the second and third rows): one dish is capped at $N$, so the other must take the remaining $S - N$ and the difference is $2N - S$ rather than $S$.
- **$S$ smaller than $N$** (the first row, $S = 1$ with $N = 3$): the whole sum fits in one dish, the other is $0$, and the difference is $S$ itself — which $2S - S$ gives.
- **The cap must be $\min(N, S)$.** Using $N$ alone makes the second tastiness negative when $S < N$; using $S$ alone breaks the per-dish ceiling when $S > N$.
- **$S = 2N$** (the second row, $N = S = 4$ gives $2 \cdot 4 - 4 = 4$; a true $S = 2N$ case like $N = 2, S = 4$) leaves both dishes full and the difference $0$.
- **Feasibility is guaranteed** — the statement promises some valid pair with $T_1 + T_2 = S$ — so $S \leq 2N$ and the formula never returns a negative number.
- **Tastiness may be $0$**, which is what makes the $S < N$ case work at all.

## Dry run

| $N$ | $S$ | $\min(N, S)$ | other dish | difference $2\min(N,S) - S$ |
|---:|---:|---:|---:|---:|
| 3 | 1 | 1 | 0 | `1` |
| 4 | 4 | 4 | 0 | `4` |
| 2 | 3 | 2 | 1 | `1` |

Row 3 is the capped case: the best split is $2 + 1$, not $3 + 0$, because no dish may exceed $N = 2$.

---

Same problem in rating order (#188 of 486): [../../by-rating/188-MAX_DIFF.md](../../by-rating/188-MAX_DIFF.md)
