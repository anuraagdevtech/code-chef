# 1437 &middot; Permutation Xority

> CodeChef problem code [`PERMXORITY`](https://www.codechef.com/problems/PERMXORITY) &middot; time limit **1s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topics used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Cancelling a XOR with a 1-2-3 triple |
| **CodeChef tags** | `Mathematics`, `Bit Manipulation`, `Algorithms`, `Bitwise Operation`, `Observation` |
| **CodeChef category** | easy |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

Same write-up grouped by topic: [../docs/constructive/PERMXORITY.md](../docs/constructive/PERMXORITY.md)

## Question

You are given an integer $N$. Construct a permutation $A$ of length $N$ which is **attractive**.

A permutation is called **attractive** if the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) of all absolute differences of adjacent pairs of elements is equal to $0$.

Formally, a permutation $A = [A_1, A_2, \ldots, A_N]$ of length $N$ is said to be attractive if:

$$|A_{1}-A_{2}|  \oplus |A_{2}-A_{3}| \oplus \ldots \oplus |A_{N-1} - A_{N}| = 0$$

where $\oplus$ denotes the bitwise XOR operation.

Output **any** attractive permutation of length $N$. If no attractive permutation exists, print $-1$ instead.

**Note:** A permutation of length $N$ is an array $A = [A_1, A_2, \ldots, A_N]$ such that every integer from $1$ to $N$ occurs exactly once in $A$. For example, $[1, 2, 3]$ and $[2, 3, 1]$ are permutations of length $3$, but $[1, 2, 1]$, $[4, 1, 2]$, and $[2, 3, 1, 4]$ are not.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- Each test case consists of a single line of input, containing one integer $N$.

**Output**

For each test case, output on a single line an attractive permutation of $N$ integers, or $-1$ if no attractive permutation exists.

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$
- Sum of $N$ over all cases won't exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
2
3
6
```

**Sample output**

```
3 2 1
5 2 3 6 4 1
```

<details><summary>Explanation</summary>

**Test Case $1$:** $ |3-2| \oplus |2-1|  =  1 \oplus 1 = 0$

Note that there are other correct answers — for example, $[1, 2, 3]$ would also be accepted as correct.

**Test Case $2$:** $ |5-2| \oplus |2-3| \oplus |3-6| \oplus |6-4| \oplus |4-1| = 3 \oplus 1 \oplus 3 \oplus 2 \oplus 3 = 0$

</details>

## Approach

Start from the identity permutation $[1, 2, \ldots, N]$. Every adjacent difference is $1$, and there are $N-1$ of them, so the XOR is $1$ when $N-1$ is odd and $0$ when it is even.

**$N$ odd.** Then $N-1$ is even, the $1$s cancel in pairs, and the identity permutation already works.

**$N$ even.** The identity leaves a stray $1$ that needs cancelling. Rearranging the opening to $[2, 3, 1, 4, 5, \ldots, N]$ does it. The differences become

$$\underbrace{|2-3|,\ |3-1|,\ |1-4|}_{1,\ 2,\ 3} ,\ \underbrace{1,\ 1,\ \ldots,\ 1}_{N-4 \text{ of them}}$$

The leading triple satisfies $1 \oplus 2 \oplus 3 = 0$, so it vanishes. And because $N$ is even, $N-4$ is even as well, so the trailing $1$s cancel in pairs. The whole XOR is $0$.

Note that the third difference, $|1 - 4| = 3$, is the junction into the untouched tail — the reordering of three elements is what manufactures the $1, 2, 3$ triple out of what would otherwise be three $1$s.

So $[2, 3, 1, 4, 5, \ldots, N]$ is attractive for every even $N \geq 4$.

**$N = 2$ is impossible.** Both permutations, $[1,2]$ and $[2,1]$, give the single difference $1$, whose XOR is $1 \neq 0$. With only one term there is nothing to cancel against, so the answer is $-1$.

Checking $N = 6$: $[2,3,1,4,5,6]$ gives differences $1, 2, 3, 1, 1$, and $1 \oplus 2 \oplus 3 \oplus 1 \oplus 1 = 0$.

**Any attractive permutation is accepted**, so this is judged by a checker. The samples show different arrangements — `3 2 1` for $N=3$ and `5 2 3 6 4 1` for $N=6$ — both equally valid, so a verbatim diff would report a false mismatch.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + i])
        if n == 2:
            # One difference, nothing to cancel it against.
            out.append("-1")
        elif n % 2:
            # n - 1 differences of 1, an even count, so they cancel.
            out.append(" ".join(map(str, range(1, n + 1))))
        else:
            # Differences 1, 2, 3 cancel; the remaining n - 4 ones pair off.
            rest = range(4, n + 1)
            out.append(" ".join(map(str, (2, 3, 1, *rest))))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
