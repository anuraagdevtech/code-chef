[Index](../../README.md) &middot; [211. Gift Shop and Coupon &rarr;](GFTSHP.md)

# 126. Inside The Stadium

> CodeChef problem code [`INSTDUM`](https://www.codechef.com/problems/INSTDUM) &middot; difficulty **895** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Running total compared against the index |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Shubman Gill is playing an international match.
He played a total of $N$ balls, where, in the $i^{th}$ ball, he scored $A_{i}$ runs.

The *strike rate* of a player is calculated as : $\frac{\text{no. of runs}}{\text{no. of balls played}}\times 100$.

Preet, a math enthusiast, is currently watching the match. Help him find the number of times, Shubman's *strike rate* became **exactly** $100$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ - the total number of balls played by Gill.
    - The second line of each test case contains $N$ space-separated integers where $A_{i}$ denotes runs scored on $i^{th}$ ball.

**Output**

For each test case, output on a new line, the total number of times the strike rate of Gill became $100$.

## Constraints

- $1 \leq T \leq 10^{5}$
- $1 \leq N \leq 10^{5}$
- $0 \leq A_i \leq 6$
- The sum of $N$ over all test cases won't exceed $10^{6}$.

## Sample

**Sample input**

```
3
4
1 0 2 3
5
2 6 0 1 0
3
1 1 1
```

**Sample output**

```
2
0
3
```

<details><summary>Explanation</summary>

**Test case $1$:** Shubhman's strike rate would be:
- After $1$ ball: $\frac{\text{1}}{\text{1}}\times 100 = 100$.
- After $2$ balls: $\frac{\text{1}}{\text{2}}\times 100 = 50$.
- After $3$ balls: $\frac{\text{3}}{\text{3}}\times 100 = 100$.
- After $4$ balls: $\frac{\text{6}}{\text{4}}\times 100 = 150$.

Thus, the strike rate was exactly $100$ twice.

**Test case $2$:** Shubhman's strike rate would be:
- After $1$ ball: $\frac{\text{2}}{\text{1}}\times 100 = 200$.
- After $2$ balls: $\frac{\text{8}}{\text{2}}\times 100 = 400$.
- After $3$ balls: $\frac{\text{8}}{\text{3}}\times 100 = 266.66$.
- After $4$ balls: $\frac{\text{9}}{\text{4}}\times 100 = 225$.
- After $5$ balls: $\frac{\text{9}}{\text{5}}\times 100 = 180$.

Thus the strike rate was never exactly $100$.

</details>

## Approach

Strike rate after $i$ balls is $\frac{\text{runs}}{i} \times 100$, so it equals exactly $100$ precisely when the runs scored so far equal the balls faced:

$$\text{prefix sum}_i = i$$

No division is needed at all — clearing it turns a floating-point comparison into an integer identity, which is both exact and faster. Comparing `total / i * 100 == 100` would be the fragile version.

So the solution is a single pass maintaining a running total, incrementing a counter whenever that total matches the current ball number. Only the running sum needs storing, so this is $O(N)$ time and $O(1)$ space — no prefix array required, since each prefix is consumed immediately.

Sample case 3 is the all-ones case where the condition holds after every ball, giving $3$. Sample case 1 matches at balls $1$ and $3$ — after $[1]$ the total is $1$, and after $[1,0,2]$ it is $3$ — giving $2$. Sample case 2 never matches, since the opening $2$ runs off a single ball puts the total permanently ahead.

The efficiency constraints are worth reading: $T$ reaches $10^5$ and $N$ reaches $10^5$, but the **sum of $N$** is capped at $10^6$. That bound is the setter saying a linear pass per test case is intended and safe, while anything quadratic is not. Reading the whole input in one go rather than line by line matters at this volume.

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
        runs = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        total = 0
        hits = 0
        for i, r in enumerate(runs, 1):
            total += int(r)
            # Strike rate is 100 exactly when runs == balls faced.
            if total == i:
                hits += 1
        out.append(str(hits))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **No match at all** (the second row): the answer is $0$, so zero is legitimate output.
- **Every prefix matches** (all ones): the answer is $N$ — the running total tracks the index exactly.
- **A zero run breaks a match and a later run restores it.** In the first row the totals are $1, 1, 3, 6$ against indices $1, 2, 3, 4$: a match at index $1$, lost at $2$ because of the zero, regained at $3$. So the count is not monotone and the whole prefix has to be walked.
- **$A_i$ may be $0$ or as large as $6$**, so the total can jump well past the index and never come back.
- A strike rate of exactly $100$ means runs equal balls faced, which is the condition $\text{total} = i$.

## Dry run

First sample, runs $1, 0, 2, 3$:

| ball $i$ | run | total | $\text{total} = i$? |
|---:|---:|---:|:---:|
| 1 | 1 | 1 | yes |
| 2 | 0 | 1 | no |
| 3 | 2 | 3 | yes |
| 4 | 3 | 6 | no |

Two matches, so the output is `2`. The third sample ($1,1,1$) matches at every ball, giving `3`.

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#127 of 486): [../../by-rating/127-INSTDUM.md](../../by-rating/127-INSTDUM.md)
