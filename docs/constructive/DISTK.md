[&larr; 571. Yet Another Problem About Sequences](EARTSEQ.md) &middot; [Index](../../README.md) &middot; [634. No sequence &rarr;](NOSEQ.md)

# 630. K Distinct Array

> CodeChef problem code [`DISTK`](https://www.codechef.com/problems/DISTK) &middot; difficulty **2015** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | A distinct prefix, one calibrated repeat and a constant tail |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

An array is said to be **good** if all its elements are distinct, i.e. no two elements of the array are equal to each other.

You are given a positive integer $N$ and an integer $K$ such that $N \leq K \leq \binom{N+1}{2}$.

Construct an array $A$ of length $N$ that satisfies the following conditions
- $A$ has **exactly** $K$ good (contiguous) subarrays, and
- Every element of $A$ is an integer from $1$ to $N$ (both inclusive).

If there are multiple such arrays, you can print **any** of them.

**Note:** It can be shown that for all inputs satisfying the given constraints, there is **always** a valid solution.

**Input**

- The first line contains an integer $T$, the number of testcases. The description of the $T$ testcases follow.
- Each testcase consists of a single line with two space separated integers, $N$ and $K$ respectively.

**Output**

- For each testcase print $N$ space separated integers, the elements of the constructed array.
- If there are multiple outputs, you can print **any** of them.
- Your output will be considered correct only if the following conditions are satisfied,
    - Every element of the array is between $1$ and $N$, and
    - The array has exactly $K$ good subarrays

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $N \leq K \leq \binom{N+1}{2}$
- Sum of $N$ over all testcases is atmost $3 \cdot 10^5$.

## Sample

**Sample input**

```
3
5 5
5 15
5 7
```

**Sample output**

```
1 1 1 1 1
1 2 3 4 5
1 2 2 1 1
```

<details><summary>Explanation</summary>

**Test Case 1:** $N = 5, K = 5$. All subarrays of length $1$ are good, therefore every array of size $N$ has at least $N$ good subarrays. If all elements are equal then these will be the only good subarrays so the given array $\{1, 1, 1, 1, 1\}$ is a valid solution. Observe that under the constraints there are $5$ different solutions (one for each value $1$ through $5$) and all of them will be considered correct.

**Test Case 2:** $N = 5, K = 15$. There are only $\binom{N + 1}{2} = 15$ subarrays, including the array itself. Therefore the array itself must be good which leads us to the solution given above. Any permutation of $\{1, 2, 3, 4, 5\}$ is also a valid solution, thus there are $5! = 120$ different solutions to this case and all of them will be considered correct.

**Test Case 3:** $N = 5, K = 7$. The constructed array is $A = \{1, 2, 2, 1, 1\}$. You may verify that the only good subarrays of $A$, in addition to the $5$ subarrays of length $1$, are those shown below (subarrays are highlighted red).
- $\{{\color{red}1}, {\color{red}2}, 2, 1, 1\}$
- $\{1, 2, {\color{red}2}, {\color{red}1}, 1\}$

</details>

## Approach

Count good subarrays by their right end: position $i$ contributes the length of the longest all-distinct subarray ending there, which is at least 1. So every array has at least $N$ good subarrays, and we must distribute $K - N$ extra units.

Start with the distinct values $1, 2, \dots, L$: position $j$ contributes $j$, i.e. $j - 1$ extra. Extend the prefix greedily while the remaining extra is at least the cost of the next position. When it stops, the remainder $r$ satisfies $0 \le r < L$.

The next element is chosen to contribute exactly $r + 1$: repeat the value that sits $r + 1$ places from the end of the prefix, i.e. index $L - r$ (1-based). The longest distinct subarray ending at the new position then has exactly $r + 1$ elements. Fill the rest of the array with that same value; each of those positions contributes exactly 1.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        extra = next(tokens) - n
        prefix = 1
        while prefix < n and extra >= prefix:
            extra -= prefix
            prefix += 1
        result = list(range(1, prefix + 1))
        if prefix < n:
            result.append(result[prefix - extra - 1])
            result.extend([result[-1]] * (n - prefix - 1))
        out.append(' '.join(map(str, result)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $K = N$: the array is constant.
- $K = \binom{N+1}{2}$: the whole array is the distinct prefix.
- When the prefix reaches length $N$ there is nothing to append.
- Any valid array is accepted, so the judge needs a checker rather than a text comparison.

## Dry run

`N = 5, K = 7`, so 2 extra units.

Prefix: length 1 costs nothing; extending to length 2 costs 1 (extra left: 1); extending to length 3 would cost 2, too much. $L = 2$, $r = 1$.

Append the value $r + 1 = 2$ places from the end of `[1, 2]`, which is 1, then pad with 1s: `1 2 1 1 1`.

Contributions by right end: `1 2 2 1 1`, total 7.

> CodeChef tags: `Algorithms`

---

Same problem in rating order (#577 of 735): [../../by-rating/577-DISTK.md](../../by-rating/577-DISTK.md)
