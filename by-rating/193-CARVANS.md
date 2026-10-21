# 193. Carvans

> [`CARVANS`](https://www.codechef.com/problems/CARVANS) &middot; difficulty **1264** &middot; time limit **3s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Running minimum over a prefix |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

Most problems on CodeChef highlight chef's love for food and cooking but little is known about his love for racing sports. He is an avid Formula 1 fan. He went to watch this year's Indian Grand Prix at New Delhi. He noticed that one segment of the circuit was a long straight road. It was impossible for a car to overtake other cars on this segment. Therefore, a car had to lower down its speed if there was a slower car in front of it. While watching the race, Chef started to wonder how many cars were moving at their maximum speed.

Formally, you're given the maximum speed of N cars in the order they entered the long straight segment of the circuit. Each car prefers to move at its maximum speed. If that's not possible because of the front car being slow, it might have to lower its speed. It still moves at the fastest possible speed while avoiding any collisions. For the purpose of this problem, you can assume that the straight segment is infinitely long.

Count the number of cars which were moving at their maximum speed on the straight segment.

**Input**

The first line of the input contains a single integer T denoting the number of test cases to follow. Description of each test case contains 2 lines. The first of these lines contain a single integer N, the number of cars. The second line contains N space separated integers, denoting the maximum speed of the cars in the order they entered the long straight segment.

**Output**

For each test case, output a single line containing the number of cars which were moving at their maximum speed on the segment.

**Constraints**

1 ≤ T ≤ 100

1 ≤ N ≤ 10,000

All speeds are distinct positive integers that fit in a 32 bit signed integer.

Each input file will not be larger than 4 MB (4,000,000,000 bytes) in size.

**WARNING!** The input files are very large. Use faster I/O.

## Constraints

1 ≤ T ≤ 100
1 ≤ N ≤ 10,000
All speeds are distinct positive integers that fit in a 32 bit signed integer.
Each input file will not be larger than 4 MB (4,000,000,000 bytes) in size.
WARNING! The input files are very large. Use faster I/O.

## Sample

**Sample input**

```
3
1
10
3
8 3 6
5
4 5 1 2 3
```

**Sample output**

```
1
2
2
```

<details><summary>Explanation</summary>

**Test case $1$:** There is only $1$ car. Thus, it can move at its maximum speed.

**Test case $2$:** The first car moves at speed $8$. The second car can move at speed $3$ without colliding with the first car. For the third car, if it moves at speed $6$, it would collide with the second car after some finite amount of time. The maximum speed at which the third car can move avoiding any collision is $3$. Thus, $2$ cars can move at their maximum speed.

**Test case $3$:** Following are the maximum speeds of all the cars.
- The first car moves at a maximum speed of $4$.
- The maximum speed at which the second car can move without colliding is $4$.
- The third car can move at its maximum speed which is $1$.
- The maximum speed at which the fourth car can move without colliding is $1$.
- The maximum speed at which the fifth car can move without colliding is $1$.

Thus, two cars can move at their maximum speed. These cars are car $1$ and $3$.

</details>

## Approach

Overtaking is impossible, so a car's actual speed is capped by every car ahead of it. Car $i$ therefore travels at

$$\min(A_1, A_2, \ldots, A_i)$$

and it moves at its **own** maximum speed exactly when $A_i$ is no greater than everything before it — that is, when $A_i \leq \min(A_1, \ldots, A_{i-1})$.

So the solution is one pass maintaining a running minimum, counting how often the current car is at or below it. The first car is always free, and the running minimum updates to $A_i$ whenever that happens.

The key realisation is that only the **prefix minimum** matters, not the immediately preceding car. A slow car far ahead throttles everything behind it, even cars whose immediate predecessor is fast. Sample case 3, $[4,5,1,2,3]$, shows this: cars $4$ and $5$ have faster cars directly in front of them, yet both are stuck behind the $1$, so the answer is $2$, not $4$.

Sample case 2, $[8,3,6]$, gives $2$: the $8$ runs free, the $3$ is slower than everything ahead so it also runs free, and the $6$ is throttled to $3$.

Since all speeds are distinct, the comparison could be strict without changing the result — but `<=` is the safer habit.

The statement warns that input files reach 4 MB, so bulk reading via `sys.stdin.buffer.read()` rather than per-line `input()` is genuinely necessary here, not just tidy.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        speeds = data[pos + 1:pos + 1 + n]
        pos += 1 + n
        free = 0
        running_min = float("inf")
        for v in speeds:
            s = int(v)
            # Capped by every car ahead, not merely the one in front.
            if s <= running_min:
                free += 1
                running_min = s
        out.append(str(free))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The cap comes from every car ahead, not just the one immediately in front.** Take $3, 5, 4$: car $2$ is held to speed $3$, so car $3$ at max speed $4$ is held too, and the answer is $1$. Comparing each car only with its predecessor's *maximum* speed accepts car $3$ (since $4 < 5$) and answers $2$. The running minimum is what encodes the speed a car actually travels at.
- **The first car is always free**, which the initial infinite minimum handles without a special case.
- **All speeds are distinct**, so `<=` and `<` behave identically here; the non-strict form is the one that stays correct if duplicates ever appear.
- **A monotonically decreasing input** means every car runs free, giving $N$.
- **Input files up to 4 MB** with an explicit warning in the statement: a single buffered read and token split is required, and per-line reading will time out.

## Dry run

Third sample: maximum speeds $4, 5, 1, 2, 3$.

| car | max speed | running min before | $\leq$ min? | actual speed | free so far |
|---:|---:|---:|:---:|---:|---:|
| 1 | 4 | $\infty$ | yes | 4 | 1 |
| 2 | 5 | 4 | no | 4 | 1 |
| 3 | 1 | 4 | yes | 1 | 2 |
| 4 | 2 | 1 | no | 1 | 2 |
| 5 | 3 | 1 | no | 1 | 2 |

Output `2`.

---

Same problem grouped by topic: [../docs/arrays/CARVANS.md](../docs/arrays/CARVANS.md)
