[&larr; 495. Cybalphabit](CAB.md) &middot; [Index](../../README.md) &middot; [529. Even Edges &rarr;](EVEDG.md)

# 511. Chef and Hamming Distance of arrays

> CodeChef problem code [`CHEFHAM`](https://www.codechef.com/problems/CHEFHAM) &middot; difficulty **1790** &middot; time limit **3s**

| | |
|---|---|
| **Topic** | Constructive |
| **Technique** | Rotate sorted values by the maximum frequency |
| **Time** | $O(N\log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

**Read problems statements in [Vietnamese](https://www.codechef.com/download/translated/DEC17/vietnamese/CHEFHAM.pdf) **
.

Chef likes to work with arrays a lot. Today he has an array **A** of length **N** consisting of positive integers. Chef's little brother likes to follow his elder brother, so he thought of creating an array **B** of length **N**. The little brother is too small to think of new numbers himself, so he decided to use all the elements of array **A** to create the array **B**. In other words, array **B** is obtained by shuffling the elements of array **A**.

The little brother doesn't want Chef to know that he has copied the elements of his array **A**. Therefore, he wants to create the array **B** in such a way that the *Hamming distance* between the two arrays **A** and **B** is maximized. The Hamming distance between **A** and **B** is the number of indices **i** (1 ≤ **i** ≤ **N**) such that **A_i ≠ B_i**.

The brother needs your help in finding any such array **B**. Can you please find one such array for him?

Note that it's guaranteed that no element in **A** appears more than twice, i.e. frequency of each element is at most 2.

**Input**

- The first line of the input contains a single integer **T** denoting the number of test cases. The description of **T** test cases follows.

- The first line of each test case contains an integer **N** denoting the length of the array **A**.

- The second line contains **N** space-separated integers **A_1, A_2 ... A_N**.

**Output**

- For each test case, print two lines.

- The first line should contain the maximum possible Hamming distance that array **B** can have from array **A**.

- The second line should contain **N** space-separated integers denoting the array **B**; the **i**-th integer should denote the value of **B_i**. Note that **B** should be an array obtained after shuffling the elements of **A**.

**Constraints**

- 1 ≤ **T** ≤ 10

- 1 ≤ **N** ≤ 10^5

- 1 ≤ **A_i** ≤ 10^5

- The frequency of each integer in the array **A** will be at most 2.

**Subtasks**

**Subtask #1 (30 points):** all elements in the array **A** are unique

**Subtask #2 (30 points):** 5 ≤ **N** ≤ 10^5

**Subtask #3 (40 points):** original constraints

## Constraints

- 1 ≤ T ≤ 10
- 1 ≤ N ≤ 10^5
- 1 ≤ A_i ≤ 10^5
- The frequency of each integer in the array A will be at most 2.

## Sample

**Sample input**

```
3
2
1 2
3
1 2 1
4
2 6 5 2
```

**Sample output**

```
2
2 1
2
2 1 1
4
6 2 2 5
```

## Approach

Group equal values by sorting their original indices. Let $f$ be the maximum frequency. Rotate the sorted sequence by $f$ positions and assign the rotated values back to the original indices.

An equal-value block has length at most $f$. If $f\le N/2$, shifting by $f$ separates every block from itself. If $f>N/2$, at least $2f-N$ positions must match by pigeonhole; the rotation attains exactly this lower bound. Thus the construction maximises Hamming distance, including the small cases where full derangement is impossible.

## Solution (Python)

```python
import sys
from collections import Counter


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        a = [int(next(tokens)) for _ in range(n)]
        order = sorted(range(n), key=a.__getitem__)
        f = max(Counter(a).values())
        b = [0]*n
        for i, index in enumerate(order):
            b[index] = a[order[(i+f)%n]]
        out.append(str(sum(x != y for x,y in zip(a,b))))
        out.append(' '.join(map(str,b)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N\log N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- A single element necessarily has distance zero.
- For `[1,2,1]`, at most two positions differ.
- Print the actual distance and preserve the input multiset.

## Dry run

For `[1,2,1]`, sorted indices carry values `[1,1,2]`. Rotate by two to get `[2,1,1]`; restoring indices yields `[2,1,1]`, differing at exactly two positions.

> CodeChef tags: `Data Structures`, `Arrays`, `Algorithms`, `Constructive`

---

Same problem in rating order (#511 of 735): [../../by-rating/511-CHEFHAM.md](../../by-rating/511-CHEFHAM.md)
