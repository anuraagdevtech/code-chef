# 394. Three Numbers

> [`THREENUMBERS`](https://www.codechef.com/problems/THREENUMBERS) &middot; difficulty **1675** &middot; time limit **1s** &middot; 1600 to 1800 difficulty problems (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Parity invariant plus a counting identity |
| **CodeChef tags** | `Algorithms`, `Observation` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef has three numbers $A, B,$ and $C$.

He can do the following type of operation:
- Select two numbers amongst $A, B,$ and $C$;
- Add $1$ to the selected numbers;
- Subtract $1$ from the remaining number.

Determine whether Chef can make all the three numbers **equal** after applying the above operation any number of times.
If yes, output the **minimum** number of operations required by Chef.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of single line containing $3$ space-separated integers $A, B,$ and $C$.

**Output**

For each test case, output $-1$ if the numbers cannot be made equal, else output the **minimum** number of operations required to make them equal.

## Constraints

- $1 \leq T \leq 10^4$
- $1 \leq A, B, C \leq 10^9$

## Sample

**Sample input**

```
4
1 1 2
3 7 3
4 4 4
1 2 3
```

**Sample output**

```
-1
2
0
-1
```

<details><summary>Explanation</summary>

**Test case $1$:** It can be proven that we cannot make the numbers equal using any number of operations.

**Test case $2$:** We require a minimum of $2$ operations to make the numbers equal:
- Operation $1$: Select the numbers $A$ and $C$. Thus, $A$ and $C$ become $3+1 = 4$ and $3+1 = 4$ respectively. Also, $B$ becomes $7-1 = 6$.
- Operation $2$: Select the numbers $A$ and $C$. Thus, $A$ and $C$ become $4+1 = 5$ and $4+1 = 5$ respectively. Also, $C$ becomes $6-1 = 5$.

Thus, all $3$ numbers are equal after $2$ operations.

**Test case $3$:** Since all $3$ numbers are already equal, we require no operations.

**Test case $4$:** It can be proven that we cannot make the numbers equal using any number of operations.

</details>

## Approach

Each operation shifts two numbers up and one down, so the **sum rises by exactly $1$** and every pairwise difference changes by $0$ or $\pm 2$. That gives the feasibility test immediately: the differences keep their parity forever, so all three numbers must already be congruent mod $2$. Otherwise print $-1$ — as in $1\,1\,2$ and $1\,2\,3$.

Now count. Suppose $k$ operations end with all three equal to $v$; then $3v = S + k$. If $A$ is the *decremented* number $d_A$ times, it is incremented the other $k - d_A$ times, so

$$v = A + (k - d_A) - d_A \quad\Longrightarrow\quad d_A = \frac{A + k - v}{2}$$

and likewise for $B, C$. These automatically sum to $k$, so the only requirements are that each is a non-negative integer. Integrality is exactly the parity condition again. Non-negativity binds hardest on the **smallest** number $m$:

$$m + k - v \geq 0 \quad\Longleftrightarrow\quad 2k \geq S - 3m$$

So the answer is the smallest $k \geq \max\!\left(0, \left\lceil \frac{S - 3m}{2} \right\rceil\right)$ with $k \equiv -S \pmod 3$. Once the $d$ values are fixed, any interleaving of the operations realises them, so no scheduling is needed.

For $3\,7\,3$: $S = 13$ forces $k \equiv 2 \pmod 3$, and $S - 3m = 4$ needs $k \geq 2$, so $k = 2$ — decrement the $7$ twice to reach $5\,5\,5$. For $4\,4\,4$ both conditions give $k = 0$.

The second bound genuinely matters: $1\,1\,11$ also has $k \equiv 2 \pmod 3$, but $S - 3m = 10$ forces $k \geq 5$, and indeed five operations give $6\,6\,6$.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c = (int(data[1 + 3 * i]), int(data[2 + 3 * i]), int(data[3 + 3 * i]))
        if (a - b) % 2 or (b - c) % 2:
            out.append("-1")          # pairwise parities never change
            continue
        total = a + b + c
        low = min(a, b, c)
        # The smallest number must not need a negative decrement count.
        floor = max(0, (total - 3 * low + 1) // 2)
        out.append(str(floor + (-total - floor) % 3))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/basic-math/THREENUMBERS.md](../docs/basic-math/THREENUMBERS.md)
