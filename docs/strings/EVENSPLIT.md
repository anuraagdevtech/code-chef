[&larr; 205. Lucky Four](LUCKFOUR.md) &middot; [Index](../../README.md) &middot; [234. Reversing directions &rarr;](DIRECTI.md)

# 216. Even Splits

> CodeChef problem code [`EVENSPLIT`](https://www.codechef.com/problems/EVENSPLIT) &middot; difficulty **1282** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Which orderings are reachable |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

You are given a binary string $S$ of length $N$. You can perform the following operation on it:
- Pick any non-empty even-length [subsequence](https://en.wikipedia.org/wiki/Subsequence) of the string.
- Suppose the subsequence has length $2k$. Then, move the first $k$ characters to the beginning of $S$ and the other $k$ to the end of $S$ (without changing their order).

For example, suppose $S = 01100101110$. Here are some moves you can make (the chosen subsequence is marked in red):
- $0\textcolor{red}{1}10\textcolor{red}{0}101110 \to \textcolor{red}{1}010101110\textcolor{red}{0}$
- $01\textcolor{red}{10}01\textcolor{red}{0}1\textcolor{red}{1}10 \to \textcolor{red}{10}0101110\textcolor{red}{01}$
- $011\textcolor{red}{00101110} \to \textcolor{red}{0010}011\textcolor{red}{1110}$

What is the lexicographically smallest string that can be obtained after performing this operation several (possibly, zero) times?

**Note**: A binary string $A$ is said to be lexicographically smaller than another binary string $B$ of the same length if there exists an index $i$ such that:
- $A_1 = B_1, A_2 = B_2, \ldots, A_{i-1} = B_{i-1}$
- $A_i = 0$ and $B_i = 1$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases. The description of the test cases follows.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$, the length of string $S$.
    - The second line contains a binary string of length $N$.

**Output**

For each testcase, output a single line containing the lexicographically shortest binary string that can be obtained by performing the given operation several times.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $S$ is a binary string, i.e, contains only the characters $0$ and $1$.
- The sum of $N$ across all test cases won't exceed $2\cdot 10^5$.

## Sample

**Sample input**

```
4
2
10
4
1001
5
11111
7
0010100
```

**Sample output**

```
10
0011
11111
0000011
```

<details><summary>Explanation</summary>

**Test case $1$:** There's only one move possible, and it gives back the original string when made. So, $S$ cannot be changed, and the answer is $10$.

**Test case $2$:** Make the following moves:
- $1\textcolor{red}{0}0\textcolor{red}{1} \to \textcolor{red}{0}10\textcolor{red}{1}$
- $\textcolor{red}{01}01 \to \textcolor{red}{0}01\textcolor{red}{1}$

This is the lexicographically smallest string.

**Test case $3$:** Performing any move doesn't change the string.

**Test case $4$:** Make the move $\textcolor{red}{001}0\textcolor{red}{1}00 \to \textcolor{red}{00}000\textcolor{red}{11}$.

</details>

## Approach

The operation never changes **which** characters the string contains, only their order — so the count of `0`s and `1`s is invariant. The lexicographically smallest arrangement of a fixed multiset of bits is all the `0`s followed by all the `1`s, so the sorted string is the obvious target.

For $N \geq 3$ that target is reachable. The move is flexible enough to shuffle freely: choosing a subsequence of length $2k$ sends its first half to the front and its second half to the back, and repeating lets any character be driven to either end. For instance $\texttt{110} \to \texttt{101} \to \texttt{011}$ reaches the sorted form in two moves, and $\texttt{100} \to \texttt{010} \to \texttt{001}$ does the same.

**The exception is $N = 2$.** There the only non-empty even-length subsequence is the whole string, with $k = 1$: the first character moves to the front and the second to the end, leaving nothing in the middle. That is the identity, so a two-character string cannot be changed at all. Sample case 1 is precisely this — `10` stays `10`, even though `01` is smaller.

$N = 1$ is likewise frozen, having no even-length subsequence at all, but there the string is already sorted so it makes no difference.

So the rule is: output $S$ unchanged when $N \leq 2$, and the sorted string otherwise.

Sorting a binary string is just counting — emit $c_0$ zeros then $c_1$ ones — which is $O(N)$ and avoids a comparison sort entirely. With the sum of $N$ at $2 \times 10^5$ and $T$ up to $10^5$, that and bulk I/O are what keep this comfortable.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        s = data[pos + 1]
        pos += 2
        if n <= 2:
            # The only even-length subsequence is the whole string, and the
            # move is then the identity, so nothing can be rearranged.
            out.append(s.decode())
        else:
            zeros = s.count(b"0")
            out.append("0" * zeros + "1" * (n - zeros))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **$N = 2$ is a genuine exception, not an optimisation.** The only non-empty even-length subsequence is the whole string, and with $k = 1$ the move sends the first character to the front and the second to the end — the identity. So `10` stays `10` and must *not* become `01`. The first sample row exists to catch exactly this.
- **$N = 1$**: no even-length subsequence exists at all, so no move is possible and the string is returned unchanged.
- **$N \geq 3$ is fully sortable.** For `110`, one move gives `101` and a second gives `011`, and the same two-step pattern generalises — which is why every string of length $3$ or more can be fully sorted.
- **An already-sorted string** (the third row, all ones) comes back unchanged, and the count-and-rebuild path produces it correctly without detecting the case.
- **All characters identical**: every move is a no-op, as the statement's third explanation notes.
- **Sum of $N \leq 2 \cdot 10^5$**: counting the zeros and concatenating two runs is $O(N)$, cheaper than sorting the characters.

## Dry run

| $N$ | $S$ | zeros | $N \leq 2$? | output |
|---:|---|---:|:---:|---|
| 2 | `10` | 1 | **yes** | `10` (unchanged) |
| 4 | `1001` | 2 | no | `0011` |
| 5 | `11111` | 0 | no | `11111` |
| 7 | `0010100` | 5 | no | `0000011` |

Row 1 would be `01` under the general rule, which is why the length is checked first.

---

Same problem in rating order (#197 of 486): [../../by-rating/197-EVENSPLIT.md](../../by-rating/197-EVENSPLIT.md)
