[&larr; 644. Angry Cyborg](AGCY.md) &middot; [Index](../../README.md) &middot; [670. Cherry and Bits &rarr;](CENS20A.md)

# 668. Increase 2 consecutive characters

> CodeChef problem code [`CCD`](https://www.codechef.com/problems/CCD) &middot; difficulty **2171** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | The alternating sum of differences is the only invariant |
| **Time** | $O(N + Q)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

Chef has $2$ strings $A$ and $B$ of equal length $N$. Both strings contain lowercase english alphabets only.

Chef can perform several moves on string $A$. In one move, Chef has to:
- Select an index $i \space (1 \leq i \leq N-1)$.
- Replace $A[i]$ with $(A[i]+1)$.
- Replace $A[i+1]$ with $(A[i+1]+1)$.

For example, if $A = \texttt{abcze}$, a valid move would be to select index $3$. This way the string becomes $\texttt{abdae}$ after performing the move. Note that the value at an index is cyclically incremented. This means that, $\texttt{a} \rightarrow \texttt{b}$, $\texttt{b} \rightarrow \texttt{c}$, $\ldots$, $\texttt{z} \rightarrow \texttt{a}$.

Chef has been asked to answer $Q$ queries. Each query is of the form:
- $L$ $R$: Given $1 \leq L \leq R \leq N$, Chef wants to know if it is possible to convert the substring $A[L, R]$ to $B[L, R]$ by performing the above mentioned move **any** number of times.

For each query, output in a single line $\texttt{Yes}$, if the conversion is possible using any number of moves. Otherwise, print $\texttt{No}$.

**NOTE:** Queries are **independent**. Thus, the original strings $A$ and $B$ would be retained to process next query. For each query solve for substrings $A[L,R]$ and $B[L,R]$ only. So valid values for $i$ will be among $L$ to $R - 1$ only.

**Input**

- The first line will contain $T$ - the number of test cases. Then the test cases follow.
- First line of each test case contains two integers $N, Q$.
- Second line of each test case contains string $A$.
- Third line of each test case contains string $B$.
- $Q$ lines follow, where the $i^{th}$ line contains two integers $L_i R_i$ - the $i^{th}$ query.

**Output**

Output $Q$ lines, where the $i^{th}$ line contains the answer to the $i^{th}$ query. The answer is $\texttt{Yes}$, if the conversion is possible using any number of moves. Otherwise, the answer is $\texttt{No}$.

You may print each character of the string in uppercase or lowercase (for example, the strings $\texttt{yEs}$, $\texttt{yes}$, $\texttt{Yes}$ and $\texttt{YES}$ will all be treated as identical).

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- $1 \leq Q \leq 2\cdot 10^5$
- $1 \leq L \le R \le N$
- Sum of $N$ over all test cases does not exceed $2 \cdot 10^5$.
- Sum of $Q$ over all test cases does not exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
1
5 3
abcdz
nbhea
2 2
1 3
4 5
```

**Sample output**

```
Yes
No
Yes
```

<details><summary>Explanation</summary>

**Test Case $1$:**
- For the first query, the substring $A[2,2] = \texttt{b}$ is already same as $B[2,2] = \texttt{b}$. Thus, the answer is $\texttt{Yes}$.
- For the second query, it can be proven that the substring $A[1,3]$ can never be made equal to $B[1,3]$ using any number of moves.
- For the third query, the substring $A[4,5] = \texttt{dz}$ and $B[4,5] = \texttt{ea}$. Applying the move on index $4$, we get $A[4] = \texttt{e}$ and $A[5] = \texttt{a}$. Hence, after one move, $A[4,5] = B[4,5]$. Thus, the answer is $\texttt{Yes}$ in this case.

</details>

## Approach

Let $d_i = (B_i - A_i) \bmod 26$ be how much position $i$ still has to be increased. A move adds 1 to two adjacent positions, so it changes $d_i$ and $d_{i+1}$ together and leaves the alternating sum $d_L - d_{L+1} + d_{L+2} - \dots$ unchanged modulo 26. For a substring to become equal to its target this alternating sum must therefore be 0.

The condition is also sufficient: process the substring from the left, applying the move at $(i, i+1)$ exactly $d_i$ times to fix position $i$. Everything is forced, and what remains at the last position is, up to sign, the alternating sum - zero by assumption.

Store prefix sums of $\pm d_i$ with the sign given by the parity of the index. A query $[L, R]$ is Yes exactly when the two prefix values at $R$ and $L - 1$ agree modulo 26; a global sign flip does not affect whether the sum is zero.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        q = int(next(tokens))
        source = next(tokens)
        target = next(tokens)
        prefix = [0]
        for i in range(n):
            prefix.append((prefix[-1] + (target[i] - source[i]) * (1 if i % 2 == 0 else -1)) % 26)
        for _ in range(q):
            left = int(next(tokens))
            right = int(next(tokens))
            out.append('YES' if prefix[right] == prefix[left - 1] else 'NO')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N + Q)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- A single-character query has no move available: the characters must already match.
- Increments are cyclic, so all arithmetic is modulo 26.
- Moves must stay inside the queried substring, which the argument respects.
- The strings are read as bytes; only differences are used.

## Dry run

`A = abcdz`, `B = nbhea`. Differences $d$: `13 0 5 1 1` (the last is `z -> a`).

- `2 2`: $d_2 = 0$ - Yes.
- `1 3`: $13 - 0 + 5 = 18 \not\equiv 0$ - No.
- `4 5`: $1 - 1 = 0$ - Yes (one move on positions 4, 5).

> CodeChef tags: `Algorithms`, `Queries`

---

Same problem in rating order (#628 of 735): [../../by-rating/628-CCD.md](../../by-rating/628-CCD.md)
