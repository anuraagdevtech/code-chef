[&larr; 723. Smallest Difference](SMALLESTDIFF.md) &middot; [Index](../../README.md)

# 726. Adjacent Flips

> CodeChef problem code [`ADJFLIP`](https://www.codechef.com/problems/ADJFLIP) &middot; difficulty **2426** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Ones on even positions minus ones on odd positions never changes |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

You are given a *binary* string $S$ of length $N$.

You can perform the following operation on it:
- Choose an index $i$ ($1 \leq i \lt N$) such that $S_i = S_{i+1}$, and flip both $S_i$ and $S_{i+1}$.
Flipping $S_i$ means it becomes $1$ if it was originally $0$, and vice versa.

For example, if $S = \texttt{0101100}$, performing the operation with $i = 4$ would result in $S = \texttt{010\underline{00}00}$ and performing it with $i = 6$ would result in $S = \texttt{01011\underline{11}}$.

By performing this operation several (possibly, zero) times, is it possible to make $S$ contain only a single type of character (that is, $S$ should contain either all zeros or all ones)?

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the length of $S$.
    - The second line of each test case contains a binary string $S$.

**Output**

For each test case, output on a new line the answer: `Yes` if it is possible for $S$ to contain only zeros or only ones, and `No` otherwise.

Each letter of the output may be printed in either uppercase or lowercase, i.e, the strings `NO`, `No`, `nO`, and `no` will all be treated as equivalent.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 2\cdot 10^5$
- $S$ is a binary string, i.e, contains only the characters `0` and `1`.
- The sum of $N$ across all tests won't exceed $2\cdot 10^5$.

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
4
6
110110
7
0101010
6
101001
5
00000
```

**Sample output**

```
Yes
No
No
Yes
```

<details><summary>Explanation</summary>

**Test case $1$:** Perform moves as follows:
$\texttt{110110} \to \texttt{110\underline{00}0} \to \texttt{1100\underline{11}} \to \texttt{11\underline{11}11}$.
$S$ contains all ones now, as required.
It would also be acceptable to perform $\texttt{110110} \to \texttt{110\underline{00}0} \to \texttt{\underline{00}0000}$ and reach a state of all zeros.

**Test case $2$:** It's not possible to make a move at all, so the answer is `No`.

**Test case $3$:** It can be shown that no matter what, it's not possible to reach a state where all the characters are $0$ or all of them are $1$.

**Test case $4$:** The string already contains all zeros, no moves are necessary.

</details>

## Approach

An operation flips two equal neighbours, one on an even index and one on an odd index. `00 -> 11` adds a one on each parity and `11 -> 00` removes one from each, so

$$D = \#\{\text{ones on even indices}\} - \#\{\text{ones on odd indices}\}$$

is invariant.

It is also the only invariant. Complement every character on an odd index: an equal pair `00` or `11` becomes an unequal pair `01` or `10`, and flipping both characters of the original pair turns into swapping the two characters of the transformed pair. So in the transformed string the allowed moves are exactly "swap two adjacent different characters", which can rearrange the string arbitrarily while keeping its number of ones - and that number is $D$ plus a constant.

So the string can be made constant exactly when $D$ equals the value of $D$ for one of the two constant strings: 0 for all zeros; for all ones, 0 if $N$ is even and 1 if $N$ is odd (0-based indices).

## Solution (Python)

```python
import sys


def solve(tokens):
    n = int(next(tokens))
    bits = next(tokens)
    balance = sum((1 if i % 2 == 0 else -1 for i, char in enumerate(bits) if char == 49))
    return 'Yes' if balance == 0 or (n % 2 and balance == 1) else 'No'


if __name__ == "__main__":
    tokens = iter(sys.stdin.buffer.read().split())
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Already constant strings answer Yes.
- $N = 1$: always Yes.
- For even $N$ both targets require $D = 0$.
- A perfectly alternating string has no legal move at all, and its $D$ is far from the targets unless it is very short.

## Dry run

`S = 110110` (indices 0-5): ones on even indices 0 and 4, ones on odd indices 1 and 3, so $D = 0$ - Yes.

`S = 0101010`: all three ones are on odd indices, $D = -3$; the targets are 0 and 1 - No.

---

Same problem in rating order (#690 of 735): [../../by-rating/690-ADJFLIP.md](../../by-rating/690-ADJFLIP.md)
