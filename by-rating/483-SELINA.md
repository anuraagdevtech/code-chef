# 483. Jon and Selina

> [`SELINA`](https://www.codechef.com/problems/SELINA) &middot; difficulty **unrated** &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Parity bitmask over a 26-letter alphabet |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

Selina is Jon’s girlfriend.  They had planned to go for a date this evening, but Jon is stuck with a problem at work.

He has a string $S$ of length $N$, containing all lower case alphabets. The string contains a odd occurring character (characters that is present odd times). The task is to find the character (if not present print $-1$). Jon is already late for his date, so help him solve this as quickly as possible.

**Input**

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, one string $S$.

**Output**

- Print the character.
- If no such character is present, print $-1$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 1000$
- sum of $N$ over all test cases doesn't exceed $10^6$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
3
abcbacc
abcba
abccba
```

**Sample output**

```
c
c
-1
```

<details><summary>Explanation</summary>

**Case 1:** $c$ is occurred $3$ times i.e odd number of times.

**Case 2:** $c$ is occurring only $1$ time.

**Case 3:** no odd occurring character is present, printed $-1$.

</details>

## Approach

Only the **parity** of each letter's count matters, not the count itself, so the whole string compresses to 26 bits. Keep a mask and toggle one bit per character:

$$\text{mask} \;\mathrel{\oplus}= 1 \ll (c - \texttt{'a'})$$

A pair of identical letters toggles the same bit twice and cancels, so after the sweep a bit is set exactly for the letters appearing an odd number of times. That gives both answers at once: `mask == 0` means every letter is even, so print $-1$; otherwise the lowest set bit names the letter, extracted as `(mask & -mask).bit_length() - 1`.

This beats a frequency table on space ($O(1)$ instead of $O(26)$) and needs only one pass, which matters with $T$ up to $10^5$ and $\sum N$ up to $10^6$.

The common shortcut — XOR the raw character codes and print that character — is wrong in general: it only works when exactly one letter has odd count, and silently prints a garbage letter otherwise. The per-letter bitmask has no such blind spot, and it also makes the choice well defined if several letters were odd.

Note the parity argument implies $|S|$ odd $\iff$ some letter is odd, so the $-1$ case is exactly the even-length strings whose letters all pair up. The samples show all three shapes: `abcbacc` has `c` three times, `abcba` has `c` once, and `abccba` is fully paired, giving $-1$.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for word in data[1:1 + t]:
        mask = 0
        for c in word:
            # A letter seen twice toggles its bit back off.
            mask ^= 1 << (c - 0x61)
        if mask == 0:
            out.append("-1")
        else:
            out.append(chr(0x61 + (mask & -mask).bit_length() - 1))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/bit-manipulation/SELINA.md](../docs/bit-manipulation/SELINA.md)
