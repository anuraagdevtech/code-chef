# 029. Air Conditioner Temperature

> [`ACTEMP`](https://www.codechef.com/problems/ACTEMP) &middot; difficulty **584** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Intersecting interval constraints |
| **CodeChef tags** | `Mathematics`, `Basic Programming Concepts`, `Basic Math` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

There are three people sitting in a room - Alice, Bob, and Charlie. They need to decide on the temperature to set on the air conditioner. Everyone has a demand each:

- Alice wants the temperature to be at least $A$ degrees.
- Bob wants the temperature to be at most $B$ degrees.
- Charlie wants the temperature to be at least $C$ degrees.

Can they all agree on some temperature, or not?

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of a single line which contains three integers - $A, B, C$.

**Output**

For each test case, output on a new line, "Yes" or "No". "Yes", if they can decide on some temperature which fits all their demands. Or "No", if no temperature fits all their demands.

You may print each character of the string in either uppercase or lowercase (for example, the strings `NO`, `nO`, `No`, and `no` will all be treated as identical).

## Constraints

- $1 \leq T \leq 100$
- $1 \leq A, B, C \leq 100$

**Subtasks**

- **Subtask 1 (10 points):** $1 \leq M \leq 10$
- **Subtask 2 (20 points):** The sum of $N$ across all test cases won't exceed $20$.
- **Subtask 3 (70 points):** No further constraints.

## Sample

**Sample input**

```
4
30 35 25
30 35 40
30 35 35
30 25 35
```

**Sample output**

```
Yes
No
Yes
No
```

<details><summary>Explanation</summary>

**Test Case 1:** Alice wants the temperature to be $\ge 30$, Bob wants it to be $\le 35$, and Charlie wants it to be $\ge 25$. The temperatures $30, 31, 32, 33, 34, 35$ all satisfy all their demands. So they can choose any of these 6 temperatures, and so the answer is "Yes".

**Test Case 2:** Alice wants the temperature to be $\ge 30$, Bob wants it to be $\le 35$, and Charlie wants it to be $\ge 40$. A number can't be both $\ge 40$, and $\le 35$. So there is no temperature that satisfies all their demands. So the answer is "No".

**Test Case 3:** Alice wants the temperature to be $\ge 30$, Bob wants it to be $\le 35$, and Charlie wants it to be $\ge 35$. The temperature $35$ satisfies all their demands. So the answer is "Yes".

**Test Case 4:** Alice wants the temperature to be $\ge 30$, Bob wants it to be $\le 25$, and Charlie wants it to be $\ge 35$. A number can't be both $\ge 30$, and $\le 25$. So there is no temperature that satisfies all their demands. So the answer is "No".

</details>

## Approach

Each person constrains the temperature $t$ from one side: Alice needs $t \geq A$, Charlie needs $t \geq C$, and Bob needs $t \leq B$. Together they describe an interval, and the question is whether that interval is non-empty.

The two lower bounds combine into the tighter of the pair — satisfying both $t \geq A$ and $t \geq C$ is the same as satisfying $t \geq \max(A, C)$. There is a single upper bound. So a valid temperature exists exactly when

$$\max(A, C) \leq B$$

Collapsing several same-direction bounds into one extremum is the general move here: many lower bounds become their maximum, many upper bounds become their minimum, and a solution exists when the resulting low point does not pass the high point.

Equality is allowed, so a single feasible temperature is enough. Sample case 3 ($A=30, B=35, C=35$) leaves exactly one option, $35$ degrees, and answers `Yes`.

Note also that sample case 4 fails for a different reason than case 2: there $B = 25$ sits below even Alice's $A = 30$, so Bob alone conflicts with Alice. The single `max` comparison covers both failure modes without separate cases.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c = map(int, data[1 + 3 * i:4 + 3 * i])
        # Two lower bounds collapse to their max; feasible if it clears b.
        out.append("Yes" if max(a, c) <= b else "No")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/conditionals-case-work/ACTEMP.md](../docs/conditionals-case-work/ACTEMP.md)
