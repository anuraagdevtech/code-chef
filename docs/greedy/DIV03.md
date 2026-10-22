# 200. Daanish and Problems

> CodeChef problem code [`DIV03`](https://www.codechef.com/problems/DIV03) &middot; difficulty **1388** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Spending a budget from the top down |
| **Time** | $O(1)$ per test case — ten fixed difficulties |
| **Space** | $O(1)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

Daanish as always is busy creating and solving his favourite and interesting graph problems. Chef assigns each problem a difficulty — an integer between $1$ and $10$. For each valid $i$, there are $A_i$ problems with difficulty $i$.

A participant hacked Daanish's account and got access to the problem proposal document. He can delete up to $K$ problems from the document in order to reduce the difficulty of the contest for himself and his friends. Find the smallest possible value of the difficulty of the most difficult problem which remains after removing $K$ problems.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains $10$ space-separated integers $A_1, A_2, \ldots, A_{10}$.
- The second line contains a single integer $K$.

**Output**
For each test case, print a single line containing one integer — the minimum difficulty of the most difficult remaining problem.

**Constraints**
- $1 \leq T \leq 2 \cdot 10^4$
- $0 \leq A_i \leq 10^8$ for each valid $i$
- $A_1 + A_2 + \ldots + A_{10} \gt 0$
- $0 \leq K \lt A_1 + A_2 + \ldots + A_{10}$

**Subtasks**
**Subtask #1 (100 points):** original constraints

## Constraints

- $1 \leq T \leq 2 \cdot 10^4$
- $0 \leq A_i \leq 10^8$ for each valid $i$
- $A_1 + A_2 + \ldots + A_{10} \gt 0$
- $0 \leq K \lt A_1 + A_2 + \ldots + A_{10}$

## Sample

**Sample input**

```
5
1 10 1 5 3 2 4 9 0 100
100
2 0 1 0 0 0 0 0 0 10
12
2 0 1 0 0 0 0 10 0 0
0
2 0 1 0 0 0 0 0 0 10
10
1 10 1 5 3 2 4 9 0 100
125
```

**Sample output**

```
8
1
8
3
2
```

<details><summary>Explanation</summary>

**Example case 1:** The participant can remove all $100$ problems with difficulty $10$. Then, there are no problems with difficulties $9$ and $10$, so the maximum difficulty among remaining problems is $8$.

**Example case 2:** The participant can remove all problems with difficulties $3$ and $10$ and any one of the problems with difficulty $1$. Then, the only problem left has difficulty $1$.

**Example case 3:** The participant cannot remove any problem. The document does not contain any problems with difficulties $9$ or $10$, so the maximum difficulty of a problem is $8$.

</details>

## Approach

To make the hardest remaining problem as easy as possible, delete problems from the **top** difficulty downward. Any deletion spent on an easier problem is wasted, since it cannot lower the maximum while harder problems survive.

So walk difficulties $10, 9, \ldots, 1$ with a budget of $K$:

- if the whole tier fits in the budget, erase it and continue;
- otherwise the budget runs out mid-tier, that tier keeps at least one problem, and it is the answer.

The greedy is optimal because the maximum difficulty is determined solely by the hardest surviving tier, and clearing tiers from the top is the only way to reduce it.

The guarantee $K < \sum A_i$ matters: at least one problem always survives, so the scan is certain to find an answer and no empty case arises.

**Empty tiers must be skipped, not treated as answers.** A tier with $A_i = 0$ costs nothing to "clear" and cannot be the maximum. Sample case 4 is exactly this: with $K = 10$ the $10$ problems of difficulty $10$ are erased, difficulties $9$ down to $4$ are already empty, and the answer is the next non-empty tier, $3$.

Sample case 3 has $K = 0$, so nothing is deleted and the answer is just the hardest non-empty tier, $8$. Sample case 5 spends a large budget sweeping down to difficulty $2$, which survives with $9$ of its $10$ problems.

With $A_i$ up to $10^8$ the totals reach $10^9$, fine for Python and just inside 32 bits elsewhere. The fixed ten tiers make each test case constant time, which matters at $T = 2 \times 10^4$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        a = [int(v) for v in data[pos:pos + 10]]     # difficulties 1..10
        k = int(data[pos + 10])
        pos += 11
        answer = 1
        for d in range(10, 0, -1):
            count = a[d - 1]
            if count == 0:
                continue            # empty tiers are free and never the answer
            if count <= k:
                k -= count
                continue
            answer = d              # budget runs out here, so this tier stays
            break
        out.append(str(answer))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case — ten fixed difficulties
- **Space:** $O(1)$

## Edge cases

- **Empty tiers must be skipped without becoming the answer.** Cases $2$ and $4$ both have runs of zeros between the tier that gets cleared and the tier that survives; without the `continue` on a zero count, the answer would be reported as an empty difficulty.
- **$K = 0$** (case $3$): nothing is removed, and the answer is simply the hardest non-empty tier, $8$.
- **Exactly clearing a tier** (case $4$, where $K = 10$ matches the ten problems at difficulty $10$) moves on to the next non-empty tier, which becomes the answer.
- **Removing from the top down is forced**, because the answer is the *maximum* remaining difficulty: deleting anything easier leaves that maximum untouched and wastes the budget.
- **$K <$ the total is guaranteed**, so at least one problem always survives and the loop always halts at a tier it cannot clear — the `answer = 1` initialiser never actually fires.
- **The ten counts are a fixed-length record**, so each case consumes exactly $11$ tokens; a variable-length read would desynchronise the stream.

## Dry run

Second sample: counts $2, 0, 1, 0, 0, 0, 0, 0, 0, 10$ for difficulties $1$ through $10$, with $K = 12$.

| difficulty | count | action | $K$ left |
|---:|---:|---|---:|
| 10 | 10 | clear it | 2 |
| 9…4 | 0 | skip (empty) | 2 |
| 3 | 1 | clear it | 1 |
| 2 | 0 | skip (empty) | 1 |
| 1 | 2 | **cannot clear** | — |

Output `1`.

---

Same problem in rating order (#224 of 486): [../../by-rating/224-DIV03.md](../../by-rating/224-DIV03.md)
