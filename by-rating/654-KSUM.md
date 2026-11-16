[&larr; 653. Sum of Cube ](653-SUMOFCUBE.md) &middot; [Index](README.md) &middot; [655. ABC-Strings &rarr;](655-ABCSTR.md)

# 654. Maximum K Sums

> [`KSUM`](https://www.codechef.com/problems/KSUM) &middot; difficulty **2260** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Heaps |
| **Technique** | K-way merge of the decreasing lists of sums per left endpoint |
| **CodeChef tags** | `Data Structures`, `Queues`, `Algorithms`, `Simple Algos`, `Priority Queue`, `Prefix Sum` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N + K \log N)$ |
| **Space** | $O(N + K)$ |

## Question

Chef likes arrays a lot. Today, he found an array **A** consisting of **N** positive integers.

Let **L** denote the sorted (in non-increasing order) list of size **N*(N+1)/2** containing the sums of all possible contiguous subarrays of **A**. Chef is interested in finding the first **K** elements from the list **L**. Can you help him in accomplishing this task?

**Input**

There is only a single test case per input file.

The first line of input contains two space separated integer numbers **N** and **K** denoting the size of the array and the number of the maximal sums you need to find.

The following line contains **N** space separated integer numbers denoting the array **A**.

**Output**

Output **K** space separated integers where the **i^th** integer denotes the **i^th** element of **L**.

**Constraints**

**- 1 ≤ N ≤ 10^5
**
**- 1 ≤ K ≤ min(N*(N+1)/2, 10^5)
**
**- 1 ≤ A_i ≤ 10^9
**

**Subtasks**

- Subtask 1 (47 pts) : **1 ≤ N ≤ 1000, 1 ≤ K ≤ min{N*(N+1)/2, 10^5}
**
- Subtask 2 (53 pts) : **1 ≤ N ≤ 10^5, 1 ≤ K ≤ min{N*(N+1)/2, 10^5}
**

**Example**

```
**Input 1**
<tt>3 4
1 3 4</tt>

**Output 1**
<tt>8 7 4 4</tt>

**Input 2**
<tt>3 3
10 2 7</tt>

**Output 2**
<tt>19 12 10</tt>
```

**Explanation**

**Test 1:**

<img src="https://s3.amazonaws.com/hr-challenge-images/15909/1461161918-8d79d8843c-B.png" title="B.png" />

The first **4** elements of it are **[8, 7, 4, 4]**.

## Constraints

- 1 ≤ N ≤ 10^5
- 1 ≤ K ≤ min(N*(N+1)/2, 10^5)
- 1 ≤ A_i ≤ 10^9

## Approach

All elements are positive, so for a fixed left end the subarray sum grows with the right end: the largest sum starting at $l$ is the one reaching the end of the array, the next largest stops one element earlier, and so on. That gives $N$ lists, each already sorted in decreasing order, and the task is to output the $K$ largest values of their union.

Merge them with a max-heap. Initially push, for every left end, the sum of the whole suffix. Each time the maximum is popped, output it and push the next element of the same list - the same left end with the right end moved one step left - if it is still non-empty. Sums come from prefix sums in $O(1)$.

The heap never holds more than $N$ entries and exactly $K$ pops are made.

## Solution

```python
import sys
import heapq


def main():
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    n, k = (next(tokens), next(tokens))
    values = [next(tokens) for _ in range(n)]
    prefix = [0]
    for x in values:
        prefix.append(prefix[-1] + x)
    heap = [(-(prefix[n] - prefix[i]), i, n) for i in range(n)]
    heapq.heapify(heap)
    out = []
    for _ in range(k):
        negated, left, right = heapq.heappop(heap)
        out.append(str(-negated))
        if right - 1 > left:
            heapq.heappush(heap, (-(prefix[right - 1] - prefix[left]), left, right - 1))
    print(' '.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- Equal sums from different subarrays are all reported, each as its own entry.
- A list runs out when the subarray would become empty.
- $K$ can be far smaller than $N(N+1)/2$, which is why generating all sums is avoided.
- Python's heap is a min-heap, so sums are stored negated.

## Dry run

`A = [1, 3, 4]`, `K = 4`. Suffix sums by left end: 8, 7, 4.

- pop 8 (left 1); push `[1, 3] = 4`
- pop 7 (left 2); push `[3] = 3`
- pop 4 and then the other 4 - the subarrays `[1, 3]` and `[4]`

Output `8 7 4 4`.

---

Same problem grouped by topic: [../docs/heaps/KSUM.md](../docs/heaps/KSUM.md)
