[&larr; 609. Chefs in Queue](CHFQUEUE.md) &middot; [Index](../../README.md)

# 685. Distinct Values

> CodeChef problem code [`DIST_VALS`](https://www.codechef.com/problems/DIST_VALS) &middot; difficulty **2236** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Stacks |
| **Technique** | Largest and second largest of a subarray are neighbours on a monotonic stack |
| **Time** | $O(N)$ expected per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

The *beauty* value of an array is defined as the difference between the largest and second largest elements of the array. Note that the largest and second largest elements can have the same value in case of duplicates.

For example, *beauty* value of $[2, 5, 3, 1] = 5 - 3 = 2$ and *beauty* value of $[7, 6, 7] = 7 - 7 = 0$

You are given an array $A$ of length $N$. Your task is to find the total number of **distinct** *beauty* values among all *subarrays* of $A$ having length greater than $1$.

Note that, a subarray is obtained by deleting some (possibly zero) elements from the beginning and some (possibly zero) elements from the end of the array.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the size of the array.
    - The second line contains $N$ space-separated numbers - $A_{1}, A_{2},\ldots ,A_{N}$, the elements of the array.

**Output**

For each test case, output a single line, the total number of **distinct** beauty among all *subarrays* of $A$ having length greater than $1$.

## Constraints

- $1 \leq T \leq 10^{4}$
- $2 \leq N \leq 2 \cdot 10^{5}$
- $1 \leq A_i \leq 10^{9}$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
4
2
1 1
3
4 2 1
4
8 1 7 2
5
6 9 4 2 1
```

**Sample output**

```
1
2
4
4
```

<details><summary>Explanation</summary>

**Test case $1$:** The only subarray is $[1,1]$ whose beauty is $0$. Thus, there is only $1$ distinct value of beauty.

**Test case $2$:** The subarrays are $[4,2], [2,1],$ and $[4,2,1]$ having beauty $2, 1,$ and $2$ respectively. There are $2$ distinct values of beauty.

**Test case $3$:** The unique values of beauty are $7,1,6,$ and $5$.

**Test case $4$:** The unique values of beauty are $3,5,2,$ and $1$.

</details>

## Approach

Take a subarray and let $u, v$ be its largest and second largest elements. Everything between their positions is no larger than the smaller of the two, so the subarray that starts at one of them and ends at the other has the same beauty. The distinct beauties are therefore the differences over pairs of positions such that all elements strictly between them are at most the smaller endpoint.

Those pairs are exactly what a monotonic stack produces. Keep a stack of values that is strictly decreasing from bottom to top. When a new value $x$ arrives:

- every stack element $\le x$ is popped; it sees $x$ as the first element to its right that is at least as large, giving the pair with difference $x -$ (popped);
- the element left on top, if any, is larger than $x$ and is the nearest larger element to the left of $x$, giving the pair with difference (top) $- x$.

Collect the differences in a set and print its size.

## Solution (Python)

```python
import sys


def solve(tokens):
    n = next(tokens)
    values = [next(tokens) for _ in range(n)]
    stack = []
    beauties = set()
    for value in values:
        while stack and stack[-1] <= value:
            beauties.add(value - stack.pop())
        if stack:
            beauties.add(stack[-1] - value)
        stack.append(value)
    return str(len(beauties))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(N)$ expected per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Equal neighbours give beauty 0; equal values are popped, which records it.
- $N = 2$ has exactly one subarray.
- Each element is pushed and popped once, so the number of candidate pairs is at most $2N$.
- Only distinct values of beauty are counted.

## Dry run

`A = [8, 1, 7, 2]`.

- 8: push. Stack `8`.
- 1: top 8 is larger: record $8 - 1 = 7$. Stack `8 1`.
- 7: pop 1, record $7 - 1 = 6$; top 8 is larger: record $8 - 7 = 1$. Stack `8 7`.
- 2: top 7 is larger: record $7 - 2 = 5$. Stack `8 7 2`.

Distinct beauties `{7, 6, 1, 5}`: answer 4.

> CodeChef tags: `Data Structures`, `Algorithms`, `Simple Algos`

---

Same problem in rating order (#647 of 735): [../../by-rating/647-DIST_VALS.md](../../by-rating/647-DIST_VALS.md)
