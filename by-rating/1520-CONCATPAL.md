# 1520 &middot; Concat Palindrome

> CodeChef problem code [`CONCATPAL`](https://www.codechef.com/problems/CONCATPAL) &middot; time limit **2.5s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topics used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Multiset containment forced by mirroring |
| **CodeChef tags** | `Algorithms`, `Observation` |
| **CodeChef category** | easy |
| **Time** | $O(N + M)$ per test case |
| **Space** | $O(1)$ — 26 counters |

Same write-up grouped by topic: [../docs/strings/CONCATPAL.md](../docs/strings/CONCATPAL.md)

## Question

Chef has two strings $A$ and $B$ of lengths $N$ and $M$ respectively.

Chef can rearrange both strings in any way he wants. Let the rearranged string of $A$ be $A'$ and the rearranged string of $B$ be $B'$.

Determine whether we can construct rearrangements $A'$ and $B'$ such that $(A' + B')$ is a palindrome.

Here $+$ denotes the concatenation operation. For e.g. ${abc} + {xyz} = {abcxyz}$.

Note: A string is called palindrome if it reads the same backwards and forwards, for e.g. $\texttt{noon}$ and $\texttt{level}$ are palindromic strings.

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains two integers $N$ and $M$ — the length of the strings $A$ and $B$ respectively.
- The second line of each test case contains a string $A$ of length $N$ containing lowercase Latin letters only.
- The third line of each test case contains a string $B$ of length $M$ containing lowercase Latin letters only.

**Output**

For each test case, output `YES` if we can rearrange $A$ and $B$ such that $(A' + B')$ becomes a palindrome. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N, M \leq 2 \cdot 10^5$
- $A$ and $B$ consist of lowercase Latin letters only.
- The sum of $N + M$ over all test cases does not exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
4
5 2
abcdd
ac
3 3
abc
xyz
2 4
aa
aaaa
1 3
a
aax
```

**Sample output**

```
YES
NO
YES
NO
```

<details><summary>Explanation</summary>

**Test case $1$:** We can rearrange $A$ to $A' = acdbd$ and $B$ to $B' = ca$. So $A' + B' = acdbdca$ which is palindromic.

**Test case $2$:** We can not rearrange $A$ and $B$ such that $A' + B'$ is palindromic.

**Test case $3$:** For $A' = aa$ and $B' = aaaa$, $A' + B' = aaaaaa$ is palindromic.

</details>

## Approach

Both halves may be permuted freely, but a character cannot move **between** them: the first $N$ positions hold exactly the letters of $A$ and the last $M$ hold those of $B$.

Suppose $N \leq M$. In a palindrome of length $N + M$, position $i$ mirrors to position $N + M + 1 - i$. For every $i \leq N$ that mirror index is at least $M + 1 > N$, so **every position of $A$ mirrors into $B$**. Each letter of $A$ therefore needs a matching partner inside $B$, which means

$$\text{multiset}(A) \subseteq \text{multiset}(B)$$

What is left of $B$ after removing one copy of each letter of $A$ sits in the centre of the palindrome and mirrors onto itself — so that remainder must itself be rearrangeable into a palindrome, i.e. have **at most one odd count**.

Those two conditions together are exactly right, and symmetric: if $M < N$ simply swap the roles.

The subset test is the part that is easy to miss, and sample case 2 shows why it matters — `abc` and `xyz` have the same length and a combined multiset with six odd counts, but even a shared-count check would not capture that *none* of $A$'s letters can find a partner.

Sample case 4 is the second condition biting: $A = $ `a` fits inside $B = $ `aax`, but the remainder `ax` has two odd counts and cannot be a palindromic centre.

Sample case 3 passes both: `aa` sits inside `aaaa`, leaving `aa`, which is already a palindrome.

Counting with two 26-element arrays keeps this linear, which matters at $\sum (N+M) = 2\times10^5$.

## Solution (Python)

```python
import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, m = int(data[pos]), int(data[pos + 1])
        a, b = data[pos + 2], data[pos + 3]
        pos += 4
        if n > m:
            a, b = b, a
        ca, cb = Counter(a), Counter(b)
        # Every position of the shorter side mirrors into the longer one.
        if any(cb[ch] < cnt for ch, cnt in ca.items()):
            out.append("NO")
            continue
        # What is left of the longer side forms the palindromic centre.
        rest = cb - ca
        out.append("YES" if sum(1 for v in rest.values() if v % 2) <= 1 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N + M)$ per test case
- **Space:** $O(1)$ — 26 counters
