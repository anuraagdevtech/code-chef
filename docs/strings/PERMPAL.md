# 409. Permutation and Palindrome

> CodeChef problem code [`PERMPAL`](https://www.codechef.com/problems/PERMPAL) &middot; difficulty **1651** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Pairing equal letters inward from both ends |
| **Time** | $O(n)$ per test case |
| **Space** | $O(n)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You are given a string **s** with length **n**. You should find a [permutation](https://en.wikipedia.org/wiki/Permutation) **P** of numbers 1 through **n** such that if you apply this permutation on the string **s**, you will get a [palindromic](https://en.wikipedia.org/wiki/Palindrome) string.

The result of applying a permutation **P** on the string **s** is a string **t** with length **n** such that for each **i** (1 ≤ **i** ≤ **n**), the **i**-th character of **t** is given as as **t**[**i**] = **s**[**P_i**].

**Input**

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first and only line of each test case contains the string **s**.

**Output**

For each test case, print a single line. If it is impossible to find a valid permutation **P**, this line should contain a single integer -1. Otherwise, it should contain **n** space-separated integers **P_1, P_2, ..., P_n**.

If there are multiple valid permutations, you may print any one.

**Constraints**

- 1 ≤ **n** ≤ 10^5

- **s** will consist only of lowercase English letters (i.e. characters 'a' through 'z')

**Subtasks**

**Subtask #1 (20 points)**: 1 ≤ **T**, **n** ≤ 10

**Subtask #2 (20 points)**: 1 ≤ **T**, **n** ≤ 100

**Subtask #3 (60 points)**: 1 ≤ **T** ≤ 10

## Constraints

- 1 ≤ n ≤ 10^5
- s will consist only of lowercase English letters (i.e. characters 'a' through 'z')

## Sample

**Sample input**

```
4
aa
baa
abc
abab
```

**Sample output**

```
1 2
2 1 3
-1
1 2 4 3
```

<details><summary>Explanation</summary>

**Example case 1:** The string **t** obtained using the identity permutation will have **t**[1] = **s**[1] and **t**[2] = **s**[2]. That means **t** = "aa", which is a palindrome.

**Example case 2:** The characters of the string **t** obtained by applying the permutation **2, 1, 3** are **t**[1] = **s**[2], **t**[2] = **s**[1] and **t**[3] = **s**[3]. Therefore, **t** = "aba", which is a palindrome.

**Example case 3:** There is no way to find a permutation **P** such that we can obtain a palindrome from **s** using it.

**Example case 4:** Applying the permutation **1, 2, 4, 3** on **s** results in **t** = "abba", which is a palindrome. Another permutation that you may apply is **2, 1, 3, 4**; this results in **t** = "baab", which is also a palindrome.

</details>

## Approach

A multiset of letters can be arranged into a palindrome exactly when **at most one letter has an odd count** — every other letter must split evenly between the two halves. That is the feasibility test; otherwise print $-1$.

The construction then emits *indices* rather than letters, since $P$ answers "which original position supplies position $i$". Group the positions of each letter, then walk two pointers inward: for each pair of positions holding the same letter, send one to the left pointer and its partner to the right pointer. The lone odd position, if any, lands in the exact middle, which is the only slot a palindrome leaves unpaired.

$$t[i] = s[P_i] \implies t[i] = t[n+1-i]$$

holds by construction, because the two slots filled in each step hold the same letter.

Note the problem's convention: $P$ indexes *into* $s$, so $P$ is a permutation of $1 \ldots n$ and the output is those source indices in target order. It is easy to accidentally produce the inverse permutation, which is a different (and generally wrong) answer.

Many permutations work. For `abab` our pairing gives `1 2 4 3`, which happens to match the sample and yields `abba`. For `baa` the single `b` is the odd letter and goes to the middle, giving `2 1 3` and the palindrome `aba`. And `abc` has three odd counts, so $-1$.

The empty-middle case matters too: for even $n$ with all counts even, the two pointers meet exactly, and no middle slot is written.

## Solution (Python)

```python
import sys
from collections import defaultdict


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for word in data[1:1 + t]:
        n = len(word)
        spots = defaultdict(list)
        for i, c in enumerate(word):
            spots[c].append(i)
        if sum(len(v) % 2 for v in spots.values()) > 1:
            out.append("-1")
            continue
        perm = [0] * n
        left, right = 0, n - 1
        middle = -1
        for idxs in spots.values():
            for k in range(0, len(idxs) - 1, 2):
                # The two slots receive the same letter, keeping it a palindrome.
                perm[left] = idxs[k] + 1
                perm[right] = idxs[k + 1] + 1
                left += 1
                right -= 1
            if len(idxs) % 2:
                middle = idxs[-1]
        if middle >= 0:
            perm[left] = middle + 1
        out.append(" ".join(map(str, perm)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(n)$ per test case
- **Space:** $O(n)$

> CodeChef tags: `Data Structures`
