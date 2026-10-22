[&larr; 153. Rearranging digits to get a multiple of 5](153-DIGARR.md) &middot; [Index](README.md) &middot; [155. Marathon &rarr;](155-MARARUN.md)

# 154. Kitchen Timetable

> [`KTTABLE`](https://www.codechef.com/problems/KTTABLE) &middot; difficulty **950** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Consecutive differences as a window |
| **CodeChef tags** | `Basic Programming Concepts`, `Loops`, `Conditional Statements` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

There are **N** students living in the dormitory of Berland State University. Each of them sometimes wants to use the kitchen, so the head of the dormitory came up with a timetable for kitchen's usage in order to avoid the conflicts:

- The first student starts to use the kitchen at the time **0** and should finish the cooking not later than at the time **A_1**.

- The second student starts to use the kitchen at the time **A_1** and should finish the cooking not later than at the time **A_2**.

- And so on.

- The **N**-th student starts to use the kitchen at the time **A_N-1** and should finish the cooking not later than at the time **A_N**

The holidays in Berland are approaching, so today each of these **N** students wants to cook some pancakes. The **i**-th student needs **B_i** units of time to cook.

The students have understood that probably not all of them will be able to cook everything they want. How many students will be able to cook without violating the schedule?

**Input**

The first line of the input contains an integer **T** denoting the number of test cases. The description of **T** test cases follows. \
Each test case contains 3 lines of input
- The first line of each test case contains a single integer **N** denoting the number of students.
- The second line contains **N** space-separated integers **A_1**, **A_2**, ..., **A_N** denoting the moments of time by when the corresponding student should finish cooking.
- The third line contains **N** space-separated integers **B_1**, **B_2**, ..., **B_N** denoting the time required for each of the students to cook.

**Output**

For each test case, output a single line containing the number of students that will be able to finish the cooking.

## Constraints

**1** ≤ **T** ≤ **10** \
**1** ≤ **N** ≤ **10^4** \
**0** < **A_1** <  **A_2** < ... < **A_N** < **10^9** \
**1** ≤ **B_i** ≤ **10^9**

## Sample

**Sample input**

```
2
3
1 10 15
1 10 3
3
10 20 30
15 5 20
```

**Sample output**

```
2
1
```

<details><summary>Explanation</summary>

**Example case 1.** The first student has **1** unit of time - the moment **0**. It will be enough for her to cook. The second student has **9** units of time, but wants to cook for **10** units of time, and won't fit in time. The third student has **5** units of time and will fit in time, because needs to cook only for **3** units of time.

**Example case 2.** Each of students has **10** units of time, but only the second one will be able to fit in time.

</details>

## Approach

Student $i$ starts when student $i-1$ must be finished, so their slot runs from $A_{i-1}$ to $A_i$, with $A_0 = 0$ for the first student. The window available to student $i$ is therefore the **consecutive difference**

$$A_i - A_{i-1}$$

and they succeed when $B_i \leq A_i - A_{i-1}$. Counting the successes is one pass.

The crucial point is that the slots are **fixed in advance**, not consumed dynamically. A student who runs out of time simply fails; they do not eat into the next student's window, and a student who finishes early does not donate the slack forward. So each student is judged independently against their own gap, and no running clock needs maintaining.

Sample case 1 makes this concrete. Windows are $1, 9, 5$ against requirements $1, 10, 3$. The second student fails, needing $10$ but having $9$ — and the third student is **unaffected**, succeeding with $3 \leq 5$. A simulation that advanced a shared clock past the overrun would wrongly fail the third as well.

Sample case 2 has uniform windows of $10$ against $15, 5, 20$, so only the middle student manages.

Seeding with $A_0 = 0$ is what lets the first student be handled by the same expression as the rest, rather than as a special case. With $N$ up to $10^4$ and values to $10^9$, nothing is at risk numerically, and the single pass is well within limits.

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
        b = [int(v) for v in data[pos + 1 + n:pos + 1 + 2 * n]]
        pos += 1 + 2 * n
        done = 0
        prev = 0                      # the first student starts at time 0
        for i in range(n):
            # Slots are fixed, so an overrun does not eat into the next one.
            if b[i] <= a[i] - prev:
                done += 1
            prev = a[i]
        out.append(str(done))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The first student's slot starts at time $0$**, so the running marker must be initialised to $0$ rather than to $A_1$ — otherwise the first slot comes out as length zero.
- **Slots are fixed, so an overrun does not eat into the next one.** In the second sample the first student needs $15$ against a $10$-unit slot and fails, yet the second student still gets a full $10$ units. The marker advances to $A_i$ whether or not the student finished.
- **Exactly enough time** ($B_i$ equal to the slot length): counts as done, so the comparison is non-strict — the first sample's opening row turns on it.
- **$A$ is strictly increasing** by the constraints, so every slot has positive length.

## Dry run

First sample, $A = 1, 10, 15$ and $B = 1, 10, 3$:

| $i$ | slot $A_i - \text{prev}$ | $B_i$ | fits? |
|---:|---:|---:|:---:|
| 1 | $1 - 0 = 1$ | 1 | yes |
| 2 | $10 - 1 = 9$ | 10 | no |
| 3 | $15 - 10 = 5$ | 3 | yes |

Two finish, so `2`. The second sample gives slots $10, 10, 10$ against $15, 5, 20$ — only the middle one fits, so `1`.

---

Same problem grouped by topic: [../docs/arrays/KTTABLE.md](../docs/arrays/KTTABLE.md)
