[&larr; 541. Birthday Gift](541-CHEFGIFT.md) &middot; [Index](README.md) &middot; [543. Ciel and Tomya &rarr;](543-CIELTOMY.md)

# 542. Lucky Sum

> [`LUCKY3`](https://www.codechef.com/problems/LUCKY3) &middot; difficulty **1875** &middot; time limit **1.43449s** &middot; Rise from 3* to 4* (Level 4)

## Topic used

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Inclusion-exclusion over per-digit thresholds with a 4-level sum-over-subsets table |
| **Complexity class** | Exponential subset DP $O(2^K K^2)$ |
| **Time** | $O(D \cdot (N \cdot D + D \cdot 4^D))$ per test case, $D \le 9$ digits |
| **Space** | $O(4^D)$ |

## Question

Chef loves lucky numbers. Everybody knows that lucky numbers are positive integers whose decimal representation contains only the lucky digits **4** and **7**. For example, numbers **47**, **744**, **4** are lucky and **5**, **17**, **467** are not.

 Chef also use term **"lucky sum"**. Lucky sum is an operation between two integers. Let the first integer is **A**, **A[i]** equals **i-th** digit of **A** (0-base numeration, from right to left) and the second integer is **B**, **B[i]** equals to **i-th** digit of **B**. Then the lucky sum of **A** and **B** is equal to **C**, **C[i] = max(A[i], B[i])**. If **i** is greater than or equal to size of integer, the **i-th** digit is equal to **0**. For example, the lucky sum of **47** and **729** equals **749**, the lucky sum of **74** and **92** and **477** equals **497**.

 Chef has an array **W** of integers. Find a number of non-empty subsequences of **W** such that the lucky sum of integers in that subsequences is a lucky number.

 Subsequence of **W** is created by erasing some number (probably zero) elements from **W**.

**Input**

First line contains one number **T**, number of test cases. Each test is formed as follows: first line contains integer **n** - number of integers in **W**, next line contains **n** integers - array **W** for corresponding test.

**Output**

For each **T** test cases print one integer - result for the corresponding test.

**Constraints**

1 <= **T** <= 10

1 <= **n** <= 50

1 <= **Wi** < 10^9

## Constraints

1 <= T <= 10
1 <= n <= 50
1 <= Wi < 10^9

## Sample

**Sample input**

```
2
2
4 7
3
43 87 44
```

**Sample output**

```
3
2
```

## Approach

Fix the length $\ell$ of the lucky result. A subsequence qualifies when no number has more than $\ell$ digits and, in each of the $\ell$ digit positions, the maximum digit is exactly 4 or exactly 7.

"Maximum is exactly 4 or 7" in one position is (max $\le 4$) $-$ (max $\le 3$) $+$ (max $\le 7$) $-$ (max $\le 6$). Expanding this over all positions gives a signed sum over threshold vectors $t \in \{3, 4, 6, 7\}^{\ell}$ of the number of non-empty subsets whose every digit is within its threshold. If $c(t)$ numbers satisfy the thresholds, that number is $2^{c(t)} - 1$.

To get all $c(t)$ at once, classify each digit into four levels ($\le 3$, 4, 5-6, 7), drop numbers containing an 8 or 9, bucket each number by its level vector in base 4, and run a prefix sum along every coordinate. The sign of a threshold vector is negative once for every coordinate at level 0 or 2. Shorter numbers are padded with leading zeros, so a subset made only of shorter numbers has maximum 0 in the leading position and is cancelled out; it is counted under its own length instead.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        numbers = [str(next(tokens)) for _ in range(n)]
        answer = 0
        for length in range(1, max(map(len, numbers)) + 1):
            padded = [s.zfill(length) for s in numbers if len(s) <= length]
            size = 4 ** length
            count_below = [0] * size
            for s in padded:
                ix = 0
                power = 1
                for ch in reversed(s):
                    d = int(ch)
                    if d > 7:
                        break
                    level = 0 if d <= 3 else 1 if d == 4 else 2 if d <= 6 else 3
                    ix += level * power
                    power *= 4
                else:
                    count_below[ix] += 1
            power = 1
            for _ in range(length):
                for base in range(0, size, power * 4):
                    for j in range(power):
                        for digit in range(1, 4):
                            count_below[base + digit * power + j] += count_below[base + (digit - 1) * power + j]
                power *= 4
            subtotal = 0
            for ix, count in enumerate(count_below):
                sign = 1
                z = ix
                for _ in range(length):
                    if z % 4 in (0, 2):
                        sign = -sign
                    z //= 4
                subtotal += sign * ((1 << count) - 1)
            answer += subtotal
        out.append(str(answer))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- Numbers with a digit 8 or 9 can never be part of a valid subsequence.
- Numbers longer than the current length are excluded for that length.
- The count is exact, not modular, so $2^{c} - 1$ is computed with big integers.
- Duplicated values are different elements and generate different subsequences.

## Dry run

`W = [43, 87, 44]`.

Length 1: no number has a single digit, so nothing is counted. Length 2: 87 is dropped because of the 8. The remaining numbers have level vectors (tens, units) = (4-level, low) for 43 and (4-level, 4-level) for 44.

Tens position: both have digit 4, so every non-empty subset has maximum 4 there. Units position: the maximum is 4 only if 44 is included. Subsets: `{44}` and `{43, 44}`.

Answer 2.

---

Same problem grouped by topic: [../docs/combinatorics/LUCKY3.md](../docs/combinatorics/LUCKY3.md)
