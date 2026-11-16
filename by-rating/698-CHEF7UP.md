[&larr; 697. Doubly Increasing Path](697-DINCPATH.md) &middot; [Index](README.md) &middot; [699. Mex Subsequence &rarr;](699-MEXSUB.md)

# 698. Chef Up

> [`CHEF7UP`](https://www.codechef.com/problems/CHEF7UP) &middot; difficulty **2494** &middot; time limit **1s** &middot; 2000 to 2500 difficulty problems (Level 5)

## Topic used

| | |
|---|---|
| **Topic** | Sorting |
| **Technique** | Parity of the distance to Chef decides which officers can be cornered |
| **CodeChef tags** | `Basic Programming Concepts`, `Mathematics`, `Algorithms`, `Constructive`, `Loops`, `Basic Math`, `ad-hoc`, `Sorting`, `Observation` |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log N)$ per test case |
| **Space** | $O(N)$ |

## Question

Chef is a wanted criminal, and $N$ police officers are up for catching him. The officers want to catch Chef no matter the cost, and Chef also wants to eliminate as many officers as possible (preferably everyone) before getting caught (or before running away after eliminating everyone). Neither the officers nor Chef will run away before accomplishing their goals.

Chef and the officers are on a one-dimensional grid with coordinates ranging from $-10^{10}$ to $10^{10}$. Chef is initially standing at coordinate $C$, and the $i$-th officer is initially at coordinate $P_i$. The officers and Chef then take turns to move, with the officer team moving first.

During their turn, officers will have to move to an adjacent unoccupied cell one by one, in any order they want. Every officer will have to move. At every moment of time, no two officers can be in the same cell, and also no officer can be in the same cell as Chef. If the officer is unable to move to an adjacent unoccupied cell, he is eliminated (and the cell he was in becomes unoccupied). **Note that the officer team will try to move to eliminate as few officers as possible.** For example, with $P = [2, 3, 4]$ and $C = 6$, then the next positions of the officers can be $[1, 2, 3]$, $[1, 2, 5]$, $[1, 4, 5]$, or $[3, 4, 5]$. However, with $P = [2, 3, 4]$ and $C = 5$, the only possible set of the next positions of the officers is $[1, 2, 3]$.

After the officer team's turn, Chef also moves to an adjacent unoccupied cell, or gets caught if he cannot find any adjacent unoccupied cell. The process then repeats until either Chef is caught, or all officers are eliminated and Chef runs away.

You need to find out the maximum number of officers that can be eliminated by Chef, and if Chef can run away or not.

As a reminder, two cells with coordinates $X$ and $Y$ are *adjacent* if and only if $|X - Y| = 1$.

**Input**

- The first line contains $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains a single integer $N$ - the number of officers.
- The second line of each test case contains a single integer $C$ - the initial coordinate of Chef.
- The third line of each test case contains $N$ integers $P_1, P_2, \dots, P_N$ - the initial coordinates of the officers.

**Output**

For each test case, output on a single line two space-separated integers: the first integer is the maximum number of officers that can be eliminated by Chef, and the second integer is $1$ if Chef runs away or $-1$ if Chef will be caught.

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $1 \leq C \leq 10^9$
- $1 \leq P_i \leq 10^9$
- All the coordinates are unique. That means $P_i \ne C$ for all $1 \le i \le N$, and $P_i \ne P_j$ for all $1 \le i \lt j \le N$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
2
2
2
1 4
1
2
1
```

**Sample output**

```
1 -1
1 1
```

<details><summary>Explanation</summary>

- **Test case $1$**: Chef chooses to always move to the left (i.e. to the smaller coordinate); this forces the officer at coordinate $1$ to always move to the left, and eventually being cornered and eliminated. However, the officer at coordinate $4$ cannot be eliminated, and hence Chef will be caught at the end.
- **Test case $2$**: Similarly, Chef chooses to always move to the left, and eventually eliminating the only officer, thus running away at the end.

</details>

## Approach

In every round each officer moves one cell and then Chef moves one cell, so the parity of the distance between Chef and any officer is the same at the start of every round.

An officer at an *even* distance can never be forced out: after the officers move, the gap to Chef is odd, so the cell next to Chef on that side is never needed by that officer, and it can always step towards Chef. Such an officer also shields everybody behind it, because the officers further out always have room to follow.

An officer at an *odd* distance with nothing protecting it is in trouble: Chef walks towards it and it must keep backing away, since an odd gap closes to distance 1 and the officer may not enter Chef's cell. The line is finite, so the whole group being pushed is eventually pressed against the boundary and loses officers one by one.

So look at each side of Chef separately, going outwards from Chef: every officer at odd distance met before the first even-distance officer can be eliminated, and from the first even-distance officer on nobody can. The answer is the sum of the two counts; Chef runs away exactly when that is all $N$ officers, otherwise he is eventually caught.

## Solution

```python
import sys
from bisect import bisect_left


def solve(tokens):
    n, chef = (next(tokens), next(tokens))
    officers = sorted((next(tokens) for _ in range(n)))
    split = bisect_left(officers, chef)
    eliminated = 0
    for i in range(split - 1, -1, -1):
        if (officers[i] - chef) % 2 == 0:
            break
        eliminated += 1
    for i in range(split, n):
        if (officers[i] - chef) % 2 == 0:
            break
        eliminated += 1
    return str(eliminated) + ' ' + ('1' if eliminated == n else '-1')


if __name__ == "__main__":
    tokens = iter(map(int, sys.stdin.buffer.read().split()))
    t = int(next(tokens))
    out = [solve(tokens) for _ in range(t)]
    sys.stdout.write('\n'.join(out))
```

## Edge cases

- Only the parity of $P_i - C$ and the order of the officers on each side matter.
- An even-distance officer adjacent in order to Chef protects its whole side.
- Chef can clear one side and then the other, so the two counts add up.
- The second number is 1 only when every officer is eliminated.

## Dry run

`C = 2`, officers at `1` and `4`.

- Left side: the officer at 1 is at distance 1 (odd) - it can be cornered. Count 1.
- Right side: the officer at 4 is at distance 2 (even) - safe.

One officer is eliminated and one survives, so Chef is caught: `1 -1`.

With `C = 2` and a single officer at 1, the count is 1 = $N$: `1 1`.

---

Same problem grouped by topic: [../docs/sorting/CHEF7UP.md](../docs/sorting/CHEF7UP.md)
