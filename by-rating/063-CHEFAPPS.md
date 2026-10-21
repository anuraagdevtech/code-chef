# 063. Chef and his Apps

> [`CHEFAPPS`](https://www.codechef.com/problems/CHEFAPPS) &middot; difficulty **702** &middot; time limit **0.5s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Remove the largest item first |
| **Complexity class** | Constant time $O(1)$ |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef's phone has a total storage of $S$ MB. Also, Chef has $2$ apps already installed on his phone which occupy $X$ MB and $Y$ MB respectively.

He wants to install another app on his phone whose memory requirement is $Z$ MB. For this, he might have to delete the apps already installed on his phone. Determine the minimum number of apps he has to delete from his phone so that he has enough memory to install the third app.

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first and only line of each test case contains four integers $S, X, Y$ and $Z$ — the total memory of Chef's phone, the memory occupied by the two already installed apps and the memory required by the third app.

**Output**

For each test case, output the minimum number of apps Chef has to delete from his phone so that he can install the third app.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq S \leq 500$
- $1 \le X \le Y \le S$
- $X + Y \le S$
- $Z \le S$

## Sample

**Sample input**

```
4
10 1 2 3
9 4 5 1
15 5 10 15
100 20 30 75
```

**Sample output**

```
0
1
2
1
```

<details><summary>Explanation</summary>

**Test Case 1:** The unused memory in the phone is $7$ MB. Therefore Chef can install the $3$ MB app without deleting any app.

**Test Case 2:** There is no unused memory in the phone. Chef has to first delete one of the apps from the phone and then only he can install the $1$ MB app.

**Test Case 3:** There is no unused memory in the phone. Chef has to first delete both the apps from the phone and then only he can install the $15$ MB app.

**Test Case 4:** The unused memory in the phone is $50$ MB. Chef has to first delete the $30$ MB app from the phone and then only he can install the $75$ MB app.

</details>

## Approach

The free space on the phone is

$$F = S - X - Y$$

and Chef needs $Z$ megabytes. There are only three possible answers, so the solution is a short ladder — but the order in which the options are tried is the whole point.

- **Delete nothing** if $F \geq Z$.
- **Delete one app** if removing the larger of the two is enough: $F + \max(X, Y) \geq Z$.
- **Delete both** otherwise.

The greedy step is in the second line. If exactly one app is to be deleted, it should be the one that frees the most space — deleting the smaller app can only do worse, and never better. So testing $\max(X, Y)$ alone settles whether *any* single deletion suffices; there is no need to try both. The constraints happen to guarantee $X \leq Y$, making $Y$ the larger, but writing `max(x, y)` keeps the logic correct without leaning on that.

The third branch always succeeds because $Z \leq S$ is guaranteed: with both apps gone the phone is empty and has $S$ megabytes free. So the answer is never "impossible", and no fourth case is needed.

Sample case 3 is the one that forces both deletions — $Z = 15$ equals the entire $15$ MB phone, so nothing else may remain. Sample case 4 is the greedy case: deleting the $30$ MB app frees enough, while deleting the $20$ MB one would not.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        s, x, y, z = map(int, data[1 + 4 * i:5 + 4 * i])
        free = s - x - y
        if free >= z:
            out.append("0")
        elif free + max(x, y) >= z:   # if deleting one, delete the bigger
            out.append("1")
        else:
            out.append("2")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **Already enough free space** ($S = 10$, apps $1$ and $2$, need $3$): free space is $7$, so zero deletions.
- **Deleting one is enough, but it must be the larger app.** The sample's last row has $50$ free and needs $75$: removing the $30$ app gives $80$ and works, removing the $20$ app gives only $70$ and does not. A solution that deletes either app, or the smaller one, fails here.
- **Neither one alone suffices** ($S = 15$, apps $5$ and $10$, need $15$): both must go, so $2$. Since $Z \leq S$ is guaranteed, deleting both *always* works, which is why the answer never exceeds $2$.
- **An exact fit** (free space equal to $Z$): zero deletions, so the comparison is non-strict.

## Dry run

| $S$ | $X$ | $Y$ | $Z$ | free $S-X-Y$ | free $+\max(X,Y)$ | output |
|---:|---:|---:|---:|---:|---:|---|
| 10 | 1 | 2 | 3 | 7 | — | `0` |
| 9 | 4 | 5 | 1 | 0 | 5 | `1` |
| 15 | 5 | 10 | 15 | 0 | 10 | `2` |
| 100 | 20 | 30 | 75 | 50 | 80 | `1` |

Row 4 is the one that needs the *larger* app removed; row 3 needs both.

---

Same problem grouped by topic: [../docs/greedy/CHEFAPPS.md](../docs/greedy/CHEFAPPS.md)
