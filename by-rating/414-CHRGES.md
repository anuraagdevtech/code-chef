# 414. Spreading Charges

> [`CHRGES`](https://www.codechef.com/problems/CHRGES) &middot; difficulty **1708** &middot; time limit **4s** &middot; 1600 to 1800 difficulty problems (Level 3)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Runs of zeros classified by their bounding charges |
| **CodeChef tags** | `Algorithms`, `Simple Algos`, `Implementation` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef has a string $S$ of length $N$, consisting of `+, -,` and `0`, where `+` denotes a source of positive charge, `-` denotes a source of negative charge, and `0` denotes a neutral object.

Each second, the charge sources emit their respective charge to their immediate neighbours. The charge emissions cannot affect other charge sources but can convert a neutral object into a charge source as following:
- If an object was initially neutral, and had exactly one charged source as neighbour, it becomes a charged source as received by its neighbour.
- If an object was initially neutral, and had no charged source as neighbour, it remains a neutral object.
- If an object was initially neutral, and had both charged sources as neighbours, it becomes a charged source as received by its neighbours. Note that in case of neighbours with opposite charges, the object remains neutral.

For example, after one second, `+0+` becomes `+++`, `00-` becomes `0--`, `000` remains `000` and `+0-` remains `+0-`. Refer to samples for further explanation.

Find out the number of neutral objects in the string after infinite time.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- Each test case consists of multiple lines of input.
    - The first line of each test case contains an integer $N$ — the number of objects.
    - The next line contains a string $S$ of length $N$, consisting of `+, -,` and `0`, where `+` denotes a source of positive charge, `-` denotes a source of negative charge, and `0` denotes a neutral object.

**Output**

For each test case, output on a new line, the number of neutral objects in the string after infinite time.

## Constraints

- $1 \leq T \leq 2000$
- $1 \leq N \leq 10^5$
- $S$ consists of `+, -,` and `0` only.
- The sum of $N$ over all test cases won't exceed $2\cdot 10^5$.

## Sample

**Sample input**

```
4
2
00
3
-+0
6
00+-00
8
0-0+000-
```

**Sample output**

```
2
0
0
2
```

<details><summary>Explanation</summary>

**Test case $1$:** Since there is no charge source, both neutral objects will remain neutral.

**Test case $2$:** After $1$ second:
- The negative source emits a negative charge, but since there is no neutral neighbour for the negative source, it has no effect.
- The positive source emits a positive charge and since the neighbour to its right is neutral, the neutral object becomes a positive source.

Thus, the string becomes `-++` after one second. Note that the string will remain the same after this and thus, it has no neutral objects after infinite time.

**Test case $3$:**
- After $1$ second, the string is `0++--0`. Note that only the immediate neutral neighbours of charge sources have been affected.
- After $2$ seconds, the string is `+++---`. Since all objects are now charged sources, they will remain the same now onwards.

Thus, after infinite time, the string has no neutral objects.

**Test case $4$:** After $1$ second, the string is `--0++0--`. Note that the string will remain the same now onwards.

Thus, after infinite time, the string has $2$ neutral objects.

</details>

## Approach

Charges never move or change, so the only cells in play are the maximal runs of `0`. Each run fills in from whichever ends have a charge next to them, and the outcome depends only on those two bounding characters.

- **No bounding charge at all** (the whole string is zeros): nothing ever happens, so all $N$ cells stay neutral.
- **Bounded on one side only** (the run touches an end of the string): the charge marches in one cell per second and eventually fills the run — $0$ neutral.
- **Both bounds the same sign**: the run fills from both sides with the same charge — $0$ neutral.
- **Both bounds opposite**: the two fronts advance one cell per second and meet in the middle. A run of length $L$ ends with $\lfloor L/2 \rfloor$ cells of each sign, and when $L$ is **odd** the centre cell receives both charges on the same second, so it stays neutral forever.

$$\text{answer} = \sum_{\text{runs bounded by opposite signs}} (L \bmod 2)$$

The odd/even distinction is the whole problem. For `+0-` the single zero has both neighbours charged from the start and never resolves. For `+00-` the two cells are claimed one each. For `+000-` the fronts take cells $1$ and $3$, then stall on cell $2$, which is permanently caught between a `+` and a `-`.

The samples: `00` has no charges, so both cells stay neutral. `-+0` has its run bounded only on the left, so it fills. `00+-00` has two one-sided runs, both of which fill. And `0-0+000-` has a one-sided run plus two opposite-bounded runs of lengths $1$ and $3$, both odd, giving $2$.

## Solution

```python
import sys

ZERO = 0x30


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n = int(data[1 + 2 * i])
        s = data[2 + 2 * i]
        if s.count(ZERO) == n:
            out.append(str(n))          # nothing ever spreads
            continue
        neutral = 0
        run = 0
        left = None                     # charge bounding the run on the left
        for c in s:
            if c == ZERO:
                run += 1
                continue
            # Only a run squeezed between opposite charges can survive, and
            # then only its centre cell, when the run has odd length.
            if run and left is not None and left != c:
                neutral += run % 2
            run = 0
            left = c
        out.append(str(neutral))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/strings/CHRGES.md](../docs/strings/CHRGES.md)
