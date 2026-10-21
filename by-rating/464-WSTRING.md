# 464. W String

> [`WSTRING`](https://www.codechef.com/problems/WSTRING) &middot; difficulty **1809** &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Per-letter counts over hash-delimited blocks |
| **CodeChef tags** | `Algorithms`, `Dynamic Programming` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(|S| + 26 h)$ per test case, where $h$ is the number of '#' |
| **Space** | $O(|S|)$ |

## Question

Kira likes to play with strings very much. Moreover he likes the shape of 'W' very much. He takes a string and try to make a 'W' shape out of it such that each angular point is a '#' character and each sides has same characters. He calls them *W strings*.

For example, the *W string* can be formed from "aaaaa#bb#cc#dddd" such as:

```
a
     a             d
      a     #     d
       a   b c   d
        a b   c d
         #     #
```

He also call the strings which can generate a 'W' shape (satisfying the above conditions) *W strings*.

More formally, a string **S** is a *W string* if and only if it satisfies the following conditions (some terms and notations are explained in **Note**, please see it if you cannot understand):

- The string **S** contains **exactly** **3** '#' characters. Let the indexes of all '#' be **P_1 < P_2 < P_3** (indexes are **0**-origin).

- Each substring of **S[0, P_1−1], S[P_1+1, P_2−1], S[P_2+1, P_3−1], S[P_3+1, |S|−1]** contains exactly one kind of characters, where **S[a, b]** denotes the non-empty substring from **a+1**^th character to **b+1**^th character, and **|S|** denotes the length of string **S** (See **Note** for details).

Now, his friend Ryuk gives him a string **S** and asks him to find the length of the longest *W string* which is a subsequence of **S**, with only one condition that there must not be any '#' symbols between the positions of the first and the second '#' symbol he chooses, nor between the second and the third (here the "positions" we are looking at are in **S**), i.e. suppose the index of the '#'s he chooses to make the *W string* are **P_1, P_2, P_3** (in increasing order) in the original string **S**, then there must be no index **i** such that **S[i]** = '#' where **P_1 < i < P_2 or P_2 < i < P_3**.

Help Kira and he won't write your name in the **Death Note**.

**Note**:

For a given string **S**, let **S[k]** denote the **k+1**^th character of string **S**, and let the index of the character **S[k]** be **k**. Let **|S|** denote the length of the string **S**. And a substring of a string **S** is a string **S[a, b] = S[a] S[a+1] ... S[b]**, where **0 ≤ a ≤ b < |S|**. And a subsequence of a string **S** is a string **S[i_0] S[i_1] ... S[i_n−1]**, where **0 ≤ i_0 < i_1 < ... < i_n−1 < |S|**.

For example, let **S** be the string "kira", then **S[0]** = 'k', **S[1]** = 'i', **S[3]** = 'a', and **|S| = 4**. All of **S[0, 2]** = "kir", **S[1, 1]** = "i", and **S[0, 3]** = "kira" are substrings of **S**, but "ik", "kr", and "arik" are not. All of "k", "kr", "kira", "kia" are subsequences of **S**, but "ik", "kk" are not.

From the above definition of *W string*, for example, "a#b#c#d", "aaa#yyy#aaa#yy", and "o#oo#ooo#oooo" are *W string*, but "a#b#c#d#e", "#a#a#a", and "aa##a#a" are not.

**Input**

First line of input contains an integer **T**, denoting the number of test cases. Then **T** lines follow. Each line contains a string **S**.

**Output**

Output an integer, denoting the length of the longest *W string* as explained before. If **S** has no *W string* as its subsequence, then output **0**.

**Constraints**

- **1 ≤ T ≤ 100 **

- **1 ≤ |S| ≤ 10000 (10^4)**

- **S** contains no characters other than lower English characters ('a' to 'z') and '#' (without quotes)

## Constraints

- 1 ≤ T ≤ 100
- 1 ≤ |S| ≤ 10000 (10^4)
- S contains no characters other than lower English characters ('a' to 'z') and '#' (without quotes)

## Sample

**Sample input**

```
3
aaaaa#bb#cc#dddd
acb#aab#bab#accba
abc#dda#bb#bb#aca
```

**Sample output**

```
16
10
11
```

<details><summary>Explanation</summary>

In the first case: the whole string forms a *W String*.

In the second case: acb#aab#bab#accba, the longest *W string* is ac**b#aa**b**#b**a**b#a**ccb**a**

In the third case: abc#dda#bb#bb#aca, note that even though **a**bc**#dd**a**#bb**#**bb#a**c**a** (boldened characters form the subsequence) is a *W string* of length **12**, it violates Ryuk's condition that there should not be any #'s inbetween the **3** chosen # positions. One correct string of length **11** is **a**bc#dd**a#bb#bb#a**c**a**

</details>

## Approach

The extra condition — no '#' of $S$ may lie between the first and second chosen '#', nor between the second and third — is the whole key. It forces the three chosen '#' to be **consecutive among the '#' of $S$**. So if the '#' sit at $h_0 < h_1 < \cdots < h_{k-1}$, the only candidates are the $k-2$ windows $(h_t, h_{t+1}, h_{t+2})$.

With the window fixed, the four sides are independent, since each draws from a disjoint stretch of $S$ and must consist of one repeated character. The best a stretch can give is simply the count of its most frequent letter, so

$$\text{length} = 3 + \mathrm{pre}[t] + \mathrm{gap}[t] + \mathrm{gap}[t+1] + \mathrm{suf}[t+2]$$

where $\mathrm{gap}[i]$ is that maximum over the open interval $(h_i, h_{i+1})$, and $\mathrm{pre}[t]$, $\mathrm{suf}[t]$ are the same over $S[0, h_t)$ and $S(h_t, |S|)$. All four must be non-zero, since every side of the W must be non-empty.

Each quantity is a prefix/suffix tally: sweep left to right keeping 26 running counts and snapshot the maximum at each '#' for $\mathrm{pre}$, sweep right to left for $\mathrm{suf}$, and tally each inter-'#' stretch once for $\mathrm{gap}$. Total work is linear plus $26$ per '#', so no per-window scanning. Note the two middle sides contain no '#' by construction, while the outer stretches may — those are simply ignored, as the sides must be letters.

The third sample is the one that needs the window search: `abc#dda#bb#bb#aca` has four '#', and the later window scores $3 + 2 + 2 + 2 + 2 = 11$ against the earlier window's $10$, because shifting right turns the one-letter prefix `abc` into `abc#dda` with its two `d`s.

## Solution

```python
import sys

HASH = 0x23
A = 0x61


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for s in data[1:1 + t]:
        n = len(s)
        hs = [i for i, c in enumerate(s) if c == HASH]
        k = len(hs)
        if k < 3:
            out.append("0")
            continue
        # Best single letter in S[0, h_t) and in S(h_t, n), per '#'.
        counts = [0] * 26
        pre = []
        at = 0
        for i in range(n):
            if s[i] == HASH:
                pre.append(max(counts))
                at += 1
            else:
                counts[s[i] - A] += 1
        counts = [0] * 26
        suf = [0] * k
        at = k - 1
        for i in range(n - 1, -1, -1):
            if s[i] == HASH:
                suf[at] = max(counts)
                at -= 1
            else:
                counts[s[i] - A] += 1
        # Best single letter strictly between consecutive '#'.
        gap = []
        for i in range(k - 1):
            counts = [0] * 26
            for j in range(hs[i] + 1, hs[i + 1]):
                counts[s[j] - A] += 1
            gap.append(max(counts))

        best = 0
        for i in range(k - 2):
            sides = (pre[i], gap[i], gap[i + 1], suf[i + 2])
            if 0 in sides:            # every arm of the W must be non-empty
                continue
            best = max(best, 3 + sum(sides))
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/prefix-sums/WSTRING.md](../docs/prefix-sums/WSTRING.md)
