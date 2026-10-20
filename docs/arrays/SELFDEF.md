# 61. Self Defence Training

> CodeChef problem code [`SELFDEF`](https://www.codechef.com/problems/SELFDEF) &middot; difficulty **716** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Counting values inside a closed range |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

After the phenomenal success of the 36th Chamber of Shaolin, San Te has decided to start 37th Chamber of Shaolin. The aim this time is to equip women with shaolin self-defence techniques.

The only condition for a woman to be eligible for the special training is that she must be between $10$ and $60$ years of age, inclusive of both $10$ and $60$.

Given the ages of $N$ women in his village, please help San Te find out how many of them are eligible for the special training.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$, the number of women.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2,..., A_N$, the ages of the women.

**Output**

For each test case, output in a single line the number of women eligible for self-defence training.

## Constraints

- $1 \leq T \leq 20$
- $1 \leq N \leq 100$
- $1 \leq A_i \leq 100$

## Sample

**Sample input**

```
3
3
15 23 65
3
15 62 16
2
35 9
```

**Sample output**

```
2
2
1
```

<details><summary>Explanation</summary>

**Test Case $1$**: Out of the women, only the $1^{st}$ and $2^{nd}$ women are eligible for the training because their ages lie in the interval $[10,60]$. Hence the answer is 2.

**Test Case $2$**: Only the $1^{st}$ and $3^{rd}$ women are eligible for the training because their ages lie in the interval $[10,60]$. Hence the answer is again 2.

**Test Case $3$**: Only the $1^{st}$ woman with age $35$ is eligible for the training. Hence the answer is $1$.

</details>

## Approach

A woman qualifies when her age lies between $10$ and $60$ **inclusive of both ends**, so the answer is a single pass counting the values satisfying

$$10 \leq A_i \leq 60$$

Python's chained comparison writes this exactly as the mathematics does — `10 <= a <= 60` — which is both clearer and less error-prone than `a >= 10 and a <= 60`, where it is easy to flip one of the operators.

Inclusivity is the whole trap, and the samples are built around the boundaries rather than the middle. Case 1 contains $65$, just outside the upper limit; case 2 contains $62$, also outside; case 3 contains $9$, one below the lower limit. An age of exactly $10$ or exactly $60$ must count, so both comparisons need the `=`.

As with the other counting problems in this set, nothing needs to be stored: the ages stream past a counter in $O(N)$ time and $O(1)$ space. The per-test-case $N$ varies, so a cursor walks the flat token stream rather than reading line by line.

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
        ages = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        # Both 10 and 60 are eligible, so the range is closed at both ends.
        out.append(str(sum(1 for a in ages if 10 <= int(a) <= 60)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Basic Programming Concepts`
