# 999 &middot; Bear and Ladder

> CodeChef problem code [`BRLADDER`](https://www.codechef.com/problems/BRLADDER) &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topics used

| | |
|---|---|
| **Topic** | Conditionals & Case Work |
| **Technique** | Deriving an adjacency rule from an edge list |
| **CodeChef tags** | `Basic Programming Concepts`, `Algorithms`, `Conditional Statements`, `Implementation` |
| **CodeChef category** | extcontest |
| **Time** | $O(1)$ per query |
| **Space** | $O(1)$ |

Same write-up grouped by topic: [../docs/conditionals-case-work/BRLADDER.md](../docs/conditionals-case-work/BRLADDER.md)

## Question

Bearland has infinitely many cities, numbered starting from 1.
Some pairs of cities are connected with bidirectional roads:

  - There are roads 1-2, 3-4, 5-6, 7-8, and so on (there is a road between cities 2*i+1 and 2*i+2 for every non-negative integer i).

  - There are roads 1-3, 3-5, 5-7, 7-9, ... (between every two consecutive odd numbers).

  - There are roads 2-4, 4-6, 6-8, 8-10, ... (between every two consecutive even numbers).

This is how the first few cities and roads between them look like:

<img src="https://codechef_shared.s3.amazonaws.com/uploads/2017/03/LTIME46/BRLADDER.png" />

You are given **Q** queries.
In each query, for the given pair of different cities **a** and **b**, you should check if there is a road between them.
For each query, print "YES" or "NO" accordingly.

**Input**

The first line of the input contains an integer **Q**, denoting the number of queries.

Each of the following **Q** lines contains two distinct integers **a** and **b**, denoting two cities in one query.

**Output**

For each query, output a single line containing the answer — "YES" if there is a road between the given cities **a** and **b**, and "NO" otherwise (without the quotes).

**Constraints**

- 1 ≤ **Q** ≤ 1000

- 1 ≤ **a**, **b** ≤ 10^9

- **a** ≠ **b**

## Constraints

- 1 ≤ Q ≤ 1000
- 1 ≤ a, b ≤ 10^9
- a ≠ b

## Sample

**Sample input**

```
7
1 4
4 3
5 4
10 12
1 3
999999999 1000000000
17 2384823
```

**Sample output**

```
NO
YES
NO
YES
YES
YES
NO
```

<details><summary>Explanation</summary>

In the example test, the answer is "YES" for pairs (4, 3), (10, 12), (1, 3) and (999999999, 1000000000).
Roads 3-4 and 1-3 you can see on the drawing in the statement.

The answer is "NO" for example for a pair (1, 4), because there is no road between cities 1 and 4.

</details>

## Approach

The graph is infinite, so the answer has to come from a rule rather than from building anything. Read the three families of roads and work out what they mean for a pair $(a, b)$:

1. **Rungs** $2i+1 \leftrightarrow 2i+2$: the pairs $1$–$2$, $3$–$4$, $5$–$6$, … These differ by $1$, and the smaller endpoint is always **odd**.
2. **Odd rail** — consecutive odd numbers, differing by $2$.
3. **Even rail** — consecutive even numbers, also differing by $2$.

Families 2 and 3 together cover *every* pair differing by $2$, since two numbers two apart always share a parity. So the rule collapses to

$$|a - b| = 2, \quad\text{or}\quad |a - b| = 1 \text{ with } \min(a,b) \text{ odd}$$

The parity condition on the difference-of-one case is the whole problem. Not every adjacent pair is joined: $1$–$2$ and $3$–$4$ are rungs, but $2$–$3$ and $4$–$5$ are not. Sample cases 2 and 3 are placed side by side to make this exact point — $4$–$3$ is a road (smaller is $3$, odd) while $5$–$4$ is not (smaller is $4$, even).

Sample case 6 confirms the rule survives at the top of the range: $999999999$ is odd, so it is rung-joined to $1000000000$.

With coordinates to $10^9$ and $Q$ up to $1000$, only an $O(1)$ test per query is viable — which is exactly what reading the structure, rather than simulating it, buys. This graph is the infinite "ladder", and recognising the rungs-plus-rails shape is what makes the rule obvious.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    q = int(data[0])
    out = []
    for i in range(q):
        a, b = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        d = abs(a - b)
        # Difference of 2 is always a rail; difference of 1 is a rung only
        # when the lower endpoint is odd.
        road = d == 2 or (d == 1 and min(a, b) % 2 == 1)
        out.append("YES" if road else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per query
- **Space:** $O(1)$
