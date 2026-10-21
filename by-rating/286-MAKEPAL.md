# 286. Weird Palindrome Making

> [`MAKEPAL`](https://www.codechef.com/problems/MAKEPAL) &middot; difficulty **1486** &middot; time limit **0.5s** &middot; 1400 to 1600 difficulty problems (Level 2)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Odd counts and palindrome feasibility |
| **CodeChef tags** | `Algorithms`, `Implementation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

Naveej is from a tribe that speaks some weird language - their alphabet consists of $N$ distinct characters.
He has an array $A = [A_1, A_2, \dots, A_N]$, where $A_i$ denotes the number of occurrences of the $i$-th character with him.

He wants to make a [palindromic string](https://en.wikipedia.org/wiki/Palindrome) using **all** the characters he has (every character he has must be used in this string).

In order to make this possible, he can perform the following operation:
- Select an $i$ $(1 \le i \le N)$ and convert all occurrences of $i$-th alphabet to any other alphabet of his choice.

Note that Naveej just wants to be able to make any palindrome, as long as every character is used. For example, if $N = 2$ and $A = [2, 2]$ and we consider the characters to be $a$ and $b$, he can make both $abba$ and $baab$, but $aba$ is not allowed because it uses only $3$ characters.

Find the minimum number of operations required such that Naveej can make a palindromic string using all the characters he has. It can be proven that there always exists at least one sequence of operations allowing for the formation of a palindrome.

**Input**

- The first line of input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$ - the size of the alphabet.
- The second line contains $N$ space-separated integers: $A_1, A_2, ..., A_N$, where $A_i$ is the number of occurrences of the $i$-th character with Naveej.

**Output**

For each test case, output a single line containing one integer - the minimum number of operations required so that Naveej can make a palindromic string using all the characters he has.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 2 \cdot 10^5$
- $1 \leq A_i \leq 10^9$
- It is guaranteed that the sum of $N$ over all test cases does not exceed $2 \cdot 10^5$

**Subtasks**

- **Subtask 1 (100 points):** Original constraints

## Sample

**Sample input**

```
2
1
4
3
4 3 1
```

**Sample output**

```
0
1
```

<details><summary>Explanation</summary>

- In the first test case, $N = 1$. Let the character be $a$. We can make the following palindromic string: $aaaa$.

- In the second test case, $N = 3$. Let the characters be $a$, $b$, $c$. It is initially not possible to make a palindrome with the given occurrences of the characters.
We perform 1 operation:
Convert all the occurrences of $b$ to $c$.
Then, we can make the following palindromic string: $acaccaca$.

</details>

## Approach

A multiset of characters can be arranged into a palindrome exactly when **at most one** character has an odd count — that one sits in the middle, and the rest pair off symmetrically.

So let $k$ be the number of indices with $A_i$ odd. If $k \leq 1$, nothing needs doing.

Otherwise, consider what one operation achieves. Converting every occurrence of character $i$ into character $j$ adds $A_i$ to $A_j$ and zeroes $A_i$. Picking two characters that **both** have odd counts is the productive move: the emptied one is no longer odd, and the receiver's count becomes odd + odd = even. One operation removes **two** odd counts at a stroke.

Repeating until at most one remains costs

$$\left\lfloor \frac{k}{2} \right\rfloor$$

operations. The floor handles both parities: an even $k$ collapses to $0$ odd counts, and an odd $k$ collapses to exactly $1$ — which is still a valid palindrome.

The bound is tight because no operation can reduce the odd count by more than two: it touches only two characters.

Sample case 2 has $A = [4, 3, 1]$ with $k = 2$. Merging the count-$1$ character into the count-$3$ one gives $[4, 4, 0]$, so $k = 0$ and one operation suffices. Sample case 1 has a single even count and needs none.

Note the requirement to use **every** character, which is what makes the count parities the whole story — discarding characters would make this trivial instead.

Only the parities matter, so the $A_i$ themselves never need summing; with $\sum N = 2\times10^5$ the single pass is comfortable.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        odds = sum(1 for v in data[pos + 1:pos + 1 + n] if int(v) % 2)
        pos += 1 + n
        # Merging two odd-count characters removes both odd counts at once.
        out.append(str(odds // 2))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/arrays/MAKEPAL.md](../docs/arrays/MAKEPAL.md)
