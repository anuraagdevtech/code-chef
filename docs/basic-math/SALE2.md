# 94. Buy 2 Get 1 Free

> CodeChef problem code [`SALE2`](https://www.codechef.com/problems/SALE2) &middot; difficulty **821** &middot; time limit **1s**

| | |
|---|---|
| **Topic** | Basic Math |
| **Technique** | Counting free items in a repeating group |
| **Time** | $O(1)$ per test case |
| **Space** | $O(1)$ |
| **Roadmap course** | 500 to 1000 difficulty rating (Level 1) |

## Question

There is a sale going on in Chefland. For every $2$ items Chef pays for, he gets the **third** item for **free** (see sample explanations for more clarity).

It is given that the cost of $1$ item is $X$ rupees. Find the **minimum** money required by Chef to buy at least $N$ items.

**Input**

- First line will contain $T$, number of test cases. Then the test cases follow.
- Each test case contains of a single line of input, two integers $N$ and $X$.

**Output**

For each test case, output the minimum money required by Chef to buy at least $N$ items.

## Constraints

- $1 \leq T \leq 1000$
- $1 \leq N,X \leq 1000$

**Subtasks**

- **Subtask 1 (100 points):** Original constraints.

## Sample

**Sample input**

```
4
3 4
4 2
5 3
6 1
```

**Sample output**

```
8
6
12
4
```

<details><summary>Explanation</summary>

**Test Case $1$:** Chef wants $3$ items where the cost of each item is $4$ rupees. To minimise the expenditure, Chef can pay for $2$ items and get the third item for free. This way, the total money required is $4 \cdot 2 = 8$ rupees.

**Test Case $2$:** To minimise the expenditure, Chef can do the following:
- Purchase $2$ items for $2 \cdot 2 = 4$ rupees and get the third one free. Thus, the total number of items is $3$.
- Purchase $1$ item for $2 \cdot 1 = 2$ rupees. Now Chef has total $4$ items.

Thus, the minimum money required to buy $4$ items is $4 + 2 = 6$ rupees.

**Test Case $3$:** To minimise the expenditure, Chef can do the following:
- Purchase $2$ items for $3 \cdot 2 = 6$ rupees and get the third one free. Thus, the total number of items is $3$.
- Purchase $2$ items for $3 \cdot 2 = 6$ rupees. Chef gets a third item for free. Now Chef has total $6$ items which is greater than his requirement of $5$ items.

Chef wanted to buy at least $5$ items. The minimum money required for that is $6 + 6 = 12$ rupees.

**Test Case $4$:** To minimise the expenditure, Chef can do the following:
- Purchase $2$ items for $1 \cdot 2 = 2$ rupees and get the third one free. Thus, the total number of items is $3$.
- Purchase $2$ items for $1 \cdot 2 = 2$ rupees and get the third one free.. Now Chef has total $6$ items.

Thus, the minimum money required to buy $6$ items is $2 + 2 = 4$ rupees.

</details>

## Approach

Items come in blocks of three: pay for two, get the third free. Out of $N$ items, the number that are free is the number of complete blocks, $\lfloor N/3 \rfloor$, so the bill is

$$\left(N - \left\lfloor \frac{N}{3} \right\rfloor\right) \cdot X$$

This is the same structure as the Presents problem, with a block of three instead of five.

The phrase "at least $N$ items" invites a worry: could buying *more* than $N$ ever be cheaper? It cannot be cheaper, though it can tie. With $N = 5$ the formula charges for $4$ items; buying $6$ also charges for $4$ and yields an extra item for free. Since the question asks only for the money spent, both give $4X$ and the formula is already optimal. Rounding $N$ up to the next multiple of three before applying the discount would be wrong in the other direction — for $N = 4$ it would charge for $4$ rather than $3$.

The samples check both residues. $N = 3$ gives one free item, paying for $2$; $N = 4$ still gives one free, paying for $3$; $N = 6$ gives two free, paying for $4$. The free count advances only on complete blocks, which is exactly what the floor expresses.

Multiplying by $X$ at the end keeps everything in integers — the per-item price never participates in the rounding.

## Solution (Python)

```python
import sys


def main() -> None:
    data = sys.stdin.buffer.read().split()
    t = int(data[0])
    out = []
    for i in range(t):
        n, x = int(data[1 + 2 * i]), int(data[2 + 2 * i])
        # One item is free per complete block of three.
        out.append(str((n - n // 3) * x))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Complexity

- **Time:** $O(1)$ per test case
- **Space:** $O(1)$

## Edge cases

- **Exactly one block** ($N = 3$): one item free, two paid.
- **$N = 4$ and $N = 5$**: still only one free, since a partial block earns nothing — both sample rows confirm the step does not move until $N = 6$.
- **$N = 6$**: two free.
- **$N = 1$ or $2$**: nothing free.
- The price multiplies only *after* counting paid items; multiplying first and then discounting would need the same division anyway.

## Dry run

| $N$ | free $N//3$ | paid | $X$ | total | output |
|---:|---:|---:|---:|---:|---|
| 3 | 1 | 2 | 4 | 8 | `8` |
| 4 | 1 | 3 | 2 | 6 | `6` |
| 5 | 1 | 4 | 3 | 12 | `12` |
| 6 | 2 | 4 | 1 | 4 | `4` |

Rows 2 and 3 show the free count stalling at one across $N = 4, 5$.

> CodeChef tags: `Basic Programming Concepts`, `Mathematics`, `Basic Math`

---

Same problem in rating order (#97 of 486): [../../by-rating/097-SALE2.md](../../by-rating/097-SALE2.md)
