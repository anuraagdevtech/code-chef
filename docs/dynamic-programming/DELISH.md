[&larr; 588. Matrix](MATRIX2.md) &middot; [Index](../../README.md) &middot; [590. Little Elephant and Mouses &rarr;](LEMOUSE.md)

# 589. Dessert Wizard

> CodeChef problem code [`DELISH`](https://www.codechef.com/problems/DELISH) &middot; difficulty **1804** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Kadane extremes on prefixes and suffixes, joined at every split point |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

It's finally summer in Chefland! So our chef is looking forward to prepare some of the best "beat-the-heat" dishes to attract more customers. He summons the Wizard of Dessert to help him with one such dish.

 The wizard provides the chef with a sequence of **N** ingredients where the **i^th** ingredient has a delish value of **D[i]**. The preparation of the dish takes place in two phases.

**Phase 1 :** The chef chooses two indices **i** and **j** and adds the ingredients **i, i+1, ..., j** to his dish. He also finds the sum of the delish value in this range i.e **D[i] + D[i+1] + ... + D[j]**.

**Phase 2 :** The chef chooses two more indices **k** and **l** and adds the ingredients **k, k+1, ..., l** to his dish. He also finds the sum of the delish value in this range i.e **D[k] + D[k+1] + ... + D[l]**.

Note that **1**  ≤ **i**  ≤ **j** < **k**  ≤ **l** ≤ **N**.

The total delish value of the dish is determined by the absolute difference between the values obtained in the two phases. Obviously, the chef wants to maximize the total delish value for his dish. So, he hires you to help him.

**Input**

First line of input contains an integer **T** denoting the number of test cases. For each test case, the first line contains an integer **N** denoting the number of ingredients. The next line contains **N** space separated integers where the **i^th** integer represents the delish value **D[i]** of the **i^th** ingredient.

**Output**

Print the maximum delish value of the dish that the chef can get.

**Constraints**

-  **1** ≤ **T** ≤ **50**

-  **2** ≤ **N** ≤ **10000**

 -  **-1000000000 (−10^9)** ≤ **D[i]** ≤ **1000000000 (10^9)**

## Constraints

-  1 ≤ T ≤ 50
-  2 ≤ N ≤ 10000
 -  -1000000000 (−10^9) ≤ D[i] ≤ 1000000000 (10^9)

## Sample

**Sample input**

```
2
5
1 2 3 4 5
4
1 1 -1 -1
```

**Sample output**

```
13
4
```

<details><summary>Explanation</summary>

**Example case 1.**

Chef can choose **i = j = 1, k = 2, l = 5**.

The delish value hence obtained  is ** | (2+3+4+5) ? (1) | = 13 **.

**Example case 2.**

 Chef can choose **i = 1, j = 2, k = 3, l = 4**.

The delish value hence obtained  is ** | ( ( ?1 ) + ( ?1 ) ) ? ( 1 + 1 ) | = 4 **.

</details>

## Approach

The two ranges are disjoint with the first entirely to the left of the second, so some boundary separates them. For a fixed boundary the difference is largest when one side takes its maximum subarray sum and the other its minimum subarray sum.

Kadane's recurrence gives the best (and worst) non-empty subarray ending at each position; a running maximum/minimum of those gives the extremes over each prefix. The same scan from the right gives the extremes over each suffix. For every boundary evaluate both pairings, max-left minus min-right and max-right minus min-left, and keep the largest absolute value.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        values = [next(tokens) for _ in range(n)]
        prefix_min = [0] * n
        prefix_max = [0] * n
        low = high = values[0]
        prefix_min[0] = prefix_max[0] = values[0]
        for i in range(1, n):
            low = min(values[i], low + values[i])
            high = max(values[i], high + values[i])
            prefix_min[i] = min(prefix_min[i - 1], low)
            prefix_max[i] = max(prefix_max[i - 1], high)
        low = high = values[-1]
        suffix_min = suffix_max = values[-1]
        best = 0
        for i in range(n - 2, -1, -1):
            best = max(best, abs(prefix_max[i] - suffix_min), abs(prefix_min[i] - suffix_max))
            low = min(values[i], low + values[i])
            high = max(values[i], high + values[i])
            suffix_min = min(suffix_min, low)
            suffix_max = max(suffix_max, high)
        out.append(str(best))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Both ranges must be non-empty, so the Kadane variants never return an empty sum.
- All-negative or all-positive arrays still work because both a maximum and a minimum are tracked.
- Sums reach about $10^{9} \cdot N$, far beyond 32 bits.
- $N = 2$: the only choice is the two single elements.

## Dry run

`D = [1, 2, 3, 4, 5]`. The prefix minimum subarray sums are all 1 (the single element 1) and the suffix maximum sums are 14, 12, 9, 5 for suffixes starting at positions 2 to 5.

At the boundary after position 1: $|1 - 14| = 13$. Later boundaries give at most $|1 - 12| = 11$.

Answer 13.

> CodeChef tags: `Algorithms`

---

Same problem in rating order (#522 of 735): [../../by-rating/522-DELISH.md](../../by-rating/522-DELISH.md)
