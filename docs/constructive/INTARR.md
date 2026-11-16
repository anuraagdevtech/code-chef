[&larr; 653. Non Zero Subarray Xor](SUBARRAYXOR.md) &middot; [Index](../../README.md) &middot; [663. Binary Substitution &rarr;](SUBSBIN.md)

# 657. Interesting Array

> CodeChef problem code [`INTARR`](https://www.codechef.com/problems/INTARR) &middot; difficulty **2145** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Zigzag from the sorted halves, tried in both orientations |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

An array is called *interesting* if no subarray of length **greater than** $2$ is non-increasing or non-decreasing.

Chef has an array $A$ of length $N$. He wants to make the array **interesting** by rearranging the elements in any order.

If there exist multiple such arrays, output any one.
If no such array exists, print $-1$ instead.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$ denoting the length of array $A$.
    - The next line contains $N$ space separated integers, $A_1, A_2, \ldots, A_N$

**Output**

For each test case, output on a single line, any possible **interesting** array.
If no such array is possible, output $-1$.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

## Sample

**Sample input**

```
3
3
2 2 2
4
2 6 5 2
5
5 5 2 4 2
```

**Sample output**

```
-1
6 2 5 2
5 2 4 2 5
```

<details><summary>Explanation</summary>

**Test case $1$:** There is no way of arranging the elements such that no subarray of length greater than $2$ is non-increasing or non-decreasing.

**Test case $2$:** A possible rearrangement of the elements is $[6, 2, 5, 2]$. Note that the subarrays of length greater than $2$ are $\{[6, 2, 5], [2, 5, 2], [6, 2, 5, 2]\}$. None of these subarrays are non-increasing or non-decreasing.

**Test case $3$:** A possible rearrangement of the elements is $[5, 2, 4, 2, 5]$. Note that the subarrays of length greater than $2$ are $\{[5, 2, 4], [2, 4, 2], [4, 2, 5], [5, 2, 4, 2], [2, 4, 2, 5], [5, 2, 4, 2, 5]\}$. None of these subarrays are non-increasing or non-decreasing.

</details>

## Approach

No three consecutive elements may be monotone, even weakly, so the array must strictly alternate: every inner element is a strict peak or a strict valley.

Sort the values and split them into a lower and an upper half. Putting the lower half on one parity of positions and the upper half on the other gives the alternation as long as each low element is strictly below both of its neighbours. Writing both halves in the same (descending) order pairs the $k$-th largest low with the $k$-th and $(k+1)$-th largest highs, which keeps equal values as far apart as possible.

Two orientations exist - valleys on the even indices, or peaks on the even indices - and for odd $N$ they use differently sized halves. Build the first, verify it directly, and if it fails build and verify the second. If both fail, print $-1$.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        values = sorted((next(tokens) for _ in range(n)))
        arranged = [0] * n
        arranged[::2] = values[:(n + 1) // 2][::-1]
        arranged[1::2] = values[(n + 1) // 2:][::-1]
        ok = all((arranged[i - 1] < arranged[i] > arranged[i + 1] or arranged[i - 1] > arranged[i] < arranged[i + 1] for i in range(1, n - 1)))
        if not ok:
            arranged[::2] = values[n // 2:]
            arranged[1::2] = values[:n // 2]
            ok = all((arranged[i - 1] < arranged[i] > arranged[i + 1] or arranged[i - 1] > arranged[i] < arranged[i + 1] for i in range(1, n - 1)))
        out.append(' '.join(map(str, arranged)) if ok else '-1')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $N \le 2$: any order is interesting.
- A value occurring more than about half of the time makes the task impossible (for example `2 2 2`).
- For odd $N$ the extra element goes to the even indices, so the two orientations really differ.
- Any valid arrangement is accepted.

## Dry run

`A = [2, 6, 5, 2]`, sorted `2 2 5 6`.

Lower half `2 2`, upper half `5 6`, both reversed: even indices get `2 2`, odd indices get `6 5`.

Arrangement `2 6 2 5`: 6 is a peak and the second 2 is a valley, so it is valid.

> CodeChef tags: `Algorithms`, `Constructive`

---

Same problem in rating order (#616 of 735): [../../by-rating/616-INTARR.md](../../by-rating/616-INTARR.md)
