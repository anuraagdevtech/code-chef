[&larr; 488. Flip the Prefix](PREFIXFLIP.md) &middot; [Index](../../README.md) &middot; [508. Art of Balance &rarr;](ARTBALAN.md)

# 501. Palpal Strings

> CodeChef problem code [`PALPALS`](https://www.codechef.com/problems/PALPALS) &middot; difficulty **1776** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Pair supply must cover all odd-frequency centres |
| **Time** | $O(|S|)$ per test case |
| **Space** | $O(1)$ for the fixed alphabet |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

A string is called a *Palpal string* if it can be divided into contiguous substrings such that:
- Each character of the whole string belongs to exactly one substring.
- Each of these substrings is a palindrome with length greater than $1$.

For example, "abbbaddzcz" is a Palpal string, since it can be divided into "abbba", "dd" and "zcz".

You are given a string $s$. You may rearrange the characters of this string in any way you choose. Find out if it is possible to rearrange them in such a way that you obtain a Palpal string.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single string $s$.

**Output**
For each test case, print a single line containing the string `"YES"` if the characters of $s$ can be rearranged to form a Palpal string or `"NO"` if it is impossible (without quotes).

You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

**Constraints**
- $1 \le T \le 10^5$
- $1 \le |s| \le 100$
- $s$ contains only lowercase English letters
- the sum of $|s|$ over all test cases does not exceed $10^6$

**Subtasks**
**Subtask #1 (100 points):** original constraints

## Constraints

- $1 \le T \le 10^5$
- $1 \le |s| \le 100$
- $s$ contains only lowercase English letters
- the sum of $|s|$ over all test cases does not exceed $10^6$

## Sample

**Sample input**

```
3
acbbbadzdz
abcd
xyxyxy
```

**Sample output**

```
YES
NO
YES
```

<details><summary>Explanation</summary>

**Example case 1:** The string "acbbbadzdz" can be rearranged to "abbbaddzcz", which is the Palpal string mentioned above.

**Example case 2:** It can be shown that "abcd" cannot be rearranged to form a Palpal string.

**Example case 3:** The string "xyxyxy" is already a Palpal string, since it can divided into "xyx" and "yxy".

</details>

## Approach

Each palindrome of length at least two consumes at least one equal-letter pair and can contain at most one unpaired centre. Let $p=\sum\lfloor f_c/2\rfloor$ and $o$ be the number of odd frequencies.

Every unpaired character needs its own pair-supported palindrome, so $p\ge o$ is necessary. It is sufficient: form a length-three palindrome around each odd character using one pair, then use any remaining pairs as length-two palindromes. If $o=0$, the nonempty input must still contain at least one pair.

## Solution (Python)

```python
import sys
from collections import Counter


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        s = next(tokens)
        f = Counter(s)
        pairs = sum(v//2 for v in f.values())
        odd = sum(v%2 for v in f.values())
        out.append('YES' if pairs >= max(1, odd) else 'NO')
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(|S|)$ per test case
- **Space:** $O(1)$ for the fixed alphabet
- Auxiliary space excludes the buffered input and output.

## Edge cases

- A single character cannot form a valid part.
- Even frequencies can always be divided into pairs.
- Odd centres may be surrounded by a different letter.

## Dry run

For `xyxyxy`, frequencies are three and three: two pairs and two odd centres. They form `xyx` and `yxy`, so the answer is `YES`.

> CodeChef tags: `Data Structures`, `Algorithms`

---

Same problem in rating order (#502 of 735): [../../by-rating/502-PALPALS.md](../../by-rating/502-PALPALS.md)
