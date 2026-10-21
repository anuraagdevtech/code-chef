# 380. Largest Family

> CodeChef problem code [`LARGEFAM`](https://www.codechef.com/problems/LARGEFAM) &middot; difficulty **1532** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Maximising a set size under a sum budget |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

A certain parallel universe has exactly $N$ people living in it.

The $i$-th of these $N$ people claims that they are the parent of exactly $A_i$ of these $N$ people.

However, some of these people might be lying — the $i$-th person may be either telling the truth (in which case they have exactly $A_i$ children) or lying (in which case they can have any number of children).

It is known that each person has **at most one** parent. Further, as one would expect, it is **not allowed** for a person's child to also be their ancestor.

What is the **maximum** possible number of truth-tellers in this universe?

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of two lines of input.
    - The first line of each test case contains a single integer $N$, the number of people.
    - The second line of each test case contains $N$ space-separated integers $A_1, A_2, \ldots, A_N$.

**Output**

For each test case, output on a new line the maximum number of people that can be telling the truth.

## Constraints

- $1 \leq T \leq 4 \cdot 10^4$
- $1 \leq N \leq 3\cdot 10^5$
- $0 \leq A_i \lt N$
- The sum of $N$ across all test cases won't exceed $3 \cdot 10^5$.

**Subtasks**

- **Subtask 1 (20 points):**
    - $1 \leq T \leq 5$
    - $1 \leq N \leq 20$
- **Subtask 2 (80 points):**
    - No further constraints.

## Sample

**Sample input**

```
4
2
1 0
2
1 1
3
2 0 1
5
2 3 1 2 3
```

**Sample output**

```
2
1
2
2
```

<details><summary>Explanation</summary>

**Test case $1$:** Both people can be telling the truth, with the first person being the parent of the second.

**Test case $2$:** If both people were telling the truth, they would be each others' parents — and that is not allowed. Hence, at most one of them can be telling the truth.

**Test case $3$:** The first and third people cannot be telling the truth at the same time. However, it is possible for the first and second people to be truthful — person $1$ can be the parent of person $2$ and person $3$. Hence, the answer is $2$.

**Test case $4$:** There are several ways to pick $2$ people to be telling the truth — for example,
- The parent of person $2$ and person $3$ is person $1$
- The parent of person $1$ and person $5$ is person $4$

in which case persons number $1$ and $4$ would be telling the truth.

However, it can be shown that it is impossible for any three of them to be simultaneously telling the truth.

</details>

## Approach

Each person has at most one parent and no cycles, so the parent relation is a **forest**. In a forest on $N$ nodes with $r$ components, exactly $N - r$ nodes have a parent, and $r \geq 1$. A liar may have any number of children, so give them none; then the children all come from the truth-tellers, whose child sets are disjoint. Hence for a set $S$ of truth-tellers,

$$\sum_{i \in S} A_i = N - r \;\leq\; N - 1$$

That bound is also sufficient: with the out-degrees summing to at most $N-1$ there are always enough unclaimed people to hand out, and assigning children top-down from fresh nodes never makes anyone their own ancestor. So the problem is exactly

$$\text{maximise } |S| \text{ subject to } \sum_{i \in S} A_i \leq N - 1$$

which is the classic "fit as many items as possible into a budget": sort $A$ ascending and take greedily until the budget is exhausted. Taking the smallest claims first is optimal by exchange — swapping any chosen claim for an unchosen smaller one never breaks the budget.

People claiming $A_i = 0$ are free and always truthful in the optimum, which is why sorting rather than any cleverer selection is enough.

The samples show the budget binding at different points. $[1,0]$ with budget $1$ fits both. $[1,1]$ with budget $1$ fits only one — note that *both* cannot be telling the truth even though each claim is individually plausible, because two people would need two children among only two people, forcing a cycle. $[2,0,1]$ with budget $2$ takes $0$ and $1$ for $2$. And $[2,3,1,2,3]$ with budget $4$ takes $1$ and $2$, stopping before the second $2$ would push the sum to $5$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        claims = sorted(int(x) for x in data[pos + 1:pos + 1 + n])
        pos += 1 + n
        # A forest on N nodes has at most N - 1 nodes with a parent.
        budget = n - 1
        told = 0
        for c in claims:
            if c > budget:
                break
            budget -= c
            told += 1
        out.append(str(told))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N \log N)$ per test case
- **Space:** $O(N)$
