# 294. Missing Numbers

> CodeChef problem code [`MISS_NUM`](https://www.codechef.com/problems/MISS_NUM) &middot; difficulty **1594** &middot; time limit **2s**

| | |
|---|---|
| **Topic** | Brute Force |
| **Technique** | Guessing which two values are the sum and difference |
| **Time** | $O(1)$ per test case — twelve candidate assignments |
| **Space** | $O(1)$ |
| **Roadmap course** | 1400 to 1600 difficulty problems (Level 2) |

## Question

Alice (uniformly and independently) randomly picks two integers $a, b$ from the range $[1,10^4]$, and writes down the values of $a + b$, $a - b$, $a \cdot b$ and $\lfloor \frac{a}{b} \rfloor$ (integer division) in some random order. Unfortunately, she forgot the values of $a$ and $b$. You need to help her to find out if there exists two integers $a, b$ such that $1 \leq a, b \leq 10^4$ and $a + b$, $a - b$, $a \cdot b$, $\lfloor \frac{a}{b} \rfloor$ are the numbers she has written down.

If a solution exists, it is guaranteed to be unique.

**Input**

- The first line of input contains a single integer $T$, denoting the number of testcases. The description of $T$ testcases follows.
- Each testcase consists of a single line of input, containing four space-separated integers $A, B, C, D$ — the values written down by Alice. It is guaranteed that at most one of the four numbers $A,B,C,D$ will be negative.

**Output**

- For each testcase, output in a single line, separated by a space, the two numbers Alice has chosen **in order** (i.e, if the solution is $a = 1$ and $b = 2$, print $1 \ 2$ and not $2 \ 1$). If there does not exist any such choice of integers, print $-1$ **twice**, separated by a space, instead.

## Constraints

- $1 \leq T \leq 10^5$
- $-10^{9} \leq A,B,C,D \leq 10^{9}$
- At most one of $A, B, C, D$ is negative.

**Subtasks**

**Subtask #1 (100 points):** Original constraints

## Sample

**Sample input**

```
2
-1 72 0 17
1 4 5 6
```

**Sample output**

```
8 9
-1 -1
```

<details><summary>Explanation</summary>

**Test case $1$:** With $a = 8, b = 9$ we obtain $8 + 9 = 17, 8 - 9 = -1, 8 \cdot 9 = 72, \lfloor \frac{8}{9} \rfloor = 0$ which are exactly the $4$ numbers written down by Alice.

**Test case $2$:** It can be shown that no choice of integers $a, b$ can produce the given $4$ numbers.

</details>

## Approach

The four written values are $a+b$, $a-b$, $ab$ and $\lfloor a/b \rfloor$ in unknown order. Trying to identify them by size is fragile — the product is usually largest but not always, and the quotient can tie with others.

Instead, exploit that **two of them determine everything**. If we guess which value is the sum $s$ and which is the difference $d$, then

$$a = \frac{s+d}{2}, \qquad b = \frac{s-d}{2}$$

There are only $4 \times 3 = 12$ ordered choices, so try them all. For each, require $s+d$ to be even (otherwise $a$ is not an integer) and both $a$ and $b$ to lie in $[1, 10^4]$, then **verify** by recomputing all four quantities and comparing the sorted lists against the sorted input.

Verifying the full multiset rather than just the two unused values is what makes this safe: it automatically handles duplicates among the four numbers, which a positional check would mishandle.

The problem guarantees uniqueness when a solution exists, so the first match can be returned immediately.

Sample case 1, $[-1, 72, 0, 17]$: taking $s = 17$ and $d = -1$ gives $a = 8$, $b = 9$, and recomputing yields $17, -1, 72, 0$ — the same multiset, so the answer is `8 9`. Note the output order matters: $a$ first, and here $a < b$, which is why the difference is the negative value.

Sample case 2 exhausts all twelve assignments without a match and prints `-1 -1`.

The guarantee that at most one of the four is negative is a consistency hint — only $a-b$ can be — but the verification step makes relying on it unnecessary.

## Solution (Python)

```python
import sys


def solve(vals):
    target = sorted(vals)
    for i in range(4):
        for j in range(4):
            if i == j:
                continue
            s, d = vals[i], vals[j]
            if (s + d) % 2:
                continue
            a, b = (s + d) // 2, (s - d) // 2
            if not (1 <= a <= 10000 and 1 <= b <= 10000):
                continue
            # Verify the whole multiset, which handles duplicates for free.
            if sorted((a + b, a - b, a * b, a // b)) == target:
                return a, b
    return -1, -1


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        vals = [int(v) for v in data[1 + 4 * i:5 + 4 * i]]
        a, b = solve(vals)
        out.append(f"{a} {b}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case — twelve candidate assignments
- **Space:** $O(1)$

## Edge cases

- **The sum and difference pin down $a$ and $b$.** From $s = a+b$ and $d = a-b$ we get $a = (s+d)/2$ and $b = (s-d)/2$, so guessing which two of the four written values are the sum and the difference leaves nothing to search — twelve ordered pairs in all.
- **The parity check comes first**: if $s + d$ is odd the candidate cannot yield integers, so it is discarded before dividing.
- **The recovered pair must be verified against the whole multiset**, not just against $s$ and $d$ — the product and the quotient must match too. Comparing sorted lists handles duplicates for free.
- **The range $[1, 10^4]$ must be enforced** on the recovered values, or a wildly wrong candidate could accidentally reproduce some of the numbers.
- **At most one of the four can be negative** (only $a - b$ can be), which is a useful sanity check on the input but not needed by the algorithm.
- **No solution** → `-1 -1` (the second row), printed as a pair rather than a single value.
- **Uniqueness is guaranteed** when a solution exists, so the first match can be returned immediately.

## Dry run

First sample: the written values are $-1, 72, 0, 17$.

Trying $s = 17$ and $d = -1$:

| step | value |
|---|---:|
| $a = (17 + (-1))/2$ | 8 |
| $b = (17 - (-1))/2$ | 9 |
| $a + b$ | 17 ✓ |
| $a - b$ | $-1$ ✓ |
| $a \cdot b$ | 72 ✓ |
| $\lfloor a/b \rfloor$ | 0 ✓ |

All four match, so the output is `8 9`.

> CodeChef tags: `Mathematics`, `Basic Math`

---

Same problem in rating order (#339 of 486): [../../by-rating/339-MISS_NUM.md](../../by-rating/339-MISS_NUM.md)
