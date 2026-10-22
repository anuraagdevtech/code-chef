# 402. Flu Shot Lineup

> [`FLUSHOT`](https://www.codechef.com/problems/FLUSHOT) &middot; difficulty **1692** &middot; time limit **0.567226s** &middot; Jump from 2* to 3* (Level 3)

## Topic used

| | |
|---|---|
| **Topic** | Binary Search |
| **Technique** | Binary search on a real-valued answer |
| **Complexity class** | Linearithmic $O(n \log n)$ |
| **Time** | $O(N \log \frac{1}{\varepsilon})$ per test case |
| **Space** | $O(N)$ |

## Question

A new strain of flu has broken out. Fortunately, a vaccine was developed very quickly and is now being administered to the public. Your local health clinic is administering this vaccine, but the waiting line is very long.

For safety reasons, people are not allowed to stand very close to each other as the flu is not under control yet. However, many people were not aware of this precaution. A health and safety official recently examined the line and has determined that people need to spread out more in the line so that they are at least T units away from each other. This needs to be done as quickly as possible so we need to calculate the minimum distance D such that it is possible for every person to move at most D units so the distance between any two people is at least T. Specifically, D should be the minimum value such that there are locations x'_i so that |x_i - x'_i| ≤ D for each person i and |x'_i - x'_j| ≥ T for any two distinct people i,j. Furthermore, since nobody can move past the receptionist we must also have that x'_i ≥ 0.

The location of each person is given by the number of meters they are standing from the receptionist. When spreading out, people may move either forward or backward in line but nobody may move past the location of the receptionist.

**Input**

The first line of input contains a single integer K ≤ 30 indicating the number of test cases to follow. Each test case begins with a line containing an integer N (the number of people) and a floating point value T (the minimum distance that should be between people). The location of each person i is described by single floating point value x_i which means person i is x_i meters from the receptionist. These values appear in non-decreasing order on the following N lines, one value per line.

Bounds: 1 ≤ N ≤ 10,000 and T and every x_i is between 0 and 1,000,000 and is given with at most 3 decimals of precision.

**Output**

For each test case, you should output the minimum value of D with exactly 4 decimals of precision on a single line.

## Constraints

- $1 \leq K \leq 30$
- $1 \leq N \leq 10{,}000$
- $T$ and every $x_i$ lies between $0$ and $1{,}000{,}000$, given with at most 3 decimals of precision
- the $x_i$ appear in non-decreasing order

## Sample

**Sample input**

```
3
2 4
1
2
2 2
1
2
4 1
0
0.5
0.6
2.75
```

**Sample output**

```
2.0000
0.5000
1.4000
```

<details><summary>Explanation</summary>

**Test case $1$:** To maintain a distance of $4$ units, the first person can move to location $0$ and the second can move to location $4$. The maximum distance a person has to move is $2$.

**Test case $2$:** To maintain a distance of $2$ units, the first person can move to location $0.5$ and the second person can move to location $2.5$. The maximum distance a person has to move is $0.5$.

**Test case $3$:** To maintain a distance of $1$ unit, the first person does not move, the second moves to location $1$, the third moves to location $2$, and the fourth moves to location $3$. The corresponding distances moved by each of them is $0, 0,5, 1.4,$ and $0.25$ respectively. Thus, the maximum distance moved by any person is $1.4$ moved by the third person.

</details>

## Approach

Ask whether a given maximum movement $D$ suffices. Each person $i$ may end up anywhere in $[x_i - D,\ x_i + D]$, clipped below at $0$ since nobody may pass the receptionist, and consecutive people must sit at least $T$ apart.

That feasibility test is a **left-greedy sweep**: push each person as far left as the rules permit.

$$p_1 = \max(0,\ x_1 - D), \qquad p_i = \max(p_{i-1} + T,\ x_i - D)$$

and the arrangement fails the moment some $p_i$ exceeds $x_i + D$. Placing each person as early as possible is optimal because it leaves the most room for everyone after them — any feasible arrangement can be slid left to this one.

Since the people arrive in non-decreasing order, keeping them in that order is also optimal: swapping two would only widen the distance one of them must travel.

Feasibility is monotone in $D$ — more slack never hurts — so a **binary search on the real line** finds the threshold. About $100$ halvings take the interval well below the $10^{-4}$ the output needs.

Sample case 3 is the instructive one. Three people crowd near the receptionist at $0$, $0.5$ and $0.6$ while a fourth sits far off at $2.75$. The cramped trio must spread to $0$, $1$ and $2$, and it is the person at $0.6$ who moves furthest — $1.4$ — not the isolated one, who barely shifts.

The answer is printed to four decimal places, matching the published format.

## Solution

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    k = int(data[0])
    pos = 1
    out = []
    for _ in range(k):
        n, t = int(data[pos]), float(data[pos + 1])
        xs = [float(v) for v in data[pos + 2:pos + 2 + n]]
        pos += 2 + n

        def feasible(d):
            # Push everyone as far left as allowed: that leaves the most room.
            place = max(0.0, xs[0] - d)
            if place > xs[0] + d:
                return False
            for x in xs[1:]:
                place = max(place + t, x - d)
                if place > x + d:
                    return False
            return True

        lo, hi = 0.0, t * n + xs[-1] + 1.0
        for _ in range(100):
            mid = (lo + hi) / 2
            if feasible(mid):
                hi = mid
            else:
                lo = mid
        out.append(f"{hi:.4f}")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The objective is the largest single move**, so binary searching that value turns the problem into a feasibility question: can everyone reach a legal spot within distance $d$?
- **Pushing everyone as far left as allowed is optimal**, because the leftmost legal position for person $i$ leaves the most room for everyone after them — a greedy that never needs revisiting.
- **The order is preserved.** People stay in line, so person $i$'s new spot must be at least $T$ past person $i-1$'s, which is what `max(place + T, x - d)` enforces.
- **Nobody may step behind position $0$**, hence the clamp on the first placement.
- **Infeasibility shows up as overshooting the right bound**: if the forced spot exceeds $x + d$, this $d$ is too small.
- **The inputs carry up to three decimals**, so the answer is real-valued and $100$ bisection rounds take the interval far below the required precision.
- **The upper bound must be generous** — $T \cdot N + x_N$ covers the worst spread — and the answer is printed to four decimals.

## Dry run

Third sample: $N = 4$, $T = 1$, positions $0, 0.5, 0.6, 2.75$. Testing $d = 1.4$:

| person | original | earliest legal spot | within $x + d$? |
|---:|---:|---:|:---:|
| 1 | 0 | $\max(0, 0 - 1.4) = 0$ | $0 \leq 1.4$ ✓ |
| 2 | 0.5 | $\max(0 + 1, -0.9) = 1$ | $1 \leq 1.9$ ✓ |
| 3 | 0.6 | $\max(1 + 1, -0.8) = 2$ | $2 \leq 2.0$ ✓ |
| 4 | 2.75 | $\max(2 + 1, 1.35) = 3$ | $3 \leq 4.15$ ✓ |

Feasible, and person $3$ sits exactly on its bound — so $1.4$ is the answer. Output `1.4000`.

---

Same problem grouped by topic: [../docs/binary-search/FLUSHOT.md](../docs/binary-search/FLUSHOT.md)
