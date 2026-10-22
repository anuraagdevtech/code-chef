[&larr; 063. Chef and his Apps](063-CHEFAPPS.md) &middot; [Index](README.md) &middot; [065. Minimum number of coins &rarr;](065-MINCOINS.md)

# 064. Chef Eren

> [`CHEFEREN`](https://www.codechef.com/problems/CHEFEREN) &middot; difficulty **706** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Counting odd and even positions |
| **CodeChef tags** | `Mathematics`, `Basic Math` |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef is a very big fan of Eren Yeager.

In the last season of Attack on Titan, there were $N$ episodes numbered from $1$ to $N$.
Each even indexed episode was $A$ minutes long and each odd indexed episode was $B$ minutes long.

Calculate the total duration (in minutes) of the last season.

**Input**

- The first line of input contains a single integer $T$, the number of test cases.
- The first and only line of each test case contains three integers $N$, $A,$ and $B$, the number of episodes and the durations of each even-indexed and odd-indexed episodes respectively in minutes.

**Output**

For each test case, print a single integer on a new line, the total duration of the last season in minutes.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq N \leq 60$
- $1 \leq A, B \leq 60$

## Sample

**Sample input**

```
3
1 2 2
2 3 4
4 20 30
```

**Sample output**

```
2
7
100
```

<details><summary>Explanation</summary>

**Test case $1$:** There is only one episode, so there is $1$ odd-indexed episode, and $0$ even-indexed episode. The total duration of the season $= 0\cdot A + 1\cdot B = 0\cdot 2 + 1\cdot 2 = 2$.

**Test case $2$:** There are two episodes with indices $\{1, 2\}$. Thus, there is $1$ odd-indexed episode $(\{1\})$, and $1$ even-indexed episode $(\{2\})$. The total duration of the season $= 1\cdot A + 1\cdot B = 1\cdot 3 + 1\cdot 4 = 7$.

**Test case $3$**: There are four episodes with indices $\{1, 2, 3, 4\}$. Thus, there are $2$ odd-indexed episodes $(\{1, 3\})$, and $2$ even-indexed episodes $(\{2, 4\})$. The total duration of the season $= 2\cdot A + 2\cdot B = 2\cdot 20 + 2\cdot 30 = 100$.

</details>

## Approach

Episodes are numbered $1$ to $N$. Odd-numbered ones run $B$ minutes and even-numbered ones run $A$, so the total is

$$B \cdot (\text{odd count}) + A \cdot (\text{even count})$$

Among $1 \ldots N$ there are $\lceil N/2 \rceil = \lfloor (N+1)/2 \rfloor$ odd numbers and $\lfloor N/2 \rfloor$ even ones. Note the asymmetry: the odds get the extra episode when $N$ is odd, because the sequence *starts* at $1$. Writing both counts as $N/2$ would silently lose an episode on every odd $N$.

Two further traps sit in the wording. The indexing is **one-based**, so episode $1$ is odd and takes $B$; a zero-based reading swaps the roles entirely. And the input order is $N, A, B$ with $A$ attached to *even* episodes, which is the reverse of the order the two durations are naturally read in. Binding $A$ to the odd count is the most likely bug here, and sample case 3 would not catch it — with $N = 4$ the counts are equal, so $20 \cdot 2 + 30 \cdot 2 = 100$ either way. Sample case 2 is the one that discriminates: $N = 2$ gives one odd and one even episode for $4 + 3 = 7$, and case 1 with $N = 1$ gives $B$ alone.

A loop over the episodes would also work at $N \leq 60$, but the closed form is $O(1)$ and makes the parity structure explicit.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, a, b = map(int, data[1 + 3 * i:4 + 3 * i])
        # Episodes are numbered from 1, so the odd positions take the extra one.
        odd, even = (n + 1) // 2, n // 2
        out.append(str(b * odd + a * even))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **$N = 1$**: only the first episode exists, and episodes are numbered from $1$, so it is an *odd* position and takes $B$. The sample's first row confirms this.
- **$N$ odd**: the odd positions get the extra episode, so $\lceil N/2 \rceil$ of them against $\lfloor N/2 \rfloor$ even ones.
- **$N$ even** ($N = 2$ and $N = 4$ in the sample): an exact split.
- **The parity convention is the trap.** Counting from $0$ instead of $1$ swaps which of $A$ and $B$ gets the extra episode, which changes every odd-$N$ answer.
- **Largest input** ($N = 60$): an even split of $30$ each.

## Dry run

| $N$ | $A$ | $B$ | odd slots $\lceil N/2 \rceil$ | even slots $\lfloor N/2 \rfloor$ | total $B\cdot\text{odd} + A\cdot\text{even}$ | output |
|---:|---:|---:|---:|---:|---:|---|
| 1 | 2 | 2 | 1 | 0 | $2$ | `2` |
| 2 | 3 | 4 | 1 | 1 | $4 + 3$ | `7` |
| 4 | 20 | 30 | 2 | 2 | $60 + 40$ | `100` |

Row 1 is the case that pins the numbering down.

---

Same problem grouped by topic: [../docs/basic-math/CHEFEREN.md](../docs/basic-math/CHEFEREN.md)
