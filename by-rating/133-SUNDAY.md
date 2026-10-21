# 133. Count the Holidays

> [`SUNDAY`](https://www.codechef.com/problems/SUNDAY) &middot; difficulty **907** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Sets |
| **Technique** | Union of a fixed set with input values |
| **CodeChef tags** | `Basic Programming Concepts`, `Mathematics`, `Basic Math`, `Loops`, `Arithmetic` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(N)$ |

## Question

A particular month has $30$ days, numbered from $1$ to $30$.

Day $1$ is a Monday, and the usual $7$-day week is followed (so day $2$ is Tuesday, day $3$ is Wednesday, and so on).

Every Saturday and Sunday is a holiday. There are $N$ festival days, which are also holidays. Note that it is possible for a festival day to occur on a Saturday or Sunday.

You are given the dates of the festivals. Determine the total number of holidays in this month.

**Input**

- The first line of input contains a single integer $T$, denoting the number of test cases. The description of $T$ test cases follows.
- The first line of each test case contains an integer $N$ denoting the number of festival days.
- The second line of each test case contains $N$ **distinct** space-separated integers $A_1, A_2, \ldots A_N$, denoting the festival days. Note that the $A_i$ are **not necessarily given in sorted order.**

**Output**

For each test case, output a new line containing the total number of holidays.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N \leq 30$
- $1 \leq A_i \leq 30$
- All the $A_i$ are distinct

## Sample

**Sample input**

```
3
2
5 7
3
23 1 6
1
13
```

**Sample output**

```
9
10
8
```

<details><summary>Explanation</summary>

**Test Case $1$:** Days $6, 13, 20$ and $27$ are Saturdays, and days $7, 14, 21, 28$ are Sundays. The festivals fall on day $5$ and day $7$, but day $7$ is already a Sunday. This gives us $9$ holidays in total — days $5, 6, 7, 13, 14, 20, 21, 27, 28$.

**Test Case $2$:** Days $6, 13, 20$ and $27$ are Saturdays, and days $7, 14, 21, 28$ are Sundays. The festivals fall on day $1$, day $6$, and day $23$. This gives us $10$ holidays in total — days $1, 6, 7, 13, 14, 20, 21, 23, 27, 28$.

**Test Case $3$:** Days $6, 13, 20$ and $27$ are Saturdays, and days $7, 14, 21, 28$ are Sundays. The only festival is on day $13$, which is already a holiday. This gives us $8$ holidays in total — days $6, 7, 13, 14, 20, 21, 27, 28$.

</details>

## Approach

Day $1$ is a Monday, so within a $30$-day month the Saturdays fall on days $6, 13, 20, 27$ and the Sundays on $7, 14, 21, 28$ — eight weekend days, fixed and independent of the input.

The festivals add more holidays, but the statement warns that a festival **may land on a weekend**, in which case it is already a holiday and must not be counted twice. That makes this a set union rather than a sum:

$$|\,\text{weekends} \cup \text{festivals}\,|$$

Computing it as `len(WEEKEND | set(festivals))` handles the overlap automatically. Adding $8 + N$ would overcount, and sample case 1 catches it immediately: festivals $\{5, 7\}$ include day $7$, a Sunday, so the answer is $9$ rather than $10$. Sample case 3 is the extreme — its single festival on day $13$ is a Saturday, contributing nothing, leaving the bare $8$.

Precomputing the weekend set once, outside the loop, keeps each test case to a single set construction and union.

The $A_i$ are promised distinct, so no duplicates need removing among the festivals themselves — but building a set is the natural way to union them anyway. The note that they arrive unsorted is irrelevant to a set-based solution, though it would matter to one attempting a sorted merge.

## Solution

```python
import sys

# Day 1 is a Monday, so in a 30-day month these are the Saturdays and Sundays.
WEEKEND = {6, 7, 13, 14, 20, 21, 27, 28}


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    pos = 1
    out = []
    for _ in range(t):
        n = int(data[pos])
        fests = {int(v) for v in data[pos + 1:pos + 1 + n]}
        pos += 1 + n
        # A festival may fall on a weekend, so union rather than add.
        out.append(str(len(WEEKEND | fests)))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **A festival falling on a weekend adds nothing.** The third row's single festival is day $13$, already a Saturday, so the answer stays at the eight weekend days. Adding $N$ to $8$ would give $9$.
- **Partial overlap** (the first row has $7$ on a weekend and $5$ not): only the new day counts.
- **The $A_i$ are guaranteed distinct**, so there are no duplicate festivals to collapse — but the union is still needed for weekend collisions.
- **Day $1$ is a Monday**, which fixes the weekend set as $\{6,7,13,14,20,21,27,28\}$ in a $30$-day month. A different starting weekday changes every answer, so that convention is the one assumption to get right.

## Dry run

Weekend days: $6, 7, 13, 14, 20, 21, 27, 28$ — eight of them.

| festivals | already a weekend | new days | total |
|---|---|---:|---:|
| $5, 7$ | $7$ | $5$ | `9` |
| $23, 1, 6$ | $6$ | $23, 1$ | `10` |
| $13$ | $13$ | none | `8` |

---

Same problem grouped by topic: [../docs/sets/SUNDAY.md](../docs/sets/SUNDAY.md)
