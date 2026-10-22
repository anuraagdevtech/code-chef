[&larr; 148. Car Range](148-CARRANGE.md) &middot; [Index](README.md) &middot; [150.  Am I Lucky! &rarr;](150-SPCP4.md)

# 149. Vaccine Dates 

> [`VDATES`](https://www.codechef.com/problems/VDATES) &middot; difficulty **938** &middot; time limit **1s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Classifying a value against an interval |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef has taken his first dose of vaccine $D$ days ago. He may take the second dose no less than $L$ days and no more than $R$ days since his first dose.

Determine if Chef is too early, too late, or in the correct range for taking his second dose.

**Input**

- First line will contain $T$, number of testcases. Then the testcases follow.
- Each testcase contains of a single line of input, three integers $D, L, R$.

**Output**

For each test case, print a single line containing one string - "Too Early" (without quotes) if it's too early to take the vaccine, "Too Late" (without quotes) if it's too late to take the vaccine, "Take second dose now" (without quotes) if it's the correct time to take the vaccine.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq D \leq 10^9$
- $1 \leq L \leq R \leq 10^9$

**Subtasks**

- **Subtask 1 (100 points):** Original constraints

## Sample

**Sample input**

```
4
10 8 12 
14 2 10
4444 5555 6666 
8 8 12
```

**Sample output**

```
Take second dose now
Too Late
Too Early
Take second dose now
```

<details><summary>Explanation</summary>

**Test case $1$:** The second dose needs to be taken within $8$ to $12$ days and since the Day $10$ lies in this range, we can take the second dose now.

**Test case $2$:** The second dose needs to be taken within $2$ to $10$ days since Day $14$ lies after this range, it is too late now.

**Test case $3$:** The second dose needs to be taken within $5555$ to $6666$ days and since the Day $4444$ lies prior to this range, it is too early now.

</details>

## Approach

The valid window for the second dose is $[L, R]$ days after the first, and $D$ days have passed. Three outcomes:

- $D < L$ — the window has not opened: `Too Early`
- $D > R$ — the window has closed: `Too Late`
- otherwise — `Take second dose now`

Testing the two extremes first and letting the middle fall through to the `else` keeps the in-range case free of a two-sided comparison.

Both endpoints are **inclusive**, which is the detail the samples check. Case 4 has $D = L = 8$, exactly on the opening day, and the correct answer is `Take second dose now` rather than `Too Early`. A strict `<=` in the wrong place would flip it.

The output strings must match exactly, including the capitalisation and the spaces in `Take second dose now` — the problem does not say the checker is case-insensitive here, unlike many of its neighbours.

The constraint $L \leq R$ guarantees the window is never empty, so every input falls into exactly one of the three cases.

With $T$ up to $10^5$ and values to $10^9$, the only performance consideration is bulk input reading; the comparisons themselves are trivial.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        d, l, r = map(int, data[1 + 3 * i:4 + 3 * i])
        # Both ends of the window are inclusive.
        out.append("Too Early" if d < l else "Too Late" if d > r else "Take second dose now")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **$D$ exactly at the lower edge** ($D = L = 8$): inside the window, so `Take second dose now`. The sample's last row tests it, and both ends are inclusive.
- **$D$ exactly at the upper edge** ($D = R$): also inside.
- **Past the window** ($D = 14$ against $R = 10$): `Too Late`.
- **Before the window** ($D = 4444$ against $L = 5555$): `Too Early`.
- **The output strings are exact**, including capitalisation and spacing — `Take second dose now`, `Too Early`, `Too Late`.
- $L \leq R$ is guaranteed, so the window is never empty and the three branches are exhaustive.

## Dry run

| $D$ | $L$ | $R$ | position | output |
|---:|---:|---:|---|---|
| 10 | 8 | 12 | inside | `Take second dose now` |
| 14 | 2 | 10 | past $R$ | `Too Late` |
| 4444 | 5555 | 6666 | before $L$ | `Too Early` |
| 8 | 8 | 12 | on $L$ | `Take second dose now` |

---

Same problem grouped by topic: [../docs/conditionals-case-work/VDATES.md](../docs/conditionals-case-work/VDATES.md)
