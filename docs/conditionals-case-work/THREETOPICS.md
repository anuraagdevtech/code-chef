# 19. The Three Topics

> CodeChef problem code [`THREETOPICS`](https://www.codechef.com/problems/THREETOPICS) &middot; difficulty **573** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Membership test |
| **Time** | $O(1)$ |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

The Chef has reached the finals of the Annual Inter-school Declamation contest.

For the finals, students were asked to prepare $10$ topics. However, Chef was only able to prepare three topics, numbered $A$, $B$ and $C$ — he is totally blank about the other topics. This means Chef can only win the contest if he gets the topics $A$, $B$ or $C$ to speak about.

On the contest day, Chef gets topic $X$. Determine whether Chef has any chances of winning the competition.

Print "Yes" if it is possible for Chef to win the contest, else print "No".

You may print each character of the string in either uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes`, and `YES` will all be treated as identical).

**Input**

- The first and only line of input will contain a single line containing four space-separated integers $A$, $B$, $C$, and $X$ — the three topics Chef has prepared and the topic that was given to him on contest day.

**Output**

- For each testcase, output in a single line "Yes" or "No".
- You may print each character of the string in either uppercase or lowercase (for example, the strings `yEs`, `yes`, `Yes`, and `YES` will all be treated as identical).

## Constraints

- $1 \leq A,B,C,X \leq 10$
- $A, B, C$ are distinct.

**Subtasks**

**Subtask #1 (100 points):** Original constraints

## Sample

**Sample 1 input**

```
2 3 7 3
```

**Sample 1 output**

```
Yes
```

<details><summary>Explanation</summary>

Chef had prepared the topics: $2, 3, 7$. Chef gets to speak on the topic: $3$. Since Chef had already prepared this, there is a chance that he can win the contest.

</details>

**Sample 2 input**

```
4 6 8 5
```

**Sample 2 output**

```
No
```

<details><summary>Explanation</summary>

Chef had prepared the topics: $4, 6, 8$. Chef gets to speak on the topic: $5$. Since Chef didn't prepare this topic, there is no chance that he can win the contest.

</details>

## Approach

Chef prepared topics $A$, $B$ and $C$, and was handed topic $X$. He has a chance precisely when $X$ is one of the three he prepared:

$$X \in \{A, B, C\}$$

In Python that is literally `x in (a, b, c)`, which reads exactly like the mathematics and avoids the three-way `or` chain that is easy to mistype — writing `x == a or x == b or c` is a classic bug, since the bare `c` is truthy for every non-zero value and would answer `Yes` always.

The guarantee that $A$, $B$ and $C$ are distinct is a convenience, not something the solution depends on; a membership test behaves identically with duplicates.

The one genuine gotcha is the input format. Unlike almost every other problem in this set, there is **no $T$ on the first line** — the input is a single line of four integers, one test case. The output section's "for each testcase" phrasing is boilerplate left over from a template and contradicts the input section. Reading a leading $T$ here would consume $A$ as the count and produce nonsense, so the format is worth confirming against the sample before writing the loop.

## Solution (Python)

```python
import sys


def main() -> None:
    # Single test case: one line of four integers, with no leading T.
    a, b, c, x = map(int, sys.stdin.buffer.read().split()[:4])
    print("Yes" if x in (a, b, c) else "No")


main()
```

## Complexity

- **Time:** $O(1)$
- **Space:** $O(1)$

> CodeChef tags: `Basic Programming Concepts`
