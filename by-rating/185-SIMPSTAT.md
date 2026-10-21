# 185. Simple Statistics

> [`SIMPSTAT`](https://www.codechef.com/problems/SIMPSTAT) &middot; difficulty **1222** &middot; time limit **1s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Trimmed mean |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

Sergey has made **N** measurements. Now, he wants to know the average value of the measurements made.

In order to make the average value a better representative of the measurements, before calculating the average, he wants first to remove the highest **K** and the lowest **K** measurements. After that, he will calculate the average value among the remaining **N - 2K** measurements.

Could you help Sergey to find the average value he will get after these manipulations?

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of each test case contains two space-separated integers **N** and **K** denoting the number of measurements and the number of the greatest and the lowest values that will be removed.

The second line contains **N** space-separated integers **A_1**, **A_2**, ..., **A_N** denoting the measurements.

**Output**

For each test case, output a single line containing the average value after removing **K** lowest and **K** greatest measurements.

Your answer will be considered correct, in case it has absolute or relative error, not exceeding **10^-6**.

**Constraints**

- **1** ≤ **T** ≤ **100**

- **1** ≤ **N** ≤ **10^4**

- **0** ≤ **2K** < **N**

- **-10^6** ≤ **A_i** ≤ **10^6**

**Subtasks**

- Subtask #1 (50 points): **K = 0**

- Subtask #2 (50 points): **no additional constraints**

## Constraints

- 1 ≤ T ≤ 100
- 1 ≤ N ≤ 10^4
- 0 ≤ 2K < N
- -10^6 ≤ A_i ≤ 10^6

## Sample

**Sample input**

```
3
5 1
2 9 -10 25 1
5 0
2 9 -10 25 1
3 1
1 1 1
```

**Sample output**

```
4.000000
5.400000
1.000000
```

<details><summary>Explanation</summary>

**Example case 1.** After removing **1** greatest and **1** lowest measurement, we get the set **{2, 9, 1}**. The average value in this set is **(2+9+1)/3=4**.

**Example case 2.** The average value in the set **{2, 9, -10, 25, 1}** is **(2+9-10+25+1)/5=5.4**.

**Example case 3.** After removing the **1** largest and smallest measurements, Sergey will be left with only one measurement, i.e. **1**. Average of this is **1** itself.

</details>

## Approach

Sort the measurements, discard the first $K$ and the last $K$, and average what remains. In Python the trimmed slice is `a[k:n-k]`, and the mean is its sum over its length.

This is the **trimmed mean**, a standard robust statistic: dropping the extremes keeps a few wild readings from dragging the average around. Sample cases 1 and 2 show the effect on the same data — with $K = 1$ the mean is $4$, but with $K = 0$ the outlier $25$ pulls it to $5.4$.

The constraint $2K < N$ guarantees at least one measurement survives, so the division never hits zero. That is worth noticing, since $K$ can be large relative to $N$: sample case 3 trims $[1,1,1]$ down to a single value.

Two practical points. Measurements may be **negative** (down to $-10^6$), so the sum can be negative and no clamping is appropriate. And the output must carry enough precision — printing with six decimal places via an f-string comfortably satisfies the stated tolerance of $10^{-6}$ absolute or relative error.

Doing the sum in integers and dividing once at the end keeps the arithmetic exact up to the final division, which avoids accumulating floating-point drift across up to $10^4$ additions.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        a = sorted(int(v) for v in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        kept = a[k:n - k]          # 2k < n guarantees this is non-empty
        # Sum in integers, divide once, to avoid accumulating float error.
        out.append(f"{sum(kept) / len(kept):.6f}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **$K = 0$ trims nothing** (the second row): the slice must be `a[0:n]`, so writing the bounds as `a[k:n-k]` rather than special-casing zero is what keeps this correct.
- **$2K < N$ is guaranteed**, so the kept slice always holds at least one element and the division is never by zero.
- **Negative values must sort numerically.** The $-10$ in the first two rows is trimmed at $K = 1$ but counted at $K = 0$; sorting the raw byte tokens would place `-10` by its leading `-` instead of its value.
- **Summing in integers and dividing once** keeps the result exact until the final division, avoiding the drift of a running float average.
- **Equal values trimmed from both ends** (the third row, all ones): the answer is still exact, and six decimal places are required in the output.

## Dry run

First sample: $N = 5$, $K = 1$, values $2, 9, -10, 25, 1$.

| step | result |
|---|---|
| sorted | $-10, 1, 2, 9, 25$ |
| trim $K=1$ from each end | drop $-10$ and $25$ |
| kept | $1, 2, 9$ |
| sum / count | $12 / 3$ |
| output | `4.000000` |

With $K = 0$ the same values give $27 / 5 = $ `5.400000`, as in the second row.

---

Same problem grouped by topic: [../docs/sorting/SIMPSTAT.md](../docs/sorting/SIMPSTAT.md)
