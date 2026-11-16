[&larr; 656. Saving a gift of love](656-ASHIGIFT.md) &middot; [Index](README.md) &middot; [658. Chroma Swap &rarr;](658-ASH57.md)

# 657. Longest Subarray

> [`LONGESTARRAY`](https://www.codechef.com/problems/LONGESTARRAY) &middot; difficulty **2267** &middot; time limit **1.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Two pointers with per-bit counts - every bit must appear both inside and outside |
| **CodeChef tags** | `Mathematics`, `Bit Manipulation`, `Algorithms`, `Simple Algos`, `Bitwise Operation`, `Prefix Sum` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(30 \cdot N)$ per test case |
| **Space** | $O(30 \cdot N)$ |

## Question

You are given an array $A$ of length $N$.

Find the **maximum length** of any subarray of $A$, such that, the [bitwise OR](https://en.wikipedia.org/wiki/Bitwise_operation#OR) of all the elements of the subarray is equal to the [bitwise OR](https://en.wikipedia.org/wiki/Bitwise_operation#OR) of the remaining elements of the array.

Report $-1$ if no such subarray exists.

Note:
- A subarray is formed by deleting some (possibly zero) elements from the beginning of the array and some (possibly zero) elements from the end of the array.
- The bitwise OR of an empty array is considered to be $0$.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains an integer $N$ — the length of the array $A$.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$ representing the array $A$.

**Output**

For each test case, output on a new line, the **length** of **longest** subarray such that the bitwise OR of all elements of the subarray is equal to the bitwise OR of the remaining elements of the array, or output $-1$ if no such subarray exists.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 5 \cdot 10^5$
- $1 \leq A_i \lt 2^{30}$
- The sum of $N$ over all test cases won't exceed $5 \cdot 10^5$.

## Sample

**Sample input**

```
3
3
1 2 4
3
1 3 2
4
2 3 4 7
```

**Sample output**

```
-1
1
3
```

<details><summary>Explanation</summary>

**Test case $1$:** For no subarray of $A$, the bitwise OR of the elements of the subarray equals the bitwise OR of the remaining elements.

**Test case $2$:** Consider the subarray $[3]$ having length $1$. The bitwise OR of the subarray is $3$ and the bitwise OR of the remaining elements of the array is $1 | 2 = 3$. Thus, the bitwise OR of all elements of the subarray is equal to the bitwise OR of the remaining elements of the array.

**Test case $3$:** Consider the subarray $[2, 3, 4]$ having length $3$. The bitwise OR of the subarray is $2|3|4 = 7$ and the bitwise OR of the remaining elements of the array is $7$. Thus, the bitwise OR of all elements of the subarray is equal to the bitwise OR of the remaining elements of the array.

</details>

## Approach

The OR of the subarray and the OR of the rest are both submasks of the OR of the whole array, and together they cover it. If they are equal, both equal the total OR. So the condition is: every bit that occurs in the array occurs at least once inside the window and at least once outside it.

"At least once outside" means the window must not contain *all* occurrences of any bit; this property is lost by growing the window and regained by shrinking it. So for every right end, advance the left end while some bit has all its occurrences inside - this gives the longest window ending there that leaves every bit outside. If that window also contains every bit it is a valid answer; if it does not, no shorter window ending at the same place can, since shrinking only loses bits.

Maintain for every bit its count inside the window, the number of distinct bits present inside, and the number of bits whose inside count equals their total count.

## Solution

```python
import sys


def solve(tokens):
    n = next(tokens)
    values = [next(tokens) for _ in range(n)]
    bits = []
    total = [0] * 30
    for x in values:
        own_bits = []
        while x:
            z = x & -x
            k = z.bit_length() - 1
            own_bits.append(k)
            total[k] += 1
            x -= z
        bits.append(own_bits)
    active = sum((v > 0 for v in total))
    inside = [0] * 30
    have = bad = left = 0
    best = -1
    for right, own_bits in enumerate(bits):
        for k in own_bits:
            if inside[k] == 0:
                have += 1
            inside[k] += 1
            if inside[k] == total[k]:
                bad += 1
        while bad:
            for k in bits[left]:
                if inside[k] == total[k]:
                    bad -= 1
                inside[k] -= 1
                if not inside[k]:
                    have -= 1
            left += 1
        if have == active:
            best = max(best, right - left + 1)
    return str(best)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- A bit that occurs only once in the whole array makes the answer $-1$.
- $N = 1$: the remaining part is empty and can never match.
- The window is always a proper subarray because the "outside" condition forbids taking everything.
- Each element's set bits are extracted once and reused when it enters and leaves the window.

## Dry run

`A = [2, 3, 4, 7]`. Bit totals: bit 0 twice (3, 7), bit 1 three times (2, 3, 7), bit 2 twice (4, 7).

- right end at 4 (index 3): window `[2, 3, 4]` contains bit 0 once, bit 1 twice, bit 2 once - none completely, and all three bits are present. Length 3 is valid.
- right end at 7: the window `[2, 3, 4, 7]` would contain every occurrence of every bit, so the left end moves right until each bit has an occurrence outside again; that leaves only `[7]`, length 1.

Answer 3.

---

Same problem grouped by topic: [../docs/bit-manipulation/LONGESTARRAY.md](../docs/bit-manipulation/LONGESTARRAY.md)
