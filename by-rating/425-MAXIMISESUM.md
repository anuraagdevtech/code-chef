# 425. Maximise Sum

> [`MAXIMISESUM`](https://www.codechef.com/problems/MAXIMISESUM) &middot; difficulty **1715** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Per-position ceiling from prefix and suffix maxima |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

You are given an array $A$ consisting of $N$ positive integers.

You are allowed to do the following operation any number of times:

- Select two integers $l$ and $r$ such that $1 \leq l < r \leq N$;
- Change $A_i$ to $\min(A_l, A_r)$ for all $l < i < r$.

Find the **maximum** value of $\sum_{i=1}^{N} A_i$ that you can achieve after any (possibly zero) number of operations.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$ — the length of the array $A$.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$ representing the array $A$.

**Output**

For each test case, output on a new line, the maximum sum that you can achieve after any (possibly zero) number of operations.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^9$
- The sum of $N$ over all test cases won't exceed $5 \cdot 10^5$.

## Sample

**Sample input**

```
3
2
2 3
3
5 1 7
4
5 5 5 5
```

**Sample output**

```
5
17
20
```

<details><summary>Explanation</summary>

**Test case $1$:** The only possible value of $(l, r)$ can be $(1, 2)$ but that does not impact any $A_i$. Thus, the maximum sum we can achieve is $2+3=5$.

**Test case $2$:** Select $(l, r)$ as $(1, 3)$ and change $A_2=\min(A_1, A_3) = 5$. Thus, the array becomes $[5, 5, 7]$ with sum $5+5+7 = 17$.

**Test case $3$:** Since all elements of the array are same, we cannot change any $A_i$ using an operation. Thus, the maximum sum we can achieve is $5+5+5+5=20$.

</details>

## Approach

The operation only ever writes a **minimum of two existing values**, so no value in the array can rise above what is already present. Fix a position $i$: any operation that touches it uses some $l < i$ and $r > i$ and writes $\min(A_l, A_r)$, so whatever lands there is bounded by the best value available on each side:

$$A_i^{\text{final}} \;\leq\; \max\Bigl(A_i,\ \min\bigl(\max_{j<i} A_j,\ \max_{j>i} A_j\bigr)\Bigr)$$

(the outer $\max$ because we may simply leave $A_i$ alone). Positions $1$ and $N$ are never interior to any operation, so they are untouchable.

That bound is attained everywhere at once. Taking $l$ to be an argmax of the prefix and $r$ an argmax of the suffix, the single operation on $(l, r)$ raises *every* strictly-interior position to $\min$ of those two maxima, and positions already above it are only among $l$, $r$ and the ends — none of which the operation disturbs if chosen as the extreme positions. So

$$\text{answer} = \sum_{i=1}^{N} \max\Bigl(A_i,\ \min\bigl(\mathrm{pre}_{i-1},\ \mathrm{suf}_{i+1}\bigr)\Bigr)$$

with $\mathrm{pre}$ and $\mathrm{suf}$ the prefix and suffix maxima and the out-of-range entries treated as $0$.

The samples show the two regimes. $[5,1,7]$ lifts the middle to $\min(5,7) = 5$, giving $17$ — the one position that can be improved. $[5,5,5,5]$ is already flat, so nothing changes and the sum stays $20$. And $[2,3]$ has no interior position at all.

Note the operation can *lower* values, which is why every term keeps $A_i$ as a floor: for $[1,10,1]$ the middle must be left alone, since $\min(1,1) = 1$ would waste $9$.

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
        a = [int(x) for x in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        pre = [0] * (n + 1)
        for i in range(n):
            pre[i + 1] = max(pre[i], a[i])
        suf = [0] * (n + 2)
        for i in range(n - 1, -1, -1):
            suf[i + 1] = max(suf[i + 2], a[i])
        # No operation can write a value above both neighbouring maxima.
        total = sum(max(a[i], min(pre[i], suf[i + 2])) for i in range(n))
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The operation writes $\min(A_l, A_r)$**, so position $i$ can never exceed $\min(\max \text{ of the left part},\, \max \text{ of the right part})$ — and that ceiling is reached in a single operation using the two argmaxes.
- **The prefix and suffix maxima are invariant**, since every write is at most the larger of two existing values — so no sequence of operations can raise the ceiling, and one pass suffices.
- **A position already above its ceiling keeps its value**, hence the outer maximum: the operation is optional per position.
- **The two ends can never be raised**, because $l < i < r$ excludes them — their prefix or suffix maximum is empty, which the zero sentinels encode.
- **A single large value in the middle lifts nothing** unless it has company on both sides, which is why the second sample's $5$ and $7$ lift only the $1$ between them.
- **An already-uniform array gains nothing** (the third row), since every ceiling equals the value already there.
- **The zero sentinels are safe** because $A_i \geq 1$, so a real value always beats an empty side.

## Dry run

Second sample: $A = 5, 1, 7$.

| $i$ | $A_i$ | max to the left | max to the right | ceiling $\min$ | kept |
|---:|---:|---:|---:|---:|---:|
| 1 | 5 | — ($0$) | 7 | 0 | 5 |
| 2 | 1 | 5 | 7 | **5** | 5 |
| 3 | 7 | 5 | — ($0$) | 0 | 7 |

Sum $5 + 5 + 7 = $ `17`, achieved by one operation with $l = 1$, $r = 3$.

---

Same problem grouped by topic: [../docs/prefix-sums/MAXIMISESUM.md](../docs/prefix-sums/MAXIMISESUM.md)
