[&larr; 691. Max Shift After XOR](691-MAXCYCSHIFT.md) &middot; [Index](README.md) &middot; [693. Good Sequence &rarr;](693-GSEQ.md)

# 692. Balanced Suffix

> [`BALSUFF`](https://www.codechef.com/problems/BALSUFF) &middot; difficulty **2447** &middot; time limit **2.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Build left to right, keeping the remaining multiset balanced |
| **CodeChef tags** | `Algorithms`, `Greedy` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(26 \cdot N)$ per test case |
| **Space** | $O(N)$ |

## Question

You're given a string $S$ of length $N$ and an integer $K$.

Let $C$ denote the **set** of all characters in $S$. The string $S$ is called *good* if, for **every** *suffix* of S:
- The difference between the frequencies of any two characters in $C$ does not exceed $K$.
In particular, if the set $C$ has a single element, the string $S$ is *good*.

Find whether there exists a rearrangement of $S$ which is *good*.
If multiple such rearrangements exist, print the **lexicographically smallest** rearrangement.
If no such rearrangement exists, print $-1$ instead.

Note that a suffix of a string is obtained by deleting some (possibly **zero**) characters from the beginning of the string. For example, the suffixes of $S = abca$ are $\{a, ca, bca, abca\}$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space-separated integers $N$ and $K$ — the length of the string and the positive integer as mentioned in the statement, respectively.
    - The next line consists of a string $S$ of length $N$ containing lowercase English alphabets only.

**Output**

For each test case, output on a new line the lexicographically smallest *good* rearrangement of $S$.

If no such rearrangement exists, print $-1$ instead.

## Constraints

- $1 \leq T \leq 2000$
- $1 \leq N \leq 10^5$
- $1 \leq K \leq N$
- $S$ consists of lowercase english alphabets only.
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

## Sample

**Sample input**

```
4
3 1
aaa
4 2
baba
4 1
babb
7 2
abcbcac
```

**Sample output**

```
aaa
aabb
-1
abcabcc
```

<details><summary>Explanation</summary>

**Test case $1$:** Since $C = \{a\}$, the string $S$ is *good*.

**Test case $2$:** The set $C = \{a, b\}$. Consider the rearrangement $aabb$. Let $f_a$ and $f_b$ denote the frequencies of $a$ and $b$ respectively:
- In suffix $b$, $f_b = 1$ and $f_a = 0$. Thus, $|f_b-f_a| = 1 \le K$.
- In suffix $bb$, $f_b = 2$ and $f_a = 0$. Thus, $|f_b-f_a| = 2 \le K$.
- In suffix $abb$, $f_b = 2$ and $f_a = 1$. Thus, $|f_b-f_a| = 1 \le K$.
- In suffix $aabb$, $f_b = 2$ and $f_a = 2$. Thus, $|f_b-f_a| = 0 \le K$.

Thus, the rearrangement $aabb$ is good. It is also the lexicographically smallest rearrangement possible of string $S$.

**Test case $3$:** It can be proven that there exists no rearrangement of $S$ which is *good*.

**Test case $4$:** The set $C = \{a, b, c\}$. Consider the rearrangement $abcabcc$. Let $f_a, f_b,$ and $f_c$ denote the frequencies of $a, b,$ and $c$ respectively:
- In suffix $c$, $f_a = 0, f_b = 0, $ and $f_c = 1$. Thus, $|f_b-f_a|, |f_c-f_b|,$ and $|f_a-f_c|$ are all less than or equal to $K = 2$.
- In suffix $cc$, $f_a = 0, f_b = 0, $ and $f_c = 2$. Thus, $|f_b-f_a|, |f_c-f_b|,$ and $|f_a-f_c|$ are all less than or equal to $K = 2$.
- In suffix $bcc$, $f_a = 0, f_b = 1, $ and $f_c = 2$. Thus, $|f_b-f_a|, |f_c-f_b|,$ and $|f_a-f_c|$ are all less than or equal to $K = 2$.
- In suffix $abcc$, $f_a = 1, f_b = 1, $ and $f_c = 2$. Thus, $|f_b-f_a|, |f_c-f_b|,$ and $|f_a-f_c|$ are all less than or equal to $K = 2$.
- In suffix $cabcc$, $f_a = 1, f_b = 1, $ and $f_c = 3$. Thus, $|f_b-f_a|, |f_c-f_b|,$ and $|f_a-f_c|$ are all less than or equal to $K = 2$.
- In suffix $bcabcc$, $f_a = 1, f_b = 2, $ and $f_c = 3$. Thus, $|f_b-f_a|, |f_c-f_b|,$ and $|f_a-f_c|$ are all less than or equal to $K = 2$.
- In suffix $abcabcc$, $f_a = 2, f_b = 2, $ and $f_c = 3$. Thus, $|f_b-f_a|, |f_c-f_b|,$ and $|f_a-f_c|$ are all less than or equal to $K = 2$.

Thus, the rearrangement $abcabcc$ is good. It is also the lexicographically smallest *good* rearrangement of string $S$.

</details>

## Approach

After a prefix has been written, what remains is exactly a suffix of the final string. So the string is good when, at every moment of the construction, the remaining counts of all characters of $C$ - including characters whose remaining count has dropped to 0 - differ by at most $K$.

The whole string is a suffix too, so if the initial counts are not within $K$ of each other the answer is $-1$.

Otherwise build greedily: at each step take the smallest character whose removal keeps the remaining multiset balanced. Removing one copy of $x$ only lowers the count of $x$, so the only thing that can break is the gap between the current maximum and the new count of $x$: the move is legal exactly when $\max - (\text{cnt}_x - 1) \le K$.

A legal move always exists - removing a character with the maximum count is always fine - so the greedy never gets stuck, and since any legal choice can be completed, taking the smallest legal character at each step gives the lexicographically smallest good string.

## Solution

```python
import sys
from collections import Counter


def solve(tokens):
    n, limit = (int(next(tokens)), int(next(tokens)))
    left = Counter(next(tokens).decode())
    chars = sorted(left)
    out = []
    if max(left.values()) - min(left.values()) > limit:
        return '-1'
    for _ in range(n):
        largest = max(left.values())
        for char in chars:
            if left[char] and largest - (left[char] - 1) <= limit:
                left[char] -= 1
                out.append(char)
                break
    return ''.join(out)


if __name__ == "__main__":
    tokens = iter(sys.stdin.buffer.read().split())
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- A single distinct character: the string itself.
- $K \ge$ the largest count: every arrangement is good, so the answer is the sorted string.
- Characters that have run out still count with frequency 0.
- The alphabet has at most 26 letters, so scanning it at every step is cheap.

## Dry run

`S = abcbcac`, `K = 2`. Counts `a:2 b:2 c:3`.

| step | remaining before | choice | reason |
|---:|---|---|---|
| 1 | 2 2 3 | a | $3 - 1 = 2 \le 2$ |
| 2 | 1 2 3 | b | `a` would give $3 - 0 = 3$; `b` gives $3 - 1 = 2$ |
| 3 | 1 1 3 | c | `a` and `b` would give 3; `c` gives $3 - 2 = 1$ |
| 4 | 1 1 2 | a | $2 - 0 = 2$ |
| 5 | 0 1 2 | b | $2 - 0 = 2$ |
| 6 | 0 0 2 | c | |
| 7 | 0 0 1 | c | |

Answer `abcabcc`.

---

Same problem grouped by topic: [../docs/greedy/BALSUFF.md](../docs/greedy/BALSUFF.md)
