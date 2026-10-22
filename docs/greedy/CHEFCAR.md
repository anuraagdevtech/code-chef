# 415. Chef and Water Car

> CodeChef problem code [`CHEFCAR`](https://www.codechef.com/problems/CHEFCAR) &middot; difficulty **1683** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Pricing each litre by its earliest legal purchase |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 1600 to 1800 difficulty problems (Level 3) |

## Question

Chef is a great mechanic. As the cost of petrol is increasing day by day he decided to build a water car to take his girlfriend Natasha on a date. Water car has great build quality but is able to travel only $1$ Km on every $1$ liter of water. To show off his water car to Natasha he took her to the formula racing track which is an ($N-1$) km long road with checkpoints numbered $1$ to $N$ from left to right. The distance between two adjacent checkpoints is $1$ Km.

Initially, Chef is at checkpoint number $1$ and the tank of the water car is empty. At every checkpoint, there is a water station, but the cost of filling $1$ liter of water at a checkpoint is equal to the checkpoint number. Chef can not store more than $V$ liters of water in the tank of a car. Chef is interested in both minimum as well as the maximum cost of filling that can happen to reach the checkpoint number $N$.

You shouldn't have any water left after reaching $N^{th}$ checkpoint. Also, you are not allowed to pour out water.

**Input**

- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first and only line of each test case contains two space-separated integers $N, V$.

**Output**

For each test case, output two integers separated by space representing the maximum and minimum cost of filling respectively.

## Constraints

- $1 \le T \le 10^3$
- $1 \le N, V \le 10^9$

**Subtasks**

**Subtask 1 (20 points):** $V = 1$

**Subtask 2 (80 points):** Original constraints

## Sample

**Sample input**

```
3
3 1
4 2
4 3
```

**Sample output**

```
3 3
6 4
6 3
```

<details><summary>Explanation</summary>

**Test case $1$**: Given $N = 3$ and $V = 1$, Chef will start at checkpoint $1$, fill $1$ liter of water at a cost of $1$ and move $1$ Km right to reach checkpoint $2$. At checkpoint $2$, Chef will fill $1$ liter of water again at a cost of $2$  and move $1$ Km right to reach the destination i.e checkpoint $3$. Hence total cost incurred is $3$. There is no other way to reach the destination with a different expense.

</details>

## Approach

Think per **litre** rather than per stop. The journey is $N-1$ km, so exactly $N-1$ litres are bought, and the litre that powers the leg from checkpoint $i$ to $i+1$ costs whatever the checkpoint it was bought at is numbered.

**Maximum.** Buy each litre as late as possible: one litre at checkpoint $i$, burned immediately. The tank never holds more than $1 \leq V$ litres, so this is always legal:

$$\text{max} = 1 + 2 + \cdots + (N-1) = \frac{N(N-1)}{2}$$

Note $V$ does not appear — a bigger tank cannot make the trip *more* expensive.

**Minimum.** Buy each litre as early as possible. A litre bought at checkpoint $j$ and burned on leg $i$ sits in the tank across legs $j, \ldots, i$, which is $i - j + 1$ litres on board when leaving $j$, so capacity forces $i - j + 1 \leq V$. The earliest legal purchase is therefore $j = \max(1,\, i - V + 1)$ and

$$\text{min} = \sum_{i=1}^{N-1} \max(1,\, i - V + 1)$$

The first $\min(N-1, V)$ legs cost $1$ each and the rest cost $2, 3, \ldots$, giving the closed form $V + \frac{(N-V)(N-V+1)}{2} - 1$ when $N - 1 > V$, and simply $N-1$ otherwise.

Per-litre accounting is what makes this clean; reasoning stop by stop invites the wrong greedy. With $N = 4, V = 2$, "fill up whenever empty" buys $2$ litres at checkpoint $1$ and $1$ at checkpoint $3$ for $5$, but the optimum buys $2$ at checkpoint $1$ and $1$ at checkpoint $2$ for $4$ — topping up early beats waiting until empty.

The samples confirm both ends: $N = 4$ gives a maximum of $6$ for either tank size, while the minimum drops from $4$ at $V = 2$ to $3$ at $V = 3$, where one tank covers the whole road.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, v = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        legs = n - 1
        most = n * legs // 2                 # one litre bought at each checkpoint
        if legs <= v:
            least = legs                     # every litre can come from checkpoint 1
        else:
            # V legs at price 1, then prices 2, 3, ... up to N - V.
            least = v + (n - v) * (n - v + 1) // 2 - 1
        out.append(f"{most} {least}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Each litre is priced by where it is bought**, and the litre burned on leg $i$ must be bought at a checkpoint between $\max(1, i - V + 1)$ and $i$ — the tank only holds $V$ litres, so it cannot be bought too early.
- **The minimum therefore prices each litre at $\max(1, i - V + 1)$**, which gives $V$ litres at price $1$ and then prices $2, 3, \dots, N-V$ for the rest.
- **A large tank makes everything cost $1$.** When $N - 1 \leq V$ the whole trip can be fuelled at checkpoint $1$, so the minimum is just the number of legs (the third sample).
- **The maximum buys each litre as late as possible**, one at every checkpoint $1 \dots N-1$, costing $1 + 2 + \dots + (N-1) = N(N-1)/2$ — independent of $V$, since one litre always fits.
- **Per-litre accounting is what makes this clean**; reasoning stop by stop invites the wrong greedy, as "fill up only when empty" overpays.
- **No water may be left at the end and none poured out**, which is why exactly $N-1$ litres are bought in total.
- **$N, V$ up to $10^9$** put the maximum near $5 \times 10^{17}$ — past 32-bit, so the closed forms must stay in exact integers.

## Dry run

Second sample: $N = 4$ checkpoints (three legs), tank $V = 2$.

| leg | earliest checkpoint it can be bought at | cheapest price | dearest price |
|---:|---:|---:|---:|
| 1 | 1 | 1 | 1 |
| 2 | 1 | 1 | 2 |
| 3 | 2 | 2 | 3 |

Minimum $1 + 1 + 2 = 4$, maximum $1 + 2 + 3 = 6$. Output `6 4`.

> CodeChef tags: `Mathematics`, `Algorithms`

---

Same problem in rating order (#397 of 486): [../../by-rating/397-CHEFCAR.md](../../by-rating/397-CHEFCAR.md)
