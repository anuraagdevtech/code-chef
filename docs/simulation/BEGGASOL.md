# 178. Gasoline Introduction

> CodeChef problem code [`BEGGASOL`](https://www.codechef.com/problems/BEGGASOL) &middot; difficulty **1263** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Simulation |
| **Technique** | Collecting fuel while moving forward |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | Level up from 1* to 2* (Level 2) |

## Question

There are $N$ cars (numbered $1$ through $N$) on a circular track with length $N$. For each $i$ ($2 \le i \le N$), the $i$-th of them is at a distance $i-1$ clockwise from car $1$, i.e. car $1$ needs to travel a distance $i-1$ clockwise to reach car $i$. Also, for each valid $i$, the $i$-th car has $f_i$ litres of gasoline in it initially.

You are driving car $1$ in the clockwise direction. To move one unit of distance in this direction, you need to spend $1$ litre of gasoline. When you pass another car (even if you'd run out of gasoline exactly at that point), you steal all its gasoline. Once you do not have any gasoline left, you stop.

What is the total clockwise distance travelled by your car?

**Input**
- The first line of the input contains a single integer $T$ denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains a single integer $N$.
- The second line contains $N$ space-separated integers $f_1, f_2, \ldots, f_N$.

**Output**
For each test case, print a single line containing one integer ― the total clockwise distance travelled.

**Constraints**
- $1 \le T \le 100$
- $1 \le N \le 100$
- $0 \le f_i \le 100$ for each valid $i$

**Subtasks**
**Subtask #1 (100 points):** original constraints

## Constraints

- $1 \le T \le 100$
- $1 \le N \le 100$
- $0 \le f_i \le 100$ for each valid $i$

## Sample

**Sample input**

```
3
5
3 0 0 0 0
5
1 1 1 1 1
5
5 4 3 2 1
```

**Sample output**

```
3
5
15
```

<details><summary>Explanation</summary>

**Test case $1$:** The car starts with $3$ liters of gasoline. Using this, the car can travel $3$ units. On its journey, there is no other car having gasoline. Thus, the car stops after $3$ units.

**Test case $2$:** The car starts with $1$ liter of gasoline.
- After traveling $1$ unit, it passes another car with $1$ liter gasoline. Thus, the amount of gasoline left after traveling $1$ unit is $1$ liter.
- After traveling $2$ units, it passes another car with $1$ liter gasoline. Thus, the amount of gasoline left after traveling $2$ units is $1$ liter.
- After traveling $3$ units, it passes another car with $1$ liter gasoline. Thus, the amount of gasoline left after traveling $3$ units is $1$ liter.
- After traveling $4$ units, it passes another car with $1$ liter gasoline. Thus, the amount of gasoline left after traveling $4$ units is $1$ liter.
- After traveling $5$ units, there is no car with gasoline. Thus, the car stops after $5$ units.

**Test case $3$:** The car starts with $5$ liters of gasoline.
- After traveling $1$ unit, it passes another car with $4$ liters gasoline. Thus, the amount of gasoline left after traveling $1$ unit is $5-1+4 = 8$ liters.
- After traveling $2$ units, it passes another car with $3$ liters gasoline. Thus, the amount of gasoline left after traveling $2$ units is $8-1+3 = 10$ liters.
- After traveling $3$ units, it passes another car with $2$ liters gasoline. Thus, the amount of gasoline left after traveling $3$ units is $10-1+2 = 11$ liters.
- After traveling $4$ units, it passes another car with $1$ liter gasoline. Thus, the amount of gasoline left after traveling $4$ units is $11-1+1 = 11$ liters.
- After traveling $5$ units, there is no car with gasoline. Thus, after $5$ units, $10$ liters of gasoline is left.

The car can move $10$ more units using the leftover gasoline. The total distance travelled is $15$ units.

</details>

## Approach

You start at car $1$ with $f_1$ litres and drive clockwise, spending one litre per unit and absorbing each car's fuel as you pass it. The simulation is a single forward pass, but two details decide correctness.

**Stealing happens on arrival, even at zero fuel.** The statement is explicit: passing a car takes its fuel "even if you'd run out of gasoline exactly at that point". So the loop must spend the litre, arrive, *then* collect — not test for fuel after collecting. Sample case 2, with every car holding $1$ litre, depends on this: you arrive at each car with exactly zero and are refuelled each time.

**After the last car, the leftover is pure distance.** Once car $N$ has been passed there is nothing more to collect, so whatever fuel remains converts directly into distance. Stopping the simulation at car $N$ would under-count.

Putting those together: walk from car $1$ to car $N$, spending one litre and collecting $f_i$ at each step, halting early if the tank is empty; then add the remaining fuel to the distance.

Sample case 1, $[3,0,0,0,0]$, runs dry: three litres carry you to car $4$, which is empty, and you stop at distance $3$. Sample case 3, $[5,4,3,2,1]$, collects everything — total fuel $15$, and since the track is only length $5$ you lap it three times over empty cars, giving $15$.

That lapping is why the answer can exceed $N$ and why the track being circular barely matters: the cars are emptied on the first pass.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        f = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        fuel = f[0]
        dist = 0
        for i in range(1, n):
            if fuel == 0:
                break
            fuel -= 1
            dist += 1
            # Arriving with exactly zero still collects this car's fuel.
            fuel += f[i]
        # Past the last car there is nothing left to collect.
        dist += fuel
        out.append(str(dist))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(N)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Arriving with exactly zero fuel still collects that car's fuel.** The decrement happens before the pickup, so `1 1 1 1 1` works: the tank hits $0$ on arrival at every car and is immediately refilled to $1$.
- **The stop test comes before the move**, not after. With `3 0 0 0 0` the car travels three units and halts at car $4$ because there is no fuel left to reach car $5$.
- **Leftover fuel past the last car converts one-for-one into distance.** The third row arrives at car $5$ with $11$ units spare and adds every one of them, so the final `dist += fuel` is not an afterthought — it supplies most of the answer.
- **$f_i$ may be $0$, including $f_1$**, in which case the car never moves and the answer is $0$.
- **$N = 1$**: the loop body never runs and the answer is $f_1$ alone.

## Dry run

Third sample: fuel per car $5, 4, 3, 2, 1$.

| at car | fuel on arrival | distance | collects | fuel after |
|---:|---:|---:|---:|---:|
| 1 | — | 0 | 5 | 5 |
| 2 | 4 | 1 | 4 | 8 |
| 3 | 7 | 2 | 3 | 10 |
| 4 | 9 | 3 | 2 | 11 |
| 5 | 10 | 4 | 1 | 11 |

Past car $5$ the remaining $11$ units carry the car $11$ further: $4 + 11 = $ `15`.

> CodeChef tags: `Algorithms`

---

Same problem in rating order (#192 of 486): [../../by-rating/192-BEGGASOL.md](../../by-rating/192-BEGGASOL.md)
