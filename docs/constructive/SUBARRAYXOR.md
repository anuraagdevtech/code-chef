[&larr; 652. LCM Mania](LCMMANIA.md) &middot; [Index](../../README.md) &middot; [657. Interesting Array &rarr;](INTARR.md)

# 653. Non Zero Subarray Xor

> CodeChef problem code [`SUBARRAYXOR`](https://www.codechef.com/problems/SUBARRAYXOR) &middot; difficulty **2101** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Choose the prefix xors first - make them 0, 1, ..., N |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ for the output |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

JJ is back with another challenge. He challenges you to construct an array $A$ containing $N$ integers such that the following conditions hold:
- For all $1 \le i \le N$, $1 \le A_i \le 10^6$
- Every [subarray](https://stackoverflow.com/a/45686639) has non-zero XOR. That is, for every $1 \le L \le R \le N$, $A_L \oplus A_{L+1} \oplus \ldots \oplus A_R \ne 0$. Here, $\oplus$ denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR).

Can you complete JJ's challenge?

Under the given constraints, it can be proved that there always exists at least one array satisfying these conditions. If there are multiple possible arrays, **print any of them**.

**Input**

- The first line contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains an integer $N$ — the size of the array $A$ to be constructed.

**Output**

For each test case, output a single line containing $N$ space-separated integers, denoting the elements of array $A$. The $i^{th}$ of these $N$ integers is $A_i$. If multiple arrays exist which satisfy the conditions, print any of them.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 10^5$
- It is guaranteed that the sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
3
1
6
6
```

**Sample output**

```
7
1 2 4 8 16 32
2 3 5 7 11 13
```

<details><summary>Explanation</summary>

**Test Case $1$**: There is only one subarray, $[7]$. Its XOR is non-zero.

**Test Case $2$**: Some of the subarray XORS are:
- $\texttt{XOR}([2,4,8]) = 14 \ne 0$
- $\texttt{XOR}([1,2]) = 3 \ne 0$
- $\texttt{XOR}([4,8,16,32]) = 60 \ne 0$.

Similarly, it can be checked that every subarray has non-zero XOR.

**Test Case $3$**: Some of the subarray XORS are:
- $\texttt{XOR}([2,3,5,7]) = 3 \ne 0$
- $\texttt{XOR}([7, 11]) = 12 \ne 0$
- $\texttt{XOR}([2, 3, 5, 7, 11, 13]) = 5 \ne 0$

Similarly, it can be checked that every subarray has non-zero XOR.

</details>

## Approach

The xor of a subarray $[L, R]$ equals $P_R \oplus P_{L-1}$, where $P$ is the prefix-xor array with $P_0 = 0$. It is non-zero for every subarray exactly when all $N + 1$ prefix values are pairwise distinct.

So pick the prefix values directly: $P_i = i$. Then $A_i = P_i \oplus P_{i-1} = i \oplus (i - 1)$, a number of the form $2^k - 1$, which is at least 1 and at most $2N$ - well inside the allowed range for $N \le 10^5$.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        out.append(' '.join((str(i ^ i - 1) for i in range(1, n + 1))))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$ for the output
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $A_i$ is never 0 because $i \ne i - 1$.
- The largest element is below $2^{18}$, under the $10^6$ limit.
- Many arrays are valid (powers of two, primes, ...), so the judge uses a checker.
- $N = 1$ prints `1`.

## Dry run

`N = 6`: $A = 1, 3, 1, 7, 1, 3$.

Prefix xors: `1 2 3 4 5 6` - all distinct and non-zero, so no subarray has xor 0. For example the subarray `3 1 7` has xor $P_4 \oplus P_1 = 4 \oplus 1 = 5$.

---

Same problem in rating order (#608 of 735): [../../by-rating/608-SUBARRAYXOR.md](../../by-rating/608-SUBARRAYXOR.md)
