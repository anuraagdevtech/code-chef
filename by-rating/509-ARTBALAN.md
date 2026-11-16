[&larr; 508. Total Diamonds](508-VK18.md) &middot; [Index](README.md) &middot; [510. Strange Function &rarr;](510-ABX01.md)

# 509. Art of Balance

> [`ARTBALAN`](https://www.codechef.com/problems/ARTBALAN) &middot; difficulty **1788** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Enumerate feasible alphabet sizes and retain most occurrences |
| **CodeChef tags** | `Data Structures`, `Mathematics`, `Number Theory`, `Integer Factorisation`, `String`, `Divisors` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(|S|+26^2)$ per test case |
| **Space** | $O(26)$ |

## Question

"Everything in the universe is balanced. Every disappointment you face in life will be balanced by something good for you! Keep going, never give up."

Let's call a string *balanced* if all characters that occur in this string occur in it the same number of times.

You are given a string $S$; this string may only contain uppercase English letters. You may perform the following operation any number of times (including zero): choose one letter in $S$ and replace it by another uppercase English letter. Note that even if the replaced letter occurs in $S$ multiple times, only the chosen occurrence of this letter is replaced.

Find the minimum number of operations required to convert the given string to a balanced string.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single string $S$.

**Output**
For each test case, print a single line containing one integer ― the minimum number of operations.

**Constraints**
- $1 \le T \le 10,000$
- $1 \le |S| \le 1,000,000$
- the sum of $|S|$ over all test cases does not exceed $5,000,000$
- $S$ contains only uppercase English letters

**Subtasks**
**Subtask #1 (20 points):**
- $T \le 10$
- $|S| \le 18$

**Subtask #2 (80 points):** original constraints

## Constraints

- $1 \le T \le 10,000$
- $1 \le |S| \le 1,000,000$
- the sum of $|S|$ over all test cases does not exceed $5,000,000$
- $S$ contains only uppercase English letters

## Sample

**Sample input**

```
2
ABCB
BBC
```

**Sample output**

```
1
1
```

<details><summary>Explanation</summary>

**Example case 1:** We can change 'C' to 'A'. The resulting string is "ABAB", which is a balanced string, since the number of occurrences of 'A' is equal to the number of occurrences of 'B'.

**Example case 2:** We can change 'C' to 'B' to make the string "BBB", which is a balanced string.

</details>

## Approach

If exactly $d$ letters appear, each must occur $|S|/d$ times, so $d$ divides $|S|$ and $d\le26$. For a fixed target count $f$, choosing a letter with initial frequency $c$ preserves $\min(c,f)$ characters. The largest frequencies maximise this total.

Pad to 26 frequencies, sort descending, and try all valid $d$. The answer is the length minus the largest number of preservable characters.

## Solution

```python
import sys
from collections import Counter


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        s = next(tokens)
        n = len(s)
        f = sorted(list(Counter(s).values())+[0]*26, reverse=True)[:26]
        best = 0
        for d in range(1,27):
            if n%d == 0:
                target = n//d
                best = max(best, sum(min(c,target) for c in f[:d]))
        out.append(str(n-best))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- Newly introduced letters have frequency zero and must be considered.
- A one-letter target is always feasible.
- Skip alphabet sizes that do not divide the length.

## Dry run

For `ABCB`, frequencies are `[2,1,1]`. With two letters appearing twice, preserve `2+1=3` of four positions, requiring one replacement.

---

Same problem grouped by topic: [../docs/strings/ARTBALAN.md](../docs/strings/ARTBALAN.md)
