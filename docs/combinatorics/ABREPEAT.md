# 484. Bear and AB

> CodeChef problem code [`ABREPEAT`](https://www.codechef.com/problems/ABREPEAT) &middot; difficulty **1754** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Combinatorics |
| **Technique** | Splitting pairs into within-copy and across-copy |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Limak has a string **S**, that consists of **N** lowercase English letters.
Limak then created a new string by repeating **S** exactly **K** times.
For example, for **S** = "abcb" and **K** = 2, he would get "abcbabcb".

Your task is to count the number of subsequences "ab" (not necessarily consecutive) in the new string.

In other words, find the number pairs of indices i < j, such that the i-th and j-th characters in the new string are 'a' and 'b' respectively.

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows.

The first line of each test case contains two integers **N** and **K**, denoting the length of the initial string **S** and the number of repetitions respectively.

The second line contains a string **S**.
Its length is exactly **N**, and each of its characters is a lowercase English letter.

**Output**

For each test case, output a single line containing one integer — the number of subsequences "ab" in the new string.
For the given constraints, it can be proved that the answer fits in the 64-bit signed type.

**Constraints**

- 1 ≤ **T** ≤ 10

- 1 ≤ **N** ≤ 10^5

- 1 ≤ **N** * **K** ≤ 10^9 (in other words, the new string has length up to 10^9)

## Constraints

- 1 ≤ T ≤ 10
- 1 ≤ N ≤ 10^5
- 1 ≤ N * K ≤ 10^9 (in other words, the new string has length up to 10^9)

## Sample

**Sample input**

```
3
4 2
abcb
7 1
aayzbaa
12 80123123
abzbabzbazab
```

**Sample output**

```
6
2
64197148392731290
```

<details><summary>Explanation</summary>

**Test case 1.** Limak repeated the string "abcb" 2 times, and so he got "abcbabcb". There are 6 occurrences of the subsequence "ab":

- ABcbabcb (the two letters marked uppercase)

- AbcBabcb

- AbcbaBcb

- AbcbabcB

- abcbABcb

- abcbAbcB

**Test case 2.** Since **K** = 1, the new string is equal to the given **S** ("aayzbaa"). There are 2 occurrences of the subsequence "ab" in this string: AayzBaa and aAyzBaa.

</details>

## Approach

The repeated string has length up to $10^9$, so the count must come from $S$ alone. Split the pairs by which copies they span.

**Within one copy.** Let $P$ be the number of `ab` subsequences inside $S$, computed in one pass by keeping a running count of `a`s seen and adding it at each `b`. Each of the $K$ copies contributes $P$.

**Across two copies.** For copies $u < v$, *every* `a` in copy $u$ precedes *every* `b` in copy $v$, so the pair contributes $a \cdot b$ where $a$ and $b$ are the letter counts in $S$. There are $\binom{K}{2}$ such ordered copy pairs. So

$$\text{answer} = K \cdot P \;+\; a \cdot b \cdot \frac{K(K-1)}{2}$$

The decomposition works precisely because position order between copies is total — no comparison inside $S$ is needed for the cross terms, which is what turns an apparently quadratic count into one linear pass.

The magnitudes are the real trap: with $NK \leq 10^9$ the answer reaches about $10^{17}$, so C++ needs `long long` (the statement says as much), while Python's integers are unbounded.

The samples check both terms. `abcb` with $K = 2$ has $P = 2$ and $a \cdot b = 1 \cdot 2 = 2$, giving $2 \cdot 2 + 2 \cdot 1 = 6$. `aayzbaa` with $K = 1$ has no cross term at all, leaving $P = 2$ — only the two leading `a`s precede the single `b`. And the third sample's $K \approx 8 \times 10^7$ makes the cross term dominate completely.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        k = int(data[2 + 3 * i])
        s = data[3 + 3 * i]
        seen_a = 0
        inside = 0
        for c in s:
            if c == 0x61:
                seen_a += 1
            elif c == 0x62:
                inside += seen_a
        total_b = s.count(0x62)
        # Every 'a' of an earlier copy precedes every 'b' of a later one.
        out.append(str(k * inside + seen_a * total_b * (k * (k - 1) // 2)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **The pairs split into two kinds**: both characters inside one copy, or the `a` in an earlier copy and the `b` in a later one.
- **Within-copy pairs are counted once per copy**, so the single-copy count multiplies by $K$.
- **Across-copy pairs multiply by $\binom{K}{2}$**, since *every* `a` of the earlier copy precedes *every* `b` of the later one — giving $(\text{total } a) \times (\text{total } b)$ per ordered pair of copies.
- **$K = 1$ leaves only the within-copy term**, as $\binom{1}{2} = 0$ (the second sample row).
- **The answer is huge**: at $NK \leq 10^9$ the count reaches about $6 \times 10^{16}$, past 32-bit and into the upper reaches of 64-bit.
- **Characters other than `a` and `b` are ignored**, but they still occupy positions — which is why the counting is by letter rather than by index.
- **A string with no `a` or no `b`** gives $0$ from both terms.

## Dry run

First sample: $S = $ `abcb` repeated $K = 2$ times, giving `abcbabcb`.

| quantity | value |
|---|---:|
| `a`s in one copy | 1 |
| `b`s in one copy | 2 |
| `ab` pairs inside one copy | 2 |
| within-copy total, $K \times 2$ | 4 |
| copy pairs, $K(K-1)/2$ | 1 |
| across-copy total, $1 \times 2 \times 1$ | 2 |

Total `6`.

> CodeChef tags: `Data Structures`, `Mathematics`

---

Same problem in rating order (#454 of 486): [../../by-rating/454-ABREPEAT.md](../../by-rating/454-ABREPEAT.md)
