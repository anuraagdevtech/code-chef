[&larr; 104. Smallest Numbers of Notes](FLOW005.md) &middot; [Index](../../README.md) &middot; [131. Avoid Contact &rarr;](AVOIDCONTACT.md)

# 127. Peaceful Party

> CodeChef problem code [`MAYOR_PARTY`](https://www.codechef.com/problems/MAYOR_PARTY) &middot; difficulty **898** &middot; time limit **0.5s**

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Choosing between mutually exclusive groups |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

The mayor of your city has decided to throw a party to gather the favour of his people in different regions of the city.

There are $3$ distinct regions in the city namely $A$, $B$, $C$ comprising of $P_A$, $P_B$ and $P_C$ number of people respectively.

However, the mayor knows that people of the region $B$ are in conflict with people of regions $A$ and $C$. So, there will be a conflict if people from region $B$ are present at the party along with people from region $A$ or $C$.

The mayor wants to invite as many people as possible and also avoid any conflicts. Help him invite **maximum** number of people to the party.

**Input**

- The first line contains a single integer $T$ - the number of test cases. Then the test cases follow.
- The first line of each test case contains three integers $P_A$, $P_B$ and $P_C$ - number of people living in regions $A$, $B$ and $C$ respectively.

**Output**

For each test case, output the **maximum** number of people that can be invited to the party.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq P_A, P_B, P_C \leq 1000$

**Subtasks**

- 30 points : $1 \leq R \leq 10000$
- 70 points : $1 \leq R \leq 10^9$

## Sample

**Sample input**

```
3
2 3 4
1 5 2
8 8 8
```

**Sample output**

```
6
5
16
```

<details><summary>Explanation</summary>

**Test case-1:** Mayor can invite all the people from region $A$ and $C$. So the maximum number of people invited is $6$.

**Test case-2:** Mayor can invite all the people from region $B$. So the maximum number of people invited is $5$.

</details>

## Approach

Region $B$ conflicts with both $A$ and $C$, while $A$ and $C$ have no quarrel with each other. So any peaceful guest list is one of two shapes:

- invite $B$ alone, seating $P_B$ people;
- invite $A$ and $C$ together, seating $P_A + P_C$.

Those are the only maximal options, so the answer is

$$\max(P_B,\; P_A + P_C)$$

The key observation is that $A$ and $C$ are **not** in conflict, so there is never a reason to invite just one of them — taking both is free. That collapses what looks like a subset-selection problem over three groups into a choice between two candidates. Inviting nobody, or only $A$, are both dominated.

Sample case 2 is the case where $B$ wins: $P_B = 5$ beats $P_A + P_C = 3$. The other two samples favour the $A+C$ coalition. A solution that always picked $A + C$, or always picked the single largest region, would fail one of these.

This is the smallest instance of the **maximum weight independent set** problem on a graph — here a path $A - B - C$, where the two independent sets worth considering are $\{B\}$ and $\{A, C\}$. On larger graphs that problem is genuinely hard, but on a three-vertex path the enumeration is immediate.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        pa, pb, pc = map(int, data[1 + 3 * i:4 + 3 * i])
        # A and C do not conflict, so the only choice is B alone vs A plus C.
        out.append(str(max(pb, pa + pc)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **B alone beats A and C together** ($1, 5, 2$): the answer is $5$, so a solution that always takes $A + C$ fails this row.
- **A and C together win** ($2, 3, 4 \to 6$).
- **All three equal** ($8, 8, 8$): $A + C = 16$ wins, because two groups beat one.
- **A and C do not conflict with each other**, so the only decision is $B$ against $A \cup C$ — there is no third combination to consider, which is why a two-way maximum is exhaustive rather than greedy.

## Dry run

| $P_A$ | $P_B$ | $P_C$ | $B$ alone | $A + C$ | output |
|---:|---:|---:|---:|---:|---|
| 2 | 3 | 4 | 3 | 6 | `6` |
| 1 | 5 | 2 | 5 | 3 | `5` |
| 8 | 8 | 8 | 8 | 16 | `16` |

Row 2 is the one where excluding $B$ would be a mistake.

> CodeChef tags: `Mathematics`

---

Same problem in rating order (#128 of 486): [../../by-rating/128-MAYOR_PARTY.md](../../by-rating/128-MAYOR_PARTY.md)
