# 172. Tom And Jerry 1

> CodeChef problem code [`TANDJ1`](https://www.codechef.com/problems/TANDJ1) &middot; difficulty **1379** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Grid reachability by distance and parity |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

There is a grid of size $10^5 \times 10^5$, covered completely in railway tracks. Tom is riding in a train, currently in cell $(a, b)$, and Jerry is tied up in a different cell $(c, d)$, unable to move. The train has no brakes. It shall move exactly $K$ steps, and then its fuel will run out and it shall stop. In one step, the train must move to one of its neighboring cells, sharing a side. Tom can’t move without the train, as the grid is covered in tracks. Can Tom reach Jerry’s cell after exactly $K$ steps?

**Note:** Tom can go back to the same cell multiple times.

**Input**

- The first line contains an integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, five integers $a, b, c, d, K$.

**Output**

For each testcase, output in a single line "YES" if Tom can reach Jerry's cell in exactly $K$ moves and "NO" if not.

You may print each character of the string in uppercase or lowercase (for example, the strings "yEs", "yes", "Yes" and "YES" will all be treated as identical).

## Constraints

- $1 \leq T \leq 10^5$
- $0 \leq a, b, c, d \leq 10^5$
- $(a, b) \ne (c, d)$
- $1 \leq K \leq 2 \cdot 10^5$

**Subtasks**

**Subtask #1 (100 points):** original constraints

## Sample

**Sample input**

```
3
1 1 2 2 2
1 1 2 3 4
1 1 1 0 3
```

**Sample output**

```
YES
NO
YES
```

<details><summary>Explanation</summary>

**Test Case $1$:** A possible sequence of moves is $(1, 1) \to (1, 2) \to (2, 2)$.

**Test Case $2$:** There is a possible sequence in $3$ moves, but not in exactly $4$ moves.

**Test Case $3$:** A possible sequence of moves is $(1, 1) \to (1, 0) \to (0, 0) \to (1, 0)$.

</details>

## Approach

Each step changes one coordinate by one, so the shortest route from $(a,b)$ to $(c,d)$ is the **Manhattan distance**

$$D = |a - c| + |b - d|$$

Reaching the target in *exactly* $K$ steps needs two conditions:

1. $K \geq D$ — the train cannot arrive faster than the direct route.
2. $K - D$ is **even** — any surplus must be burned off in wasted moves, and every detour returns to the same square only after an even number of steps (one away, one back).

Both are necessary and together sufficient, since surplus steps can always be spent pacing between two adjacent cells.

The parity condition is the whole problem, and it comes from a colouring argument: tint the grid like a chessboard, and each step changes colour. So after $K$ steps the train sits on a cell whose colour is determined by $K$'s parity, and $D$ fixes the colour of the target relative to the start. If those disagree, no route of length $K$ exists however long you wander.

Sample case 2 is the parity failure: $D = 3$ and $K = 4$ differ by an odd amount, so `NO` even though $K > D$. Sample case 1 has $K = D = 2$ exactly, and case 3 has a surplus of $2$ to waste.

The grid is $10^5$ on a side and $K$ reaches $2 \times 10^5$, but the walls never bind — there is always room to pace — so the bounds need no special handling.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        a, b, c, d, k = map(int, data[1 + 5 * i:6 + 5 * i])
        dist = abs(a - c) + abs(b - d)
        # Surplus steps must be wasted in pairs, so the gap must be even.
        out.append("YES" if k >= dist and (k - dist) % 2 == 0 else "NO")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Surplus steps must be wasted in pairs.** Stepping away and back costs two moves, so $K - \mathrm{dist}$ has to be even — the second row has more than enough steps ($4$ against a distance of $3$) and still fails on parity.
- **Too few steps** → `NO` regardless of parity, which the `k >= dist` half of the test covers.
- **Exactly $K = \mathrm{dist}$** → `YES`, since a gap of $0$ is even (the first row).
- **Coordinates may be $0$** (the third row's target is $(1, 0)$), and the walk is unbounded, so no clamping to a grid is needed.
- **$(a,b) \neq (c,d)$ is guaranteed**, so the distance is at least $1$ and the degenerate "already there with $K = 0$" case never arises.
- **$T$ up to $10^5$** with constant work per case, read in one buffered call.

## Dry run

| from | to | Manhattan distance | $K$ | $K - \mathrm{dist}$ | even? | output |
|---|---|---:|---:|---:|:---:|---|
| $(1,1)$ | $(2,2)$ | 2 | 2 | 0 | yes | `YES` |
| $(1,1)$ | $(2,3)$ | 3 | 4 | 1 | **no** | `NO` |
| $(1,1)$ | $(1,0)$ | 1 | 3 | 2 | yes | `YES` |

Row 3 uses one step to arrive and wastes the other two on a step out and back.

---

Same problem in rating order (#223 of 486): [../../by-rating/223-TANDJ1.md](../../by-rating/223-TANDJ1.md)
