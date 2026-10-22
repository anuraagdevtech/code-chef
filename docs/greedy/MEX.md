# 315. Max Mex

> CodeChef problem code [`MEX`](https://www.codechef.com/problems/MEX) &middot; difficulty **1478** &middot; time limit **1.5s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Spending a budget on the smallest gaps first |
| **Time** | $O(N + V)$ per test case |
| **Space** | $O(V)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

You are given a multi-set **S** of **N** integers, and an integer **K**. You want to find the maximum value of Minimum Excluded Value ([**MEX**](https://en.wikipedia.org/wiki/Mex_(mathematics))) of the multi-set given that you are allowed to add at most any **K** integers to the multi-set. Find the maximum value of MEX that you can obtain.

MEX (Minimum Excluded Value) is defined as the smallest non-negative integer (0, 1, 2, ...) that does not appear in a given multiset or array. Few examples of MEX of a multi-set are as follows. MEX of the multi-set {0} is 1, {1} is 0, {0, 1, 3} is 2, {0, 1, 2, 3, 5, 6} is 4.

**Input**

The first line of the input contains an integer **T** denoting the number of testcases.

The first line of each test case contains two space seperated integers **N** and **K** denoting the size of the multi-set and the maximum number of extra integers that you can add in the multi-set respectively.

The second line contains **N** space separated integers denoting the multi-set **S**: **S_1**, **S_2** ,.... **S_N**.

**Output**

For each testcase, output the answer in a single line.

**Constraints**

- **1** ≤ **T** ≤ **10**

- **1** ≤ **N** ≤ **10^5**

- **0** ≤ **K** ≤ **10^5**

- **0** ≤ **S_i** ≤ **2 * 10^5**

**Subtasks**

- **Subtask #1** (15 points): **K**=0.

- **Subtask #2** (85 points): Original Constraints.

## Constraints

- 1 ≤ T ≤ 10
- 1 ≤ N ≤ 10^5
- 0 ≤ K ≤ 10^5
- 0 ≤ S_i ≤ 2 * 10^5

## Sample

**Sample input**

```
4
3 0
1 0 2
3 1
1 0 2
4 3
2 5 4 9
2 0
3 4
```

**Sample output**

```
3
4
6
0
```

<details><summary>Explanation</summary>

**Example case 1.** As **K** = 0, so we can't add any element to the multi-set. Elements of the set are {1, 0, 2}. The MEX value of this set is 3.

**Example case 2.** As **K** = 1, you are allowed to add at most 1 element to the multi-set. The multi-set are {1, 0, 2}. You can add element 3 to the multi-set, and it becomes {1, 0, 2, 3}. The MEX value of this multi-set is 4. There is no other way to have higher value of MEX of the set by adding at most one element to the multi-set.

</details>

## Approach

The MEX is the smallest non-negative integer absent from the multiset, so raising it to $m$ requires **every** value $0, 1, \ldots, m-1$ to be present. Values at or above $m$ are irrelevant.

So walk upward from $0$, and whenever a value is missing, spend one of the $K$ additions on it. Continue until the budget runs out; the first value that cannot be supplied is the answer.

Greedy is forced rather than chosen here — there is no decision to make. Every missing value below the target must be filled, so the order of spending is immaterial and walking upward simply stops at the right place.

Note what makes this cheap: duplicates in $S$ are useless, so only **membership** matters, recorded in a boolean array indexed by value.

The ceiling on the answer is $\max(S_i) + K + 1$: beyond that, even spending every addition cannot bridge the gap. With $S_i \leq 2 \times 10^5$ and $K \leq 10^5$ the scan is bounded by about $3 \times 10^5$, which keeps the loop safely terminated.

The samples cover the range. $\{1,0,2\}$ with $K=0$ already holds $0,1,2$ and stops at $3$. The same set with $K=1$ buys the $3$ and reaches $4$. $\{2,5,4,9\}$ with $K=3$ is the interesting one: the gaps at $0$, $1$ and $3$ consume exactly the budget, yielding $0$–$5$ present and a MEX of $6$ — note the $9$ contributes nothing.

$\{3,4\}$ with $K=0$ answers $0$, since $0$ itself is missing and unaffordable.

## Solution (Python)

```python
import sys

LIMIT = 2 * 10 ** 5 + 10 ** 5 + 2


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n, k = int(data[pos]), int(data[pos + 1])
        present = bytearray(LIMIT)
        for v in data[pos + 2:pos + 2 + n]:
            present[int(v)] = 1
        pos += 2 + n
        # Walk upward, buying each missing value until the budget runs out.
        m = 0
        while m < LIMIT:
            if not present[m]:
                if k == 0:
                    break
                k -= 1
            m += 1
        out.append(str(m))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N + V)$ per test case
- **Space:** $O(V)$

## Edge cases

- **$K = 0$** (the first and fourth rows) reduces the answer to the plain MEX of the array.
- **The budget must be spent on the smallest missing values**, and there is no choice about it: MEX requires an unbroken run from $0$ upward, so skipping a gap is never useful.
- **The array may be entirely above $0$** (the fourth row starts at $3$), in which case the answer is $0$ with no budget.
- **The answer can exceed $\max(S_i) + 1$.** The third row reaches $6$ by buying $0$, $1$ and $3$, even though the array already contains $9$.
- **The membership table must extend past $2 \cdot 10^5$.** With $K$ up to $10^5$ purchases on top of values up to $2 \cdot 10^5$, the answer can reach $3 \cdot 10^5$ — sizing the table at $\max(S_i) + 1$ truncates the walk.
- **Duplicates cost nothing**: only membership matters, so repeated values are absorbed by the table.

## Dry run

Third sample: $K = 3$, values $2, 5, 4, 9$.

| $m$ | present? | action | budget left |
|---:|:---:|---|---:|
| 0 | no | buy | 2 |
| 1 | no | buy | 1 |
| 2 | yes | — | 1 |
| 3 | no | buy | 0 |
| 4 | yes | — | 0 |
| 5 | yes | — | 0 |
| 6 | no | **cannot buy** | — |

Output `6`.

---

Same problem in rating order (#276 of 486): [../../by-rating/276-MEX.md](../../by-rating/276-MEX.md)
