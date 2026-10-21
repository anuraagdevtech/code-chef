# unrated &middot; Counting Sort

> CodeChef problem code [`CNTSORT`](https://www.codechef.com/problems/CNTSORT) &middot; time limit **1s** &middot; Jump from 2* to 3* (Level 3)

## Topics used

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Counting sort over a small value range |
| **CodeChef category** | main |
| **Time** | $O(N + V)$ per test case with $V = 100$ |
| **Space** | $O(V)$ |

Same write-up grouped by topic: [../docs/sorting/CNTSORT.md](../docs/sorting/CNTSORT.md)

## Question

Given an array $A$ of $N$ integers, such that $1 \le A[i] \le 100$,,

sort $A$ in non-decreasing/ascending order, and display the elements of the sorted array.

### Input:

- The first line contains an integer $T$, denoting the number of test cases.
- The first line of each test case contains an integer $N$, the number of elements in $A$.
- The next line contains $N$ space-separated integers, denoting the elements of array $A$.

### Output:
For each test case, display the elements of the sorted array, in a new line, separated by a space.

### Constraints
- $1 \le T \le 3$
- $1 \le N \le 10^6$
- $1 \le A[i] \le 100$

## Constraints

- $1 \le T \le 3$
- $1 \le N \le 10^6$
- $1 \le A[i] \le 100$

## Sample

**Sample input**

```
2
5
7 2 9 10 1
4
3 7 7 3
```

**Sample output**

```
1 2 7 9 10
3 3 7 7
```

<details><summary>Explanation</summary>

The sample outputs are the sorted orders of the input arrays respectively, sorted in non-decreasing/ascending order.

</details>

## Approach

The values are confined to $1 \ldots 100$, which is the signal to use a **counting sort** rather than a comparison sort.

Tally how many times each value occurs in one pass, then emit each value that many times in increasing order. That is $O(N + V)$ — linear in the input — against the $O(N \log N)$ lower bound that applies to comparison sorts. The small, known value range is exactly the extra information that lets the bound be beaten.

Space is $O(V)$, a fixed $100$ counters regardless of how large $N$ grows.

With $N$ up to $10^6$ the practical concern is less the sorting than the **I/O**: reading a million tokens with per-line parsing and printing them one at a time would dominate the runtime. Reading the whole stream at once and emitting a single joined write is what keeps this fast.

The sample shows both the distinct case, $[7,2,9,10,1] \to [1,2,7,9,10]$, and the duplicate case, $[3,7,7,3] \to [3,3,7,7]$ — duplicates simply emit their value repeatedly, which counting sort handles naturally without any tie-breaking.

Note that Python's built-in `sorted` would also pass comfortably here; the point of the problem is to practise the counting technique, and the counting version is genuinely faster at this size.

## Solution (Python)

```python
import sys

MAX_VALUE = 100


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        # Values are bounded by 100, so tally rather than compare.
        counts = [0] * (MAX_VALUE + 1)
        for v in data[pos + 1:pos + 1 + n]:
            counts[int(v)] += 1
        pos += 1 + n
        parts = []
        for value in range(1, MAX_VALUE + 1):
            if counts[value]:
                parts.extend([str(value)] * counts[value])
        out.append(" ".join(parts))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N + V)$ per test case with $V = 100$
- **Space:** $O(V)$
