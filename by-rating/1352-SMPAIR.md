# 1352 &middot; The Smallest Pair

> CodeChef problem code [`SMPAIR`](https://www.codechef.com/problems/SMPAIR) &middot; time limit **1s** &middot; Level up from 1* to 2* (Level 2)

## Topics used

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | The two smallest elements |
| **CodeChef category** | main |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/sorting/SMPAIR.md](../docs/sorting/SMPAIR.md)

## Question

You are given a sequence **a_1, a_2, ..., a_N**. Find the smallest possible value of **a_i + a_j**, where 1 ≤ **i** < **j** ≤ **N**.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows. 

The first line of each description consists of a single integer **N**.

The second line of each description contains **N** space separated integers - **a_1, a_2, ..., a_N** respectively.

**Output**

For each test case, output a single line containing a single integer - the smallest possible sum for the corresponding test case.

**Constraints**

- **T** = **10^5**, **N** = **2** : 13 points.

- **T** = **10^5**, **2** ≤ **N** ≤ **10** : 16 points.

- **T** = **1000**, **2** ≤ **N** ≤ **100** : 31 points.

- **T** = **10**, **2** ≤ **N** ≤ **10^5** : 40 points.

- **1** ≤ **a_i** ≤ **10^6**

## Constraints

- T = 10^5, N = 2 : 13 points.
- T = 10^5, 2 ≤ N ≤ 10 : 16 points.
- T = 1000, 2 ≤ N ≤ 100 : 31 points.
- T = 10, 2 ≤ N ≤ 10^5 : 40 points.
- 1 ≤ a_i ≤ 10^6

## Sample

**Sample input**

```
1
4
5 1 3 4
```

**Sample output**

```
4
```

<details><summary>Explanation</summary>

Here we pick **a_2** and **a_3**. Their sum equals to 1 + 3 = 4.

</details>

## Approach

The smallest sum $a_i + a_j$ over distinct indices is simply the sum of the **two smallest values** in the array. Any other pair replaces one of them with something at least as large.

Two ways to get them. Sorting and taking the first two is $O(N \log N)$ and reads clearly. Better, a single pass tracking the smallest and second-smallest is $O(N)$ — and with the hardest subtask allowing $N = 10^5$ across $T = 10$ cases, plus $T = 10^5$ cases of $N = 2$, the linear version is the one that comfortably fits both shapes. Python's `heapq.nsmallest(2, a)` does it in one pass without a full sort.

The constraint $i < j$ means two **distinct positions**, not two distinct values. So an array like $[3, 3]$ answers $6$: the two entries are separate elements even though they are equal. A solution deduplicating the values first would break on that, and it is the most likely bug here.

The guarantee $N \geq 2$ means a valid pair always exists, so no empty case needs handling.

Sample: $[5, 1, 3, 4]$ has smallest $1$ and second smallest $3$, giving $4$. Note the two need not be adjacent in the input.

With $a_i$ up to $10^6$ the sum stays small; the subtask table in the constraints is really a hint about which complexities will pass, and only the $O(N)$ or $O(N \log N)$ approaches clear all four.

## Solution (Python)

```python
import sys
import heapq


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        # Two distinct positions, so equal values are still a valid pair.
        lo1, lo2 = heapq.nsmallest(2, a)
        out.append(str(lo1 + lo2))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$
