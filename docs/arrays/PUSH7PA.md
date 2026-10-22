# 218. Pushpa 

> CodeChef problem code [`PUSH7PA`](https://www.codechef.com/problems/PUSH7PA) &middot; difficulty **1266** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Frequency combined with value |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

Pushpa has entered Chefland and wants to establish Pushpa-Raj here too.

Chefland has $N$ towers where the height of the $i^{th}$ tower is $H_i$. To establish Pushpa-Raj, Pushpa does the following:
- Initially, Pushpa chooses any tower $i$ $(1\le i \le N)$ and lands on the roof of that tower.
- Let $X$ denote the height of the tower Pushpa is currently on, then, Pushpa can land on the roof of any tower $j$ $(1\le j \le N)$ such that the height of the $j^{th}$ tower is $(X+1)$.

Let $i$ denote the index of the tower on which Pushpa lands, then, the height of all towers **except** tower $i$ **increases** by $1$ after each jump **including the initial jump**.

To establish Pushpa-Raj, Pushpa wants to land at the **maximum** height possible. Determine the maximum height Pushpa can reach.

**Input**

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ - the number of towers
- The second line of each test case contains $N$ space-separated integers $H_1, H_2, \dots, H_N$ denoting the initial heights of each of the towers from the ground.

**Output**

For each test case, output in a single line the **maximum** height achieved by Pushpa.

## Constraints

- $1 \leq T \leq 10$
- $1 \leq N \leq 10^5$
- $1 \leq H_i \leq 10^9$

## Sample

**Sample input**

```
2
4
1 2 1 3
1
2
```

**Sample output**

```
3
2
```

<details><summary>Explanation</summary>

- **Test case $1$**: If Pushpa chooses to start from tower at index $1$ with height of $1$ unit, then, the new heights will be $[ 1, 3, 2, 4 ]$. He can then jump to the $3^{rd}$ tower (with height $2$ units). The updated heights of the towers is $[2, 4, 2, 5]$. Pushpa is unable to make any more jumps.

The optimal way to in this case is to take an initial jump at tower $4$ with height $3$. The maximum height Pushpa can reach is $3$.

- **Test case $2$**: There is only $1$ tower so Pushpa reaches the maximum height of $2$ units.

</details>

## Approach

The rule that every tower **except the one landed on** rises by $1$ after each jump is what makes this collapse.

Suppose Pushpa lands first on a tower of height $h$. Every other tower is now $h' + 1$. To jump next he needs a tower currently at $h + 1$, so he needs $h' + 1 = h + 1$ — that is, $h' = h$. After that jump he stands at height $h+1$, every untouched tower has risen twice, and the same argument gives $h'' = h$ again.

So **every tower he ever visits had the same original height**. If a height $h$ occurs $c$ times, he lands on one of them and jumps $c - 1$ more times, gaining a metre each jump, finishing at

$$h + c - 1$$

The answer maximises that over all distinct heights:

$$\max_h \bigl(h + \mathrm{count}(h) - 1\bigr)$$

The trade-off between the two terms is the point, and sample case 1 shows both sides. With heights $[1,2,1,3]$, the value $1$ appears twice for $1 + 1 = 2$, while the lone $3$ gives $3 + 0 = 3$ — so the tallest single tower beats the repeated short one. On an input like $[1,1,1,1]$ the frequency would win instead.

Sample case 2 is a single tower: one landing, no jumps, final height $2$.

A `Counter` gives the frequencies in one pass; heights reach $10^9$, so hashing rather than an array indexed by height is essential.

## Solution (Python)

```python
import sys
from collections import Counter


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        counts = Counter(int(v) for v in data[pos + 1:pos + 1 + n])
        pos += 1 + n
        # Every tower on the route started at the same height, so a height
        # occurring c times carries Pushpa to h + c - 1.
        out.append(str(max(h + c - 1 for h, c in counts.items())))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(N)$

## Edge cases

- **Frequency can beat raw height.** With heights $2, 1, 1, 1$ the tallest tower reaches only $2$, while the three $1$s stack to $1 + 3 - 1 = 3$ — so taking $\max(H)$ is wrong even though the sample does not expose it.
- **A single tower** ($N = 1$, the second row): the count is $1$ and the answer is $H_1$ exactly, which is what the $-1$ in $h + c - 1$ ensures.
- **All heights distinct**: every count is $1$, so the answer degenerates to $\max(H)$.
- **$H_i$ up to $10^9$** while counts are at most $N = 10^5$, so the sum stays small and no overflow concern arises.
- Grouping by height is the whole trick: towers of *different* heights never combine, so the maximum is taken over groups rather than over the array.

## Dry run

First sample: heights $1, 2, 1, 3$.

| height | count $c$ | reach $h + c - 1$ |
|---:|---:|---:|
| 1 | 2 | 2 |
| 2 | 1 | 2 |
| 3 | 1 | **3** |

Output `3`. Note the two $1$s reach as high as the lone $2$.

---

Same problem in rating order (#194 of 486): [../../by-rating/194-PUSH7PA.md](../../by-rating/194-PUSH7PA.md)
