[&larr; 604. Can You Reach The End](604-RECHEND.md) &middot; [Index](README.md) &middot; [606. LCM Mania &rarr;](606-LCMMANIA.md)

# 605. TripTastic

> [`TRPTSTIC`](https://www.codechef.com/problems/TRPTSTIC) &middot; difficulty **2095** &middot; time limit **1 - 1.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Binary Search |
| **Technique** | Binary search on the Chebyshev radius with 2D prefix sums |
| **CodeChef tags** | `Data Structures`, `Arrays`, `Algorithms`, `Searching`, `Simple Algos`, `2D Arrays`, `Binary Search`, `Prefix Sum` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \cdot M \cdot \log \max(N, M))$ per test case |
| **Space** | $O(N \cdot M)$ |

## Question

A school wants to plan a trip for a group of $K$ students and **one** mentor.
A hotel is booked for their stay, where the rooms are formatted in form of a matrix $A$ with $N$ rows and $M$ columns. There are a total of $N\times M$ rooms where the room $(i, j)$ has a capacity of $A_{(i,j)}$ people.

The *distance* between the rooms $(i_1, j_1)$ and $(i_2, j_2)$ is given by $\max( |i_1-i_2| , |j_1-j_2| )$, where $|X|$ denotes the absolute value of $X$.

To ensure that the trip goes smoothly, the rooms should be booked in a way such that the *distance* between the mentor's room and the farthest room of a student is **minimal**.
Note that the mentor and students can stay in the **same** room.

Your task is to find the **minimal distance** between the mentor's room and the farthest room of a student.
In case the total capacity of the hotel is less than $K+1$, print $-1$ instead.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
    - The first line of each test case contains three space-separated integers $N, M,$ and $K$ — the number of rows, columns, and students, respectively.
    - The next $N$ lines contain $M$ space-separated integers each, denoting the capacity of each room.

**Output**

For each test case, output on a new line, the **minimal** distance between the mentor's room and the farthest room of a student.

In case the total capacity of the hotel is less than $K+1$, print $-1$ instead.

## Constraints

- $1 \leq T \leq 500$
- $1 \leq N, M \leq 10^{6}$
- $1 \leq K \leq 10^{9}$
- $0 \leq A_{(i,j)} \leq 10^{5}$
- The sum of $N\cdot M$ over all test cases won't exceed $10^{6}$.

## Sample

**Sample input**

```
4
1 7 5
2 1 0 1 3 0 1
2 4 3
1 0 4 0
0 2 0 3
2 2 7
1 0
4 1
3 2 3
0 2
1 0
1 0
```

**Sample output**

```
3
0
-1
1
```

<details><summary>Explanation</summary>

**Test case $1$:** Mentor can stay in room $(1, 2)$, two students in room $(1, 1)$, one student in room $(1, 4)$ and two students in room $(1, 5)$.
The farthest room of a student would be $(1, 5)$ with distance $3$.
We can show that in no other arrangement, we can achieve a distance less than $3$.

**Test case $2$:** Mentor and all $3$ students can stay in room $(1, 3)$. Thus, the distance is $0$.

**Test case $3$:** The hotel does not have enough capacity.

</details>

## Approach

With distance $\max(|\Delta i|, |\Delta j|)$, the rooms within distance $d$ of the mentor's room form a $(2d+1) \times (2d+1)$ square centred there, clipped to the hotel. Everybody fits within distance $d$ of a given mentor room exactly when that room has positive capacity (the mentor needs a place) and the square's total capacity is at least $K + 1$; who sleeps where inside the square does not matter.

Feasibility is monotone in $d$, so binary search the smallest radius. One check walks over all rooms with positive capacity and reads the clipped square's sum from a 2D prefix-sum table in $O(1)$.

If the capacity of the whole hotel is below $K + 1$ the answer is $-1$; otherwise the radius $\max(N, M) - 1$, which covers everything from any room, is always feasible.

## Solution

```python
import sys
from array import array


def main() -> None:
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    out = []
    for _ in range(next(tokens)):
        n = next(tokens)
        m = next(tokens)
        people = next(tokens) + 1
        capacity = [next(tokens) for _ in range(n * m)]
        stride = m + 1
        prefix = array('q', [0]) * ((n + 1) * stride)
        for i in range(n):
            cur = 0
            row = (i + 1) * stride
            prev = i * stride
            for j in range(m):
                cur += capacity[i * m + j]
                prefix[row + j + 1] = prefix[prev + j + 1] + cur
        if prefix[-1] < people:
            out.append('-1')
            continue

        def possible(radius):
            for i in range(n):
                top = max(0, i - radius) * stride
                bot = min(n, i + radius + 1) * stride
                for j in range(m):
                    if capacity[i * m + j]:
                        l = max(0, j - radius)
                        r = min(m, j + radius + 1)
                        if prefix[bot + r] - prefix[top + r] - prefix[bot + l] + prefix[top + l] >= people:
                            return True
            return False
        low = 0
        high = max(n, m) - 1
        while low < high:
            mid = (low + high) // 2
            if possible(mid):
                high = mid
            else:
                low = mid + 1
        out.append(str(low))
    print('\n'.join(out))


if __name__ == "__main__":
    main()
```

## Edge cases

- The mentor counts as a person: $K + 1$ places are needed.
- A room with capacity 0 cannot be the mentor's room even if its neighbourhood is large.
- Radius 0 means everybody shares the mentor's room.
- The matrix can be a single very long row or column; the prefix table is stored flat to handle any shape.

## Dry run

`1 x 7` hotel `2 1 0 1 3 0 1`, $K = 5$, so 6 places are needed.

- radius 2: the windows around the rooms with positive capacity hold `3 4 5 5 4` places - not enough.
- radius 3: the mentor in room 2 (capacity 1) reaches rooms 1-5 with total $2 + 1 + 0 + 1 + 3 = 7 \ge 6$.

Answer 3.

---

Same problem grouped by topic: [../docs/binary-search/TRPTSTIC.md](../docs/binary-search/TRPTSTIC.md)
