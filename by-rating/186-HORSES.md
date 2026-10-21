# 186. Racing Horses

> [`HORSES`](https://www.codechef.com/problems/HORSES) &middot; difficulty **1231** &middot; time limit **1.5s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Minimum adjacent difference after sorting |
| **CodeChef tags** | `Algorithms`, `Sorting`, `Brute Force` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

Chef is very fond of horses. He enjoys watching them race. As expected, he has a stable full of horses. He, along with his friends, goes to his stable during the weekends to watch a few of these horses race. Chef wants his friends to enjoy the race and so he wants the race to be close. This can happen only if the horses are comparable on their skill i.e. the difference in their skills is less.

There are **N** horses in the stable. The skill of the horse **i** is represented by an integer **S[i]**. The Chef needs to pick 2 horses for the race such that the difference in their skills is *minimum*. This way, he would be able to host a very interesting race. Your task is to help him do this and report the minimum difference that is possible between 2 horses in the race.

**Input:**

First line of the input file contains a single integer **T**, the number of test cases.

Every test case starts with a line containing the integer **N**.

The next line contains **N** space separated integers where the **i**-th integer is **S[i]**.

**Output:**

For each test case, output a single line containing the minimum difference that is possible.

**Constraints:**

```
1 ≤ **T** ≤ 10
2 ≤ **N** ≤ 5000
1 ≤ **S[i]** ≤ 1000000000
```

## Constraints

1 ≤ T ≤ 10
2 ≤ N ≤ 5000
1 ≤ S[i] ≤ 1000000000

## Sample

**Sample input**

```
1
5
4 9 1 32 13
```

**Sample output**

```
3
```

<details><summary>Explanation</summary>

The minimum difference can be achieved if we pick horses with skills 1 and 4 for the race.

</details>

## Approach

The closest pair of values in a set must be **adjacent once sorted**. If two values $x < y$ had anything between them, that in-between value would be closer to each of them than they are to each other — so the minimum difference can only occur between neighbours.

That observation turns an $O(N^2)$ comparison of all pairs into a sort plus a single linear scan:

$$\min_{1 \leq i < N} \bigl(S_{i+1} - S_i\bigr)$$

on the sorted array. At $N = 5000$ the quadratic version is about $12$ million comparisons and would likely pass, but the sorted scan is both faster and the idea that generalises.

After sorting, the differences are automatically non-negative, so no absolute value is needed — a small simplification that only holds *because* the array is sorted.

Sample: $[4, 9, 1, 32, 13]$ sorts to $[1, 4, 9, 13, 32]$ with gaps $3, 5, 4, 19$, so the answer is $3$, from the pair $(1, 4)$ that sits far apart in the original input.

Duplicates, if present, would give a difference of $0$, which the scan reports correctly with no special case.

Values reach $10^9$, so a difference fits comfortably in 32 bits — but a C solution computing anything cumulative would want care. The guarantee $N \geq 2$ means at least one pair exists.

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
        s = sorted(int(v) for v in data[pos + 1:pos + 1 + n])
        pos += 1 + n
        # The closest pair is always adjacent once sorted.
        out.append(str(min(s[i + 1] - s[i] for i in range(n - 1))))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The closest pair is always adjacent once sorted.** For $i < j < k$ in sorted order, $a_k - a_i \geq a_k - a_j$, so any non-adjacent pair is beaten by a pair nested inside it — which is why only $N-1$ differences need examining instead of all $\binom{N}{2}$.
- **Duplicate skills give $0$**, the smallest possible answer, and need no special handling.
- **$N \geq 2$ is guaranteed**, so there is always at least one pair and `min` never sees an empty sequence.
- **The best pair need not be at either end.** In the sample the winning difference of $3$ comes from $1$ and $4$ at the low end, but the array also has a run $9, 13$ with difference $4$ — all adjacent gaps must be compared, not just the first or last.
- **Values up to $10^9$**: differences stay well inside the integer range.

## Dry run

Values $4, 9, 1, 32, 13$, sorted to $1, 4, 9, 13, 32$.

| pair | difference |
|---|---:|
| $1, 4$ | **3** |
| $4, 9$ | 5 |
| $9, 13$ | 4 |
| $13, 32$ | 19 |

Output `3`.

---

Same problem grouped by topic: [../docs/sorting/HORSES.md](../docs/sorting/HORSES.md)
