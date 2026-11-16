[&larr; 500. Monks](MONKS.md) &middot; [Index](../../README.md) &middot; [510. Prefix Zeros &rarr;](PREZ.md)

# 505. 01 Subsequence

> CodeChef problem code [`ZEROONE`](https://www.codechef.com/problems/ZEROONE) &middot; difficulty **1781** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Sort zero blocks downwards and one blocks upwards |
| **Time** | $O(N\log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You are handed a binary string $S$, but not in any ordinary form. Instead of being directly given the value of $S$, you are given an array $C$ of size $N$ representing the *01-compression representation* of $S$. This means $S$ first contains $C_1$ $\texttt{0}$ characters, then $C_2$ $\texttt{1}$ characters, then $C_3$ $\texttt{0}$ characters, and so on. For example, the array $C = [2, 3, 4, 3]$ corresponds with the binary string $\texttt{001110000111}$.

You are allowed to modify $S$ by swapping elements of $C$. More specifically, you are allowed to swap $C_i$ and $C_j$ *as long as* $C_i$ and $C_j$ both encodes blocks of the same character. For example, from $C = [2, 3, 4, 3]$, you can swap $C_1$ and $C_3$ because both of them encode blocks of $\texttt{0}$'s, turning $C$ to $[4, 3, 2, 3]$ and $S$ to $\texttt{000011100111}$. However, you cannot swap $C_1$ and $C_2$ because $C_1$ encodes a block of $\texttt{0}$'s, while $C_2$ encodes a block of $\texttt{1}$s.

Perform the swapping operation in any way as many times as you want (including zero times) so that the final string $S$ has as many $\texttt{01}$ subsequences as possible. As a reminder, a subsequence of a string is a sequence that can be derived by deleting zero or more characters without changing the order of the remaining characters.

You need to find any optimal final array $C$, for which the number of $\texttt{01}$ subsequence will be the largest possible.

**Input**

- The first line contains $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer $N$ - the size of the array $C$.
- The second line of each test case contains $N$ integers $C_1, C_2, \dots, C_N$ - the $\texttt{01}$-compression representation of $S$.

**Output**

For each test case, output two lines: the first line contains $N$ integers representing the optimal array $C$, and the second line contains the maximum number of $\texttt{01}$ subsequences.

## Constraints

- $ 1 \leq T \leq 1000 $
- $ 1 \leq N \leq 100 $
- $ 1 \leq  C_i \leq 1000 $

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
1
4
2 3 4 3
```

**Sample output**

```
4 3 2 3
30
```

<details><summary>Explanation</summary>

- **Test case $1$:** $C = [2, 3, 4, 3]$, which means $S$ corresponds to $\texttt{001110000111}$. The optimal list of operations is to only swap $C_1$ and $C_3$, resulting in $C = [4, 3, 2, 3]$ and $S = $ $\texttt{000011100111}$, which has $30$ subsequences of $\texttt{01}$.

</details>

## Approach

A zero block contributes its size times the total length of all later one blocks. Those suffix totals decrease from left to right, so larger zero blocks belong earlier. Equivalently, a one block contributes its size times all preceding zeros; those prefix totals increase, so larger one blocks belong later.

Sorting zero blocks descending and one blocks ascending satisfies both exchange arguments simultaneously. Interleave them, then accumulate the score with a running zero count.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        c = [int(next(tokens)) for _ in range(n)]
        c[::2] = sorted(c[::2], reverse=True)
        c[1::2] = sorted(c[1::2])
        zeros = answer = 0
        for i, value in enumerate(c):
            if i%2 == 0:
                zeros += value
            else:
                answer += zeros*value
        out.append(' '.join(map(str,c)))
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N\log N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Swaps are allowed only within the same parity of block indices.
- A final zero block contributes no pairs.
- Print both the optimal compression array and the count.

## Dry run

For `[2,3,4,3]`, sort zero blocks to `[4,2]`. Interleaving gives `[4,3,2,3]`; its score is `4*3+6*3=30`.

> CodeChef tags: `Algorithms`, `Constructive`

---

Same problem in rating order (#506 of 735): [../../by-rating/506-ZEROONE.md](../../by-rating/506-ZEROONE.md)
