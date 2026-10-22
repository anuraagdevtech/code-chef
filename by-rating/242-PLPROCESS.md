[&larr; 241. Say No To Drugs](241-NODRUGS.md) &middot; [Index](README.md) &middot; [243. Reversing directions &rarr;](243-DIRECTI.md)

# 242. Parallel Processing

> [`PLPROCESS`](https://www.codechef.com/problems/PLPROCESS) &middot; difficulty **1425** &middot; time limit **7.5s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Minimising the heavier side of a split |
| **CodeChef tags** | `Algorithms`, `Simple Algos`, `Prefix Sum` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

There are $N$ tasks waiting in line to be executed. The execution time for the $i^{th}$ task is $A_i$ seconds.

Chef has **two processors** to execute these $N$ tasks. Both these processors work simultaneously. Each processor executes the assigned tasks one by one.

Chef assigns a **prefix** of these tasks to the first processor and the remaining tasks to the second processor.

For example, if there are $3$ tasks, Chef can do one of the following:
- Assign no task to the first processor. This means, the second processor will execute tasks $1, 2$ and $3$.
- Assign task $1$ to the first processor. This means, the second processor will execute tasks $2$ and $3$.
- Assign tasks $1$ and $2$ to the first processor. This means, the second processor will execute task $3$.
- Assign tasks $1, 2$ and $3$ to the first processor. Thus, second processor would execute no tasks.

Find the **minimum** time in which all the tasks can be executed.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer $N$, the number of tasks waiting to be executed.
- The second line of each test case contains $N$ space separated positive integers $A_1, A_2, \ldots, A_N$ denoting the execution time for each task.

**Output**

For each test case, output in a single line, the minimum time in which all tasks can be executed.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 10^5$
- $1 \leq A_i \leq 10^5$
- The sum of $N$ over all test cases is not more than $2\cdot 10^5$.

**Subtasks**

**Subtask #1 (100 points):** original constraints

## Sample

**Sample input**

```
3
3
4 2 3
6
1 1 1 1 1 1
1
5
```

**Sample output**

```
5
3
5
```

<details><summary>Explanation</summary>

**Test Case 1:** Chef assigns task $1$ to the first processor and tasks $2$ and $3$ to the second processor. The first processor takes $4$ seconds to execute task $1$. The second processor takes $2+3 = 5$ seconds to execute tasks $2$ and $3$. Thus, atleast $5$ seconds are required to execute all tasks.

**Test Case 2:** Chef assigns tasks $1, 2$ and $3$ to the first processor. Processes $4, 5$ ad $6$ are executed by second processor.

**Test Case 3:** Chef assigns task $1$ to the first processor. No task is executed by second processor.

</details>

## Approach

The split point is the only decision: the first processor takes a prefix, the second takes the rest. Both run **simultaneously**, so the finishing time is the larger of the two workloads, not their sum:

$$\min_{0 \leq c \leq N} \max\bigl(\text{prefix}(c),\ \text{total} - \text{prefix}(c)\bigr)$$

Computing the total once, then sweeping $c$ from $0$ to $N$ with a running prefix sum, evaluates every split in $O(N)$ with no stored array.

Taking the **maximum** rather than the sum is the crux. Sample case 1, $[4,2,3]$, totals $9$ but finishes in $5$ — one processor runs $4$ while the other runs $2+3 = 5$, and they overlap.

The split must be a **contiguous prefix**, which is what keeps this simple. Were any subset allowed, this would be the partition problem and NP-hard; the prefix restriction reduces it to a linear scan.

Note the two extreme splits are legal — all tasks to one processor — so $c = 0$ and $c = N$ must both be considered. Sample case 3, a single task, relies on that: whichever processor takes it, the answer is $5$.

Sample case 2 splits six unit tasks evenly into $3$ and $3$. The best split is not always perfectly even, though: with $[4,2,3]$ the halves are $4$ and $5$, since the boundary can only fall between tasks.

Values reach $10^5$ with $N$ up to $10^5$, so totals reach $10^{10}$ — beyond 32 bits, though Python is unaffected.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        a = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        total = sum(a)
        # Both split extremes are legal, so start from an empty prefix.
        best = total
        prefix = 0
        for v in a:
            prefix += v
            # They run at the same time, so the cost is the heavier side.
            best = min(best, max(prefix, total - prefix))
        out.append(str(best))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The split must be a prefix/suffix cut**, not an arbitrary partition — the jobs keep their order, which is what makes a single scan enough instead of a subset-sum search.
- **Giving everything to one processor is legal**, which is why `best` starts at the full total and the final iteration (an empty suffix) is included. The third row, with $N = 1$, has no other option.
- **The two processors run in parallel**, so the cost is the *heavier* side — summing them would just reproduce the total.
- **$\max(\text{prefix}, \text{total} - \text{prefix})$ is V-shaped** in the cut point, since $A_i \geq 1$ makes prefixes strictly increase; so the single pass finds the true minimum and no binary search is needed.
- **A balanced split may be impossible.** The first row's best is $5$ against $4$, not an even $4.5$ — the answer is the achievable maximum, not half the total.
- **Sum of $N \leq 2 \cdot 10^5$**: one pass per case with a running prefix rather than a stored prefix array.

## Dry run

Second sample: six jobs of cost $1$, total $6$.

| cut after | prefix | suffix | heavier side |
|---:|---:|---:|---:|
| 1 | 1 | 5 | 5 |
| 2 | 2 | 4 | 4 |
| 3 | 3 | 3 | **3** |
| 4 | 4 | 2 | 4 |
| 5 | 5 | 1 | 5 |
| 6 | 6 | 0 | 6 |

Output `3`, at the balanced cut.

---

Same problem grouped by topic: [../docs/prefix-sums/PLPROCESS.md](../docs/prefix-sums/PLPROCESS.md)
