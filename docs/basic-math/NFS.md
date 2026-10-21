# 169. Turn It

> CodeChef problem code [`NFS`](https://www.codechef.com/problems/NFS) &middot; difficulty **1350** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Rearranging a kinematic inequality |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

Chef is playing Need For Speed. Currently, his car is running on a straight road with a velocity $U$ metres per second and approaching a $90^{\circ}$ turn which is $S$ metres away from him. To successfully cross the turn, velocity of the car when entering the turn must not exceed $V$ metres per second.

The brakes of Chef's car allow him to slow down with a deceleration (negative acceleration) not exceeding $A$ metres per squared second. Tell him whether he can cross the turn successfully. The velocity $v$ when entering the turn can be determined from Newton's 2nd law to be $v^2 = U^2 + 2 \cdot a \cdot S$ if the car is moving with a uniform acceleration $a$.

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains four space-separated integers $U$, $V$, $A$ and $S$.

**Output**
For each test case, print a single line containing the string `"Yes"` if Chef can cross the turn successfully or `"No"` if he cannot (without quotes).

You may print each character of each string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

**Constraints**
- $1 \leq T \leq 10^5$
- $1 \leq U, V, A, S \leq 10^4$

**Subtasks**
**Subtask #1 (100 points):** original constraints

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq U, V, A, S \leq 10^4$

## Sample

**Sample input**

```
3
1 1 1 1
2 1 1 1
2 2 1 1
```

**Sample output**

```
Yes
No
Yes
```

<details><summary>Explanation</summary>

**Example case 1:** Since $U = V = 1$, Chef does not need to brake and will be able to turn successfully.

**Example case 2:** The smallest velocity Chef's car can have even with the maximum deceleration is $\sqrt{2 \cdot 2 - 2 \cdot 1 \cdot 1} = \sqrt{2}$, which is greater than the maximum allowed velocity for a safe turn.

**Example case 3:** The smallest velocity Chef's car can have with the maximum deceleration is again $\sqrt{2}$, which is smaller than the maximum allowed velocity for a safe turn.

</details>

## Approach

The statement supplies $v^2 = U^2 + 2aS$. Chef brakes as hard as he can, so $a = -A$ and the speed at the turn satisfies

$$v^2 = U^2 - 2AS$$

He crosses safely when $v \leq V$, which — since both are non-negative — is equivalent to comparing the squares:

$$U^2 - 2AS \leq V^2$$

Working with $v^2$ rather than $v$ is the whole trick. It keeps everything in integers and avoids a square root, which would introduce floating point and, worse, a domain error.

That domain point is the case to watch. If $U^2 - 2AS$ is **negative**, the car would have come to a stop before reaching the turn, so it enters at $v = 0$ and certainly succeeds. Taking $\sqrt{U^2 - 2AS}$ there is undefined, but the inequality form handles it without a branch: a negative left side is automatically $\leq V^2$. Sample case 1 is exactly this, with $1 - 2 = -1$.

Braking hardest is optimal because the goal is only to be *slow enough*; there is no reward for arriving fast, so the maximum deceleration gives the best chance. That is why $a = -A$ rather than something in between.

Sample case 2 is the failure: $4 - 2 = 2$ against $V^2 = 1$, so the car is still too fast. Case 3 has the same approach speed but a more forgiving limit, $V^2 = 4$, and passes.

With all values to $10^4$, $U^2$ and $2AS$ reach $10^8$ and $2 \times 10^8$ — inside 32 bits, though a C solution should be careful.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        u, v, a, s = map(int, data[1 + 4 * i:5 + 4 * i])
        # Compare squares: no sqrt, and a negative left side (the car stops
        # before the turn) is handled without a special case.
        out.append("Yes" if u * u - 2 * a * s <= v * v else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$
