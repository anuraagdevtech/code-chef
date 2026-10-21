# 1442 &middot; Average Flex

> CodeChef problem code [`AVGFLEX`](https://www.codechef.com/problems/AVGFLEX) &middot; time limit **0.5s** &middot; Level up from 1* to 2* (Level 2)

## Topics used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Counting against a global threshold |
| **CodeChef category** | main |
| **Time** | $O(N^2)$ per test case at these bounds, or $O(N \log N)$ sorted |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/arrays/AVGFLEX.md](../docs/arrays/AVGFLEX.md)

## Question

There are $N$ students in a class, where the $i$-th student has a score of $A_i$.

The $i$-th student will *boast* if and only if the number of students scoring less than or equal $A_i$ is greater than the number of students scoring greater than $A_i$.

Find the number of students who will boast.

**Input**

- The first line contains $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer $N$ - the number of students.
- The second line of each test case contains $N$ integers $A_1, A_2, \dots, A_N$ - the scores of the students.

**Output**

For each test case, output in a single line the number of students who will boast.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 100$
- $0 \leq A_i \leq 100$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
3
3
100 100 100
3
2 1 3
4
30 1 30 30
```

**Sample output**

```
3
2
3
```

<details><summary>Explanation</summary>

- **Test case $1$:** All three students got the highest score. So all three of them will boast.
- **Test case $2$:** Only the student with score $1$ will not be able to boast.
- **Test case $3$:** Only the student with score $1$ will not be able to boast.

</details>

## Approach

Student $i$ boasts when the number scoring $\leq A_i$ exceeds the number scoring $> A_i$. Those two groups partition the class, so if $c_i$ is the count of scores $\leq A_i$ then the other group has $N - c_i$, and the condition becomes

$$c_i > N - c_i \quad\Longleftrightarrow\quad 2c_i > N$$

In words: a student boasts exactly when they are at or above the **median** — more precisely, when strictly more than half the class scores no higher than they do.

The complement trick is the useful part: one count plus the total replaces two counts, the same move used for the even/odd and contest-code problems.

Note that $c_i$ counts the student themselves, since $A_i \leq A_i$. Sample case 1, with three identical scores, has $c_i = 3$ for everyone, and $6 > 3$ makes all three boast — ties count in your favour, which is what the `<=` encodes. Using a strict `<` would give $c_i = 0$ and nobody boasting.

Sample case 3 is the same effect with duplicates: the three students scoring $30$ each see $c_i = 4$, comfortably clearing the bar, while the lone $1$ does not.

With $N \leq 100$ the direct $O(N^2)$ double loop is perfectly fine and reads closest to the statement. Sorting once and using binary search would give $O(N \log N)$, which is the shape to reach for if $N$ grew.

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
        a = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        # Boasts when strictly more than half the class scores no higher,
        # counting yourself: 2 * c > n.
        boasters = sum(1 for x in a if 2 * sum(1 for y in a if y <= x) > n)
        out.append(str(boasters))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N^2)$ per test case at these bounds, or $O(N \log N)$ sorted
- **Space:** $O(1)$
