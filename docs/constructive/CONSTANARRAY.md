[&larr; 718. Tree Distances](TDISTS.md) &middot; [Index](../../README.md) &middot; [723. Smallest Difference &rarr;](SMALLESTDIFF.md)

# 721. Construct An Array

> CodeChef problem code [`CONSTANARRAY`](https://www.codechef.com/problems/CONSTANARRAY) &middot; difficulty **2419** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Blocks of M distinct values keep all frequencies within one of each other |
| **Time** | $O(N + M)$ expected per test case |
| **Space** | $O(N + M)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

You are given a positive integer $M$ and an array $A \ (1 \leq A_i \leq M)$ consisting of $N$ positive integers.

Construct an array $B$ of length $N$ such that:
- $1 \leq B_i \leq M$ for all $1 \leq i \leq N$;
- For all $1 \leq i \leq N$, there does not exist an index $1 \leq j \leq i$ such that the frequency of $B_j$ is more than that of $A_i$ in the subarray $[B_1, B_2, \ldots, B_i]$

It can be proved that at least one such array $B$ exists for any array $A$.
If there are multiple valid arrays, you can print any one.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains two space separated integers $N$ and $M$ — the length of the array $A$ and upper bound on $A_i$.
    - The second line of each test case contains $N$ space-separated integers $A_1,A_2,\ldots,A_N$ representing the array $A$.

**Output**

For each test case, output on a new line, $N$ space-separated integers representing a valid array $B$.

It can be proved that at least one such array $B$ exists for any array $A$.
If there are multiple valid arrays, you can print any one.

## Constraints

- $1 \leq T \leq 2000$
- $1 \leq N \leq 2000$
- $1 \leq M \leq N$
- $1 \leq A_i \leq M$
- The sum of $N$ over all test cases won't exceed $2000$.

## Sample

**Sample input**

```
4
1 1
1
3 2
1 1 1
3 2
1 1 1
4 4
1 2 3 4
```

**Sample output**

```
1
1 1 1
1 2 1
1 2 3 4
```

<details><summary>Explanation</summary>

**Test case $1$:** Consider the array $B = [1]$. The only subarray is $[1]$ where the frequency of $B_1$ is less than equal to that of $A_1$.

**Test case $2$:** Consider the array $B = [1, 1, 1]$.
- For $i=1$: The frequency of both $A_1$ and $B_1$ in subarray $[B_1]$ is $1$.
- For $i=2$: The frequency of $A_2$ is same as that of $B_1, B_2$ in subarray $[B_1, B_2]$.
- For $i=3$: The frequency of $A_3$ is same as that of $B_1, B_2, B_3$ in subarray $[B_1, B_2, B_3]$.

**Test case $3$:** Consider the array $B = [1, 2, 1]$.
- For $i=1$: The frequency of both $A_1$ and $B_1$ in subarray $[B_1]$ is $1$.
- For $i=2$: The frequency of $A_2$ is same as that of $B_1$ and $B_2$ in subarray $[B_1, B_2]$.
- For $i=3$: The frequency of $A_3$ is same as that of $B_1, B_3$ and higher than $B_2$ in subarray $[B_1, B_2, B_3]$.

</details>

## Approach

The condition says that after every prefix, $A_i$ must be one of the most frequent values of $B_1 \dots B_i$.

Build $B$ in consecutive blocks of $M$ positions, each block being a permutation of $1 \dots M$. Then after any prefix every value has occurred either $q$ or $q + 1$ times, where $q$ is the number of completed blocks, and the values with $q + 1$ occurrences are exactly those already placed in the current block.

So at position $i$ it is enough to make sure that $A_i$ has been placed in the current block: if $A_i$ is still unused in this block, place it now; otherwise it was placed earlier in the block and any unused value can go here. Either way $A_i$ has frequency $q + 1$, the maximum.

Two sets track which values are still available in the current block; when the block is full they are reset.

## Solution (Python)

```python
import sys


def solve(tokens):
    n, m = (next(tokens), next(tokens))
    wanted = [next(tokens) for _ in range(n)]
    result = []
    used = set()
    unused = set(range(1, m + 1))
    for want in wanted:
        if not unused:
            unused = set(range(1, m + 1))
            used.clear()
        if want in unused:
            pick = want
            unused.remove(pick)
        else:
            pick = unused.pop()
        used.add(pick)
        result.append(pick)
    return ' '.join(map(str, result))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(N + M)$ expected per test case
- **Space:** $O(N + M)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- $M = 1$: the array is all ones.
- The last block may be incomplete, which is fine.
- When $A_i$ was already used in the block, the filler value is arbitrary.
- Many arrays are valid, so the output is validated by a checker.

## Dry run

`N = 3, M = 2, A = [1, 1, 1]`.

- position 1: 1 is unused in the block - place 1.
- position 2: 1 is already used - place the other value, 2. The block `1 2` is complete; both values have frequency 1.
- position 3: new block, place 1. Frequencies: 1 twice, 2 once.

Output `1 2 1`.

---

Same problem in rating order (#685 of 735): [../../by-rating/685-CONSTANARRAY.md](../../by-rating/685-CONSTANARRAY.md)
