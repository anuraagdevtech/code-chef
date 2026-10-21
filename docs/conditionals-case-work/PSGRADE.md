# 129. Passing Marks

> CodeChef problem code [`PSGRADE`](https://www.codechef.com/problems/PSGRADE) &middot; difficulty **904** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Conjunction of per-subject and aggregate thresholds |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Recently, Chef's College Examination has concluded. He was enrolled in $3$ courses and he scored $A, B, C$ in them, respectively. To pass the semester, he must score at least $A_{min}, B_{min}, C_{min}$ marks in the respective subjects along with a cumulative score of at least $T_{min}$, i.e, $A + B + C \ge T_{min}$.

Given seven integers $A_{min}, B_{min}, C_{min}, T_{min}, A, B, C$, tell whether Chef passes the semester or not.

**Input:**
- The first line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, seven integers $A_{min}, B_{min}, C_{min}, T_{min}, A, B, C$ each separated by aspace.

**Output:**
Output in a single line, the answer, which should be "YES" if Chef passes the semester and "NO" if not.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

**Constraints**
- $1 \leq T \leq 100$
- $1 \leq A_{min}, B_{min}, C_{min}, A, B, C \leq 100$
- $A_{min} + B_{min} + C_{min} \leq T_{min} \leq 300$

## Constraints

- $1 \leq T \leq 100$
- $1 \leq A_{min}, B_{min}, C_{min}, A, B, C \leq 100$
- $A_{min} + B_{min} + C_{min} \leq T_{min} \leq 300$

## Sample

**Sample input**

```
5
1 1 1 300 2 2 2
3 2 2 6 2 2 2
2 3 2 6 2 2 2
2 2 3 6 2 2 2
100 100 100 300 100 100 100
```

**Sample output**

```
NO
NO
NO
NO
YES
```

<details><summary>Explanation</summary>

**TestCase 1:** Chef is passing in all the subjects individually but his total score ($2 + 2 + 2 = 6$) is much below the required threshold of $300$ marks. So Chef doesn't pass the semester.

**TestCase 2:** Chef's score in the first subject is less than the threshold, so he doesn't pass the semester.

**TestCase 3:** Chef's score in the second subject is less than the threshold, so he doesn't pass the semester.

**TestCase 4:** Chef's score in the third subject is less than the threshold, so he doesn't pass the semester.

**TestCase 5:** Chef is passing in all the subjects individually and also his total score is equal to the required threshold of $300$ marks. So Chef passes the semester.

</details>

## Approach

Chef passes only if **all four** conditions hold:

$$A \geq A_{\min}, \quad B \geq B_{\min}, \quad C \geq C_{\min}, \quad A + B + C \geq T_{\min}$$

The per-subject minimums and the aggregate minimum are independent requirements, so this is a conjunction — a strong total cannot rescue a failed subject, and clearing every subject does not guarantee the total.

The samples are built to show both failure modes. Case 1 clears all three subjects comfortably but totals $6$ against $T_{\min} = 300$, so the aggregate check is what fails. Cases 2 through 4 each fail exactly one subject — $A$, then $B$, then $C$ — while the other two pass, which is a deliberate sweep to catch a solution that forgets one of the three comparisons. Case 5 passes everything with no margin at all, landing exactly on each threshold.

That last case makes the inclusivity essential: "at least" means `>=`, and a strict `>` would fail all five samples.

The input order is $A_{\min}, B_{\min}, C_{\min}, T_{\min}, A, B, C$ — all four minimums first, then all three scores. Interleaving them while reading is the likeliest bug, and the constraint $A_{\min} + B_{\min} + C_{\min} \leq T_{\min}$ confirms the grouping, since it only makes sense among the minimums.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        # Order: the three minimums, the total minimum, then the three scores.
        amin, bmin, cmin, tmin, a, b, c = map(int, data[1 + 7 * i:8 + 7 * i])
        ok = a >= amin and b >= bmin and c >= cmin and a + b + c >= tmin
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Algorithms`
