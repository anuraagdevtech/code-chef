# 1159 &middot; Lapindromes

> CodeChef problem code [`LAPIN`](https://www.codechef.com/problems/LAPIN) &middot; time limit **1s** &middot; Level up from 1* to 2* (Level 2)

## Topics used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Comparing character frequencies |
| **CodeChef tags** | `Data Structures`, `Arrays`, `Frequency Arrays`, `Maps`, `Hashmaps` |
| **CodeChef category** | hard |
| **Time** | $O(|S|)$ per test case |
| **Space** | $O(1)$ — at most 26 counters |

Same write-up grouped by topic: [../docs/strings/LAPIN.md](../docs/strings/LAPIN.md)

## Question

*Lapindrome* is defined as a string which when split in the middle, gives two halves having the same characters and same frequency of each character. If there are odd number of characters in the string, we ignore the middle character and check for lapindrome. For example ***gaga*** is a lapindrome, since the two halves ***ga*** and ***ga*** have the same characters with same frequency. Also, ***abccab***, ***rotor*** and ***xyzxy*** are a few examples of lapindromes. Note that ***abbaab*** is NOT a lapindrome. The two halves contain the same characters but their frequencies do not match.
 Your task is simple. Given a string, you need to tell if it is a lapindrome.

**Input:**

First line of input contains a single integer **T**, the number of test cases.

Each test is a single line containing a string **S** composed of only lowercase English alphabet.

**Output:**

For each test case, output on a separate line: "YES" if the string is a lapindrome and "NO" if it is not.

**Constraints:**

- 1 ≤ **T** ≤ 100

- 2 ≤ |**S**| ≤ 1000, where |**S**| denotes the length of **S**

## Constraints

- 1 ≤ T ≤ 100
- 2 ≤ |S| ≤ 1000, where |S| denotes the length of S

## Sample

**Sample input**

```
6
gaga
abcde
rotor
xyzxy
abbaab
ababc
```

**Sample output**

```
YES
NO
YES
YES
NO
NO
```

## Approach

Split the string at its midpoint and ask whether the two halves use **the same characters with the same multiplicities**. That is a multiset comparison, which `collections.Counter` performs directly:

```python
Counter(s[:h]) == Counter(s[len(s) - h:])
```

Counting is essential, not optional. Comparing `set(left) == set(right)` checks only which letters appear, ignoring how often — and the statement calls that out explicitly with `abbaab`, whose halves `abb` and `aab` share the same letters in different quantities. That is sample case 5, and it is the whole point of the problem.

Note this is **not** a palindrome test either. `gaga` is a lapindrome but reads differently backwards, while `rotor` happens to be both. Order within each half is irrelevant.

For odd lengths the middle character is discarded. Taking the left half as `s[:n//2]` and the right as `s[n - n//2:]` handles both parities with the same expression: for even $n$ the two slices meet exactly, and for odd $n$ they skip the single middle character. Sample cases 3 and 4, `rotor` and `xyzxy`, both rely on that.

Sample case 6, `ababc`, has halves `ab` and `bc` — same length, different contents — and fails.

With $|S| \leq 1000$ the linear pass is trivial; the counter holds at most 26 entries, so the space is effectively constant.

## Solution (Python)

```python
import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s = data[1 + i]
        h = len(s) // 2
        # s[n-h:] skips the middle character when the length is odd.
        same = Counter(s[:h]) == Counter(s[len(s) - h:])
        out.append("YES" if same else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(|S|)$ per test case
- **Space:** $O(1)$ — at most 26 counters
