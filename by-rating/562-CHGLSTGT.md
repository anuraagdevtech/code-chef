[&larr; 561. Random decreasing function](561-RDF.md) &middot; [Index](README.md) &middot; [563. Sereja and Commands &rarr;](563-SEACO.md)

# 562. Girl Friend and String Gift

> [`CHGLSTGT`](https://www.codechef.com/problems/CHGLSTGT) &middot; difficulty **1986** &middot; time limit **2s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Minimum prefix partition using rolling palindrome detection |
| **Complexity class** | Quadratic $O(n^2)$ |
| **Time** | $O(|S|^2)$ per test case |
| **Space** | $O(|S|)$ |

## Question

** Read problems statements in Russian [here](https://www.codechef.com/download/translated/LTIME05/russian/CHGLSTGT.pdf)**

Chef's Girl Friend has given him a unique gift. She has given him a string **S**. Chef being a gentleman wants to return her gift in a unique way. He wants to break the string he has received into some number of substrings so that each substring is a palindrome. However he does not want break the string into too many substrings, otherwise the average size of his strings will become small. What is the minimum number of substrings in which the given string can be broken so that each substring is a palindrome.

**Tips: **

Refer [http://en.wikipedia.org/wiki/Palindrome](http://en.wikipedia.org/wiki/Palindrome) for the definition of a "palindrome"

**Input**

Input description.

- The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows:

- The first line of each test case contains a single integer **N** denoting the number of alphabets in the given string. The second line contains the given string.

**Output**

For each test case output a single integer the answer to the given test case. Print answer for each test case on a separate line.

**Constraints**

All characters in the given string are upper case English alphabets.

- **1** ≤ **T** ≤ **10**

- **1** ≤ **|S|** ≤ **5000**

** Scoring **

 ** Subtask 1: (15 points):**

- **1** ≤ **|S|** ≤ **20**

 ** Subtask 2: (25 points):**

- **1** ≤ **|S|** ≤ **250**

 ** Subtask 1: (60 points):**

- **1** ≤ **|S|** ≤ **5000**

## Constraints

All characters in the given string are upper case English alphabets.
- 1 ≤ T ≤ 10
- 1 ≤ |S| ≤ 5000

## Sample

**Sample input**

```
1 
7
ABCCBDA
```

**Sample output**

```
4
```

<details><summary>Explanation</summary>

**Example case 1.** The given string can be broken into **"A" , "BCCB" , "D" , "A"**. It can be verified that you can't break the given string into less than 4 substrings such that each substring in a palindrome.

</details>

## Approach

Let $best[r]$ be the minimum number of palindrome parts for the first $r$ characters, with $best[0]=0$. For each palindrome ending at the current right endpoint and starting at $l$, try `best[l]+1`.

Detect palindromes using one rolling array: equal endpoints form a palindrome if the length is at most two or the interior substring was a palindrome at the previous right endpoint. Scan left endpoints in ascending order to preserve that previous interior value until it is used. Every partition is considered by its final part.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        s = next(tokens)
        palindrome = bytearray(n)
        best = list(range(n+1))
        for right in range(n):
            optimum = right+1
            for left in range(right+1):
                palindrome[left] = s[left] == s[right] and (right-left < 2 or palindrome[left+1])
                if palindrome[left]:
                    optimum = min(optimum,best[left]+1)
            best[right+1] = optimum
        out.append(str(best[n]))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Edge cases

- A whole-string palindrome needs one part.
- A string with no longer palindrome may need one part per character.
- All characters are uppercase, but the recurrence does not depend on case.

## Dry run

For `ABCCBDA`, final parts can be `A | BCCB | D | A`, using four palindromes. The prefix DP finds no partition with fewer parts.

---

Same problem grouped by topic: [../docs/dynamic-programming/CHGLSTGT.md](../docs/dynamic-programming/CHGLSTGT.md)
