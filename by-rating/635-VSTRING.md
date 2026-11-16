[&larr; 634. Pyramid Traversal](634-PYRAMIDMOVES.md) &middot; [Index](README.md) &middot; [636. Chef and insomnia &rarr;](636-CHINSM.md)

# 635. Valid String

> [`VSTRING`](https://www.codechef.com/problems/VSTRING) &middot; difficulty **2194** &middot; time limit **0.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Circular gaps between ones - at most one may be too long |
| **CodeChef tags** | `Data Structures`, `Algorithms`, `String`, `Observation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

Given a binary string $S$ consisting of $0's$ and $1's$, find whether there exists a rightwise  [circular rotation](https://en.wikipedia.org/wiki/Circular_shift) of the string such that every 2 adjacent $1's$ are separated by at most $C$ $0's$.

**Note:** The last occurrence of $1$ in the rotated string won't have any $1$ next to it, i.e, first and the last ones in the string are not considered to be adjacent.

**Input:**
- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of two lines of input.
- First line contains two space separated integers $N, C$, length of the string and the upper limit on a number of $0's$ between $2$ adjacent $1's$.
-  Second line contains the binary string $S$.

**Output:**
For each testcase, output in a single line "YES" if there exists a rightwise circular rotation of string satisfying the criteria and "NO" if it doesn't exist.

**Note:** The output is case-insensitive ― each letter may be printed in upper case or lower case.

**Constraints**
- $1 \leq N \leq 5*10^5$
- $0 \leq C \leq max(0, N - 2)$
- Sum of $N$ over all tests is atmost $10^6$.

## Constraints

- $1 \leq N \leq 5*10^5$
- $0 \leq C \leq max(0, N - 2)$
- Sum of $N$ over all tests is atmost $10^6$.

## Sample

**Sample input**

```
3
4 1
1100
4 0
0101
6 1
101001
```

**Sample output**

```
YES
NO
YES
```

<details><summary>Explanation</summary>

**Case 1:** In the original configuration maximum number of $0's$ between $2$ adjacent $1's$ is $0$, therefore it satisfies the criteria.

**Case 2:** The $4$ circular rotations of the string S = {"0101", "1010", "0101", "1010"}. In all the cases the maximum number of $0's$ between $2$ consecutive $1's$ is $1$ which doesn't satisfies the criteria.

**Case 3:** The $6$ circular rotations of the string S = {"101001", "110100", "011010", "001101", "100110", "010011"} out of which $second$, $third$ and $fourth$ strings satisfy the criteria.

</details>

## Approach

Place the string on a circle. Between consecutive ones there are gaps of zeros, and with $m \ge 2$ ones there are $m$ such circular gaps, including the one that wraps from the last `1` to the first.

A rotation chooses where the circle is cut. The gap that contains the cut becomes the leading and trailing zeros of the linear string and is no longer "between two adjacent ones", while every other gap stays as it is. So a valid rotation exists exactly when at most one circular gap is longer than $C$: cut inside that one, or anywhere if there is none.

With fewer than two ones there are no adjacent ones at all and the answer is YES.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        limit = int(next(tokens))
        bits = next(tokens).decode()
        ones = [i for i, v in enumerate(bits) if v == '1']
        if len(ones) < 2:
            out.append('YES')
            continue
        gaps = [ones[i] - ones[i - 1] - 1 for i in range(1, len(ones))] + [n + ones[0] - ones[-1] - 1]
        out.append('YES' if sum((g > limit for g in gaps)) <= 1 else 'NO')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- No `1` or a single `1`: YES.
- With exactly two ones there are two gaps, and the answer is NO only if both exceed $C$.
- The wrap-around gap is $N + \text{first} - \text{last} - 1$.
- $C = 0$ demands that all ones be contiguous on the circle.

## Dry run

`N = 6, C = 1, S = 101001`. Ones at indices 0, 2, 5.

Gaps: between 0 and 2 one zero; between 2 and 5 two zeros; wrapping from 5 to 0 none. Only one gap exceeds $C = 1$, so cut there: the rotation `110100` works. YES.

For `0101` with $C = 0$ both gaps have one zero, two gaps exceed the limit: NO.

---

Same problem grouped by topic: [../docs/strings/VSTRING.md](../docs/strings/VSTRING.md)
