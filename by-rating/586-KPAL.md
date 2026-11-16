[&larr; 585. Consecutive Adding](585-CONSADD.md) &middot; [Index](README.md) &middot; [587. Symmetric Swaps &rarr;](587-SYMARRSWAP.md)

# 586. K Increment Palindrome

> [`KPAL`](https://www.codechef.com/problems/KPAL) &middot; difficulty **2038** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Only two obstructions - K = N, and a parity clash |
| **CodeChef tags** | `Algorithms`, `Constructive`, `ad-hoc` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

Chef has an array $A$ of size $N$ and an integer $K$. He can perform the following operation on $A$ any number of times:
- Select any $K$ distinct indices $i_1, i_2, \ldots, i_K$ and increment the array elements at these $K$ indices by $1$.
Formally, set $A_{i_j} := A_{i_j} + 1$ for all $1 \le j \le K$.

For example, if $A = [3, 2, 8, 4, 6]$ and we select the indices $2, 3, 5$, then $A$ becomes $[3, 2 + 1, 8 + 1, 4, 6 + 1]$ i.e. $[3, 3, 9, 4, 7]$.

Determine if Chef can make the array $A$ palindromic by applying the given operation **any** number of times.

Note: An array is called palindrome if it reads the same backwards and forwards, for e.g. $[4, 10, 10, 4]$ and $[7, 1, 7]$ are palindromic arrays.

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $N$ and $K$ — the size of the array $A$ and the parameter mentioned in the statement.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

**Output**

For each test case, output `YES` if we can make $A$ palindromic by applying the given operation. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

## Constraints

- $1 \leq T \leq 10^5$
- $1 \le K \le N \le 10^5$
- $1 \le A_i \le 10^6$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
4
5 3
2 4 5 4 2
6 1
4 5 5 4 6 4
6 2
4 5 5 4 6 4
4 2
1 2 3 3
```

**Sample output**

```
YES
YES
YES
NO
```

<details><summary>Explanation</summary>

**Test case $1$:** The given array $A$ is already palindromic.

**Test case $2$:** We can apply the following operations:
- Select index $[4]$: $A$ becomes $[4, 5, 5, 5, 6, 4]$
- Select index $[2]$: $A$ becomes $[4, 6, 5, 5, 6, 4]$

**Test case $3$:** We can apply the following operations:
- Select index $[2, 4]$: $A$ becomes $[4, 6, 5, 5, 6, 4]$

**Test case $4$:** It can be proven that $A$ can not be converted into a palindrome using the given operations.

</details>

## Approach

If $K = N$ every operation raises all elements together, so nothing relative ever changes: the array must already be a palindrome.

If $K < N$, two operations that differ in a single index have the net effect "add 1 to $i$" versus "add 1 to $j$". Combining such pairs on top of a large common number of operations lets us move single units around freely, so any target of non-negative increments is reachable as long as the total number of increments is a multiple of $K$ (and large enough). To make the array a palindrome we need increments that equalise each mirrored pair; adding the same amount to both members of a pair, or to the middle element, adjusts the total without breaking the palindrome.

- $N$ odd: the middle element absorbs any amount, so the total can be fixed to a multiple of $K$.
- $N$ even: the final sum is even, because it is twice the sum of one half. If $K$ is odd the parity of the sum can be changed by one more operation, so it is fine; if $K$ is even the parity of the sum never changes, and the initial sum has to be even.

So for $K < N$ the answer is No only when $N$ and $K$ are even and the sum is odd.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        k = next(tokens)
        values = [next(tokens) for _ in range(n)]
        ok = values == values[::-1] if n == k else n % 2 == 1 or k % 2 == 1 or sum(values) % 2 == 0
        out.append('YES' if ok else 'NO')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- $K = N$ depends on the actual values; all other cases depend only on parities.
- $N = 1$ forces $K = 1 = N$, and a single element is a palindrome.
- $K = 1$ with $N > 1$ is always Yes.
- The increments needed can be large, but the question is only about existence.

## Dry run

- `N = 4, K = 2, A = [1, 2, 3, 3]`: both even and the sum 9 is odd - NO.
- `N = 6, K = 2, A = [4, 5, 5, 4, 6, 4]`: both even and the sum 28 is even - YES.
- `N = 5, K = 3`: $N$ is odd - YES whatever the values.

---

Same problem grouped by topic: [../docs/constructive/KPAL.md](../docs/constructive/KPAL.md)
