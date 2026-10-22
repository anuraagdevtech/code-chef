# 335. Attendance

> CodeChef problem code [`ATTND`](https://www.codechef.com/problems/ATTND) &middot; difficulty **1148** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Frequency of a key field |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Jump from 2* to 3* (Level 3) |

## Question

Chef is teaching a cooking course. There are $N$ students attending the course, numbered $1$ through $N$.

Before each lesson, Chef has to take attendance, i.e. call out the names of students one by one and mark which students are present. Each student has a first name and a last name. In order to save time, Chef wants to call out only the first names of students. However, whenever there are multiple students with the same first name, Chef has to call out the full names (both first and last names) of all these students. For each student that does not share the first name with any other student, Chef may still call out only this student's first name.

Help Chef decide, for each student, whether he will call out this student's full name or only the first name.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- $N$ lines follow. For each valid $i$, the $i$-th of the following $N$ lines contains two space-separated strings denoting the first and last name of student $i$.

**Output**
For each test case, print $N$ lines. For each valid $i$, the $i$-th of these lines should describe how Chef calls out the $i$-th student's name ― it should contain either the first name or the first and last name separated by a space.

**Constraints**
- $1 \le T \le 100$
- $2 \le N \le 100$
- all first and last names contain only lowercase English letters
- the lengths of all first and last names are between $1$ and $10$ inclusive

**Subtasks**
**Subtask #1 (100 points):** original constraints

## Constraints

- $1 \le T \le 100$
- $2 \le N \le 100$
- all first and last names contain only lowercase English letters
- the lengths of all first and last names are between $1$ and $10$ inclusive

## Sample

**Sample input**

```
1
4
hasan jaddouh
farhod khakimiyon
kerim kochekov
hasan khateeb
```

**Sample output**

```
hasan jaddouh
farhod
kerim
hasan khateeb
```

## Approach

Chef calls a student's full name exactly when their **first name is shared** with someone else in the class. So tally the first names, then make a second pass deciding each student's output.

Two passes are needed and cannot be merged: when the first student is printed, we do not yet know whether a later student shares their first name. Counting everything before emitting anything resolves that.

$$\text{output}_i = \begin{cases} \text{first}_i & \text{count}[\text{first}_i] = 1 \\ \text{first}_i \; \text{last}_i & \text{otherwise}\end{cases}$$

The sample is built around this. Two students share the first name `hasan`, so **both** are called in full — including the first one, which is the detail a single-pass solution gets wrong. The other two have unique first names and are called by first name alone.

Note the rule depends only on the first name; last names are never compared and may freely repeat.

A `Counter` over the first names does the tally in one pass, and the decision per student is then an $O(1)$ lookup.

Each test case produces $N$ output lines, one per student in the original input order — the output is not sorted or grouped.

## Solution (Python)

```python
import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        pos += 1
        firsts = [data[pos + 2 * i] for i in range(n)]
        lasts = [data[pos + 2 * i + 1] for i in range(n)]
        pos += 2 * n
        # Count first, then decide: a shared first name makes *both* students
        # full-named, including the earlier one.
        counts = Counter(firsts)
        for f, l in zip(firsts, lasts):
            out.append(f.decode() if counts[f] == 1 else f"{f.decode()} {l.decode()}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **Both students sharing a first name get the full name, the earlier one included.** A single pass that decides as it reads prints just `hasan` for the first of them, because the clash has not been seen yet — which is why the counting pass must complete first. The sample is built on exactly this.
- **Last names may repeat freely**; only first names are ever compared, so two students called `x jones` and `y jones` are both called by first name alone.
- **All first names distinct**: every line is a bare first name.
- **All first names identical**: every line is a full name.
- **Output is $N$ lines per test case, in the original input order** — not sorted and not grouped.

## Dry run

| student | first name | times that first name appears | output |
|---|---|---:|---|
| hasan jaddouh | hasan | 2 | `hasan jaddouh` |
| farhod khakimiyon | farhod | 1 | `farhod` |
| kerim kochekov | kerim | 1 | `kerim` |
| hasan khateeb | hasan | 2 | `hasan khateeb` |

The first line needs the count from the fourth, which is why one pass is not enough.

---

Same problem in rating order (#172 of 486): [../../by-rating/172-ATTND.md](../../by-rating/172-ATTND.md)
