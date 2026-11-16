[&larr; 694. Saving a gift of love](ASHIGIFT.md) &middot; [Index](../../README.md) &middot; [705. Palindrome In Making &rarr;](MAKEPAL3.md)

# 696. Chroma Swap

> CodeChef problem code [`ASH57`](https://www.codechef.com/problems/ASH57) &middot; difficulty **2271** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Colours present in B form free pools; pick the smallest usable value greedily |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

You have two arrays $A = A_1, A_2, \ldots, A_N$ and $B = B_1, B_2, \ldots, B_N$. Each of these elements also has a color associated with them, which is an integer. This is denoted by the arrays $ColorA_1, ColorA_2, \ldots, ColorA_N$, and $ColorB_1, ColorB_2, \ldots, ColorB_N$.

In a single operation, you can swap any element of array $A$ with any element of array $B$, if they have the same color.

Your goal is to do as many operations as you want, and eventually have the elements in array $A$ be in non-decreasing order. That is, after you are done with the operations, you want $A_1 \leq A_2 \leq \ldots \leq A_N$.

Output "Yes" if this is possible to do so, and "No" otherwise.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of five lines of input.
    - The first line of each test case contains a single integer $N$, denoting the size of the arrays.
    - The next line has $N$ integers: $A_1, A_2, \ldots, A_N$
    - The next line has $N$ integers: $ColorA_1, ColorA_2, \ldots, ColorA_N$
    - The next line has $N$ integers: $B_1, B_2, \ldots, B_N$
    - The next line has $N$ integers: $ColorB_1, ColorB_2, \ldots, ColorB_N$

**Output**

- For each testcase, in a new line, output "Yes" if it is possible to end up with the array $A$ having elements in non-decreasing order. Else, print "No".
- You may print each character of the string in uppercase or lowercase (for example, the strings YES, yEs, yes, and yeS will all be treated as identical).

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $1 \leq A_i, B_i \leq 10^9$
- $0 \leq ColorA_i, ColorB_i \leq 2N$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
3
2 
3 2
1 2 
1 2 
1 1
1
13
1
23
1
2
2 1 
2 1 
2 1
2 1
```

**Sample output**

```
Yes
Yes
No
```

<details><summary>Explanation</summary>

**Testcase 1:** The given arrays are:
- $A = [3, 2]$
- $ColorA = [1, 2]$
- $B = [1, 2]$
- $ColorB = [1, 1]$

$A_1$ and $B_1$ have the same color ($1$). So, we can swap them, and now we have the arrays as:
- $A = [1, 2]$
- $B = [3, 2]$

Now, array $A$ is sorted in non-decreasing order. So, it is possible to achieve this, and hence the answer is "Yes".

**Testcase 2:** The given arrays are:
- $A = [13]$
- $ColorA = [1]$
- $B = [23]$
- $ColorB = [1]$

We see that the array $A$ is already sorted. Hence, the answer is "Yes".

**Testcase 3:** The given arrays are:
- $A = [2, 1]$
- $ColorA = [2, 1]$
- $B = [2, 1]$
- $ColorB = [2, 1]$

We see that no matter how many operations we do, the two arrays will remain the same, and $A$ can never be sorted. Hence the answer is "No".

</details>

## Approach

If a colour occurs somewhere in $B$, then all elements of that colour in both arrays can be rearranged arbitrarily among the positions they occupy: any element of $A$ can be exchanged with the $B$ element, and that $B$ element works as a spare slot for further exchanges. If a colour does not occur in $B$, its elements in $A$ cannot be swapped at all and stay where they are.

So each position of $A$ either holds a fixed value, or may receive any still unused value from the pool of its colour (the pool being all $A$ and $B$ values of that colour). We need the resulting sequence to be non-decreasing.

Go through $A$ from left to right, remembering the previous value. At a fixed position, fail if its value is smaller than the previous one. At a free position, take the smallest unused pool value that is at least the previous value - a smaller choice keeps the running value as low as possible and saves the larger pool values for later, so it can never hurt. Pools are sorted once and each keeps a pointer, with a binary search to jump to the first usable value.

## Solution (Python)

```python
import sys
from bisect import bisect_left


def solve(tokens):
    n = next(tokens)
    first = [next(tokens) for _ in range(n)]
    first_color = [next(tokens) for _ in range(n)]
    second = [next(tokens) for _ in range(n)]
    second_color = [next(tokens) for _ in range(n)]
    active = set(second_color)
    groups = {}
    for value, color in zip(first, first_color):
        if color in active:
            groups.setdefault(color, []).append(value)
    for value, color in zip(second, second_color):
        groups.setdefault(color, []).append(value)
    for pool in groups.values():
        pool.sort()
    pointer = {}
    previous = -1
    ok = True
    for value, color in zip(first, first_color):
        if color in active:
            pool = groups[color]
            j = bisect_left(pool, previous, pointer.get(color, 0))
            if j == len(pool):
                ok = False
                break
            value = pool[j]
            pointer[color] = j + 1
        if value < previous:
            ok = False
            break
        previous = value
    return 'Yes' if ok else 'No'


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Elements of $B$ never need to be sorted; they only serve as a reservoir.
- A colour that occurs in $A$ only is frozen even if it occurs many times.
- Pool values skipped because they are too small are never needed again, since the required minimum only grows.
- Colours go up to $2N$ and are used as dictionary keys.

## Dry run

Third sample: `A = [2, 1]` with colours `[2, 1]`, `B = [2, 1]` with colours `[2, 1]`.

Pools: colour 2 holds `{2, 2}`, colour 1 holds `{1, 1}`.

- Position 1 (colour 2): the smallest pool value is 2. Previous becomes 2.
- Position 2 (colour 1): it needs a value $\ge 2$, but its pool only has ones.

Answer No.

---

Same problem in rating order (#658 of 735): [../../by-rating/658-ASH57.md](../../by-rating/658-ASH57.md)
