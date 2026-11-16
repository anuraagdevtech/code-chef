[&larr; 338. Book Exercises](BEX.md) &middot; [Index](../../README.md) &middot; [609. Chefs in Queue &rarr;](CHFQUEUE.md)

# 498. Lunchtime

> CodeChef problem code [`LUNCHTIM`](https://www.codechef.com/problems/LUNCHTIM) &middot; difficulty **1773** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Stacks |
| **Technique** | Monotone groups bounded by taller students |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

There are $N$ students standing in a canteen queue, numbered $1$ to $N$ from left to right. For each valid $i$, the $i$-th student has a height $h_i$.

Two students $i$ and $j$ can see each other if there are no taller students standing between them. Formally, students $i$ and $j$ ($i \lt j$) can see each other if for each integer $k$ ($i \lt k \lt j$), $h_k \le h_i, h_j$.

For each valid $i$, determine the number $c_i$ of students that have the same height as student $i$ and can be seen by student $i$.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $h_1, h_2, \ldots, h_N$.

**Output**
For each test case, print a single line containing $N$ space-separated integers $c_1, c_2, \ldots, c_N$.

**Constraints**
- $1 \le T \le 10$
- $1 \le N \le 10^5$
- $1 \le h_i \le 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^5$

**Subtasks**
**Subtask #1 (30 points):** the sum of $N$ over all test cases does not exceed $10^3$

**Subtask #2 (70 points):** original constraints

## Constraints

- $1 \le T \le 10$
- $1 \le N \le 10^5$
- $1 \le h_i \le 10^9$ for each valid $i$
- the sum of $N$ over all test cases does not exceed $10^5$

## Sample

**Sample input**

```
1
5
1 2 2 3 2
```

**Sample output**

```
0 1 1 0 0
```

<details><summary>Explanation</summary>

**Example case 1:** Student $3$ can see students $2$ and $4$, but only student $2$ has the same height (height $2$). On the other hand, student $3$ cannot see student $5$ since student $4$ is taller and therefore blocking the view.

</details>

## Approach

Maintain a decreasing stack of height groups. Shorter groups are closed when a taller student arrives, because that student blocks any future equal-height student. Finalise a group of size $f$ by assigning $f-1$ to every member. If the current student has the height of the top group, append their index; otherwise create a new group.

Each index is inserted and finalised once. Lower students can be removed without blocking taller equal-height groups.

## Solution (Python)

```python
import sys


def main() -> None:
    tokens = iter(sys.stdin.buffer.read().split())
    out = []
    for _ in range(int(next(tokens))):
        n = int(next(tokens))
        heights = [int(next(tokens)) for _ in range(n)]
        answer = [0]*n
        stack = []
        for i, h in enumerate(heights):
            while stack and stack[-1][0] < h:
                _, group = stack.pop()
                count = len(group)-1
                for index in group:
                    answer[index] = count
            if stack and stack[-1][0] == h:
                stack[-1][1].append(i)
            else:
                stack.append((h, [i]))
        for _, group in stack:
            count = len(group)-1
            for i in group:
                answer[i] = count
        out.append(' '.join(map(str, answer)))
    sys.stdout.write("\n".join(out) + "\n")


if __name__ == "__main__":
    main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$
- Auxiliary space excludes the buffered input and output.

## Edge cases

- Count other students only, excluding the student itself.
- Equal-height intervening students do not block visibility.
- A taller student splits equal heights into different groups.

## Dry run

For `[1,2,2,3,2]`, height 1 closes alone, the two adjacent height-2 students form a group of size two, and height 3 closes that group. The final 2 stands alone: `[0,1,1,0,0]`.

> CodeChef tags: `Data Structures`, `Algorithms`

---

Same problem in rating order (#497 of 735): [../../by-rating/497-LUNCHTIM.md](../../by-rating/497-LUNCHTIM.md)
