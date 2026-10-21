# 1486 &middot; Chef Odd

> CodeChef problem code [`CHEFODD`](https://www.codechef.com/problems/CHEFODD) &middot; time limit **2.5s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topics used

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Parity and capacity constraints together |
| **CodeChef tags** | `Mathematics` |
| **CodeChef category** | easy |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/number-theory/CHEFODD.md](../docs/number-theory/CHEFODD.md)

## Question

You want to partition the set $S = \{1, 2, \ldots, N\}$ into $K$ sets $S_1, S_2, \ldots, S_K$, such that $|S_i| \ge 2$, and the sum of elements in each $S_i$ is odd.

Is it possible to do so?

**Note 1:** Partitioning the set $S = \{1, 2, \ldots, N\}$ into $K$ sets $S_1, S_2, \ldots, S_K$ means that every element of $S$ should be in exactly one of the sets $S_1, S_2, \ldots, S_K$, and $S_i \subseteq S$, for all $1 \leq i \leq K$.

**Note 2:** $|A|$ denotes the number of elements in the set $A$.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first line and only line of each test case contains two space-separated integers, $N$ and $K$.

**Output**

For each test case, output `YES` if you can partition the set satisfying the requirements. Otherwise, output `NO`.

You may print each character of `YES` and `NO` in uppercase or lowercase (for example, `yes`, `yEs`, `Yes` will be considered identical).

## Constraints

- $1 \leq T \leq 10^5$
- $2 \leq N \leq 10^{18}$
- $1 \leq K \leq 10^{18}$

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
2
5 2
14 5
```

**Sample output**

```
NO
YES
```

<details><summary>Explanation</summary>

**Test case $1$**: There is no way you can partition $\{1, 2, 3, 4, 5\}$ into $2$ subsets such that each has an odd sum and each subset contains at least $2$ integers.

**Test case $2$**: One of the ways to partition is $\{1, 4, 6, 12\}, \{2, 5\}, \{3, 14\}, \{7, 10, 11, 13\}, \{9, 8\}$. The sum of elements in each subset is $23, 7, 17, 41, 17$, each of which is odd and each subset contains at least $2$ integers.

</details>

## Approach

Two independent requirements must both hold.

**Capacity.** Every part needs at least $2$ elements, so $K$ parts consume at least $2K$ of the $N$ available:

$$N \geq 2K$$

**Parity.** A subset has an odd sum exactly when it contains an **odd number of odd elements**. The set $\{1, \ldots, N\}$ contains $O = \lceil N/2 \rceil$ odd numbers, and each of the $K$ parts must take an odd count of them. Summing $K$ odd numbers gives a total with the same parity as $K$, so

$$O \equiv K \pmod 2$$

Those two conditions are also sufficient. Give each part one odd number — possible since $N \geq 2K$ forces $O \geq K$ — then the remaining $O - K$ odds are even in number and can be handed out two at a time without disturbing any part's parity. The evens are unconstrained and fill the parts up to size $2$.

Sample case 1 fails the parity test: $N = 5$ has $O = 3$ odd numbers against $K = 2$ parts, and $3 \not\equiv 2 \pmod 2$. The capacity is fine ($5 \geq 4$), so a solution checking only sizes would wrongly say yes.

Sample case 2 passes both: $N = 14$ gives $O = 7 \equiv 5 \pmod 2$, and $14 \geq 10$.

Note the parity condition is equivalent to saying the total $\frac{N(N+1)}{2}$ has the same parity as $K$ — the evens contribute nothing, so the grand total's parity is just $O \bmod 2$.

With $N, K$ up to $10^{18}$, only this $O(1)$ test is viable; $2K$ can reach $2 \times 10^{18}$, which still fits a 64-bit signed integer but only just.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, k = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        odds = (n + 1) // 2
        # Each part needs two elements, and each needs an odd count of odds.
        ok = n >= 2 * k and odds % 2 == k % 2
        out.append("YES" if ok else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
