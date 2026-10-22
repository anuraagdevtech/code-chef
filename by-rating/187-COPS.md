[&larr; 186. Racing Horses](186-HORSES.md) &middot; [Index](README.md) &middot; [188. The Two Dishes &rarr;](188-MAX_DIFF.md)

# 187. Cops and the Thief Devu

> [`COPS`](https://www.codechef.com/problems/COPS) &middot; difficulty **1242** &middot; time limit **1s** &middot; Level up from 1* to 2* (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Simulation |
| **Technique** | Marking covered ranges over a small domain |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(100 + M)$ per test case |
| **Space** | $O(1)$ |

## Question

There are 100 houses located on a **straight line**. The first house is numbered 1 and the last one is numbered 100. Some **M** houses out of these 100 are occupied by cops.

Thief Devu has just stolen PeePee's bag and is looking for a house to hide in.

PeePee uses fast 4G Internet and sends the message to all the cops that a thief named Devu has just stolen her bag and ran into some house.

Devu knows that the cops run at a maximum speed of **x** houses per minute in a straight line and they will search for a maximum of **y** minutes. Devu wants to know how many houses are safe for him to escape from the cops. Help him in getting this information.

**Input**

First line contains **T**, the number of test cases to follow.

First line of each test case contains 3 space separated integers: **M**, **x** and **y**.

For each test case, the second line contains **M** space separated integers which represent the house numbers where the cops are residing.

**Output**

For each test case, output a single line containing the number of houses which are safe to hide from cops.

**Constraints**

- 1 ≤ **T** ≤ 10^4

- 1 ≤ **x, y, M** ≤ 10

## Constraints

- 1 ≤ T ≤ 10^4
- 1 ≤ x, y, M ≤ 10

## Sample

**Sample input**

```
3
4 7 8
12 52 56 8
2 10 2
21 75
2 5 8
10 51
```

**Sample output**

```
0
18
9
```

<details><summary>Explanation</summary>

**Test case $1$:** Based on the speed, each cop can cover $56$ houses on each side. These houses are:
- Cop in house $12$ can cover houses $1$ to $11$ if he travels left and houses $13$ to $68$ if he travels right. Thus, this cop can cover houses numbered $1$ to $68$.
- Cop in house $52$ can cover houses $1$ to $51$ if he travels left and houses $53$ to $100$ if he travels right. Thus, this cop can cover houses numbered $1$ to $100$.
- Cop in house $56$ can cover houses $1$ to $55$ if he travels left and houses $57$ to $100$ if he travels right. Thus, this cop can cover houses numbered $1$ to $100$.
- Cop in house $8$ can cover houses $1$ to $7$ if he travels left and houses $9$ to $64$ if he travels right. Thus, this cop can cover houses numbered $1$ to $64$.

Thus, there is no house which is not covered by any of the cops.

**Test case $2$:** Based on the speed, each cop can cover $20$ houses on each side. These houses are:
- Cop in house $21$ can cover houses $1$ to $20$ if he travels left and houses $22$ to $41$ if he travels right. Thus, this cop can cover houses numbered $1$ to $41$.
- Cop in house $75$ can cover houses $55$ to $74$ if he travels left and houses $76$ to $95$ if he travels right. Thus, this cop can cover houses numbered $55$ to $95$.

Thus, the safe houses are house number $42$ to $54$ and $96$ to $100$. There are $18$ safe houses.

</details>

## Approach

A cop at house $c$ runs at $x$ houses per minute for $y$ minutes, so they sweep everything within $x \cdot y$ houses in either direction — the closed interval

$$[\,c - xy,\; c + xy\,]$$

Devu is safe in any house of $1 \ldots 100$ covered by no cop. Since the domain is only $100$ houses, the simplest correct approach is to mark a boolean array: for each cop, flag the intersection of their interval with $[1, 100]$, then count the unflagged houses.

Clamping to $[1, 100]$ is what keeps the marking in bounds — a cop near either end reaches past the street, and those positions simply do not exist. Sample case 1 has cops whose combined reach of $56$ houses blankets the entire street, leaving $0$ safe houses.

The intervals **overlap**, which is why a union (or a marking array) is needed rather than summing interval lengths. Sample case 3 is built on that: cops at $10$ and $51$ with reach $40$ cover $[1,50]$ and $[11,91]$, which overlap heavily; their union is $[1,91]$, leaving $9$ safe houses. Adding the interval sizes would badly overcount the danger and under-report the safe houses.

Sample case 2 leaves two separate safe stretches — $42$–$54$ and $96$–$100$ — showing the answer need not be contiguous.

With $x, y, M \leq 10$ the reach is at most $100$, and the whole simulation is trivially fast even at $T = 10^4$.

## Solution

```python
import sys

HOUSES = 100


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        m, x, y = int(data[pos]), int(data[pos + 1]), int(data[pos + 2])
        cops = [int(v) for v in data[pos + 3:pos + 3 + m]]
        pos += 3 + m
        reach = x * y
        covered = [False] * (HOUSES + 1)
        for c in cops:
            # Clamp to the street; ranges from different cops may overlap.
            lo = max(1, c - reach)
            hi = min(HOUSES, c + reach)
            for h in range(lo, hi + 1):
                covered[h] = True
        out.append(str(sum(1 for h in range(1, HOUSES + 1) if not covered[h])))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **The input order is $M$, $X$, $Y$** — the count comes first, before the two speed values. Reading them as $X, Y, M$ transposes the reach and the cop count and passes none of the sample rows.
- **Ranges must be clamped to $[1, 100]$.** In the first row the reach is $7 \times 8 = 56$, so a cop at house $12$ covers from $-44$ — an unclamped index would wrap around to the end of the array in Python and mark the wrong houses.
- **Overlapping ranges must not be double-counted.** The third row has a cop covering $[1, 50]$ and another $[11, 91]$; summing range lengths gives $131$ "covered" houses out of $100$. Marking a boolean array makes the overlap free.
- **Total coverage** (the first row): the answer is $0$.
- **Gaps can be interior as well as at the ends.** The second row leaves $42$–$54$ in the middle *and* $96$–$100$ at the end, totalling $18$ — a solution that only measures the ends of the street misses half of it.
- The street is fixed at $100$ houses regardless of the inputs.

## Dry run

Second sample: $M = 2$, $X = 10$, $Y = 2$, so reach $= 20$; cops at $21$ and $75$.

| cop | raw range | clamped |
|---:|---|---|
| 21 | $[1, 41]$ | $[1, 41]$ |
| 75 | $[55, 95]$ | $[55, 95]$ |

| uncovered stretch | houses |
|---|---:|
| $42$–$54$ | 13 |
| $96$–$100$ | 5 |

Output `18`.

---

Same problem grouped by topic: [../docs/simulation/COPS.md](../docs/simulation/COPS.md)
