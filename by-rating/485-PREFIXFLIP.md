[&larr; 484. Cool Guys](484-COOLGUYS.md) &middot; [Index](README.md) &middot; [486. Optimal Denomination &rarr;](486-MINNOTES.md)

# 485. Flip the Prefix

> [`PREFIXFLIP`](https://www.codechef.com/problems/PREFIXFLIP) &middot; difficulty **1758** &middot; time limit **2s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Sliding window over mandatory boundary flips |
| **CodeChef tags** | `Data Structures`, `Algorithms`, `String`, `Simple Algos` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

You are given a **binary** string $S$ of length $N$ and an integer $K$. You can perform the following operation on the string:
- Select a *prefix* of the string $S$ and flip all the characters of the prefix. A flip corresponds to changing $0$ to $1$ and vice-versa.

Find the **minimum** number of operations required to obtain a substring of length $K$ such that all characters of the substring are $1$.

Note:
- A prefix is obtained by deleting some (possibly zero) characters from the end of the string.
- A substring is obtained by deleting some (possibly zero) characters from the beginning of the string and some (possibly zero) characters from the end of the string.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $K$ — the length of the string and the length length of substring containing all $1$s we want to achieve.
    - The next line contains the binary string $S$.

**Output**

For each test case, output on a new line, the **minimum** number of operations required to obtain a substring of length $K$ such that all characters of the substring are $1$.

## Constraints

- $1 \leq T \leq 2000$
- $1 \leq K \le N \leq 3\cdot 10^5$
- $S$ consists of $0$ and $1$ only.
- The sum of $N$ over all test cases won't exceed $3\cdot 10^5$.

## Sample

**Sample input**

```
3
3 3
000
4 2
0110
5 3
10101
```

**Sample output**

```
1
0
2
```

<details><summary>Explanation</summary>

**Test case $1$:** We need to obtain a substring containing three $1$s. Using one operation, we can select the prefix $S[1,3]$ and flip all the characters in the prefix. Thus, the string becomes $111$.

**Test case $2$:** The string already contains a substring having two $1$s. Thus, we do not need any operation.

**Test case $3$:** We need to obtain a substring containing three $1$s. We can do so using $2$ operations:
- Operation $1$: Select the prefix $S[1, 4]$ and flip all characters in the prefix. Thus, the string becomes $01011$.
- Operation $2$: Select the prefix $S[1, 3]$ and flip all characters in the prefix. Thus, the string becomes $10111$.

Thus, we have a substring $S[3,5]$ of length $3$ where all characters of the substring are $1$. It can be shown that we cannot obtain such substring using less than $2$ operations.

</details>

## Approach

For a fixed window, every unequal adjacent pair inside it requires one flip ending at that boundary. A prefix flip changes no other internal boundary. In addition, its rightmost character must become one, requiring one further flip if it is zero. Thus the exact cost is the number of internal transitions plus the indicator that the last character is zero.

Slide a length-$K$ window, removing its old left boundary and adding its new right boundary. Take the smallest exact cost.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n, k = int(next(tokens)), int(next(tokens))
        s = next(tokens)
        changes = sum(s[i] != s[i-1] for i in range(1, k))
        answer = changes + (s[k-1] == 48)
        for right in range(k, n):
            changes -= s[right-k] != s[right-k+1]
            changes += s[right-1] != s[right]
            answer = min(answer, changes + (s[right] == 48))
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- $K=1$ has no internal boundaries.
- An existing run of $K$ ones costs zero.
- A full zero window needs just one flip.

## Dry run

For `10101`, $K=3$, the three window costs are `2, 3, 2`; the minimum is `2`.

---

Same problem grouped by topic: [../docs/strings/PREFIXFLIP.md](../docs/strings/PREFIXFLIP.md)
