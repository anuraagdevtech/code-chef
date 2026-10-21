# 099. The Preparations

> [`SUPCHEF`](https://www.codechef.com/problems/SUPCHEF) &middot; difficulty **823** &middot; time limit **0.5s** &middot; 500 to 1000 difficulty rating (Level 1)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Strict comparison against a deadline |
| **CodeChef tags** | `Basic Programming Concepts`, `Mathematics`, `Conditional Statements`, `Basic Math` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef has an exam which will start exactly $M$ minutes from now. However, instead of preparing for his exam, Chef started watching Season-$1$ of Superchef. Season-$1$ has $N$ episodes, and the duration of **each** episode is $K$ minutes.

Will Chef be able to finish watching Season-$1$ **strictly before** the exam starts?

$\textbf{Note:}$ Please read the explanations of the sample test cases carefully.

**Input**

- The first line contains an integer $T$ denoting the number of test cases. $T$ test cases then follow.
- The first and only line of each test case contains $3$ space separated integers $M$, $N$ and $K$.

**Output**

For each test case, output on one line YES if it is possible to finish Season-1 **strictly before** the exam starts, or NO if it is not possible to do so.

Output is case insensitive, which means that "yes", "Yes", "YEs", "no", "nO" - all such strings will be acceptable.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq M \leq 10^9$
- $1 \leq N, K \leq 10^4$

## Sample

**Sample input**

```
3
10 1 10
25 2 10
15 2 10
```

**Sample output**

```
NO
YES
NO
```

<details><summary>Explanation</summary>

**Test Case $1$:** The duration of the only episode is $10$ minutes, and the exam starts exactly after $10$ minutes. So, Chef will **not** be able to finish watching Season-$1$ strictly before the exam starts.

**Test Case $2$:** There are two episodes in Season-$1$, each of duration $10$ minutes. Therefore, Chef will require $10 + 10 = 20$ minutes to finish watching Season-$1$. As the exam starts after $25$ minutes, Chef will be able to finish watching Season-$1$ strictly before the exam starts.

**Test Case $3$:** There are two episodes in Season-$1$, each of duration $10$ minutes. Therefore, Chef will require $10 + 10 = 20$ minutes to finish watchin Season-$1$. As the exam starts after $15$ minutes, Chef will **not** be able to finish watching Season-$1$ strictly before the exam starts.

</details>

## Approach

Watching $N$ episodes of $K$ minutes each takes $NK$ minutes, and Chef must finish **strictly before** the exam at minute $M$:

$$N \cdot K < M$$

The whole problem is that strict `<`. Sample case 1 is built on it: one episode of $10$ minutes against an exam $10$ minutes away means Chef finishes exactly as the exam starts, which does not count as "before", so the answer is `NO`. A `<=` would get this wrong while passing the other two samples — the classic way this problem is failed.

Sample case 3 is the straightforward overrun ($20$ minutes of episodes against a $15$-minute window), and case 2 the comfortable fit ($20 < 25$).

On magnitudes: $M$ reaches $10^9$ while $N$ and $K$ each reach $10^4$, so the product $NK$ can reach $10^8$ — comfortably inside a 32-bit signed integer, though a C solution multiplying before checking would want to be sure. In Python the question does not arise.

With $T$ up to $10^4$, reading the stream in one go and writing one joined block is worth doing; the arithmetic itself is free.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        m, n, k = map(int, data[1 + 3 * i:4 + 3 * i])
        # "Strictly before" - finishing exactly at minute M is too late.
        out.append("YES" if n * k < m else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/basic-math/SUPCHEF.md](../docs/basic-math/SUPCHEF.md)
