# 452. Even Subset Xor

> CodeChef problem code [`EVENXOR`](https://www.codechef.com/problems/EVENXOR) &middot; difficulty **1714** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Even-popcount numbers form a linear subspace |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

A number $X$ is called *bad* if its binary representation contains odd number of $1$ bits. For example, $X = 13 = (1101)_2$ is bad while $X = 3 = (11)_2$ is not bad.

Chef calls an array $A$ of length $N$ **special** if the following conditions hold:
- For each $1 \le i \le N$, $0 \le A_i \lt 2^{20}$
- All the elements of $A$ are **distinct**
- There does not exist any non-empty [subset](https://en.wikipedia.org/wiki/Subset) of $A$ such that the [bitwise XOR](https://en.wikipedia.org/wiki/Bitwise_operation#XOR) of the subset is bad.

For example,
- $A = [2, 3, 4]$ is not **special** because the XOR of the subset $[2, 3]$ is $2 \oplus 3 = 1$, which is *bad*. ($\oplus$ denotes the bitwise XOR operation)
- $A = [3, 3]$ is not special because its elements are not distinct.
- $A = [3, 5]$ is special because it satisfies all the conditions.

Chef challenges you to construct **any** special array of length $N$. Can you complete Chef's challenge?

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains a single integer $N$ — the length of the special array to be constructed.

**Output**

For each test case, output a single line containing $N$ space-separated integers, denoting the elements of the special array of length $N$ you constructed.

**Note:** It can be proved that a special array of length $N$ always exists under the given constraints.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 1000$
- $0 \leq A_i \lt 2^{20}$

## Sample

**Sample input**

```
2
1
2
```

**Sample output**

```
6
3 5
```

<details><summary>Explanation</summary>

**Test Case $1$:** There is only one non-empty subset of the given array, namely $[6]$. The XOR of this subset is $6 = (110)_2$, which is not bad.

**Test Case $2$:** The given array has three non-empty subsets, namely $[3], [5]$, and $[3, 5]$.
- $[3]$ has XOR $3 = (11)_2$, which is not bad.
- $[5]$ has XOR $5 = (101)_2$, which is not bad.
- $[3, 5]$ has XOR $6 = (110)_2$, which is not bad.

None of the subsets have bad XOR, and the elements are distinct. Hence, the array is special.

</details>

## Approach

Popcount parity is **linear over XOR**:

$$\mathrm{popcount}(a \oplus b) \equiv \mathrm{popcount}(a) + \mathrm{popcount}(b) \pmod 2$$

because a bit position where $a$ and $b$ agree contributes $0$ or $2$ ones to the pair and $0$ to the XOR, while a position where they differ contributes $1$ to each side. So the even-popcount numbers are the **kernel** of a linear functional on $\mathbb{F}_2^{20}$ — a subspace of dimension $19$, closed under XOR.

That settles both directions. If every element has even popcount, every subset XOR does too, so the array is special. And conversely each singleton is a subset, so every element *must* have even popcount. The condition is therefore element-wise, with no subset enumeration anywhere.

The subspace has $2^{19} = 524288$ members, far more than the $N \leq 1000$ needed, so a simple indexing suffices:

$$A_k = 2k + \bigl(\mathrm{popcount}(k) \bmod 2\bigr), \qquad k = 1, \ldots, N$$

Doubling $k$ shifts its bits up without changing the popcount, and the low bit then repairs the parity, so $\mathrm{popcount}(A_k) = \mathrm{popcount}(k) + (\mathrm{popcount}(k) \bmod 2)$ is always even. Distinctness is immediate since $A_k \in \{2k, 2k+1\}$, and $A_k \leq 2N+1$ stays well inside $2^{20}$.

For $N = 2$ this gives `3 5` — matching the sample — because $k = 1$ needs the parity fix and $k = 2$ does too. For $N = 1$ we print `3` where the sample prints `6`; both have popcount $2$, and any special array is accepted.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for tok in data[1:1 + t]:
        n = int(tok)
        # Doubling preserves the popcount, so the low bit repairs the parity.
        out.append(" ".join(str(2 * k + (k.bit_count() & 1))
                            for k in range(1, n + 1)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
