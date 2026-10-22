[&larr; 204. Smallest Possible Whole Number](204-SMOL.md) &middot; [Index](README.md) &middot; [206. Maximise the Subsequence Sum &rarr;](206-SIGNFLIP.md)

# 205. Maximum Weight Difference

> [`MAXDIFF`](https://www.codechef.com/problems/MAXDIFF) &middot; difficulty **1308** &middot; time limit **2s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Taking an extreme K-subset |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

Chef has gone shopping with his 5-year old son. They have bought **N** items so far. The items are numbered from **1** to **N**, and the item **i** weighs **W_i** grams.

Chef's son insists on helping his father in carrying the items. He wants his dad to give him a few items. Chef does not want to burden his son. But he won't stop bothering him unless he is given a few items to carry. So Chef decides to give him some items. Obviously, Chef wants to give the kid less weight to carry.

However, his son is a smart kid. To avoid being given the bare minimum weight to carry, he suggests that the items are split into two groups, and one group contains exactly **K** items. Then Chef will carry the heavier group, and his son will carry the other group.

Help the Chef in deciding which items should the son take. Your task will be simple. Tell the Chef the maximum possible difference between the weight carried by him and the weight carried by the kid.

**Input:**

The first line of input contains an integer **T**, denoting the number of test cases. Then **T** test cases follow. The first line of each test contains two space-separated integers **N** and **K**. The next line contains **N** space-separated integers **W_1**, **W_2**, ..., **W_N**.

**Output:**

For each test case, output the maximum possible difference between the weights carried by both in grams.

**Constraints:**

- **1 ≤ T ≤ 100**

- **1 ≤ K < N ≤ 100**

- **1 ≤ W_i ≤ 100000 (10^5)**

## Constraints

- 1 ≤ T ≤ 100
- 1 ≤ K < N ≤ 100
- 1 ≤ W_i ≤ 100000 (10^5)

## Sample

**Sample input**

```
2
5 2
8 4 5 2 10
8 3
1 1 1 1 1 1 1 1
```

**Sample output**

```
17
2
```

<details><summary>Explanation</summary>

**Case #1:** The optimal way is that Chef gives his son **K=2** items with weights **2** and **4**. Chef carries the rest of the items himself. Thus the difference is: **(8+5+10) - (4+2) = 23 - 6 = 17**.

**Case #2:** Chef gives his son **3** items and he carries **5** items himself.

</details>

## Approach

The son carries exactly $K$ items and Chef carries the other $N - K$. If the chosen $K$ weigh $S$ out of a total $W$, the gap between the two loads is

$$|W - 2S|$$

Maximising that means pushing $S$ as far from $W/2$ as possible — so $S$ should be either the **smallest** possible or the **largest** possible sum of $K$ items. After sorting, those are the first $K$ and the last $K$ entries, and the answer is the larger of the two resulting gaps.

Both candidates are genuinely needed in general, which is easy to miss. The statement says Chef carries the heavier group, so intuitively the son takes the lightest items — and for sample case 1 that is right: the son takes $2 + 4 = 6$, leaving Chef $23$, a gap of $17$. Taking the two heaviest would give only $7$.

But which extreme wins depends on $K$ relative to $N$. When $K$ is large, handing the son the $K$ **heaviest** items can leave a bigger imbalance, because he is carrying most of the shipment anyway. Evaluating both and taking the maximum covers either case without needing to work out the crossover.

Sample case 2 is the degenerate one: eight identical weights mean every $K$-subset sums the same, so both candidates agree at $|8 - 6| = 2$.

The absolute value matters because the chosen group may be the heavier one; without it the second candidate would come out negative and lose the `max` spuriously.

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
        w = sorted(int(v) for v in data[pos + 2:pos + 2 + n])
        pos += 2 + n
        total = sum(w)
        # The son's K items should be the lightest or the heaviest; which one
        # wins depends on K, so evaluate both.
        lightest, heaviest = sum(w[:k]), sum(w[n - k:])
        out.append(str(max(abs(total - 2 * lightest), abs(total - 2 * heaviest))))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Both extremes must be evaluated.** Giving the son the $K$ lightest is a different outcome from the $K$ heaviest, and which wins depends on $K$ and the weights: in the first row the lightest choice gives $17$ and the heaviest only $7$.
- **All weights equal** (the second row): the answer is $|N - 2K| = |8 - 6| = 2$, not $0$ — the difference comes from the group *sizes*, since $K < N$ forces unequal counts.
- **$K < N$ is guaranteed**, so neither group is ever empty and both slices are valid.
- **The result is an absolute difference**, so it does not matter which of the two gets the larger total; taking `abs` of both candidates covers it.
- **Only the $K$ smallest or $K$ largest can be optimal**, because swapping an interior item for a more extreme one moves the two sums further apart.
- Weights up to $10^5$ with $N \leq 100$ keeps every sum small.

## Dry run

First sample: weights $8, 4, 5, 2, 10$ sorted to $2, 4, 5, 8, 10$, total $29$, $K = 2$.

| son's share | son's sum | other's sum | difference |
|---|---:|---:|---:|
| lightest two: $2, 4$ | 6 | 23 | **17** |
| heaviest two: $8, 10$ | 18 | 11 | 7 |

Output `17`.

---

Same problem grouped by topic: [../docs/sorting/MAXDIFF.md](../docs/sorting/MAXDIFF.md)
