# 265. Magical Planks

> [`MKGPLNKS`](https://www.codechef.com/problems/MKGPLNKS) &middot; difficulty **1467** &middot; time limit **0.5s** &middot; 1400 to 1600 difficulty problems (Level 2)

> _Edge cases and dry run for this problem are still to be written._

## Topic used

| | |
|---|---|
| **Topic** | Strings |
| **Technique** | Counting runs |
| **CodeChef tags** | `Data Structures`, `Algorithms`, `Constructive`, `String`, `ad-hoc` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

Ryan is a boy from a small town,  who has been given a task by his father. He has $N$ wooden planks, numbered from $1$ to $N$, which are colored either black or white.

His task is to color all planks the same color! But there is some magic in the winds of his small town. Whenever he colors the $i^{th}$ ( plank which has the color $S_i$ ) to a color $P$ then following events happen:
 - if $2 \leq i \leq N$ and $S_i = S_{i - 1}$, then color of $(i - 1)^{th}$ plank changes to $P$.
 - if $1 \leq i \leq N - 1$ and $S_i = S_{i + 1}$, then color of $(i + 1)^{th}$ plank changes to $P$.

Now this process continues for the newly colored planks also. If none of the neighbors have same color, then nothing happens to the neighbors.

Suppose Ryan has planks which have their coloring : $B B W W W B$
If Ryan colors the fourth plank( whose color is $W$ ) to color $B$, then the finally the planks would be colored as following:

 $B B B B B B$

Ryan can choose any **one** of the $N$ planks and change its color as many times as he wants. Determine the minimum number of times Ryan has to paint a plank such that all planks get the same color at the end.

**Input**

- First line will contain $T$, number of testcases. Then the testcases follow.
- The first line of each test case consists of an integer $N$ the number of planks
- Second line of each test case consists of a string $S$ of size $N$,where the $i$ th character denotes the color of plank $i$

**Output**

For each testcase, output a single integer denoting the minimum number of times Ryan has to paint a **single** plank such that all planks get the same color at the end.

## Constraints

- $1 \leq T \leq 10^{5}$
- $1 \leq N \leq 10^5$
-  $S$ consists only of characters $B$ and $W$
- The sum of $N$ over all cases doesn't exceed $10^{5}$.

## Sample

**Sample input**

```
4
6
BBWWWB
5
WWBWB
2
BB
9
WWBBBBBWW
```

**Sample output**

```
1
2
0
1
```

<details><summary>Explanation</summary>

**Test case 1:**
The first test case is already described in the question.

**Test case 2:**
Ryan can paint the third plank to $W$. After doing so the color string of planks become $W W W W B$. Then he can again paint the third plank to the color $B$.
After doing so the string goes through following transitions:
 - The color of **third** plank changes to $B$. ( The string becomes $W W B W B$ )
 - The color of **second** and **fourth** plank changes to $B$. ( The string becomes $W B B B B$ )
 - The color of **first** plank changes to $B$. ( The string becomes $B B B B B$ )

Finally, all planks have same color.

**Test case 3:**
All planks have the same color.

**Test case 4:**
Ryan can paint any of the planks numbered from $3$ to $7$ to $W$, and all these planks will be colored to $W$!

</details>

## Approach

The spreading rule means painting a plank repaints its **entire maximal run** of equal colour — the change propagates to any neighbour sharing the old colour, and onward from there. So the plank's identity hardly matters; what matters is the run it currently sits in.

Collapse the string into runs. If there are $k$ runs, then painting a plank in a run that has neighbours on *both* sides flips that run to the other colour, merging it with both neighbours and turning three runs into one — **$k$ drops by $2$** per operation. Repeating from a well-chosen interior position drives $k$ down to $1$, and the answer is

$$\left\lfloor \frac{k}{2} \right\rfloor$$

Both parities land correctly: an odd $k$ reaches $1$ after $(k-1)/2$ merges, and an even $k$ reaches $2$ and then needs one final paint to merge the last pair — which is $k/2$ in total. The floor expresses both.

Ryan is restricted to **one** plank, repainted repeatedly, and that is fine: after each merge the chosen plank still sits inside the new combined run, which keeps absorbing its neighbours.

The samples walk the cases. `BBWWWB` has runs `BB | WWW | B`, so $k=3$ and one paint of the middle run turns everything black. `WWBWB` has $k=4$ and needs two. `BB` is already uniform at $k=1$. `WWBBBBBWW` has $k=3$ again, needing one.

Counting runs is a single pass comparing each character with its predecessor, which keeps this $O(N)$ at $\sum N = 10^5$.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        # data[pos] is N, which Python does not need.
        s = data[pos + 1]
        pos += 2
        # Painting a plank repaints its whole run, merging it with both
        # neighbours, so each operation removes two runs.
        runs = 1 + sum(1 for i in range(1, len(s)) if s[i] != s[i - 1])
        out.append(str(runs // 2))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

---

Same problem grouped by topic: [../docs/strings/MKGPLNKS.md](../docs/strings/MKGPLNKS.md)
