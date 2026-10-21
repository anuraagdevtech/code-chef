# 296. IPC Trainers

> [`IPCTRAIN`](https://www.codechef.com/problems/IPCTRAIN) &middot; difficulty **1500** &middot; time limit **2.5s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Exchange argument with a max-heap |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O((N + D) \log N)$ per test case |
| **Space** | $O(N + D)$ |

## Question

During the Indian Programming Camp (IPC), there are **N** trainers. The camp runs for **D** days. Each day, there can be at most one lecture. The i-th trainer arrives on day **D**_i and then stays till the end of the camp. He also wants to teach exactly **T**i lectures. For each lecture that a trainer was not able to teach, he will feel sad and his sadness level will be increased by **S_i**.

You are the main organizer of the contest. You want to find minimum total sadness of the trainers.

**Input**

The first line of the input contains an integer **T**, denoting the number of testcases.

For each test case, the first line contains two space separated integers, **N, D**.

The i-th of the next **N** lines will contain three space separated integers: **D**_i, **T**_i, **S**_i respectively.

**Output**

For each test case, output a single integer corresponding to the minimum total sadness of the trainers achievable.

**Constraints**

- 1 ≤ **T** ≤ 10

- 1 ≤ **N, D** ≤ 10^5

- 1 ≤  **D**_i,  **T**_i ≤ D

- 1 ≤  **S**_i ≤ 10^5

**Subtasks**

**Subtask #1 (40 points)**

- 1 ≤ **T** ≤ 10

- 1 ≤ **N, D** ≤ 10^3

- 1 ≤  **D**_i,  **T**_i ≤ D

- 1 ≤  **S**_i ≤ 10^3

**Subtask #2 (60 points)**

- Original constraints

## Constraints

- 1 ≤ T ≤ 10
- 1 ≤ N, D ≤ 10^5
- 1 ≤  D_i,  T_i ≤ D
- 1 ≤  S_i ≤ 10^5

## Sample

**Sample input**

```
3
2 3
1 2 300
2 2 100
2 3
1 1 100
2 2 300
2 3
3 2 150
1 1 200
```

**Sample output**

```
100
0
150
```

<details><summary>Explanation</summary>

**Example case 1**. Both the first and second trainer want to take exactly two lectures. The first trainer arrives on the 1st day and the second trainer arrives on the 2nd day. Consider a schedule where the first trainer takes the first two lectures, and the second trainer takes the last lecture on the day 3. This way the second trainer will take only one lecture but wanted to take two. Thus, his sadness will be 100. The first trainer took all the lectures that he wanted to take (ie. two lectures). Thus the total sadness is 100 + 0 = 100. You can check that no other way of assigning trainers to the days will give a better answer than this.

**Example case 2**. In this case, the trainers can all take all their ideal number of lectures.

**Example case 3**. In this case, the first trainer arrives on day 3 and wants to take two lectures. This is not possible as he can take at most one lecture on day 3 and the camp ends on day 3. The second trainer wants to take only one lecture which he can take on any one of the 1st or 2nd days. You can see that in one of the first or second days, no lecture will be held.

</details>

## Approach

Flip the objective. If nothing were scheduled the sadness would be the fixed total $\sum T_i S_i$, so minimising sadness is the same as **maximising the sadness avoided**, and each lecture granted to trainer $i$ avoids exactly $S_i$. Since there is at most one lecture per day, we are choosing which trainer gets each of the $D$ days.

A trainer arrives on day $D_i$ and stays to the end, so their availability is a **suffix** of days — trainer $i$ can use any day $\geq D_i$, up to $T_i$ of them. Walking days forward, the set of candidates only grows as trainers arrive.

The greedy is: on each day give the lecture to the available trainer with the largest $S_i$ who still wants lectures. The exchange argument is short. Suppose an optimal schedule gives day $d$ to trainer $y$ while trainer $x$ with $S_x > S_y$ is available on $d$ and has an unused quota. If $x$ is idle at some later day, swap — $x$ gains a lecture and $y$ loses one, changing the total by $S_x - S_y > 0$. If $x$ is busy on every later day, swap day $d$ with any one of them, which leaves the multiset of assignments unchanged. Either way the greedy choice is no worse.

Because availability is a suffix, a trainer once available never becomes unavailable, so a **max-heap keyed on $S_i$** is enough: bucket trainers by arrival day, push them as that day comes round, and each day serve the heap's top, decrementing its remaining lectures and popping when it hits zero.

The three samples show the three shapes. In the first, the $300$-trainer takes days 1 and 2 and the $100$-trainer gets only day 3, leaving one missed $100$-lecture. In the second, there is just enough room for everyone, so the answer is $0$. In the third, the $150$-trainer only arrives on day 3, so day 2 goes **unused** even though lectures are still wanted — a greedy that tried to pack days densely without respecting arrival would wrongly report $0$.

## Solution

```python
import heapq
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, d = int(data[pos]), int(data[pos + 1])
        pos += 2
        arriving = [[] for _ in range(d + 1)]
        total = 0
        for _ in range(n):
            day, want, sad = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
            pos += 3
            total += want * sad
            arriving[day].append([-sad, want])      # negated for a max-heap
        heap = []
        avoided = 0
        for day in range(1, d + 1):
            for trainer in arriving[day]:
                heapq.heappush(heap, trainer)
            if heap:
                top = heap[0]
                avoided -= top[0]
                # Only the quota changes, never the key, so the heap stays valid.
                top[1] -= 1
                if top[1] == 0:
                    heapq.heappop(heap)
        out.append(str(total - avoided))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **A trainer cannot teach before arriving**, which is why each is pushed into the heap on their arrival day rather than all at once; they stay to the end, so nothing is ever removed for being too late.
- **Taking the highest-sadness available trainer each day is optimal** by exchange: swapping any day to a trainer with greater sadness never increases the total, so the greedy is safe.
- **A day with nobody available is simply idle.** The third sample has no trainer present on day $2$ — the only one who has arrived is already finished — so that day is wasted.
- **Demand can outlast the camp.** The first sample has four lectures wanted across three days, so at least one is missed whatever the schedule.
- **Mutating the quota inside the heap entry is safe** because the ordering key (the negated sadness) never changes; mutating the key itself would silently break the heap invariant.
- **The answer is computed as total sadness minus what was avoided**, so the baseline assumes every lecture is missed and each taught day refunds that trainer's $S_i$.
- **$T_i$ and $D_i$ both lie in $[1, D]$**, so the arrival buckets need exactly $D+1$ slots.

## Dry run

First sample: trainer A arrives day $1$, wants $2$, sadness $300$; trainer B arrives day $2$, wants $2$, sadness $100$. Baseline sadness $2(300) + 2(100) = 800$.

| day | available | taught by | avoided | remaining quota |
|---:|---|---|---:|---|
| 1 | A | **A** (300) | 300 | A: 1 |
| 2 | A, B | **A** (300) | 600 | A: 0 (done), B: 2 |
| 3 | B | **B** (100) | 700 | B: 1 |

Output $800 - 700 = $ `100` — one of B's lectures is missed.

---

Same problem grouped by topic: [../docs/greedy/IPCTRAIN.md](../docs/greedy/IPCTRAIN.md)
