# 483. Digit Removal

> CodeChef problem code [`DIGITREM`](https://www.codechef.com/problems/DIGITREM) &middot; difficulty **1754** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Digit-position candidates for the next clean number |
| **Time** | $O(\log^2 N)$ per test case |
| **Space** | $O(\log N)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You are given an integer $N$ and a digit $D$. Find the minimum non-negetive integer you should add to $N$ such that the final value of $N$ does not contain the digit $D$.

**Input**

- The first line contains $T$ denoting the number of test cases. Then the test cases follow.
- Each test case contains two integers $N$ and $D$ on a single line denoting the original number and the digit you need to avoid.

**Output**

For each test case, output on a single line the minimum non-negetive integer you should add to $N$.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^9$
- $0 \leq D \leq 9$

**Subtasks**

- **Subtask 1 (100 points):** Original constraints

## Sample

**Sample input**

```
5
21 5
8 8
100 0
5925 9
434356 3
```

**Sample output**

```
0
1
11
75
5644
```

<details><summary>Explanation</summary>

**Test case $1$:** $N = 21$ does not contain the digit $D = 5$. Hence there is no need to add any integers to $N$.

**Test case $2$:** If $1$ is added to $N = 8$, it becomes equal to $9$, which does not contain the digit $D = 8$.

**Test case $3$:** The minimum integer you should add to $N = 100$ such that the final value of $N$ does not contain the digit $D = 0$ is $11$.

**Test case $5$:** The minimum integer which is greater than $434356$ and does not contain the digit $D = 3$ is $440000$. So we should add $440000 - 434356 = 5644$.

</details>

## Approach

We want the smallest $M \geq N$ whose decimal form avoids the digit $D$; the answer is $M - N$.

Let $p$ be the **leftmost** position where $N$'s digit equals $D$. If there is none, $M = N$ and the answer is $0$. Otherwise, let $i$ be the first position where $M$ and $N$ differ. Then $M_i > N_i$ (else $M < N$), and $M$ agrees with $N$ before $i$, so those digits must be clean — forcing $i \leq p$. That gives at most $p+1$ candidates, one per $i$:

- keep $N$'s digits before $i$;
- at $i$, take the **smallest** digit above $N_i$ that is not $D$;
- fill the rest with the smallest allowed digit, which is $0$ unless $D = 0$, in which case it is $1$.

Take the smallest candidate. A position can fail outright when the digit would have to exceed $9$ — and if *every* position fails, $M$ must be longer than $N$, so the answer is the smallest clean number with one more digit: leading $1$ (or $2$ when $D = 1$) followed by the fill digit.

Filling with the smallest digit rather than copying $N$'s tail is the point: once a more significant digit has been raised, the tail is free, and zeroing it out is what keeps $M$ minimal.

The samples walk through each branch. $21$ with $D = 5$ is already clean. $8$ with $D = 8$ raises the only digit to $9$, costing $1$. $100$ with $D = 0$ raises position $1$ to $1$ and fills with $1$, giving $111$ — not $200$, because the more significant raise is dearer. $5925$ with $D = 9$ cannot raise the $9$ at all, so it raises the leading $5$ to $6$ and zeroes the rest: $6000$. And $434356$ with $D = 3$ raises the second digit to $4$, giving $440000$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, d = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        s = str(n)
        fill = "0" if d else "1"
        bad = next((j for j, ch in enumerate(s) if int(ch) == d), -1)
        if bad < 0:
            out.append("0")
            continue
        best = None
        # M first differs from N at some position at or before the leftmost D.
        for j in range(bad, -1, -1):
            v = int(s[j]) + 1
            if v == d:
                v += 1
            if v > 9:
                continue
            cand = int(s[:j] + str(v) + fill * (len(s) - j - 1))
            if best is None or cand < best:
                best = cand
        if best is None:
            # Every digit position overflowed, so M needs one more digit.
            best = int(("2" if d == 1 else "1") + fill * len(s))
        out.append(str(best - n))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(\log^2 N)$ per test case
- **Space:** $O(\log N)$

> CodeChef tags: `Mathematics`, `Basic Math`
