[&larr; 214. Turn It](214-NFS.md) &middot; [Index](README.md) &middot; [216. Magical Doors &rarr;](216-MAGDOORS.md)

# 215. The Smallest Pair

> [`SMPAIR`](https://www.codechef.com/problems/SMPAIR) &middot; difficulty **1352** &middot; time limit **1s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | The two smallest elements |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

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

## Solution

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

## Edge cases

- **Equal values are a valid pair**, because the problem asks for two distinct *positions*, not two distinct values — $[2, 2]$ answers $4$.
- **$N = 2$**: the only pair, which the $13$- and $16$-point subtasks hammer at $T = 10^5$.
- **`nsmallest(2, …)` is linear**, not $O(N \log N)$, which matters for the $40$-point subtask at $N = 10^5$ while keeping the per-case overhead tiny for the $T = 10^5$ subtasks.
- **The subtasks have very different shapes** — many tiny cases versus a few large ones — so both the per-case cost and the per-element cost have to stay low, hence a single buffered read for the whole file.
- **$a_i$ up to $10^6$**, so the sum reaches $2 \cdot 10^6$ and fits anywhere.
- **The two smallest need not be adjacent** in the input, so a scan comparing neighbours is wrong; the sample's $1$ and $3$ sit either side of a larger value.

## Dry run

Input $5, 1, 3, 4$.

| rank | value |
|---|---:|
| smallest | 1 |
| second smallest | 3 |

Output `4`. The $5$ and $4$ are never considered.

---

Same problem grouped by topic: [../docs/sorting/SMPAIR.md](../docs/sorting/SMPAIR.md)
