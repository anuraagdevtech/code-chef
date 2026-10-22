[&larr; 47. Finding Square Roots](FSQRT.md) &middot; [Index](../../README.md) &middot; [49. Blackjack &rarr;](BLACKJACK.md)

# 48. The Last Levels

> CodeChef problem code [`LASTLEVELS`](https://www.codechef.com/problems/LASTLEVELS) &middot; difficulty **679** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Counting separators, not groups |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

Chef is playing a videogame, and is getting close to the end. He decides to finish the rest of the game in a single session.

There are $X$ levels remaining in the game, and each level takes Chef $Y$ minutes to complete. To protect against eye strain, Chef also decides that every time he completes $3$ levels, he will take a $Z$ minute break from playing. Note that there is no need to take this break if the game has been completed.

How much time (in minutes) will it take Chef to complete the game?

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
- The first and only line of input will contain three space-separated integers $X$, $Y$, and $Z$.

**Output**

For each test case, output on a new line the answer — the length of Chef's gaming session.

## Constraints

- $1 \leq T \leq 100$
- $1 \leq X \leq 100$
- $5 \leq Y \leq 100$
- $5 \leq Z \leq 15$

## Sample

**Sample input**

```
4
2 12 10
3 12 10
7 20 8
24 45 15
```

**Sample output**

```
24
36
156
1185
```

<details><summary>Explanation</summary>

**Test case 1: 2 12 10**
- X = 2 (2 levels remain)
- Y = 12 (each level takes 12 minutes)
- Z = 10 (Chef would take a 10-minute break every 3 levels, but since there are only 2 levels, no break is needed)

Since there are only 2 levels, and no break is needed (because Chef takes a break only after every 3 levels).

The total time = X × Y = 2 × 12 = 24 minutes.

**Test case 3: 7 20 8**
- X = 7 (7 levels remain)
- Y = 20 (each level takes 20 minutes)
- Z = 8  (Chef takes an 8-minute break after every 3 levels)

Now, let's break this down: \
Chef completes the first 3 levels: 3 x 20 = 60 minutes.\
After completing these 3 levels, Chef takes an 8-minute break.\
Chef completes another 3 levels: 3 x 20 = 60 minutes. \
After completing these 3 levels, Chef takes another 8-minute break.\
Now, Chef completes the remaining 1 level: 1 x 20 = 20 minutes.

So, the total time = 60 + 8 + 60 + 8 + 20 = 156  minutes.

</details>

## Approach

Playing time is straightforward: $X$ levels at $Y$ minutes each gives $XY$. The interesting part is counting the breaks.

Chef rests after every third level, **except** that no break is taken once the game is finished. So the breaks fall *between* blocks of three levels rather than after each block — they are separators, not group markers. The number of complete three-level blocks that are followed by more play is

$$\left\lfloor \frac{X - 1}{3} \right\rfloor$$

and the total is

$$XY + Z \left\lfloor \frac{X - 1}{3} \right\rfloor$$

The $-1$ is the whole problem. The tempting $\lfloor X/3 \rfloor$ over-counts whenever $X$ is a multiple of three, because it charges a break after the final level with nothing left to play. Sample case 2 catches it exactly: $X = 3$ gives $\lfloor 3/3 \rfloor = 1$ break and an answer of $46$, where the expected answer is $36$ with no break at all.

Sample case 4 confirms the formula at scale: $24 \times 45 = 1080$ playing minutes plus $\lfloor 23/3 \rfloor = 7$ breaks at $15$ minutes, giving $1080 + 105 = 1185$.

The general shape — *$n$ items have $n - 1$ gaps between them* — recurs constantly, in joining strings with separators as much as in scheduling rests.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        x, y, z = map(int, data[1 + 3 * i:4 + 3 * i])
        # Breaks sit between blocks of 3, so none follows the final level.
        out.append(str(x * y + z * ((x - 1) // 3)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Three levels or fewer** ($X = 2$ and $X = 3$, both in the sample): breaks sit *between* blocks of three, so there is no break at all and the answer is just $XY$. $X = 3$ is the boundary.
- **$X = 4$**: $(4-1)//3 = 1$, the first break appears.
- **$X$ a multiple of $3$** ($X = 6$): $(6-1)//3 = 1$, not $2$ — no break follows the final level, which is the whole reason the formula uses $X - 1$ rather than $X$.
- **Largest sample** ($X = 24$): $23 // 3 = 7$ breaks, not $8$.
- Counting separators rather than groups is the trap: there are always one fewer gaps than blocks.

## Dry run

| $X$ | $Y$ | $Z$ | play $XY$ | breaks $(X-1)//3$ | rest $Z \cdot {\cdot}$ | output |
|---:|---:|---:|---:|---:|---:|---|
| 2 | 12 | 10 | 24 | 0 | 0 | `24` |
| 3 | 12 | 10 | 36 | 0 | 0 | `36` |
| 7 | 20 | 8 | 140 | 2 | 16 | `156` |
| 24 | 45 | 15 | 1080 | 7 | 105 | `1185` |

Row 2 sits on the boundary where no break has appeared yet.

> CodeChef tags: `Basic Programming Concepts`, `Mathematics`

---

Same problem in rating order (#53 of 486): [../../by-rating/053-LASTLEVELS.md](../../by-rating/053-LASTLEVELS.md)
