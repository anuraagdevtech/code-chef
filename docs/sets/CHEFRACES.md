# 73. Chef and Races

> CodeChef problem code [`CHEFRACES`](https://www.codechef.com/problems/CHEFRACES) &middot; difficulty **745** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Sets |
| **Technique** | Set difference |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

The National Championships are starting soon. There are $4$ race categories, numbered from $1$ to $4$, that Chef is interested in. Chef is participating in exactly $2$ of these categories.

Chef has an arch-rival who is, unfortunately, the only person participating who is better than Chef, i.e, Chef can't defeat the arch-rival in any of the four race categories but can defeat anyone else. Chef's arch-rival is also participating in exactly $2$ of the four categories.

Chef hopes to not fall into the same categories as that of the arch-rival.

Given $X, Y, A, B$ where $X, Y$ are the races that Chef participates in, and $A, B$ are the races that Chef's arch-rival participates in, find the **maximum** number of gold medals (first place) that Chef can win.

**Input**

- The first line of input contains an integer $T$, denoting the number of testcases. The description of $T$ testcases follows.
- Each testcase consists of a single line containing four space-separated integers — the values of $X, Y, A$, and $B$ respectively.

**Output**

- For each testcase, print a single line containing one integer — the **maximum** number of gold medals that Chef can win.

## Constraints

- $1 \leq T \leq 144$
- $1 \leq X, Y, A, B \leq 4$
- $X \neq Y$
- $A \neq B$

**Subtasks**

**Subtask #1 (100 points):** Original constraints

## Sample

**Sample input**

```
3
4 3 1 2
4 2 1 2
2 1 1 2
```

**Sample output**

```
2
1
0
```

<details><summary>Explanation</summary>

**Test case $1$:** Chef participates in the races $4, 3$, whereas Chef's rival participates in $1, 2$. As Chef's only rival does not participate in any of the races that Chef takes part in, Chef can win the gold medal in both of the races, thus the answer is $2$.

**Test case $2$:** Chef participates in the races $4, 2$, whereas Chef's rival participates in $1, 2$. Chef cannot win race $2$ as Chef will be beaten by the arch-rival, however Chef can win the gold medal for race $4$. Thus the answer is $1$.

**Test case $3$:** Chef participates in the races $2, 1$, whereas Chef's rival participates in $1, 2$. Chef will be beaten by the arch-rival in both races, thus the answer is $0$.

</details>

## Approach

Chef loses to his rival in any category they share and beats everyone else, so he takes gold in exactly those of his own races that the rival is **not** entered in. That is a set difference:

$$\left|\{X, Y\} \setminus \{A, B\}\right|$$

In Python this is literally `len({x, y} - {a, b})`, which reads as the mathematics does and sidesteps the comparison chain the problem invites. Writing it by hand means testing each of Chef's two races against each of the rival's two — four comparisons — and it is easy to mis-pair one of them.

Note the sets are genuinely sets: the constraints promise $X \neq Y$ and $A \neq B$, so each has exactly two elements and no duplicate-collapsing surprises arise.

The three samples walk through the whole range of answers. No overlap gives $2$ gold medals; one shared category gives $1$; and identical entries give $0$, with the rival shutting Chef out entirely.

Framing a problem as set operations — difference, intersection, union — rather than as nested conditionals is a habit that pays off well beyond four races: the expression stays the same size as the sets grow.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, a, b = map(int, data[1 + 4 * i:5 + 4 * i])
        # Gold in Chef's races that the rival did not enter.
        out.append(str(len({x, y} - {a, b})))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Basic Programming Concepts`
