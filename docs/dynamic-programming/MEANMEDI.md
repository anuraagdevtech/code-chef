[&larr; 579. Blackjack](BLKJK.md) &middot; [Index](../../README.md) &middot; [581. Count palindromes &rarr;](COUNTPAL.md)

# 580. Mean Mean Medians

> CodeChef problem code [`MEANMEDI`](https://www.codechef.com/problems/MEANMEDI) &middot; difficulty **2719** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Dynamic Programming |
| **Technique** | Fixed median with cardinality-indexed subset-sum bitsets on both sides |
| **Time** | $O(N \cdot K \cdot S / w + N \cdot S)$ per test case, $S$ the largest reachable sum |
| **Space** | $O(N \cdot S / w)$ machine words |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

"Medians can't be very mean!", retorted Chef's brother. One would wish Chef's ego wouldn't
	come in the way, but Chef has taken up the challenge to prove otherwise. He asks for your help. Given N numbers, select
	K out of them, such that, the absolute difference between the mean and the median of the selected numbers, is as low
	as possible.

Mean of K numbers is defined as the sum of the numbers divided by K.

Median of K numbers is defined as the number that appears at the order index, floor((K+1)/2);
	that is, the I'th element in the sorted order of the K numbers (where numbering starts from 1),
	where I = floor((K+1)/2). Note that, if K is even, the median would be the smaller value among the two values that
	lie in the center.

Input format

The first line contains the number T, the number of test cases. In the following lines,
	T test cases follow (without any newlines between them.)
Each case consists of only 2 lines.
The first line of each test case contains N and K, separated by a single space.
The second line contains N positive integers, separated by a single space.

Output format

For each test case, print the minimum absolute difference between the mean and the median
	that you can get, by selecting any K numbers, from the N numbers. Output the result rounded to 3 digits of precision
	after the decimal.

Constraints

1 ≤ T ≤ 20

1 ≤ N ≤ 60

1 ≤ K ≤ N

1 ≤ numbers ≤ 1200

Sample input

```
2
8 2
4 9 1 3 5 9 4 10
5 4
10 7 4 5 9
```

Sample output

```
0.000
0.500
```

Explanation

In the first case, you can select [4, 4].

In the second case, you can select [10, 7, 4, 9]. The mean would be 7.500, where as
	median would be 7.

## Constraints

1 ≤ T ≤ 20
1 ≤ N ≤ 60
1 ≤ K ≤ N
1 ≤ numbers ≤ 1200

## Approach

Sort the numbers and fix which position $i$ supplies the median. With $K$ chosen numbers the median is the $\lfloor (K+1)/2 \rfloor$-th smallest, so exactly $\lfloor (K-1)/2 \rfloor$ chosen numbers come from before $i$ and $\lfloor K/2 \rfloor$ from after it.

$|\text{mean} - \text{median}| = |\text{sum} - K \cdot a_i| / K$, so we want the left sum plus the right sum to be as close as possible to $(K-1) \cdot a_i$. A knapsack indexed by how many numbers are taken, stored as big-integer bitsets, gives for every prefix the set of sums reachable with exactly the left count, and symmetrically for every suffix.

For each median position, walk over the set bits of the left bitset; for a left sum $s$ the best partner is the reachable right sum nearest to $(K-1) a_i - s$, found with two bit tricks: the highest set bit at or below the target and the lowest set bit at or above it. Stop early once a difference of zero is found, and print the best difference divided by $K$ with three decimals.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n, k = (next(tokens), next(tokens))
        values = sorted((next(tokens) for _ in range(n)))
        left_count = (k - 1) // 2
        right_count = k // 2
        dp = [1] + [0] * max(left_count, right_count)
        left = []
        for x in values:
            left.append(dp[left_count])
            for j in range(left_count, 0, -1):
                dp[j] |= dp[j - 1] << x
        dp = [1] + [0] * right_count
        right = [0] * n
        for i in range(n - 1, -1, -1):
            right[i] = dp[right_count]
            for j in range(right_count, 0, -1):
                dp[j] |= dp[j - 1] << values[i]
        best = 10 ** 9
        for i in range(left_count, n - right_count):
            left_sums = left[i]
            right_sums = right[i]
            target = values[i] * (k - 1)
            while left_sums:
                bit = left_sums & -left_sums
                s = bit.bit_length() - 1
                left_sums -= bit
                t = target - s
                if t < 0:
                    distance = s + (right_sums & -right_sums).bit_length() - 1 - target
                else:
                    lower = right_sums & (1 << t + 1) - 1
                    distance = abs(lower.bit_length() - 1 - t) if lower else 10 ** 9
                    upper = right_sums >> t
                    if upper:
                        distance = min(distance, (upper & -upper).bit_length() - 1)
                best = min(best, distance)
                if best == 0:
                    break
            if best == 0:
                break
        out.append('%.3f' % (best / k))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N \cdot K \cdot S / w + N \cdot S)$ per test case, $S$ the largest reachable sum
- **Space:** $O(N \cdot S / w)$ machine words
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $K = 1$: both counts are zero, the mean equals the median and the answer is `0.000`.
- Even $K$ uses the lower middle element, so the two sides have different sizes.
- Equal values are harmless: sorting places them consistently and any of them may act as the median.
- The target for the right sum can be negative when the left sum already overshoots; then the smallest right sum is the best partner.

## Dry run

`N = 3, K = 3`, values `[1, 2, 4]`. One number is needed on each side, so only the middle position can be the median: $a_i = 2$, target $(K-1) \cdot 2 = 4$.

Left sums `{1}`, right sums `{4}`. For $s = 1$ the wanted right sum is 3; the nearest reachable one is 4, distance 1.

Answer $1/3$, printed as `0.333`.

---

Same problem in rating order (#708 of 735): [../../by-rating/708-MEANMEDI.md](../../by-rating/708-MEANMEDI.md)
