# 1612 &middot; Different String

> CodeChef problem code [`DIFSTR`](https://www.codechef.com/problems/DIFSTR) &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Cantor diagonalisation |
| **CodeChef tags** | `Data Structures`, `Algorithms`, `Constructive`, `String`, `ad-hoc` |
| **CodeChef top tag** | `Ad Hoc` |
| **CodeChef category** | easy |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

Same write-up grouped by topic: [../docs/constructive/DIFSTR.md](../docs/constructive/DIFSTR.md)

## Question

You are given $N$ binary strings of length $N$ each. You need to find a binary string of length $N$ which is different from all of the given strings.

Note:

- A binary string is defined as a string consisting only of `'0'` and `'1'`.
- A string is considered different from another string when they have different lengths, or when they differ in at least one position.

**Input**

- The first line will contain $T$ - the number of test cases. Then the test cases follow.

- The first line of each test case contains $N$  - the number of strings and length of strings.

- Each of the next $N$ lines contains a binary string of length $N$.

**Output**

For each test case, print on one line a binary string of length $N$, which is different from all of the given strings. If there are multiple possible answers, print any.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 100$

## Sample

**Sample input**

```
2
3
101
110
100
4
1100
1010
0100
0010
```

**Sample output**

```
111
1101
```

<details><summary>Explanation</summary>

**Test case $1$:** $111$ is different from $101$ , $110$ , $100$.

**Test case $2$:** $1101$ is different from $1100$ , $1010$ , $0100$ , $0010$.

</details>

## Approach

The input is deliberately square — $N$ strings of length $N$ — which is exactly the setting for **diagonalisation**. Build the answer by flipping the diagonal:

$$R_i = 1 - S_i[i]$$

Then $R$ differs from $S_i$ at position $i$, for every $i$. One position per string, each string handled by a different position, and there are just enough positions to go around. This is Cantor's argument from the proof that the reals are uncountable, run on a finite square.

No search is needed, and the construction is $O(N)$ rather than the $O(N^2)$ of reading the input — it touches only one character per string, so it would even work on a stream where each string is read and discarded.

A counting sanity check: there are $2^N$ binary strings of length $N$ and only $N$ are forbidden, so for $N \geq 1$ an answer always exists (and for $N \geq 5$ the vast majority of strings work). The diagonal construction is just a way to name one without searching.

Many answers are accepted. For the first sample — `101`, `110`, `100` — the diagonal is $1, 1, 0$, so we print `001`, while the sample prints `111`; both differ from all three. For the second sample the diagonal of `1100`, `1010`, `0100`, `0010` is $1, 0, 0, 0$, giving `0111` against the sample's `1101`.

Note the problem counts strings of different lengths as different too, but since every candidate must have length $N$ that clause never comes into play.

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
        rows = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        # Flipping the diagonal differs from row i exactly at position i.
        out.append("".join("1" if rows[i][i] == 0x30 else "0" for i in range(n)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
