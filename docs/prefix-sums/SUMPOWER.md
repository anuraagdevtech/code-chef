[&larr; 440. Mystical Numbers](XORGAND.md) &middot; [Index](../../README.md) &middot; [456. Maximise Sum &rarr;](MAXIMISESUM.md)

# 447. Summary Power

> CodeChef problem code [`SUMPOWER`](https://www.codechef.com/problems/SUMPOWER) &middot; difficulty **1709** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Prefix Sums |
| **Technique** | Counting each boundary's contribution |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

You work as an engineer. You were given an empty board with $K$ consecutive cells; at any moment, each cell can display one character.

You want the board to display a string $S$ with length $N > K$. Since the board isn't large enough, you want to display the string in $N-K+1$ steps. In the $i$-th step ($1 \le i \le N-K+1$), you'll make the board display the characters $S_i, S_{i+1}, \dots, S_{i+K-1}$.

The power required to switch the board from step $i$ to step $i+1$ (for $1 \le i \le N-K$) is equal to the number of characters displayed on the board that have to change between these steps. You should find the total power required for the whole process of displaying a string, i.e. the sum of powers required for switching between all consecutive pairs of steps.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains two space-separated integers $N$ and $K$.
- The second line contains a single string $S$ with length $N$.

**Output**
For each test case, print a single line containing one integer — the total power required for text switching.

**Constraints**
- $1 \le T \le 1,000$
- $2 \le N \le 10^5$
- $1 \le K \lt N$
- each character of $S$ is a lowercase English letter
- the sum of $N$ for all test cases does not exceed $10^6$

**Subtasks**
**Subtask #1 (20 points):**
- $1 \le T \le 100$
- $2 \le N \le 50$

**Subtask #2 (80 points):** original constraints

## Constraints

- $1 \le T \le 1,000$
- $2 \le N \le 10^5$
- $1 \le K \lt N$
- each character of $S$ is a lowercase English letter
- the sum of $N$ for all test cases does not exceed $10^6$

## Sample

**Sample input**

```
3
6 3
aabbcc
5 2
abccc
4 3
aabb
```

**Sample output**

```
4
3
1
```

<details><summary>Explanation</summary>

**Example case 1:**
- In step $1$, the board is displaying "aab".
- In step $2$, the board is displaying "abb".
- In step $3$, the board is displaying "bbc".
- In step $4$, the board is displaying "bcc".

The power required for switching from the $1$-st to the $2$-nd step is $1$, because cell $1$ changes from 'a' to 'a' (requiring power $0$), cell $2$ changes from 'a' to 'b' (requiring power $1$) and cell $3$ changes from 'b' to 'b' (requiring power $0$); $0 + 1 + 0 = 1$.

The power required for switching between the $2$-nd and $3$-rd step is $2$ and the power required for switching between the $3$-rd and $4$-th step is $1$.

Therefore, the answer is $1 + 2 + 1 = 4$.

</details>

## Approach

Board slot $j$ shows $S_{i+j}$ at step $i$ and $S_{i+j+1}$ at step $i+1$, so it changes exactly when those two characters differ. The power of one switch is therefore the number of **adjacent mismatches** inside a window:

$$\text{power}(i) = \sum_{p=i}^{i+K-1} d_p, \qquad d_p = [\,S_p \neq S_{p+1}\,]$$

Summing over all $N-K$ switches and swapping the order of summation turns the double sum into a weighted single sum: each boundary $p$ is counted once for every step $i$ whose window covers it, that is for $i \in [\max(1, p-K+1),\ \min(N-K, p)]$. So

$$\text{answer} = \sum_{p=1}^{N-1} d_p \cdot \Bigl(\min(N-K,\, p) - \max(1,\, p-K+1) + 1\Bigr)$$

with negative weights clamped to zero. Counting by contribution is what makes this linear — evaluating each window separately would be $O(NK)$, which at $\sum N = 10^6$ and $K$ near $N$ is hopeless.

A boundary near either end of the string gets a smaller weight, because fewer windows reach it; interior boundaries get the full $\min(K, N-K)$.

The samples make the weights visible. `aabbcc` with $K = 3$ has mismatches at $p = 2$ and $p = 4$, each covered by two of the three steps, giving $4$. `abccc` with $K = 2$ has mismatches at $p = 1$ and $p = 2$, weighted $1$ and $2$, giving $3$. And `aabb` with $K = 3$ has a single switch and a single mismatch inside it, giving $1$.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 3 * i]), int(data[2 + 3 * i])
        s = data[3 + 3 * i]
        steps = n - k
        total = 0
        for p in range(1, n):            # boundary between S_p and S_{p+1}
            if s[p - 1] == s[p]:
                continue
            # How many windows cover this boundary.
            hi = min(steps, p)
            lo = max(1, p - k + 1)
            if hi >= lo:
                total += hi - lo + 1
        out.append(str(total))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Count by boundary, not by step.** A board cell changes between steps $i$ and $i+1$ exactly when the two characters it shows differ, so each adjacent pair $(S_p, S_{p+1})$ of different letters contributes once for every window that spans it.
- **The window count for boundary $p$ is $\min(N-K,\, p) - \max(1,\, p-K+1) + 1$**, clipped at both ends — the step index must stay within $1 \dots N-K$ and the boundary must fall inside the window.
- **Equal adjacent characters contribute nothing**, however many windows cover them, which is what makes `aabbcc` cheaper than an alternating string of the same length.
- **Boundaries near the ends are covered by fewer windows**, which the clipping captures: in the second sample the first boundary is seen once and the second twice.
- **$N > K$ is guaranteed**, so there is at least one transition and the step count is positive.
- **A clip can empty the interval**, hence the explicit guard, though with $N > K$ every interior boundary has at least one covering window.
- **Sum of $N \leq 10^6$**: one pass over the boundaries with constant work each.

## Dry run

First sample: $N = 6$, $K = 3$, $S = $ `aabbcc`, so there are $3$ transitions.

| boundary $p$ | $S_p, S_{p+1}$ | differ? | windows covering it | contribution |
|---:|---|:---:|---|---:|
| 1 | `a`, `a` | no | — | 0 |
| 2 | `a`, `b` | yes | steps $1, 2$ | 2 |
| 3 | `b`, `b` | no | — | 0 |
| 4 | `b`, `c` | yes | steps $2, 3$ | 2 |
| 5 | `c`, `c` | no | — | 0 |

Total `4`.

> CodeChef tags: `Data Structures`

---

Same problem in rating order (#417 of 486): [../../by-rating/417-SUMPOWER.md](../../by-rating/417-SUMPOWER.md)
