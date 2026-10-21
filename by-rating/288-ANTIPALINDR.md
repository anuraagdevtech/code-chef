# 288. Anti Palindrome

> [`ANTIPALINDR`](https://www.codechef.com/problems/ANTIPALINDR) &middot; difficulty **1488** &middot; time limit **4.5s** &middot; 1400 to 1600 difficulty problems (Level 2)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Forcing a palindrome to be impossible |
| **CodeChef tags** | `Algorithms`, `Constructive`, `ad-hoc`, `Observation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

**Definitions:**

A string $T$ is called **semi-palindrome** if you can rearrange the characters of $T$ to make it into a [palindrome](https://en.wikipedia.org/wiki/Palindrome).\
For eg. if $T = aabb$, it isn't a palindrome as of now, but it can be rearranged to form $abba$, which is a palindrome. Thus, $T = aabb$ is a semi-palindrome.

An **anti-palindrome** is the opposite of a semi-palindrome. In particular, a string $T$ is called an anti-palindrome if it is not possible to rearrange the characters of $T$ to make it into a palindrome.\
For eg. if $T = abc$, there is no rearrangement of this string which makes it into a palindrome. Hence, $T = abc$ is an anti-palindrome.

---
Now on to the problem:

You are given a string $S = S_1S_2 \ldots S_N$ consisting of $N$ english lowercase letters.

Your aim is to convert $S$ into an anti-palindrome. For this, you are allowed to do the following operation as many times as you want (even 0 times) :
- Select an index $i$ $(1 \leq i \leq N)$ and change $S_i$ to any other english lowercase letter.

Find the minimum number of operations needed to make $S$ into an anti-palindrome.

**Note:** It can be proven that for the given constraints ($2 \leq N \leq 10^5$), it is always possible to make $S$ into an anti-palindrome using the operations.

**Input**

- The first line of input will contain a single integer $C$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$ — the length of the string $S$.
    - The next line contains the string $S$ of length $N$.

**Output**

For each test case, output the minimum number of operations needed to make $S$ into an anti-palindrome.

## Constraints

- $1 \leq C \leq 5 \cdot 10^5$
- $2 \leq N \leq 10^5$
- $S$ contains only english lowercase letters.
- The sum of $N$ over all testcases won't exceed $10^5$.

## Sample

**Sample input**

```
5
2
ab
2
aa
3
abc
3
aaa
3
abb
```

**Sample output**

```
0
1
0
2
1
```

<details><summary>Explanation</summary>

**Testcase 1:** The given string $ab$ is already an anti-palindrome, since there is no way to rearrange the letters to make it into a palindrome. So, we don't need to do any operations on it to make it an anti-palindrome. Hence the answer is $0$.

**Testcase 2:** The given string $aa$ is a palindrome, and so it is not an anti-palindrome. We can change it to $ab$ using $1$ operation, and it becomes an anti-palindrome. Hence the answer is $1$.

**Testcase 3:** The given string $abc$ is already an anti-palindrome, since there is no way to rearrange the letters to make it into a palindrome. So, we don't need to do any operations on it to make it an anti-palindrome. Hence the answer is $0$.

**Testcase 4:** The given string $aaa$ is a palindrome, and so it is not an anti-palindrome. We can change it to $abc$ using $2$ operations, and it becomes an anti-palindrome. There is no way to make it into an anti-palindrome using only 1 operation. Hence the answer is $2$.

**Testcase 5:** The given string $abb$ is a semi-palindrome, since it can be rearranged to form $bab$ which is a palindrome. So $abb$ is not an anti-palindrome. We can change it to $abc$ using $1$ operation, and it becomes an anti-palindrome. Hence the answer is $1$.

</details>

## Approach

A multiset rearranges into a palindrome exactly when at most one character has an odd count. So an **anti**-palindrome needs at least two odd counts — and since the counts sum to $N$, the number of odd counts $k$ has the same parity as $N$. The targets are therefore:

- $N$ even → need $k \geq 2$ (and $k$ is even, so $k = 0$ is the only failure)
- $N$ odd → need $k \geq 3$ (and $k$ is odd, so $k = 1$ is the only failure)

**$N$ even, $k = 0$.** One edit fixes it: take a character from some letter with a positive even count and write a letter not yet used. Both counts flip to odd, giving $k = 2$.

**$N$ odd, $k = 1$.** Here the answer depends on what else is present. An edit changes two counts, each flipping parity, so $k$ moves by $-2$, $0$ or $+2$ — and reaching $3$ needs a $+2$, which requires taking from a letter whose count is **even**. If some even-count letter exists (necessarily with count $\geq 2$), one edit does it.

But if the string is a **single repeated letter**, the only non-zero count is the odd one, and there is nothing even to draw from. The first edit merely moves the oddness around, leaving $k = 1$; a second then reaches $k = 3$. That is sample case 4, `aaa`, which costs $2$ — the case that defeats a naive "$\lceil (3-k)/2 \rceil$" formula.

The remaining samples cover the rest: `ab` and `abc` are already anti-palindromes at $k = 2$ and $k = 3$; `aa` is the even-$N$ repair at $1$; and `abb` has an even-count `b` to draw from, so also $1$.

## Solution

```python
import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    c = int(data[0])
    pos = 1
    out = []
    for _ in range(c):
        n = int(data[pos])
        counts = Counter(data[pos + 1])
        pos += 2
        odds = sum(1 for v in counts.values() if v % 2)
        if n % 2 == 0:
            # k is even, so only k == 0 fails, and one edit lifts it to 2.
            out.append("0" if odds >= 2 else "1")
        elif odds >= 3:
            out.append("0")
        elif len(counts) == 1:
            # Nothing with an even count to draw from, so it takes two edits.
            out.append("2")
        else:
            out.append("1")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/strings/ANTIPALINDR.md](../docs/strings/ANTIPALINDR.md)
