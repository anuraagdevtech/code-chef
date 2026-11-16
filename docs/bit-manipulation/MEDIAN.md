[&larr; 598. Offer for Chef](CHEFOFR.md) &middot; [Index](../../README.md) &middot; [629. NASA &rarr;](PALIXOR.md)

# 604. Little Elephant and Median

> CodeChef problem code [`MEDIAN`](https://www.codechef.com/problems/MEDIAN) &middot; difficulty **2023** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Bit Manipulation |
| **Technique** | Memoised search over bitmasks with maximal windows and dominance pruning |
| **Time** | $O(2^N \cdot N^2)$ in the worst case; pruning keeps the visited states far below that for $N \le 30$ |
| **Space** | $O(2^N)$ worst case for the memo |
| **Roadmap course** | Rise from 3* to 4* (Level 4) |

## Question

Little Elephant from Zoo of Lviv likes medians so much. Let us define **median** term for some array **A**. Let **B** be the same array **A**, but sorted in non-decreasing order. Median of **A** is **B_m** (1-based indexing), where **m** equals to **(n div 2)+1**. Here **'div'** is an integer division operation. So, for a sorted array with 5 elements, median is the 3rd element and for a sorted array with 6 elements, it is the 4th element.

Little Elephant has an array **A** with **n** integers. In one turn he can apply the following operation to any consecutive subarray **A[l..r]**: assign to all **A_i (l <= i <= r)** median of subarray **A[l..r]**.

Let **max** be the maximum integer of **A**. Little Elephant wants to know the minimum number of operations needed to change **A** to an array of **n** integers each with value **max**.

For example, let **A = [1, 2, 3]**. Little Elephant wants to change it to **[3, 3, 3]**. He can do this in two operations, first for subarray **A[2..3]** (after that **A** equals to **[1, 3, 3]**), then operation to **A[1..3]**.

**Input**

First line of the input contains single integer **T** - the number of test cases. Then **T** test cases follow, each of such format: first line - integer **n**, second line - array **A** consisted of **n** integers.

**Output**

In **T** lines print the results for each test case, one per line.

**Constraints**

1 <= **T** <= 100

1 <= **n** <= 30

1 <= **A[i]** <= 10^9

## Constraints

1 <= T <= 100
1 <= n <= 30
1 <= A[i] <= 10^9

## Sample

**Sample input**

```
2
3
1 2 3
4
2 1 1 2
```

**Sample output**

```
2
1
```

## Approach

Only one thing matters about an element: whether it already equals the maximum. Encode the array as a bitmask of those positions. An operation on $[l, r]$ turns the whole window into the maximum exactly when the median of the window is the maximum, i.e. when at least half of its entries are ones; any other operation cannot create a new maximum and is useless.

Search with memoisation on the mask:

- full mask: 0 operations;
- at least half of all positions set: 1 operation on the whole array;
- otherwise try windows. For a fixed left end only the farthest right end with a non-negative balance (ones minus zeros) is worth trying, since a larger filled window is never worse. Among the resulting masks, skip any that is a subset of another already kept one.

The answer for a state is one plus the best successor; a successor that finishes in one more operation cannot be beaten, so the loop stops at 2.

## Solution (Python)

```python
import sys
from functools import lru_cache


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        values = [next(tokens) for _ in range(n)]
        largest = max(values)
        initial = sum((1 << i for i, x in enumerate(values) if x == largest))
        full = (1 << n) - 1

        @lru_cache(None)
        def solve(mask):
            if mask == full:
                return 0
            if mask.bit_count() * 2 >= n:
                return 1
            best = n
            candidates = set()
            for start in range(n):
                balance = 0
                right = -1
                for end in range(start, n):
                    balance += 1 if mask >> end & 1 else -1
                    if balance >= 0:
                        right = end
                if right >= start:
                    new = mask | (1 << right - start + 1) - 1 << start
                    if new != mask:
                        candidates.add(new)
            ordered = sorted(candidates, key=int.bit_count, reverse=True)
            kept = []
            for state in ordered:
                if any((state | other == other for other in kept)):
                    continue
                kept.append(state)
                best = min(best, 1 + solve(state))
                if best == 2:
                    break
            return best
        out.append(str(solve(initial)))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(2^N \cdot N^2)$ in the worst case; pruning keeps the visited states far below that for $N \le 30$
- **Space:** $O(2^N)$ worst case for the memo
- Auxiliary space excludes the buffered input and output.

## Edge cases

- If every element is already the maximum the answer is 0.
- The median index is $\lfloor n/2 \rfloor + 1$, so a window with exactly half ones already works - the balance test is `>= 0`.
- A window that does not change the mask is not a move.
- The memo is per test case because the meaning of a mask depends on $N$.

## Dry run

`A = [1, 2, 3]`: mask `001` (only the last position). One of three is less than half, so one operation is not enough.

From left end 2 the window `[2, 3]` has balance 0, giving mask `011`. Now two of three positions are set, which is at least half: one more operation on the whole array finishes.

Answer 2. For `[2, 1, 1, 2]` the mask `1001` already has half of the positions, so the answer is 1.

---

Same problem in rating order (#580 of 735): [../../by-rating/580-MEDIAN.md](../../by-rating/580-MEDIAN.md)
