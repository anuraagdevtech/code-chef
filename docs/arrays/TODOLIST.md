# 21. Problems in your to-do list

> CodeChef problem code [`TODOLIST`](https://www.codechef.com/problems/TODOLIST) &middot; difficulty **580** &middot; time limit **4s**

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Counting with a predicate |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

*CodeChef recently revamped its [practice page](https://www.codechef.com/practice) to make it easier for users to identify the next problems they should solve by introducing some new features:*
- *Recent Contest Problems - contains only problems from the last 2 contests*
- *Separate Un-Attempted,  Attempted, and All tabs*
- *Problem Difficulty Rating - the Recommended dropdown menu has various difficulty ranges so that you can attempt the problems most suited to your experience*
- *Popular Topics and Tags*

Like most users, Chef didn’t know that he could add problems to a personal to-do list by clicking on the magic **'+'** symbol on the top-right of each problem page. But once he found out about it, he went crazy and added loads of problems to his [to-do](https://www.codechef.com/practice/todo) list without looking at their difficulty rating.

Chef is a beginner and should ideally try and solve only problems with difficulty rating strictly less than $1000$. Given a list of difficulty ratings for problems in the Chef’s to-do list, please help him identify how many of those problems Chef should **remove** from his to-do list, so that he is only left with problems of difficulty rating less than $1000$.

**Input**

- The first line of input will contain a single integer $T$, the number of test cases. Then the testcases follow.
- Each testcase consists of 2 lines of input.
- The first line of input of each test case contains a single integer, $N$, which is the total number of problems that the Chef has added to his to-do list.
- The second line of input of each test case contains $N$ space-separated integers $D_1, D_2, \ldots, D_N$, which are the difficulty ratings for each problem in the to-do list.

**Output**

For each test case, output in a single line the number of problems that Chef will have to remove so that all remaining problems have a difficulty rating strictly less than $1000$.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 1000$
- $1 \leq D_i \leq 5000$

**Subtasks**

- **Subtask 1 (100 points):**
    - Original constraints

## Sample

**Sample input**

```
5
3
800 1200 900
4
999 1000 1001 1002
5
1 2 2 2 5000
5
1000 1000 1000 1000 1000
3
900 700 800
```

**Sample output**

```
1
3
1
5
0
```

<details><summary>Explanation</summary>

**Test case $1$:** Among the three difficulty ratings, Chef only needs to remove the problem with difficulty rating $1200$, since it is $\ge 1000$. So, the answer is $1$.

**Test case $2$:** Among the four difficulty ratings, Chef needs to remove the problems with difficulty ratings of $1000$, $1001$, and $1002$, since they are $\ge 1000$. So, the answer is $3$.

**Test case $3$:** Among the five difficulty ratings, Chef needs to remove the problem with a difficulty rating of $5000$, since it is $\ge 1000$. So, the answer is $1$.

**Test case $4$:** Chef needs to remove all the five problems, since they are all rated $\ge 1000$. So, the answer is $5$.

**Test case $5$:** Chef does not need to remove any problem, since they are all rated $\lt 1000$. So, the answer is $0$.

</details>

## Approach

Chef should keep only problems rated **strictly below** $1000$, so the number to remove is the count of ratings that are $\geq 1000$.

There is no need to sort, to build a filtered list, or to actually delete anything — the question asks only *how many*, so a single pass with a counter answers it in $O(N)$ time and $O(1)$ extra space. In Python the whole loop collapses to `sum(1 for d in ratings if d >= 1000)`, since summing a boolean generator counts the matches.

The trap is the direction of the comparison. "Keep ratings strictly less than $1000$" means remove $\geq 1000$, so $1000$ itself is **removed**. Sample case 2 isolates this: of $999, 1000, 1001, 1002$ only the $999$ survives, giving an answer of $3$. Case 4 pushes it further with five ratings of exactly $1000$, all of which must go.

Each test case spans two lines ($N$, then the array), but reading the entire input as one flat token stream makes the line breaks irrelevant — a cursor walks forward by $N$ after each case.

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
        ratings = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        # "Keep strictly below 1000" means 1000 itself has to go.
        out.append(str(sum(1 for d in ratings if int(d) >= 1000)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Data Structures`
