# 458. Oracle Devu and Longest Common Subsequence

> CodeChef problem code [`ORACLCS`](https://www.codechef.com/problems/ORACLCS) &middot; difficulty **1726** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Binary alphabet reduces the LCS to two letter counts |
| **Time** | $O(nm)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Devu is a disastrous oracle: his predictions about various events of your life are horrifying. Instead of providing good luck, he "blesses" you with bad luck. The secret behind his wickedness is a hidden omen which is a string of length **m**. On your visit to him, you can ask a lot of questions about your future, each of which should be a string of length **m**. In total you asked him **n** such questions, denoted by strings **s_1**, **s_2**, ... , **s_n** of length **m** each. Each of the question strings is composed of the characters 'a' and 'b' only.

Amount of bad luck this visit will bring you is equal to the length of longest common subsequence ([LCS](https://en.wikipedia.org/wiki/Longest_common_subsequence_problem)) of all the question strings and the hidden omen string. Of course, as the omen string is hidden, you are wondering what could be the least value of bad luck you can get.

Can you find out what could be the least bad luck you can get? Find it fast, before Devu tells you any bad omens.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

First line of each test case contains a single integer **n** denoting number of strings.

For each of next **n** lines, the **i**^th line contains the string **s_i**.

**Output**

For each test case, output a single integer corresponding to the answer of the problem.

**Constraints**

- All the strings (including the hidden omen) contain the characters 'a' and 'b' only.

** Subtask #1:** (40 points)

- **1** ≤ **T, n, m** ≤ **14**

** Subtask #2:** (60 points)

- **1** ≤ **T, n, m** ≤ **100**

## Constraints

- All the strings (including the hidden omen) contain the characters 'a' and 'b' only.

## Sample

**Sample input**

```
3
2
ab
ba
2
aa
bb
3
aabb
abab
baab
```

**Sample output**

```
1
0
2
```

<details><summary>Explanation</summary>

**In the first example**, the minimum value of LCS of all the strings is 1, the string by oracle can be one of these {aa, ab, ba, bb}.

**In the second example**, whatever string oracle has does not matter, LCS will always be zero.

</details>

## Approach

All strings, the hidden omen included, have the same length $m$ and use only `a` and `b`. The omen is chosen adversarially to make the common LCS as small as possible.

**Upper bound.** An all-`a` omen has only runs of `a` as subsequences, so the LCS of everything is $\min_i \mathrm{cnt}_a(s_i)$. An all-`b` omen likewise gives $\min_i \mathrm{cnt}_b(s_i)$. So the adversary achieves

$$\min\Bigl(\min_i \mathrm{cnt}_a(s_i),\ \min_i \mathrm{cnt}_b(s_i)\Bigr)$$

**Lower bound.** Write $\alpha = \min_i \mathrm{cnt}_a$, $\beta = \min_i \mathrm{cnt}_b$ and suppose the omen has $x$ letters `a` and $m - x$ letters `b`. The run $\texttt{a}^{\min(\alpha, x)}$ is a common subsequence of everything, and so is $\texttt{b}^{\min(\beta, m-x)}$, so the LCS is at least $\max$ of those two. Could the adversary keep both small — $x < \alpha$ and $m - x < \beta$? That would need $m < \alpha + \beta$. But each string has length $m$, so $\mathrm{cnt}_b(s_i) = m - \mathrm{cnt}_a(s_i)$ and hence $\beta = m - \max_i \mathrm{cnt}_a$, giving $\alpha + \beta \leq m$. So no: at least one of the two runs is at full length, and the LCS is at least $\min(\alpha, \beta)$.

The bounds meet, so the answer is exactly $\min(\alpha, \beta)$ — the whole problem is two letter counts per string, with no LCS dynamic programming at all.

The samples: `ab` and `ba` both have one of each letter, giving $1$. `aa` and `bb` give $\alpha = 0$ and $\beta = 0$, so an omen of either kind kills the LCS — $0$. And the three length-$4$ strings each have two of each letter, giving $2$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        words = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        # An all-a or all-b omen caps the LCS at the scarcest letter count.
        fewest_a = min(w.count(b"a") for w in words)
        fewest_b = min(w.count(b"b") for w in words)
        out.append(str(min(fewest_a, fewest_b)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(nm)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Algorithms`
