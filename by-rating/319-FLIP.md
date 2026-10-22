[&larr; 318. Sheokand and Number](318-SHKNUM.md) &middot; [Index](README.md) &middot; [320. Javelin Qualification &rarr;](320-JAVELIN.md)

# 319. Flip the String

> [`FLIP`](https://www.codechef.com/problems/FLIP) &middot; difficulty **1538** &middot; time limit **1.5s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Two independent parity classes |
| **CodeChef tags** | `Data Structures`, `Algorithms`, `String`, `Greedy`, `Implementation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(|A|)$ per test case |
| **Space** | $O(|A|)$ |

## Question

You are given two binary strings $A$ and $B$ with the same length.

You may perform the following operation any number of times (including zero): pick a substring of $A$ with odd length and invert all the bits (change '0' to '1' or vice versa) at odd positions in this substring. For example, if we choose a substring "**0**1**0**1**1**", we can convert it to "**1**1**1**1**0**" (bits at odd positions are bold).

Determine the minimum number of operations required to change the string $A$ to the string $B$.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single string $A$.
- The second line contains a single string $B$.

**Output**
For each test case, print a single line containing one integer — the minimum number of operations required.

**Constraints**
- $1 \le T \le 10^3$
- $1 \le |A| = |B| \le 10^5$
- $A$ and $B$ contain only characters '0' and '1'
- the sum of $|A|$ over all test cases does not exceed $10^5$

## Constraints

- $1 \le T \le 10^3$
- $1 \le |A| = |B| \le 10^5$
- $A$ and $B$ contain only characters '0' and '1'
- the sum of $|A|$ over all test cases does not exceed $10^5$

## Sample

**Sample input**

```
3
100001
110111
1010
1010
000
111
```

**Sample output**

```
2
0
2
```

<details><summary>Explanation</summary>

**Example case 1:** Initially, $A$ is "100001". We choose the substring "**0**0**0**" between the $2$-nd and $4$-th character and convert it to "**1**0**1**".

Now $A$ becomes "110101". We choose the string "**0**" containing only the $5$-th character and convert it to "**1**".

Finally, $A$ becomes "110111", which is equal to $B$.

**Example case 2:** $A$ and $B$ are initially equal, so there is no need to perform any operation.

</details>

## Approach

Look carefully at which positions an operation touches. Choosing a substring starting at index $i$ with odd length, the inverted bits are the ones at odd positions *within* the substring — that is, the global indices $i, i+2, i+4, \ldots$, ending at the substring's last index because the length is odd.

So an operation flips a **contiguous run inside one parity class** and never mixes the two. The even-indexed positions and the odd-indexed positions are entirely independent problems.

Within a class, we must flip exactly the positions where $A$ and $B$ differ, and each operation flips one contiguous block of that class. The minimum number of blocks covering a set exactly is its number of **maximal runs** — merging across a non-differing position would flip something that already matches.

So the answer is the run count in the even class plus the run count in the odd class, both computed in a single pass.

Sample case 1, `100001` against `110111`, differs at indices $1, 3, 4$. In the even class $(0,2,4)$ only index $4$ differs — one run. In the odd class $(1,3,5)$ indices $1$ and $3$ differ, and they are *adjacent within that class*, so also one run. Total $2$.

That adjacency is the subtlety: globally, indices $1$ and $3$ have index $2$ between them, but index $2$ belongs to the other class and does not break the run.

Sample case 3, `000` to `111`, differs everywhere: one run in each class, giving $2$ — not $1$, since no single operation spans both parities.

## Solution

```python
import sys


def runs(diff, start, n):
    """Maximal runs of True in diff[start], diff[start+2], ..."""
    count = 0
    prev = False
    for i in range(start, n, 2):
        if diff[i] and not prev:
            count += 1
        prev = diff[i]
    return count


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b = data[1 + 2 * i], data[2 + 2 * i]
        n = len(a)
        diff = [a[j] != b[j] for j in range(n)]
        # An operation flips a contiguous run inside one parity class only.
        out.append(str(runs(diff, 0, n) + runs(diff, 1, n)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **One operation touches a single parity class.** The chosen substring has odd length and its *odd positions* flip, which in the original string means a contiguous run of indices stepping by two — all of the same parity. So the two parity classes are entirely independent.
- **The substring's odd length forces both ends to flip**, which is why an operation covers a complete run $s, s+2, \dots, s+2m$ and cannot stop half-way.
- **The answer is the number of maximal difference runs within each class, summed.** Each such run needs its own operation, and one operation suffices for it.
- **Already equal** (the second row) → $0$ operations.
- **Adjacent differing positions belong to different classes.** The third row, `000` against `111`, differs everywhere; the even class holds indices $0$ and $2$ — consecutive *within that class*, so one run — and the odd class holds index $1$, giving $2$ in total rather than $1$ or $3$.
- **A gap inside a class splits a run.** The first row's even class differs only at index $4$, while its odd class differs at $1$ and $3$ (consecutive within the class), giving $1 + 1 = 2$.
- **Sum of $|A| \leq 10^5$**: two strided passes.

## Dry run

First sample: $A = $ `100001`, $B = $ `110111`.

| index | $A$ | $B$ | differs? | class |
|---:|---:|---:|:---:|---|
| 0 | 1 | 1 | no | even |
| 1 | 0 | 1 | **yes** | odd |
| 2 | 0 | 0 | no | even |
| 3 | 0 | 1 | **yes** | odd |
| 4 | 0 | 1 | **yes** | even |
| 5 | 1 | 1 | no | odd |

Even class: differences at $\{4\}$ → one run. Odd class: differences at $\{1, 3\}$, adjacent within the class → one run. Output `2`.

---

Same problem grouped by topic: [../docs/strings/FLIP.md](../docs/strings/FLIP.md)
