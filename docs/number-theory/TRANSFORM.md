# 41. Mario and Transformation

> CodeChef problem code [`TRANSFORM`](https://www.codechef.com/problems/TRANSFORM) &middot; difficulty **649** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Number Theory |
| **Technique** | Cyclic state via modulo |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Mario transforms each time he eats a mushroom as follows:
- If he is currently `small`, he turns `normal`.
- If he is currently `normal`, he turns `huge`.
- If he is currently `huge`, he turns `small`.

Given that Mario was initially `normal`, find his size after eating $X$ mushrooms.

**Input**

- The first line of input will contain one integer $T$, the number of test cases. Then the test cases follow.
- Each test case contains a single line of input, containing one integer $X$.

**Output**

For each test case, output in a single line Mario's size after eating $X$ mushrooms.

Print:
- $\texttt{NORMAL}$, if his final size is `normal`.
- $\texttt{HUGE}$, if his final size is `huge`.
- $\texttt{SMALL}$, if his final size is `small`.

You may print each character of the answer in either uppercase or lowercase (for example, the strings $\texttt{Huge}$, $\texttt{hUgE}$, $\texttt{huge}$ and $\texttt{HUGE}$ will all be treated as identical).

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 100$

## Sample

**Sample input**

```
3
2
4
12
```

**Sample output**

```
SMALL
HUGE
NORMAL
```

<details><summary>Explanation</summary>

**Test case $1$:** Mario's initial size is `normal`. On eating the first mushroom, he turns `huge`. On eating the second mushroom, he turns `small`.

**Test case $2$:** Mario's initial size is `normal`. On eating the first mushroom, he turns `huge`. On eating the second mushroom, he turns `small`. On eating the third mushroom, he turns `normal`. On eating the fourth mushroom, he turns `huge`.

</details>

## Approach

The three sizes form a closed cycle: `normal` → `huge` → `small` → `normal`. Because the cycle has length $3$, eating three mushrooms returns Mario to exactly where he started, so only $X \bmod 3$ matters.

Starting from `normal`, the mapping is

| $X \bmod 3$ | size |
|---|---|
| $0$ | `NORMAL` |
| $1$ | `HUGE` |
| $2$ | `SMALL` |

so the answer is a lookup into the list `["NORMAL", "HUGE", "SMALL"]` at index `x % 3`.

Simulating the $X$ steps in a loop would also pass at these bounds, but the modulo is both $O(1)$ and the idea that transfers: whenever a process returns to its initial state after a fixed number of steps, the step count collapses modulo the cycle length. With $X$ up to $10^9$ the loop would be hopeless and the modulo unchanged.

The ordering of the lookup table encodes the starting point. Mario begins `normal`, so index $0$ must be `NORMAL`; had he started `small` the same cycle would need its table rotated. Writing the table in cycle order starting from the initial state is what keeps this correct.

Check $X = 4$: $4 \bmod 3 = 1$, giving `HUGE` — one full cycle plus one step.

## Solution (Python)

```python
import sys

# The cycle normal -> huge -> small -> normal, written from the start state.
CYCLE = ("NORMAL", "HUGE", "SMALL")


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = [CYCLE[int(data[1 + i]) % 3] for i in range(t)]
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

> CodeChef tags: `Algorithms`
