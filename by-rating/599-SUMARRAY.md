[&larr; 598. Double Burgers](598-BURGER.md) &middot; [Index](README.md) &middot; [600. Equivalent Numbers &rarr;](600-EQUIVALENT.md)

# 599. Array Sum

> [`SUMARRAY`](https://www.codechef.com/problems/SUMARRAY) &middot; difficulty **2077** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Start from the minimum array and raise elements in steps of two |
| **CodeChef tags** | `Algorithms`, `Constructive` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

You are given an **even** integer $N$ and an integer $K$.
Generate an array $A$ of size $N$ such that:
- $1 \le A_i \le 10^5$ for all $1\le i \le N$;
- The number of **odd** elements in the array is same as the number of **even** elements.
- The sum of all elements of the array is $K$.

If multiple such arrays exist, print any. If no such array exists, print $-1$ instead.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two space-separated integers $N$ and $K$ — the size of the array and the required sum.

**Output**

For each test case, output on a new line, $N$ space-separated integers, denoting the array $A$ satisfying the given conditions.

If multiple such arrays exist, print any. If no such array exists, print $-1$ instead.

## Constraints

- $1 \leq T \leq 1000$
- $2 \leq N \leq 10^5$, $N$ is even
- $1 \leq K \leq 10^9$
- The sum of $N$ over all test cases won't exceed $10^6$.

## Sample

**Sample input**

```
3
2 5
4 1
4 20
```

**Sample output**

```
4 1
-1
3 4 5 8
```

<details><summary>Explanation</summary>

**Test case $1$:** Consider the array $A = [4, 1]$. It contains $1$ even as well as $1$ odd element. Also, the sum of elements of the array is $4+1=5$.

**Test case $2$:** It can be proven that there exists no array which satisfies the given conditions.

**Test case $3$:** Consider the array $A = [3, 4, 5, 8]$. It contains $2$ even as well as $2$ odd elements. Also, the sum of elements of the array is $3+4+5+8 = 20$.

</details>

## Approach

Half of the elements must be odd and half even. The smallest such array is $N/2$ ones and $N/2$ twos with sum $3N/2$; the largest uses 99999 for the odd half and 100000 for the even half, sum $199999 \cdot N/2$.

Changing an element without changing its parity moves the sum by a multiple of 2, so the parity of $K$ must equal the parity of the minimum sum. Conversely, if $K$ lies between the two bounds and $K - 3N/2$ is even, distribute $(K - 3N/2)/2$ steps of $+2$ greedily: each element can take up to 49999 steps (1 up to 99999, 2 up to 100000). The total capacity is exactly the gap between the bounds, so the greedy always fits.

## Solution

```python
import sys


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        k = next(tokens)
        half = n // 2
        smallest = 3 * half
        largest = 199999 * half
        if k < smallest or k > largest or (k - smallest) % 2:
            out.append('-1')
            continue
        result = [1] * half + [2] * half
        steps = (k - smallest) // 2
        for i in range(n):
            take = min(steps, 49999)
            result[i] += 2 * take
            steps -= take
        out.append(' '.join(map(str, result)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- $K$ below $3N/2$ or above $199999 \cdot N/2$: print $-1$.
- Wrong parity of $K - 3N/2$: print $-1$.
- Elements may repeat; only the range and the parity balance are required.
- Any valid array is accepted, so the judge uses a checker.

## Dry run

`N = 4, K = 20`. Minimum array `1 1 2 2` with sum 6; the gap 14 is even, so 7 steps of $+2$ are needed.

The first element takes all 7: $1 + 14 = 15$.

Output `15 1 2 2` - two odd, two even, sum 20.

---

Same problem grouped by topic: [../docs/constructive/SUMARRAY.md](../docs/constructive/SUMARRAY.md)
