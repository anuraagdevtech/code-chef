[&larr; 700. Expected Sum](700-EXPECTEDSUM.md) &middot; [Index](README.md) &middot; [702. Chef and Pepperoni Pizza Again &rarr;](702-PEPPERA.md)

# 701. College Admissions

> [`ADMIT`](https://www.codechef.com/problems/ADMIT) &middot; difficulty **2496** &middot; time limit **0.5s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Simulation |
| **Technique** | Simulate the admissions in exam-rank order until Chef chooses |
| **CodeChef tags** | `Basic Programming Concepts`, `Mathematics`, `Algorithms`, `Conditional Statements`, `Basic Math`, `Sorting`, `Brute Force`, `Implementation` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(M \log M + \sum \text{list lengths})$ per test case |
| **Space** | $O(N + M + \sum \text{list lengths})$ |

## Question

College admissions are starting and Chef has also recently completed his high school. There are $N$ colleges, numbered from $1$ to $N$, and they are ranked from $1$ to $N$. Each college has only a single seat left. To apply for the colleges, every student has to give a common exam, the result of which decides their destiny, i.e, the student having best rank (scoring max marks) gets to choose the college of their preference first.

Each student has a list of colleges that they like. They will want to get to the best-ranked college from their list. If they can't get into it, they will want to get into the second-ranked college from among their list, and so on.

If the single vacant seat of a college gets filled, the admission for that year is closed in that college. Then, the people who have applied for that college have to look for a lower-ranked college in their preference list provided that it still has vacancies.

Given information about $M$ students, about their marks scored in the exam (given as ranks) and the id’s of the college they are applying for, find which college Chef will land into given that he is the student with $id = 1$.

Every student tries to get into the highest-ranked college on his list which has a vacancy and if not possible to get into any of the colleges on his list, he won’t join any college this year.

**Input:**
- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains $M + 3$ lines of input.
- First line contains $2$ space separated integers $N$, $M$, the total number of colleges, and total number of students respectively.
- Second line contain $N$ distinct space separated integers $R_i$, rank of the $i^{th}$ college. Here $1$ denotes a higher rank and $N$ denotes a lower rank.
- Third line contains $M$ distinct space separated integers $S_i$, the rank of the $i^{th}$ student in the exam. Here $1$ denotes a higher rank, i.e, maximum marks scored and $M$ denotes a lower rank, i.e, minimum marks scored.
- Next $M$ lines contain $K + 1$ space separated integers which the first integer $K$ is the number of colleges $i^{th}$ student will apply to and the next $K$ integers describe the same.

**Output:**
For each testcase, output in a single line the college in which Chef applies and $0$ if he won't be joining any college this year.

**Constraints**
- $1 \leq N, M \leq 5*10^4$
- $R$ is the permutation of integers from $[1, N]$
- $S$ is the permutation of integers from $[1, M]$
- Sum of $N$ over all tests is atmost $3* 10^5$
- Sum of $M$ over all tests is atmost $3.5 * 10^5$
- Sum of $K$ over all students over all tests is atmost $1.5*10^6$
- Every student applies to atleast $1$ college and all the applied colleges are different.

**Note:** Language multiplier for $Java$ is $3$ and for $python$ is $5$ and its recommended to use **Fast Input-Output** for this problem.

## Constraints

- $1 \leq N, M \leq 5*10^4$
- $R$ is the permutation of integers from $[1, N]$
- $S$ is the permutation of integers from $[1, M]$
- Sum of $N$ over all tests is atmost $3* 10^5$
- Sum of $M$ over all tests is atmost $3.5 * 10^5$
- Sum of $K$ over all students over all tests is atmost $1.5*10^6$
- Every student applies to atleast $1$ college and all the applied colleges are different.

## Sample

**Sample input**

```
3
2 2
2 1
1 2
2 1 2
2 1 2
1 2
1
2 1
1 1
1 1
2 1
1 2
1
2 2 1
```

**Sample output**

```
2
0
1
```

<details><summary>Explanation</summary>

**Case 1:** Here since Chef has the highest rank, he gets to choose the highest rank college in his preference list first, that is college with $id = 2$.

**Case 2:** Here since there is only $1$ college and Chef stood second, he won't be able to apply to any of the colleges this year, so we print $id = 0$.

**Case 3:** Here since Chef is the only student and thus has the highest rank, he gets to choose the highest rank college in his preference list first, that is college with $id = 1$.

</details>

## Approach

The process is deterministic: students choose in the order of their exam ranks, and each takes the best-ranked college on their own list that still has its seat, or nothing if all of them are taken.

So sort the students by exam rank and simulate. For each student scan their list for the free college with the smallest rank value and mark it as taken. When Chef (student 1) is reached, print his college - or 0 if none on his list is free - and stop: students after him cannot affect his result.

Every list is scanned at most once, so the simulation is linear in the input size after the sort.

## Solution

```python
import sys


def solve(tokens):
    n, m = (next(tokens), next(tokens))
    college_rank = [next(tokens) for _ in range(n)]
    student_rank = [next(tokens) for _ in range(m)]
    prefs = []
    for _ in range(m):
        k = next(tokens)
        prefs.append([next(tokens) - 1 for _ in range(k)])
    used = set()
    for i in sorted(range(m), key=student_rank.__getitem__):
        choice = min((college for college in prefs[i] if college not in used), key=college_rank.__getitem__, default=-1)
        if i == 0:
            return str(choice + 1)
        if choice >= 0:
            used.add(choice)


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- Chef may get no college at all: print 0.
- Rank 1 is the best, both for colleges and for students.
- A student whose colleges are all taken occupies nothing.
- The college ids in the lists are converted to 0-based indices.

## Dry run

First sample: college ranks `2 1` (college 2 is the best), student ranks `1 2` (Chef is first), both students list colleges 1 and 2.

Chef chooses first and takes the best college on his list, college 2.

Second sample: one college; Chef has exam rank 2 and the other student takes the college first. Chef gets nothing: 0.

---

Same problem grouped by topic: [../docs/simulation/ADMIT.md](../docs/simulation/ADMIT.md)
