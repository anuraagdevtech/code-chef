[&larr; 151. Janmansh at Fruit Market](151-JMARKET.md) &middot; [Index](README.md) &middot; [153. Rearranging digits to get a multiple of 5 &rarr;](153-DIGARR.md)

# 152. Non-Negative Product

> [`NONNEGPROD`](https://www.codechef.com/problems/NONNEGPROD) &middot; difficulty **948** &middot; time limit **1s** &middot; 500 to 1000 difficulty rating (Level 1)

## Topic used

| | |
|---|---|
| **Topic** | Arrays |
| **Technique** | Sign of a product from the count of negatives |
| **CodeChef tags** | `Basic Programming Concepts`, `Mathematics`, `Loops`, `Basic Math` |
| **Complexity class** | Linear $O(n)$ |
| **Time** | $O(N)$ per test case |
| **Space** | $O(1)$ |

## Question

Alice has an array of $N$ integers — $A_1, A_2, \ldots, A_N$. She wants the product of all the elements of the array to be a non-negative integer. That is, it can be either $0$ or positive. But she doesn't want it to be negative.

To do this, she is willing to remove some elements of the array. Determine the  minimum number of elements that she will have to remove to make the product of the array's elements non-negative.

**Input**

- The first line of input will contain a single integer $T$, denoting the number of test cases.
    - The first line of each test case contains a single integer $N$ — the number of elements in the array originally.
    - The next line contains $N$ space-separated integers — $A_1, A_2, \ldots, A_N$, which are the original array elements.

**Output**

For each test case, output on a new line the minimum number of elements that she has to remove from the array.

## Constraints

- $1 \leq T \leq 100$
- $2 \leq N \leq 10000$
- $-1000 \leq A_i \leq 1000$

## Sample

**Sample input**

```
4
3
1 9 8
4
2 -1 9 100
4
2 -1 0 100
4
2 -1 -1 100
```

**Sample output**

```
0
1
0
0
```

<details><summary>Explanation</summary>

**Test case $1$:** The product of the elements of the array is $1 \times 9 \times 8 = 72$, which is already non-negative. Hence no element needs to be removed, and so the answer is $0$.

**Test case $2$:** The product of the elements of the array is $2 \times -1 \times 9 \times 100 = -1800$, which is negative. Alice can remove the element $-1$, and the product then becomes non-negative. Hence the answer is $1$.

**Test case $3$:** The product of the elements of the array is $2 \times -1 \times 0 \times 100 = 0$, which is already non-negative. Hence no element needs to be removed, and so the answer is $0$.

**Test case $4$:** The product of the elements of the array is $2 \times -1 \times -1 \times 100 = 200$, which is already non-negative. Hence no element needs to be removed, and so the answer is $0$.

</details>

## Approach

The sign of a product depends only on how many negative factors it has — and on whether any factor is zero. So the array falls into three cases:

**Contains a zero.** The product is $0$, which is non-negative. Remove nothing: answer $0$. Sample case 3 is this, and it is the case most easily missed, because the array also has an odd number of negatives and would otherwise look like it needs a removal.

**Even number of negatives, no zero.** The negatives pair up and the product is positive. Answer $0$ — samples 1 and 4.

**Odd number of negatives, no zero.** The product is negative. Removing a single negative element flips the count to even and fixes it, so the answer is $1$ — sample 2. One removal is clearly minimal, since removing nothing leaves it negative.

The check order matters: the zero test must come **first**, because a zero overrides the parity entirely. Counting negatives and branching on parity alone fails sample case 3.

Only two cheap scans are needed — whether any element is zero and how many are negative — so this is $O(N)$ time and $O(1)$ space. The product itself is never computed, which is just as well: with $N$ up to $10^4$ and values to $1000$, it would be an astronomically large number, and in a fixed-width language it would overflow long before telling you its sign.

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
        vals = [int(v) for v in data[pos + 1:pos + 1 + n]]
        pos += 1 + n
        # A zero makes the product 0, which beats any parity concern.
        if any(v == 0 for v in vals):
            out.append("0")
        else:
            negatives = sum(1 for v in vals if v < 0)
            out.append("0" if negatives % 2 == 0 else "1")
    sys.stdout.write("\n".join(out) + "\n")


main()
```

## Edge cases

- **A zero overrides the parity.** The third row has one negative *and* a zero: the product is already $0$, which is non-negative, so the answer is $0$ operations. A solution that only counts negatives answers $1$ there, which is why the zero test must come first.
- **An even number of negatives** (the fourth row, two of them): already non-negative, so $0$.
- **An odd number of negatives** (the second row, one): a single sign flip, so $1$.
- **No negatives at all** (the first row): $0$.
- The answer is therefore only ever $0$ or $1$ — one flip always suffices to fix the sign.

## Dry run

| array | contains $0$? | negatives | parity | output |
|---|:---:|---:|---|---|
| $1, 9, 8$ | no | 0 | even | `0` |
| $2, -1, 9, 100$ | no | 1 | odd | `1` |
| $2, -1, 0, 100$ | **yes** | — | — | `0` |
| $2, -1, -1, 100$ | no | 2 | even | `0` |

Row 3 short-circuits on the zero before the parity is ever considered.

---

Same problem grouped by topic: [../docs/arrays/NONNEGPROD.md](../docs/arrays/NONNEGPROD.md)
