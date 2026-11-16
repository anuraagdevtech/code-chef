[&larr; 582. Maximum And Or](582-MAXANDOR.md) &middot; [Index](README.md) &middot; [584. Gold Mining &rarr;](584-GOLMINE.md)

# 583. No sequence

> [`NOSEQ`](https://www.codechef.com/problems/NOSEQ) &middot; difficulty **2031** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Balanced base-K digits read off from the residue |
| **CodeChef tags** | `Algorithms`, `Mathematics`, `Simple Algos` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

Alice gave Bob $3$ integers $N, K,$ and $S$. Help Bob find an $S$-good sequence.

A sequence $B$ of length $N$ is called $S$-good if the following conditions are met:
- $B_i \in \{-1, 0, 1\}$ for each $1 \leq i \leq N$
- $\sum_{i=1}^N B_i\cdot K^{i-1} = S$

If there are multiple $S$-good sequences, print **any** of them.
**If no $S$-good sequence exists, print $-2$.**

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line of input containing three space-separated integers — $N, K, $ and $S$.

**Output**

For each test case:
- If no $S$-good sequence exists, print $-2$.
- Otherwise, output $N$ space-separated integers denoting the $S$-good sequence.

If multiple $S$-good sequences exist, you may print any of them.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq N \leq 100$
- $2 \leq K \leq 100$
- $1 \leq S \leq 10^{18}$

## Sample

**Sample input**

```
3
4 2 15
3 6 36
5 5 7
```

**Sample output**

```
1 1 1 1
0 0 1
-2
```

<details><summary>Explanation</summary>

**Test case $1$:** We have $B = [1,1,1,1]$ and $S = 15$
$\sum_{i=1}^N B_i\cdot K^{i-1} = 1\cdot 1 + 2\cdot 1 + 4\cdot 1 + 8\cdot 1 = 15$, hence $B$ is an $S$-good sequence.

**Test case $2$:** We have $B = [0, 0, 1]$ and $S = 36$. $6^2 = 36$ so clearly $B$ is $S$-good.

**Test case $3$:** No $S$-good sequence of length $5$ exists.

</details>

## Approach

The sum is a base-$K$ expansion of $S$ whose digits are restricted to $-1, 0, 1$. Look at it modulo $K$: only $B_1$ matters, so $B_1 \equiv S \pmod K$.

For $K > 2$ the residues $0$, $1$ and $K - 1$ correspond to the digits $0$, $1$ and $-1$ and are all different, so the digit is forced; any other residue makes the task impossible. Subtract the digit, divide by $K$ and continue with the next position. After $N$ digits the remaining value must be 0.

For $K = 2$ the residues 1 and $K - 1$ coincide and the code takes the digit $+1$, which produces the ordinary binary representation. That is sufficient: with digits in $\{-1, 0, 1\}$ the largest reachable value is $2^N - 1$, and every positive $S$ up to that bound is already reached by plain binary.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        k = next(tokens)
        target = next(tokens)
        digits = []
        ok = True
        for i in range(n):
            residue = target % k
            if residue == 0:
                digit = 0
            elif residue == 1:
                digit = 1
            elif residue == k - 1:
                digit = -1
            else:
                ok = False
                digit = 0
            digits.append(digit)
            target = (target - digit) // k
        out.append(' '.join(map(str, digits)) if ok and target == 0 else '-2')
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- A residue other than $0$, $1$, $K-1$ means no sequence exists.
- $S$ too large for $N$ digits leaves a non-zero remainder at the end.
- The digit $-1$ makes the quotient round up: $(S + 1) / K$.
- Any valid sequence is accepted; for $K > 2$ it is unique anyway.

## Dry run

`N = 3, K = 6, S = 36`:

| step | value | residue | digit | next value |
|---:|---:|---:|---:|---:|
| 1 | 36 | 0 | 0 | 6 |
| 2 | 6 | 0 | 0 | 1 |
| 3 | 1 | 1 | 1 | 0 |

Output `0 0 1`. For `N = 5, K = 5, S = 7` the first residue is 2, so the answer is `-2`.

---

Same problem grouped by topic: [../docs/constructive/NOSEQ.md](../docs/constructive/NOSEQ.md)
