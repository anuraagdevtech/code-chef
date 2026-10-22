[&larr; 342. Andrew and the Meatballs again](342-AMMEAT2.md) &middot; [Index](README.md) &middot; [344. Chef And Adjacent Sums &rarr;](344-CHFADJSUM.md)

# 343. Odd Sum

> [`ODDSUM`](https://www.codechef.com/problems/ODDSUM) &middot; difficulty **1600** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Parity of consecutive prefix sums |
| **CodeChef tags** | `Mathematics`, `Algorithms`, `Constructive`, `Basic Math`, `ad-hoc` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Given an integer $N$, consider all arrays $A$ of size $N$ such that:

- All the elements are non-negative and distinct.
- All prefix sums are odd. Formally, for all $i$ such that $1 \le i \le N$, $\sum_{j=1}^i A_j$ is odd.

Among all possible arrays $A$, output the smallest possible sum of the elements of the array.

**Note**: Since the Input/Output may be large, it is preferred to use fast I/O.

**Input**

- The first line contains $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains $N$ - the size of the array.

**Output**

For each test case, output on one line the smallest sum among all arrays satisfying the constraints.

## Constraints

- $1 \leq T \leq 10^6$
- $1 \leq N \leq 10^9$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
1
3
```

**Sample output**

```
3
```

<details><summary>Explanation</summary>

- **Test case $1$**: A possible array is $[1, 2, 0]$. $[1, 0, 0]$ is not valid because $0$ occurs twice in it; $[0, 1, 2]$ is not valid because the prefix sum until the first index is $0$, which is even. Another possible array is $[5, 2, 4]$.
$[1, 2, 0]$ yields the sum $3$, and we can prove that there are no valid arrays that have sum less than $3$.

</details>

## Approach

Consecutive prefix sums differ by one element, so $A_i = S_i - S_{i-1}$ for $i \geq 2$. Both are odd, and odd minus odd is even, which fixes the parity pattern completely:

$$A_1 \text{ is odd}, \qquad A_2, \ldots, A_N \text{ are all even}$$

Conversely any such array has all prefix sums odd, so this is the only constraint besides distinctness and non-negativity. The two halves can therefore be minimised independently.

The smallest non-negative odd number is $1$, so $A_1 = 1$. The remaining $N-1$ entries are distinct non-negative evens, and the smallest such set is $\{0, 2, 4, \ldots, 2(N-2)\}$ — note $0$ is allowed, since the elements are only required to be non-negative. Its sum is $2 \cdot \frac{(N-2)(N-1)}{2}$, giving

$$\text{answer} = 1 + (N-2)(N-1)$$

No distinctness clash arises between the halves, because $1$ is odd and every other entry is even.

For $N = 3$ the array is $[1, 0, 2]$ with prefix sums $1, 1, 3$ — all odd — and sum $3$, matching the sample. Note the prefix sums need not be *increasing*, which is what lets $0$ appear.

The formula also covers the small cases without special-casing: $N = 1$ gives $1 + (-1)(0) = 1$ and $N = 2$ gives $1 + 0 = 1$, the array $[1, 0]$.

With $T$ up to $10^6$ the arithmetic is irrelevant and the I/O is the whole problem — read the stream in one go and join the output.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        # A_1 = 1, then the smallest distinct evens 0, 2, ..., 2(N-2).
        out.append(str(1 + (n - 2) * (n - 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Only the first element may be odd.** All prefix sums are odd, so consecutive sums differ by an even amount — meaning $A_2, \dots, A_N$ are all even, and $A_1$ is odd.
- **The minimum is then forced**: $A_1 = 1$, the smallest odd non-negative value, and the rest are the smallest distinct non-negative evens $0, 2, 4, \dots, 2(N-2)$, summing to $(N-2)(N-1)$.
- **Zero is allowed and is used**, since the elements need only be non-negative and distinct — excluding it would cost two extra.
- **$N = 1$** gives $1 + (-1)(0) = 1$, the single array $[1]$; the formula handles the negative factor correctly.
- **$N = 2$** gives $1$, from $[1, 0]$ — both prefix sums are $1$.
- **Distinctness is what forces the evens apart**, so the sum grows quadratically rather than staying linear.
- **$T$ up to $10^6$** with the note to use fast I/O, so the whole input is read and the output joined once.

## Dry run

| $N$ | optimal array | prefix sums | total |
|---:|---|---|---:|
| 1 | $[1]$ | $1$ | `1` |
| 2 | $[1, 0]$ | $1, 1$ | `1` |
| 3 | $[1, 0, 2]$ | $1, 1, 3$ | `3` |
| 4 | $[1, 0, 2, 4]$ | $1, 1, 3, 7$ | 7 |

Every prefix sum is odd, and the formula $1 + (N-2)(N-1)$ matches each row.

---

Same problem grouped by topic: [../docs/basic-math/ODDSUM.md](../docs/basic-math/ODDSUM.md)
