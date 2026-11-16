[&larr; 673. Mexy Array](MEXYARR.md) &middot; [Index](../../README.md) &middot; [690. Maximize 1s &rarr;](MAX1S.md)

# 680. Mahesh and his lost array

> CodeChef problem code [`ANUMLA`](https://www.codechef.com/problems/ANUMLA) &middot; difficulty **2212** &middot; time limit **19.5s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Smallest unexplained subset sum is the next element |
| **Time** | $O(N \cdot 2^N)$ per test case |
| **Space** | $O(2^N)$ |
| **Roadmap course** | 2000 to 2500 difficulty problems (Level 5) |

## Question

Mahesh got a beautiful array named **A** as a birthday gift from his beautiful girlfriend Namratha. There are **N** positive integers in that array. Mahesh loved the array so much that he started to spend a lot of time on it everyday. One day, he wrote down all possible subsets of the array. Then for each subset, he calculated the sum of elements in that subset and wrote it down on a paper. Unfortunately, Mahesh lost the beautiful array :(. He still has the paper on which he wrote all subset sums. Your task is to rebuild beautiful array **A** and help the couple stay happy :)

**Input**

The first line of the input contains an integer **T** denoting the number of test cases.
First line of each test case contains one integer **N**, the number of elements in **A**.
Second line of each test case contains **2^N** integers, the values written on paper

**Output**

For each test case, output one line with **N** space separated integers in non-decreasing order.

**Constraints**

- **1** ≤ **T** ≤ **50**
- **1** ≤ **N** ≤ **15**
- **0** ≤ **Values on paper** ≤ **10^9**
- **All input values are valid. A solution always exists**

**Example**

```
**Input**
2
1
0 10
2
0 1 1 2

**Output**
10
1 1
```

**Explanation**

**Test case #2**
For the array [1,1], possible subsets are {}, {1}, {1}, {1,1}, respective sums are 0, 1, 1, 2.

## Constraints

- 1 ≤ T ≤ 50
- 1 ≤ N ≤ 15
- 0 ≤ Values on paper ≤ 10^9
- All input values are valid. A solution always exists

## Approach

Sort the $2^N$ subset sums and keep them as a multiset. Remove one 0 for the empty subset.

All elements are positive, so the smallest sum that is not yet explained by the elements found so far must be a single new element: any subset using two or more undiscovered elements, or an undiscovered element together with known ones, has a larger sum. Take it as the next element $x$. Every already known subset sum $s$ now also produces $s + x$; remove all of those from the multiset and append them to the list of known sums.

Repeat until $N$ elements are found. Scanning the sorted list once and skipping values whose multiplicity has dropped to zero yields the elements in non-decreasing order, which is the required output order.

## Solution (Python)

```python
import sys
from collections import Counter


def solve(tokens):
    n = next(tokens)
    sums_sorted = sorted((next(tokens) for _ in range(1 << n)))
    remaining = Counter(sums_sorted)
    remaining[0] -= 1
    sums = [0]
    found = []
    for value in sums_sorted:
        if remaining[value]:
            found.append(value)
            new = [v + value for v in sums]
            for v in new:
                remaining[v] -= 1
            sums += new
    return ' '.join(map(str, found))


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Complexity

- **Time:** $O(N \cdot 2^N)$ per test case
- **Space:** $O(2^N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Duplicate elements are handled by multiplicities - the Counter never goes negative on valid input.
- $N = 1$: the sums are `0` and the element.
- The list of known sums doubles each time, for $2^N$ in total.
- The output must be sorted in non-decreasing order.

## Dry run

Sums `0 1 1 2`, $N = 2$. After removing the empty subset the multiset is `{1, 1, 2}`; known sums `[0]`.

- Smallest remaining is 1: element 1. New sums `[1]`; multiset `{1, 2}`; known `[0, 1]`.
- Smallest remaining is 1: element 1. New sums `[1, 2]`; multiset empty.

Output `1 1`.

> CodeChef tags: `Data Structures`, `Sets`, `Algorithms`

---

Same problem in rating order (#641 of 735): [../../by-rating/641-ANUMLA.md](../../by-rating/641-ANUMLA.md)
