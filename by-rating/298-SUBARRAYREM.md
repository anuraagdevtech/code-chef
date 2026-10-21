# 298. Subarray Removal

> [`SUBARRAYREM`](https://www.codechef.com/problems/SUBARRAYREM) &middot; difficulty **1505** &middot; time limit **4.5s** &middot; 1400 to 1600 difficulty problems (Level 2)

## Topic used

| | |
|---|---|
| **Topic** | Greedy |
| **Technique** | Budgeting two resources |
| **CodeChef tags** | `Algorithms`, `Constructive`, `ad-hoc` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

Chef has a **binary** array $A$ of length $N$. In one operation, Chef does the following:

**1.** Select any $L$ and $R$ such that $(1 \le L \lt R \le |A|)$ $\\$
**2.** Add $A_L \oplus A_{L+1} \oplus \ldots \oplus A_R$ to his *score* (Here, $\oplus$ denotes the [bitwise XOR operation](https://en.wikipedia.org/wiki/Bitwise_operation#XOR)) $\\$
**3.** Remove the subarray $A_{L \dots R}$ from $A$

Determine the **maximum** score Chef can get after performing the above operation any number of times.

**Input**

- The first line contains a single integer $T$ — the number of test cases. Then the test cases follow.
- The first line of each test case contains an integer $N$ — the size of the array $A$.
- The second line of each test case contains $N$ space-separated integers $A_1, A_2, \dots, A_N$ denoting the array $A$.

**Output**

For each test case, output the maximum score Chef can get.

## Constraints

- $1 \leq T \leq 10^5$
- $1 \leq N \leq 10^5$
- $A_i \in \{0, 1\}$
- The sum of $N$ over all test cases won't exceed $2 \cdot 10^5$.

## Sample

**Sample input**

```
3
5
1 0 0 0 1
3
1 1 1
3
0 0 0
```

**Sample output**

```
2
1
0
```

<details><summary>Explanation</summary>

**Test Case 1:** We can perform the following moves:
- $A = [1, 0, 0, 0, 1]$. Select $L = 1$ and $R = 3$ and remove subarray $[1, 0, 0]$. $A$ becomes $[0, 1]$.
- $A = [0, 1]$. Select $L = 1$ and $R = 2$ and remove subarray $[0, 1]$. $A$ becomes $[]$.

Total score $= 1 + 1 = 2$

**Test Case 2:** We can perform the following move:
- $A = [1, 1, 1]$. Select $L = 1$ and $R = 3$ and remove subarray $[1, 1, 1]$. $A$ becomes $[]$.

Total score $= 1$

</details>

## Approach

XOR over a binary subarray is just the **parity of its ones**, so an operation scores $1$ when it removes an odd number of ones, and $0$ otherwise. The goal is to maximise the number of odd-parity removals, each of which must span at least two elements.

So the question becomes: how should the $o$ ones and $z$ zeros be budgeted across operations?

The cheapest scoring operation takes **one 1 plus one 0** — it costs a single one and meets the length requirement using a zero. Doing as many of these as possible gives $\min(o, z)$ operations.

Once the zeros are exhausted, any further operation must be built from ones alone, and it needs an **odd** count of at least two — so three ones. Each such operation scores $1$ for three ones, so the leftovers contribute $\lfloor (o - \min(o,z)) / 3 \rfloor$ more.

Spending zeros first is right because a zero-padded operation costs one 1 while a pure-ones operation costs three.

$$\text{score} = a + \left\lfloor \frac{o - a}{3} \right\rfloor, \qquad a = \min(o, z)$$

Sample case 1, $[1,0,0,0,1]$, has $o = 2$ and $z = 3$: two cheap operations, score $2$. Sample case 2, $[1,1,1]$, has no zeros at all, so the only option is to take all three ones in one go — score $1$, which the $\lfloor 3/3 \rfloor$ term supplies. Sample case 3 has no ones and scores $0$.

A useful edge check is $[1,1]$: no zeros and only two ones, so $\lfloor 2/3 \rfloor = 0$ — the single possible operation removes two ones and XORs to $0$.

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
        ones = sum(1 for v in data[pos + 1:pos + 1 + n] if v == b"1")
        pos += 1 + n
        zeros = n - ones
        # A zero-padded op costs one 1; without zeros an op needs three.
        cheap = min(ones, zeros)
        out.append(str(cheap + (ones - cheap) // 3))
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **An operation needs at least two elements** ($L < R$), so a lone $1$ cannot be scored by itself — it needs either a $0$ to accompany it or two more $1$s.
- **Zeros are a consumable resource.** Each `1 0` or `0 1` pair scores one point and spends one zero, which is why the cheap operation count is $\min(\text{ones}, \text{zeros})$.
- **With no zeros left, three $1$s are needed per point** (the second row: three $1$s score $1$, and two would score $0$), since the XOR must be odd and the subarray must have at least two elements.
- **No $1$s at all** (the third row) → $0$, because every XOR is zero.
- **Leftover $1$s are wasted** when fewer than three remain after the pairing.
- **Removal re-joins the array**, so the elements chosen need not have been adjacent originally — any $1$ can be matched with any $0$, which is what lets the counting ignore positions entirely.
- **Sum of $N \leq 2 \cdot 10^5$**: one pass counting ones.

## Dry run

| array | ones | zeros | cheap ops $\min$ | ones left | triples | total |
|---|---:|---:|---:|---:|---:|---:|
| $1,0,0,0,1$ | 2 | 3 | 2 | 0 | 0 | `2` |
| $1,1,1$ | 3 | 0 | 0 | 3 | 1 | `1` |
| $0,0,0$ | 0 | 3 | 0 | 0 | 0 | `0` |

Row 1 takes $[1,0]$ and then $[0,1]$, leaving a single $0$ that scores nothing.

---

Same problem grouped by topic: [../docs/greedy/SUBARRAYREM.md](../docs/greedy/SUBARRAYREM.md)
